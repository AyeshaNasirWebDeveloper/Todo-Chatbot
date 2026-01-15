from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel

class ConversationBase(SQLModel):
    title: str = Field(index=True)
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")

class Conversation(ConversationBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    messages: List["Message"] = Relationship(back_populates="conversation")

class ConversationCreate(ConversationBase):
    pass

class ConversationPublic(ConversationBase):
    id: int

class ConversationUpdate(SQLModel):
    title: Optional[str] = None
