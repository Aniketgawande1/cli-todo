import sys
import os

# Add commands directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'commands'))

from add import add_task
from list import list_tasks
from remove import remove_task

def dispatch(command, args):
    """Dispatch commands to appropriate handlers"""
    
    if command == "add":
        if not args:
            print("❌ Usage: add <task_title>")
            return
        title = " ".join(args)
        add_task(title)
    
    elif command == "list":
        list_tasks()
    
    elif command == "remove":
        if not args:
            print("❌ Usage: remove <task_id>")
            return
        try:
            task_id = int(args[0])
            remove_task(task_id)
        except ValueError:
            print("❌ Task ID must be a number")
    
    else:
        print(f"❌ Unknown command: {command}")
        print("Available commands: add, list, remove")