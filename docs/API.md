# Bearhops API Documentation

## Overview

Bearhops provides a RESTful API for interacting with AI chatbot services. The API is built with FastAPI and provides automatic OpenAPI documentation.

## Base URL

```
http://localhost:8000
```

## Authentication

Currently, the API does not require authentication. This will be added in future versions.

## Endpoints

### Health Check

Check the health status of the API.

**Endpoint:** `GET /health`

**Response:**
```json
{
  "status": "healthy"
}
```

### Root

Get basic information about the API.

**Endpoint:** `GET /`

**Response:**
```json
{
  "message": "Welcome to Bearhops AI Chatbot",
  "version": "0.1.0"
}
```

### Chat Completion

Send a message and receive an AI-generated response.

**Endpoint:** `POST /api/v1/chat`

**Request Body:**
```json
{
  "message": "Hello, how can you help me?",
  "conversation_id": "optional-unique-id",
  "model": "gpt-3.5-turbo"
}
```

**Parameters:**
- `message` (string, required): The user's message
- `conversation_id` (string, optional): Unique identifier for the conversation
- `model` (string, optional): AI model to use (default: "gpt-3.5-turbo")

**Response:**
```json
{
  "message": "I'm here to help! What would you like to know?",
  "conversation_id": "abc-123-def",
  "model": "gpt-3.5-turbo",
  "timestamp": "2024-01-01T12:00:00Z"
}
```

### Get Conversation History

Retrieve the history of a conversation.

**Endpoint:** `GET /api/v1/chat/history/{conversation_id}`

**Parameters:**
- `conversation_id` (string, required): The conversation ID

**Response:**
```json
{
  "conversation_id": "abc-123-def",
  "history": [
    {
      "role": "user",
      "content": "Hello!",
      "timestamp": "2024-01-01T12:00:00Z"
    },
    {
      "role": "assistant",
      "content": "Hi there! How can I help you?",
      "timestamp": "2024-01-01T12:00:01Z"
    }
  ]
}
```

## Error Responses

The API uses standard HTTP status codes:

- `200 OK`: Successful request
- `400 Bad Request`: Invalid request parameters
- `404 Not Found`: Resource not found
- `422 Unprocessable Entity`: Validation error
- `500 Internal Server Error`: Server error

Error response format:
```json
{
  "detail": "Error message describing what went wrong"
}
```

## Rate Limiting

Rate limiting is not currently implemented but will be added in future versions.

## Interactive Documentation

Visit `http://localhost:8000/docs` for interactive Swagger UI documentation where you can test the API endpoints directly.
