"""
Chat API routes.
"""

from fastapi import APIRouter, HTTPException, status
from uuid import uuid4

from bearhops.models.chat import ChatRequest, ChatResponse
from bearhops.services.chat_service import ChatService

router = APIRouter()
chat_service = ChatService()


@router.post("/chat", response_model=ChatResponse, status_code=status.HTTP_200_OK)
async def chat(request: ChatRequest) -> ChatResponse:
    """
    Process a chat message and return AI response.

    Args:
        request: Chat request containing the user message

    Returns:
        ChatResponse with AI-generated reply
    """
    try:
        # Generate conversation ID if not provided
        conversation_id = request.conversation_id or str(uuid4())

        # Process the chat request
        response = await chat_service.process_message(
            message=request.message,
            conversation_id=conversation_id,
            model=request.model,
        )

        return response

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error processing chat request: {str(e)}",
        )


@router.get("/chat/history/{conversation_id}")
async def get_conversation_history(conversation_id: str) -> dict:
    """
    Retrieve conversation history for a given conversation ID.

    Args:
        conversation_id: Unique identifier for the conversation

    Returns:
        Conversation history
    """
    history = await chat_service.get_conversation_history(conversation_id)
    return {"conversation_id": conversation_id, "history": history}
