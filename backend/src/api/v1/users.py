from fastapi import APIRouter, Depends
from src.api.v1.auth import get_current_user

router = APIRouter()

@router.get("/users/me")
def get_me(current_user = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email,
    }
