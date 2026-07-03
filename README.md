# python-ai-learning
python-ai-learning demo within one month

<!-- Making project steps -->

python --version
pip --version
pip install poetry
poetry --version

poetry new python-ai-project

poetry env info

<!-- this will open a shell for python coding -->
poetry shell
poetry run python

<!-- Add FastAPI -->
poetry add fastapi
Poetry updates: pyproject.toml, poetry.lock

<!-- Add Uvicorn -->
FastAPI needs an ASGI server:
poetry add uvicorn

or install with standard extras:
poetry add "uvicorn[standard]"

<!-- Install Development Dependencies -->
poetry add --group dev pytest

Add formatting and linting tools:
poetry add --group dev black
poetry add --group dev ruff

<!-- Manually runing the application  -->
poetry run uvicorn src.app.main:app --reload

http://127.0.0.1:8000/


ai-fastapi-project/
│
├── app/
│   ├── main.py
│   ├── routers/
│   ├── services/
│   ├── models/
│   ├── schemas/
│   ├── database/
│   ├── utils/
│   └── config.py
│
├── tests/
├── pyproject.toml
├── poetry.lock
└── README.md

=====================================================================================
=====================================================================================


Poetry is a Python dependency and project management tool. It:

Creates and manages virtual environments automatically.
Installs dependencies.
Locks dependency versions for reproducible builds.
Packages Python projects.

pip install poetry
poetry --version
poetry new python-ai-learning

=====================================================================================
=====================================================================================

For FastAPI, many developers prefer creating an empty folder and initializing Poetry:

mkdir ai-fastapi-project
cd ai-fastapi-project
poetry init => and have to set project definition

poetry install
poetry env info


Recommended setup for your AI learning

| Purpose                   | Tool                          |
| ------------------------- | ----------------------------- |
| Code editor               | VS Code                       |
| Python version management | Python 3.12 or 3.13           |
| Dependency management     | Poetry                        |
| Virtual environments      | Poetry (or `venv`)            |
| API framework             | FastAPI                       |
| Interactive notebooks     | Jupyter                       |
| AI models                 | Ollama (local) and OpenAI API |
| Database                  | PostgreSQL                    |
| Vector database           | ChromaDB or FAISS             |
| Containerization          | Docker                        |
| Version control           | Git + GitHub                  |


My recommendation for you

Since you've been asking about FastAPI, Docker, AWS, IoT, Saga patterns, and Python interview preparation, I recommend this stack:

IDE: VS Code
Package manager: Poetry
Database: PostgreSQL
AI framework: LangChain
LLM: Ollama (for local development) and OpenAI API
Vector database: ChromaDB
API framework: FastAPI
Deployment: Docker + Nginx + AWS EC2
Version control: GitHub

This is a modern stack that's widely used for production AI applications and aligns well with senior Python/AI engineering roles.