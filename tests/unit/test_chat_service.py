"""Unit tests for chat service."""

import pytest
from bearhops.services.chat_service import ChatService


@pytest.mark.asyncio
async def test_process_message() -> None:
    """Test processing a chat message."""
    service = ChatService()
    response = await service.process_message(
        message="Hello!", conversation_id="test-123", model="gpt-3.5-turbo"
    )

    assert response.message is not None
    assert response.conversation_id == "test-123"
    assert response.model == "gpt-3.5-turbo"


@pytest.mark.asyncio
async def test_get_conversation_history() -> None:
    """Test retrieving conversation history."""
    service = ChatService()

    # Add some messages
    await service.process_message(message="Hello!", conversation_id="test-456", model="gpt-3.5-turbo")
    await service.process_message(message="How are you?", conversation_id="test-456", model="gpt-3.5-turbo")

    # Get history
    history = await service.get_conversation_history("test-456")

    assert len(history) == 4  # 2 user messages + 2 assistant responses
    assert history[0]["role"] == "user"
    assert history[1]["role"] == "assistant"


@pytest.mark.asyncio
async def test_get_empty_conversation_history() -> None:
    """Test retrieving history for non-existent conversation."""
    service = ChatService()
    history = await service.get_conversation_history("non-existent")

    assert len(history) == 0
