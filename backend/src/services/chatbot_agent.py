import os
import json
from typing import List, Dict, Any, Optional
from mcp_sdk.agent import Agent, AgentMessage, UserMessage, ToolMessage, LLMMessage
# For OpenAI Agents SDK integration
# from openai import OpenAI
# from chatkit import ChatKit, Tool as ChatKitTool # Assuming ChatKit has a Tool type

# Placeholder for Gemini integration if using directly via OpenAI SDK or similar
import google.generativeai as genai
from src.mcp_tools.flight_tools import get_flight_information
from src.mcp_tools.task_tools import add_task, list_tasks, update_task, delete_task, complete_task

# Configure a simple in-memory tool registry for demonstration
TOOL_REGISTRY = {
    "get_flight_information": get_flight_information,
    "add_task": add_task,
    "list_tasks": list_tasks,
    "update_task": update_task,
    "delete_task": delete_task,
    "complete_task": complete_task
}

# Configure OpenAI API key from environment variables
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# if not OPENAI_API_KEY: raise ValueError("OPENAI_API_KEY environment variable not set.")

# Configure Gemini API key if used directly
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY: genai.configure(api_key=GEMINI_API_KEY)

class ChatbotAgent(Agent):
    def __init__(self, agent_name: str = "TravelAssistant"):
        super().__init__(agent_name)

        # Initialize OpenAI client with configured API key
        # self.openai_client = OpenAI(api_key=OPENAI_API_KEY)

        # Initialize ChatKit with OpenAI client and tools
        # self.chatkit = ChatKit(client=self.openai_client, tools=[get_flight_information, add_task, list_tasks, update_task, delete_task, complete_task])

        # Register MCP tools for direct use (or for the LLM agent to call)
        self.add_tool(get_flight_information)
        self.add_tool(add_task)
        self.add_tool(list_tasks)
        self.add_tool(update_task)
        self.add_tool(delete_task)
        self.add_tool(complete_task)

    async def process_message(self, user_message: str) -> str:
        # For simplicity, a direct tool call if keywords are present
        # If keywords are present, call the appropriate tool
        if "add task" in user_message.lower():
            title = user_message.lower().split("add task ")[1]
            tool_output = add_task(title=title)
            return json.dumps(tool_output)
        elif "list tasks" in user_message.lower():
            tool_output = list_tasks()
            return json.dumps(tool_output)
        elif "update task" in user_message.lower():
            parts = user_message.lower().split("update task ")[1].split(" with ")
            task_id = int(parts[0])
            # This is a very simplistic parsing and would need a robust NLP solution
            # For now, assuming "update task <id> with title <new_title>" or "completed <true/false>"
            if "title" in parts[1]:
                title = parts[1].split("title ")[1]
                tool_output = update_task(task_id=task_id, title=title)
            elif "completed" in parts[1]:
                completed = "true" in parts[1]
                tool_output = update_task(task_id=task_id, completed=completed)
            else:
                return json.dumps({"status": "error", "message": "Could not parse update task command."})
            return json.dumps(tool_output)
        elif "delete task" in user_message.lower():
            task_id = int(user_message.lower().split("delete task ")[1])
            tool_output = delete_task(task_id=task_id)
            return json.dumps(tool_output)
        elif "complete task" in user_message.lower():
            task_id = int(user_message.lower().split("complete task ")[1])
            tool_output = complete_task(task_id=task_id)
            return json.dumps(tool_output)
        elif "flight" in user_message.lower():
            tool_output = get_flight_information(user_message)
            return json.dumps(tool_output)

        # In a full integration, you would use ChatKit/OpenAI Agent to process the message
        # For example:
        # response = await self.chatkit.process_user_message(user_message)
        # return response.text

        return f"Hello! How can I help you with your travel plans? I can currently assist with flight information and managing your todo list. (OpenAI Agents SDK and ChatKit + Gemini key configured in backend/src/services/chatbot_agent.py - actual LLM processing would be here). Try asking something like: 'find me a flight from London to Paris' or 'add task buy groceries'."

# This would typically be initialized with a proper LLM, e.g., OpenAI/Gemini
def get_chatbot_agent() -> ChatbotAgent:
    return ChatbotAgent()
