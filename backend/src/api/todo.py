from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from src.database import get_session
from src.models.task import Task, TaskCreate, TaskUpdate, TaskPublic # Assuming TodoItem maps to Task
from src.api.v1.auth import get_current_user

todo_router = APIRouter()

@todo_router.post("/todos/", response_model=TaskPublic)
def create_todo_item(
    todo_item: TaskCreate,
    current_user: Any = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    db_todo_item = Task.from_orm(todo_item)
    db_todo_item.owner_id = current_user.id # Assign ownership
    session.add(db_todo_item)
    session.commit()
    session.refresh(db_todo_item)
    return db_todo_item

@todo_router.get("/todos/", response_model=List[TaskPublic])
def read_todo_items(
    current_user: Any = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    todo_items = session.exec(select(Task).where(Task.owner_id == current_user.id)).all()
    return todo_items

@todo_router.get("/todos/{todo_item_id}", response_model=TaskPublic)
def read_todo_item(
    todo_item_id: int,
    current_user: Any = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    todo_item = session.exec(select(Task).where(Task.id == todo_item_id, Task.owner_id == current_user.id)).first()
    if not todo_item:
        raise HTTPException(status_code=404, detail="TodoItem not found")
    return todo_item

@todo_router.put("/todos/{todo_item_id}", response_model=TaskPublic)
def update_todo_item(
    todo_item_id: int,
    todo_item: TaskUpdate,
    current_user: Any = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    db_todo_item = session.exec(select(Task).where(Task.id == todo_item_id, Task.owner_id == current_user.id)).first()
    if not db_todo_item:
        raise HTTPException(status_code=404, detail="TodoItem not found")

    todo_data = todo_item.dict(exclude_unset=True)
    for key, value in todo_data.items():
        setattr(db_todo_item, key, value)

    session.add(db_todo_item)
    session.commit()
    session.refresh(db_todo_item)
    return db_todo_item

@todo_router.delete("/todos/{todo_item_id}")
def delete_todo_item(
    todo_item_id: int,
    current_user: Any = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    todo_item = session.exec(select(Task).where(Task.id == todo_item_id, Task.owner_id == current_user.id)).first()
    if not todo_item:
        raise HTTPException(status_code=404, detail="TodoItem not found")

    session.delete(todo_item)
    session.commit()
    return {"message": "TodoItem deleted successfully"}
