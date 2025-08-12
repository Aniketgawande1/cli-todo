import json
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "todo.json"

def list_tasks():
    """List all tasks"""
    try:
        with open(DATA_PATH, "r") as file:
            tasks = json.load(file)
        
        if not tasks:
            print("📝 No tasks found!")
            return
        
        print("📋 Your Tasks:")
        print("-" * 40)
        
        for task in tasks:
            status = "✅" if task["completed"] else "❌"
            print(f"{task['id']}. {status} {task['title']}")
            
    except FileNotFoundError:
        print("📝 No tasks found! Add some tasks first.")
    except json.JSONDecodeError:
        print("❌ Error reading tasks file.")