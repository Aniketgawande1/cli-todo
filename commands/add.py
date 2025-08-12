import json 
from pathlib import Path 
 
DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "todo.json"

def add_task(title: str):
    """Add a new task to the todo list"""
    try:
        with open(DATA_PATH, "r") as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []

    # Create new task
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False
    }

    tasks.append(task)

    with open(DATA_PATH, "w") as file:
        json.dump(tasks, file, indent=4)
        
    print(f"✅ Task added: {title}")

