# Bearhops

AI Chatbot production grade to operate AI

## Overview

Bearhops is a production-ready AI chatbot framework designed to build intelligent conversational applications. It provides a robust foundation for creating chatbots with modern Python tools and best practices.

## Features

- 🚀 **FastAPI-based**: High-performance async API framework
- 💬 **Chat API**: RESTful endpoints for chat interactions
- 🔄 **Conversation Management**: Track and manage conversation history
- 🔌 **Extensible**: Easy to integrate with various AI services (OpenAI, Anthropic, etc.)
- 🧪 **Tested**: Comprehensive test suite with pytest
- 📝 **Type-safe**: Full type hints with Pydantic models
- 🔧 **Development Tools**: Black, Ruff, and MyPy for code quality

## Quick Start

### Prerequisites

- Python 3.9 or higher
- pip or Poetry

### Installation

1. Clone the repository:
```bash
git clone https://github.com/dungduong2412/Bearhops.git
cd Bearhops
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

Or with Poetry:
```bash
poetry install
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

### Running the Application

Start the development server:
```bash
python -m src.bearhops.main
```

Or with uvicorn directly:
```bash
uvicorn src.bearhops.main:app --reload
```

The API will be available at `http://localhost:8000`

### API Documentation

Once the server is running, access:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API Endpoints

### Health Check
```bash
GET /health
```

### Chat
```bash
POST /api/v1/chat
Content-Type: application/json

{
  "message": "Hello, Bearhops!",
  "conversation_id": "optional-conversation-id",
  "model": "gpt-3.5-turbo"
}
```

### Conversation History
```bash
GET /api/v1/chat/history/{conversation_id}
```

## Development

### Running Tests

```bash
pytest
```

With coverage:
```bash
pytest --cov=src/bearhops --cov-report=html
```

### Code Formatting

Format code with Black:
```bash
black src/ tests/
```

Lint with Ruff:
```bash
ruff check src/ tests/
```

Type check with MyPy:
```bash
mypy src/
```

## Project Structure

```
Bearhops/
├── src/
│   └── bearhops/
│       ├── api/          # API routes and endpoints
│       ├── core/         # Core configuration
│       ├── models/       # Pydantic models
│       ├── services/     # Business logic
│       └── utils/        # Utility functions
├── tests/
│   ├── unit/            # Unit tests
│   └── integration/     # Integration tests
├── docs/                # Documentation
├── .env.example         # Example environment variables
├── pyproject.toml       # Project configuration
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Support

For issues and questions, please open an issue on GitHub.
