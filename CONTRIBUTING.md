# Contributing to Bearhops

Thank you for your interest in contributing to Bearhops! This document provides guidelines and instructions for contributing.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/your-username/Bearhops.git`
3. Create a new branch: `git checkout -b feature/your-feature-name`
4. Make your changes
5. Run tests: `pytest`
6. Commit your changes: `git commit -m "Add your feature"`
7. Push to your fork: `git push origin feature/your-feature-name`
8. Open a Pull Request

## Development Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Copy environment file:
```bash
cp .env.example .env
```

3. Run tests to ensure everything works:
```bash
pytest
```

## Code Style

We use several tools to maintain code quality:

- **Black** for code formatting
- **Ruff** for linting
- **MyPy** for type checking

Run before committing:
```bash
make format
make lint
```

## Testing

All new features should include tests. We use pytest for testing.

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src/bearhops
```

## Pull Request Guidelines

- Write clear, descriptive commit messages
- Include tests for new features
- Update documentation as needed
- Ensure all tests pass
- Keep PRs focused on a single feature or fix

## Reporting Issues

When reporting issues, please include:

- Python version
- Operating system
- Steps to reproduce
- Expected vs actual behavior
- Any error messages or logs

## Code of Conduct

Be respectful and inclusive. We're all here to build something great together.

## Questions?

Feel free to open an issue for any questions about contributing.
