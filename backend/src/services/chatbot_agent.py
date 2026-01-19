from __future__ import annotations
import os
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

# Import original package
try:
    from agents import (
        Agent,
        Runner,
        RunConfig,
        OpenAIChatCompletionsModel,
        AsyncOpenAI,
        RunContextWrapper,
        function_tool,
        input_guardrail,
        dynamic_instruction,
        ModelSettings,
    )

except Exception:
    # fallback lightweight version (your previous fallback code)
    from typing import Callable

    class RunContextWrapper(dict):
        pass

    class ModelSettings:
        def __init__(self, model: str, temperature=0.0, client_options=None):
            self.model = model
            self.temperature = temperature
            self.client_options = client_options or {}

    class Agent:
        def __init__(
            self,
            name: str,
            instructions="",
            tools=None,
            model_settings=None,
            input_guardrails=None,
            dynamic_instructions=None,
        ):
            self.name = name
            self.instructions = instructions
            self.tools = tools or []
            self.model_settings = model_settings
            self.input_guardrails = input_guardrails or []
            self.dynamic_instructions = dynamic_instructions or []

    class Runner:
        @staticmethod
        def run(agent, message, context=None):
            return _mock_llm_router(agent, message, context or {})

        @staticmethod
        def run_sync(agent, message, context=None):
            return Runner.run(agent, message, context)

    def function_tool(fn: Callable):
        fn._is_tool = True
        return fn

    def input_guardrail(fn: Callable):
        fn._is_guardrail = True
        return fn

    def dynamic_instruction(fn: Callable):
        fn._is_dynamic_instruction = True
        return fn


# =============================
# USER CONTEXT
# =============================
class UserContext(BaseModel):
    name: str
    user_id: str  # reference to DB user


# =============================
# YOUR TODO TASK MOCK DATABASE
# =============================
TASK_DB: Dict[str, List[Dict[str, Any]]] = {}  # user_id → tasks list


def get_user_tasks(uid: str):
    return TASK_DB.setdefault(uid, [])


# =============================
# GUARDRAIL
# =============================
INTENTS = [
    "task",
    "todo",
    "add",
    "create",
    "update",
    "delete",
    "show",
    "list",
    "search",
    "reminder",
    "complete",
    "pending",
]


@input_guardrail
def guardrail_input(ctx: RunContextWrapper, message: str) -> Optional[str]:
    lower = message.lower()

    if any(keyword in lower for keyword in INTENTS):
        return None  

    if any(g in lower for g in ["hi", "hello", "salam", "hey", "assalam"]):
        return None

    return "I can only help with tasks, todos, reminders, and task management."


# =============================
# TOOL FUNCTIONS
# =============================

@function_tool
def create_task(user_id: str, title: str, due: Optional[str] = None):
    tasks = get_user_tasks(user_id)
    new_task = {
        "id": len(tasks) + 1,
        "title": title,
        "due": due,
        "completed": False,
    }
    tasks.append(new_task)
    return {"message": "Task created", "task": new_task}


@function_tool
def list_tasks(user_id: str):
    return {"tasks": get_user_tasks(user_id)}


@function_tool
def update_task(user_id: str, task_id: int, completed: Optional[bool] = None, title: Optional[str] = None):
    tasks = get_user_tasks(user_id)
    for t in tasks:
        if t["id"] == task_id:
            if completed is not None:
                t["completed"] = completed
            if title:
                t["title"] = title
            return {"message": "Task updated", "task": t}
    return {"error": "Task not found"}


@function_tool
def delete_task(user_id: str, task_id: int):
    tasks = get_user_tasks(user_id)
    for t in tasks:
        if t["id"] == task_id:
            tasks.remove(t)
            return {"message": "Task deleted"}
    return {"error": "Task not found"}


@function_tool
def search_tasks(user_id: str, query: str):
    tasks = get_user_tasks(user_id)
    results = [t for t in tasks if query.lower() in t["title"].lower()]
    return {"results": results}


@function_tool
def set_reminder(user_id: str, task_id: int, when: str):
    return {"message": f"Reminder set for task {task_id} at {when}"}


# =============================
# DYNAMIC PERSONALIZATION
# =============================
@dynamic_instruction
def personalize(ctx: RunContextWrapper):
    user: UserContext = ctx.get("user")
    return f"Always call the user by name ({user.name}) and keep responses short."


# =============================
# MODEL SETTINGS
# =============================
MODEL_SETTINGS = ModelSettings(
    model="gemini-2.0-flash",
    temperature=0.1,
    client_options={
        "api_key": os.environ.get("GEMINI_API_KEY"),
        "base_url": "https://generativelanguage.googleapis.com/v1beta/openai/",
    },
)


# =============================
# AGENT INSTRUCTIONS
# =============================
TODO_SYSTEM_INSTRUCTIONS = """
You are an AI Todo Assistant.
You help users manage tasks. You can:
- Create tasks
- List tasks
- Update tasks
- Delete tasks
- Search tasks
- Manage reminders

Use tools properly. Ask for task IDs when needed.
Keep replies short and helpful.
"""


todo_agent = Agent(
    name="todo-assistant",
    instructions=TODO_SYSTEM_INSTRUCTIONS,
    tools=[create_task, list_tasks, update_task, delete_task, search_tasks, set_reminder],
    model_settings=MODEL_SETTINGS,
    input_guardrails=[guardrail_input],
    dynamic_instructions=[personalize],
)


# =============================
# MOCK ROUTER (DRY RUN)
# =============================
DRY_RUN = True


@dataclass
class MockResult:
    content: str
    tool_calls: List[Dict[str, Any]]


def _mock_llm_router(agent: Agent, message: str, ctx: Dict[str, Any]) -> Dict[str, Any]:
    user: UserContext = ctx.get("user")
    name = user.name
    uid = user.user_id
    lower = message.lower()

    # greetings
    if any(g in lower for g in ["hi", "hello", "salam", "assalam", "hey"]):
        return {"role": "assistant", "content": f"Hi {name}! How can I help with your tasks?"}

    # create task
    if "add" in lower or "create" in lower:
        title = message.replace("add", "").replace("create", "").strip()
        res = create_task(uid, title)
        return {"role": "assistant", "content": f"{name}, your task is added: {res['task']['title']}"}

    # list tasks
    if "list" in lower or "show" in lower:
        tasks = list_tasks(uid)["tasks"]
        if not tasks:
            return {"role": "assistant", "content": f"{name}, you have no tasks yet."}
        text = "\n".join([f"{t['id']}. {t['title']} ({'Done' if t['completed'] else 'Pending'})" for t in tasks])
        return {"role": "assistant", "content": text}

    # search
    if "search" in lower or "find" in lower:
        query = message.replace("search", "").replace("find", "").strip()
        results = search_tasks(uid, query)["results"]
        if not results:
            return {"role": "assistant", "content": f"No tasks found for '{query}'."}
        return {"role": "assistant", "content": ", ".join([t['title'] for t in results])}

    return {"role": "assistant", "content": "I can help with creating, listing, updating, deleting and searching your tasks!"}

# ============================================================
# ChatbotAgent Wrapper (for FastAPI import)
# ============================================================

class ChatbotAgent:
    """Simple wrapper class so FastAPI can call the agent cleanly."""
    def __init__(self):
        self.agent = todo_agent  # <-- from your todo agent code

    def run(self, message: str, user_id: str, name: str):
        ctx = RunContextWrapper({
            "user": UserContext(name=name, user_id=user_id)
        })
        response = Runner.run_sync(self.agent, message, ctx)
        return response["content"]


# ============================================================
# Factory function (required by your FastAPI routes)
# ============================================================
_chatbot_instance = None

def get_chatbot_agent():
    global _chatbot_instance
    if _chatbot_instance is None:
        _chatbot_instance = ChatbotAgent()
    return _chatbot_instance
