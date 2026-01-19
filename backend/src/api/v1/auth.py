from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session
from src.database import engine
from src.models.user import User, UserCreate, UserPublic
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt, JWTError
from src.middleware.auth import BETTER_AUTH_SECRET, ALGORITHM

router = APIRouter()

ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Should come from env vars later

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


# ------------------------------------------------------------
# JWT: Create access token
# ------------------------------------------------------------
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()

    expire = datetime.utcnow() + (
        expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, BETTER_AUTH_SECRET, algorithm=ALGORITHM)
    return encoded_jwt


# ------------------------------------------------------------
# JWT: Validate token and get current user
# ------------------------------------------------------------
async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, BETTER_AUTH_SECRET, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")

        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token: no user ID found",
            )

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication token",
        )

    # Fetch user from DB
    with Session(engine) as session:
        user = session.get(User, int(user_id))
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
            )

        return user


# ------------------------------------------------------------
# SIGNUP
# ------------------------------------------------------------
@router.post("/signup", response_model=UserPublic)
def register_user(user_create: UserCreate):
    with Session(engine) as session:
        existing_user = (
            session.query(User).filter(User.email == user_create.email).first()
        )
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered",
            )

        user = User(email=user_create.email)
        user.set_password(user_create.password)

        session.add(user)
        session.commit()
        session.refresh(user)
        return user


# ------------------------------------------------------------
# LOGIN
# ------------------------------------------------------------
@router.post("/login")
def login_user(user_create: UserCreate):
    with Session(engine) as session:
        user = (
            session.query(User).filter(User.email == user_create.email).first()
        )
        if not user or not user.verify_password(user_create.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": str(user.id)}, expires_delta=access_token_expires
        )

        return {"access_token": access_token, "token_type": "bearer"}
