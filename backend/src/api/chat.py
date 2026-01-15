from fastapi import APIRouter, Depends, HTTPException, Path
from sqlmodel import Session
from typing import Dict, Any
from src.database import get_session
from src.services.chatbot_agent import get_chatbot_agent, ChatbotAgent
from src.services.conversation_manager import ConversationManager
from src.api.v1.auth import get_current_user

chat_router = APIRouter()

@chat_router.post("/chat")
async def chat_with_bot(
    user_message: Dict[str, str],
    user_id: int = Path(..., description="The ID of the user"), # Explicitly define Path for user_id
    current_user: Any = Depends(get_current_user),
    session: Session = Depends(get_session)
) -> Dict[str, Any]:
    # Ensure the authenticated user matches the path user_id for security
    if current_user.id != user_id:
        raise HTTPException(status_code=403, detail="Not authorized to access this user's chat.")

    text_message = user_message.get("message")
    if not text_message:
        raise HTTPException(status_code=400, detail="Message content is required.")

    chatbot_agent = get_chatbot_agent()
    conversation_manager = ConversationManager(user_id=user_id)

    # Get or create the default conversation for the user
    conversation = conversation_manager.get_or_create_default_conversation()

    # Add user message to conversation history
    conversation_manager.add_message_to_conversation(
        conversation_id=conversation.id,
        content=text_message,
        role="user"
    )

    # Process message with chatbot agent
    # The chatbot agent itself will handle tool calls and response generation
    agent_response_content = await chatbot_agent.process_message(text_message)

    # Add bot response to conversation history
    conversation_manager.add_message_to_conversation(
        conversation_id=conversation.id,
        content=agent_response_content,
        role="bot"
    )

    return {"response": agent_response_content}
