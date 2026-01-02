"""Unit tests for chat API routes."""

from fastapi.testclient import TestClient


def test_chat_endpoint(client: TestClient) -> None:
    """Test the chat endpoint."""
    response = client.post(
        "/api/v1/chat",
        json={"message": "Hello, Bearhops!", "model": "gpt-3.5-turbo"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "conversation_id" in data
    assert data["model"] == "gpt-3.5-turbo"


def test_chat_endpoint_with_conversation_id(client: TestClient) -> None:
    """Test the chat endpoint with conversation ID."""
    conversation_id = "test-conversation-123"
    response = client.post(
        "/api/v1/chat",
        json={
            "message": "Hello!",
            "conversation_id": conversation_id,
            "model": "gpt-3.5-turbo",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["conversation_id"] == conversation_id


def test_chat_endpoint_empty_message(client: TestClient) -> None:
    """Test the chat endpoint with empty message."""
    response = client.post(
        "/api/v1/chat",
        json={"message": "", "model": "gpt-3.5-turbo"},
    )
    # Should fail validation
    assert response.status_code == 422
