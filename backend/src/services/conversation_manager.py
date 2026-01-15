from typing import List, Dict, Any, Optional
from sqlmodel import Session, select
from src.database import get_session
from src.models.conversation import Conversation, ConversationCreate, ConversationPublic
from src.models.message import Message, MessageCreate, MessagePublic

# For mock purposes, assume a default user ID
MOCK_USER_ID = 1

def _get_session():
    """Helper to get a session for tool usage outside of FastAPI request context."""
    for session in get_session():
        return session

class ConversationManager:
    def __init__(self, user_id: int = MOCK_USER_ID):
        self.user_id = user_id

    def create_conversation(self, title: str) -> ConversationPublic:
        with _get_session() as session:
            conversation_create = ConversationCreate(title=title, user_id=self.user_id)
            db_conversation = Conversation.from_orm(conversation_create)
            session.add(db_conversation)
            session.commit()
            session.refresh(db_conversation)
            return ConversationPublic.from_orm(db_conversation)

    def get_conversation(self, conversation_id: int) -> Optional[ConversationPublic]:
        with _get_session() as session:
            conversation = session.exec(select(Conversation).where(Conversation.id == conversation_id, Conversation.user_id == self.user_id)).first()
            return ConversationPublic.from_orm(conversation) if conversation else None

    def get_conversation_history(self, conversation_id: int) -> List[MessagePublic]:
        with _get_session() as session:
            messages = session.exec(select(Message).where(Message.conversation_id == conversation_id)).all()
            return [MessagePublic.from_orm(msg) for msg in messages]

    def add_message_to_conversation(self, conversation_id: int, content: str, role: str) -> MessagePublic:
        with _get_session() as session:
            message_create = MessageCreate(content=content, role=role, conversation_id=conversation_id)
            db_message = Message.from_orm(message_create)
            session.add(db_message)
            session.commit()
            session.refresh(db_message)
            return MessagePublic.from_orm(db_message)

    def get_or_create_default_conversation(self) -> ConversationPublic:
        """
        Gets the most recent conversation or creates a new one if none exist.
        """
        with _get_session() as session:
            # Try to get the latest conversation for the user
            latest_conversation = session.exec(
                select(Conversation)
                .where(Conversation.user_id == self.user_id)
                .order_by(Conversation.id.desc())
            ).first()

            if latest_conversation:
                return ConversationPublic.from_orm(latest_conversation)
            else:
                # If no conversation exists, create a default one
                return self.create_conversation(title="New Conversation")
