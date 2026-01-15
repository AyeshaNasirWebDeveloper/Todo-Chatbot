from mcp_sdk.tool import Tool, tool_usage
from sqlmodel import Session, select
from src.database import get_session
from src.models.task import Task, TaskCreate
from typing import Dict, Any, List

# In a real application, user_id would come from the current authenticated context
# For mock purposes, let's assume a default user_id or pass it if needed
MOCK_USER_ID = 1 # Placeholder for a logged-in user

def _get_session():
    """Helper to get a session for tool usage outside of FastAPI request context."""
    for session in get_session():
        return session

@tool_usage(name="add_task", description="Add a new task to the user's todo list.")
def add_task(title: str, description: str = None) -> Dict[str, Any]:
    """
    Adds a new task to the todo list for a mock user.
    """
    with _get_session() as session:
        task_create = TaskCreate(title=title, description=description, owner_id=MOCK_USER_ID)
        db_task = Task.from_orm(task_create)
        session.add(db_task)
        session.commit()
        session.refresh(db_task)
        return {"status": "success", "message": f"Task '{db_task.title}' added successfully with ID {db_task.id}."}

@tool_usage(name="list_tasks", description="List all tasks in the user's todo list.")
def list_tasks() -> Dict[str, Any]:
    """
    Lists all tasks for a mock user.
    """
    with _get_session() as session:
        tasks = session.exec(select(Task).where(Task.owner_id == MOCK_USER_ID)).all()
        if not tasks:
            return {"status": "success", "message": "Your todo list is empty."}
        tasks_data = [{
            "id": task.id,
            "title": task.title,
            "description": task.id,
            "completed": task.completed
        } for task in tasks]
        return {"status": "success", "tasks": tasks_data}

@tool_usage(name="update_task", description="Update an existing task in the user's todo list.")
def update_task(task_id: int, title: str = None, description: str = None, completed: bool = None) -> Dict[str, Any]:
    """
    Updates an existing task by ID for a mock user.
    """
    with _get_session() as session:
        db_task = session.exec(select(Task).where(Task.id == task_id, Task.owner_id == MOCK_USER_ID)).first()
        if not db_task:
            return {"status": "error", "message": f"Task with ID {task_id} not found."}

        if title is not None: db_task.title = title
        if description is not None: db_task.description = description
        if completed is not None: db_task.completed = completed

        session.add(db_task)
        session.commit()
        session.refresh(db_task)
        return {"status": "success", "message": f"Task {task_id} updated successfully."}

@tool_usage(name="delete_task", description="Delete a task from the user's todo list.")
def delete_task(task_id: int) -> Dict[str, Any]:
    """
    Deletes a task by ID for a mock user.
    """
    with _get_session() as session:
        db_task = session.exec(select(Task).where(Task.id == task_id, Task.owner_id == MOCK_USER_ID)).first()
        if not db_task:
            return {"status": "error", "message": f"Task with ID {task_id} not found."}

        session.delete(db_task)
        session.commit()
        return {"status": "success", "message": f"Task {task_id} deleted successfully."}

@tool_usage(name="complete_task", description="Mark a task as completed in the user's todo list.")
def complete_task(task_id: int) -> Dict[str, Any]:
    """
    Marks a task as completed by ID for a mock user.
    """
    return update_task(task_id=task_id, completed=True)
