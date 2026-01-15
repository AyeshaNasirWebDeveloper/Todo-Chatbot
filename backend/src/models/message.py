from typing import Optional
from sqlmodel import Field, Relationship, SQLModel

class MessageBase(SQLModel):
    content: str
    role: str # "user" or "bot"
    conversation_id: Optional[int] = Field(default=None, foreign_key="conversation.id")

class Message(MessageBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    conversation: Optional["Conversation"] = Relationship(back_populates="messages")

class MessageCreate(MessageBase):
    pass

class MessagePublic(MessageBase):
    id: int

class MessageUpdate(SQLModel):
    content: Optional[str] = None
    role: Optional[str] = None
