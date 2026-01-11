# AI Agent Starter Template

> **Note:** This is a high-performance, asynchronous Python template designed for building scalable AI agents and services. It comes pre-configured with industry-standard patterns for configuration, database management, and AI model integration.

## 🚀 Overview

This repository serves as a foundational boilerplate for software engineers building production-ready AI applications. It abstracts away the repetitive setup of environment management, database connectivity, and tool orchestration, allowing developers to focus immediately on business logic and agent behaviors.

Built with **Modern Python** principles, it emphasizes type safety, asynchronous operations, and modular architecture.

## ✨ Key Features

* **Robust Configuration Management**: Centralized, type-safe environment configuration using `pydantic-settings` and `.env` files.
* **Async Database Layer:** Pre-configured SQLAlchemy 2.0+ setup with asynchronous session management and connection pooling.
* **AI Tooling Interface:** Structured directory for defining and registering AI tools (compatible with agents like Claude or OpenAI Assistants).
* **Telemetry & Logging:** Integrated structured logging via `rich` for beautiful console output and easy debugging.
* **Modular Architecture:** Clean separation of concerns between configuration, database, AI logic, and observability.

## 🛠️ Project Structure

```text
starterTemplate/
├── ai/                 # AI capabilities and tool definitions
│   ├── prompts/        # System prompts and agent personas
│   └── tools/          # Executable tools for agents (File I/O, Search, etc.)
├── config/             # Application configuration & Environment variables
├── db/                 # Database schema, dependencies, and connection pooling
├── telemetry/          # Logging and observability configuration
└── .gitignore          # Git ignore rules
```

## ⚡ Getting Started

### Prerequisites

* Python 3.10+
* PostgreSQL (optional, for database features)
* Git

### 1. Installation

Clone the repository and set up your virtual environment.

```bash
# Clone the repository
git clone <repository-url>
cd starterTemplate

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies (inferred)
pip install fastapi sqlalchemy pydantic-settings python-dotenv rich langchain-core asyncpg
```

### 2. Configuration

Create a `.env` file in the root directory. This project uses a strict configuration schema to ensure all necessary variables are present.

**`.env` Example:**

```ini
# General
ENV=development
PRODUCT_NAME=MyAIApp
APP_URL=http://localhost:8000
LANDING_URL=http://localhost:3000

# Database (PostgreSQL)
DB_HOST=localhost
DB_PORT=5432
DB_NAME=myapp_db
DB_USER=postgres
DB_PASSWORD=secret

# AI Providers
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4-turbo
ANTHROPIC_API_KEY=sk-ant-...
ANTHROPIC_MODEL=claude-3-opus

# GitHub Integration (Optional)
GITHUB_TOKEN=ghp_...
GITHUB_BASE_URL=https://api.github.com
```

### 3. Usage

#### Database Session

The project provides a FastAPI-ready dependency for database sessions.

```python
from app.db.dependencies import get_db_session
from sqlalchemy.ext.asyncio import AsyncSession

async def my_endpoint(session: AsyncSession = Depends(get_db_session)):
    # Use session here
    pass
```

#### AI Tools

Tools are defined in `ai/tools/` and can be compiled for use with LangChain or other agent frameworks.

```python
from ai.tools.tools import tools_compiler
from pathlib import Path

# Initialize tools bound to a specific path
project_root = Path("/path/to/analyze")
available_tools = tools_compiler(project_root)
```

## 📘 Configuration Reference

### Environment Variables (`config/env.py`)

| Variable              | Description                                             | Required |
| :-------------------- | :------------------------------------------------------ | :------: |
| `ENV`               | Environment mode (e.g.,`development`, `production`) |   Yes   |
| `PRODUCT_NAME`      | Name of the application                                 |   Yes   |
| `APP_URL`           | Base URL of the application backend                     |   Yes   |
| `OPENAI_API_KEY`    | API Key for OpenAI services                             |   Yes   |
| `ANTHROPIC_API_KEY` | API Key for Anthropic services                          |   Yes   |

### Database Settings (`db/schema.py`)

Database settings are automatically prefixed with `DB_`.

| Variable         | Default       | Description                     |
| :--------------- | :------------ | :------------------------------ |
| `DB_HOST`      | `localhost` | Database server host            |
| `DB_PORT`      | `5432`      | Database server port            |
| `DB_NAME`      | `app`       | Database name                   |
| `DB_POOL_SIZE` | `10`        | SQLAlchemy connection pool size |

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/amazing-feature`.
3. Commit your changes: `git commit -m 'Add amazing feature'`.
4. Push to the branch: `git push origin feature/amazing-feature`.
5. Open a Pull Request.

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---
