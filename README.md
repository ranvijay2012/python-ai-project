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

<!-- Option 1: Run directly from the VS Code ▶️ Run button (Recommended) -->

Your current code is almost correct, but the app path is wrong.

Since main.py is inside the src folder, change:

uvicorn.run(
    "src.main:app",
    host="127.0.0.1",
    port=8000,
    reload=True
)

Now: Open main.py
Click the ▶ Run Python File button in the top-right corner.
VS Code will execute

python src/main.py  and your FastAPI server will start automatically.


<!-- Option 2: Press F5 (Best for Development) -->
Create a .vscode folder.
Inside it create launch.json.

python-ai-project/
│
├── .vscode/
│   └── launch.json
├── src/
│   └── main.py

launch.json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Run FastAPI",
            "type": "python",
            "request": "launch",
            "module": "uvicorn",
            "args": [
                "src.main:app",
                "--reload"
            ],
            "jinja": true
        }
    ]
}

Now simply press F5.
No terminal command is required.

<!-- Option 3: Create a Run Task -->
Create .vscode/tasks.json

{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Run FastAPI",
            "type": "shell",
            "command": "poetry run uvicorn src.main:app --reload"
        }
    ]
}

Now press: Ctrl + Shift + B
and VS Code starts the server.

<!-- Option 4: Run by clicking the Python file -->
Your main.py should be:

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}

if __name__ == "__main__":
    uvicorn.run(
        "src.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )

Then simply click the Run (▶) button.


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