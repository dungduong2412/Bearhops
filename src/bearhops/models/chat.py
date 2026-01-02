"""
Data models for chat messages and requests.
"""

from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field


class ChatMessage(BaseModel):
    """Represents a single chat message."""

    role: str = Field(..., description="Role of the message sender (user, assistant, system)")
    content: str = Field(..., description="Content of the message")
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class ChatRequest(BaseModel):
    """Request model for chat completion."""

    message: str = Field(..., description="User message", min_length=1)
    conversation_id: Optional[str] = Field(None, description="Conversation ID for context")
    model: str = Field(default="gpt-3.5-turbo", description="AI model to use")


class ChatResponse(BaseModel):
    """Response model for chat completion."""

    message: str = Field(..., description="AI response message")
    conversation_id: str = Field(..., description="Conversation ID")
    model: str = Field(..., description="Model used for generation")
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class ConversationHistory(BaseModel):
    """Represents a conversation history."""

    conversation_id: str
    messages: List[ChatMessage]
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
