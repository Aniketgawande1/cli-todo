import json
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "todo.json"

def remove_task(task_id):
    """Remove a task by ID"""
    try:
        with open(DATA_PATH, "r") as file:
            tasks = json.load(file)
        
        # Find and remove task with matching ID
        task_found = False
        for i, task in enumerate(tasks):
            if task["id"] == task_id:
                removed_task = tasks.pop(i)
                task_found = True
                break
        
        if not task_found:
            print(f"❌ Task with ID {task_id} not found!")
            return
        
        # Save updated tasks
        with open(DATA_PATH, "w") as file:
            json.dump(tasks, file, indent=4)
        
        print(f"🗑️ Task removed: {removed_task['title']}")
        
    except FileNotFoundError:
        print("📝 No tasks found!")
    except json.JSONDecodeError:
        print("❌ Error reading tasks file.")