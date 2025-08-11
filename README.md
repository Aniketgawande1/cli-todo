

# ✅ To-Do CLI App — Manage Your Tasks from the Terminal

Hey there! 👋  
This is a simple yet powerful **command-line To-Do list application** built with **Python**. You can add tasks, view them, and remove them — all from your terminal 💻

---

## ⚙️ Features

- 📝 Add tasks via command line
- 📃 View all your tasks with status indicators
- ❌ Remove tasks by ID
-  Data stored locally in a `todo.json` file
- 🔧 Modular, well-structured code — easy to read and extend
- 🌱 Great for learning Python and contributing

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository:

```bash
git clone https://github.com/Aniketgawande1/cli-todo.git
cd cli-todo
```

### 2️⃣ Navigate to the todo directory:

```bash
cd todo
```

### 3️⃣ Run the App:

```bash
# Add a new task
python main.py add "Buy groceries"

# List all tasks
python main.py list

# Remove a task by ID
python main.py remove 1
```

---

## 🧠 Available Commands

| Command | Description | Usage Example |
|---------|-------------|---------------|
| `add` | Add a new task | `python main.py add "Task description"` |
| `list` | List all tasks | `python main.py list` |
| `remove` | Remove a task by ID | `python main.py remove 1` |

### Command Examples:

```bash
# Adding tasks
python main.py add "Complete Python project"
python main.py add "Buy milk from store"
python main.py add "Call dentist for appointment"

# Viewing all tasks
python main.py list
# Output:
# 📋 Your Tasks:
# ----------------------------------------
# 1. ❌ Complete Python project
# 2. ❌ Buy milk from store
# 3. ❌ Call dentist for appointment

# Removing a task
python main.py remove 2
# Output: 🗑️ Task removed: Buy milk from store
```

---

## 🗂 Project Structure

```
todo-cli/
├── todo/
│   ├── main.py             # App entry point
│   ├── parser.py           # Command line argument parser
│   ├── dispatcher.py       # Routes commands to appropriate handlers
│   └── exceptions.py       # Custom error handling
├── commands/
│   ├── __init__.py         # Package initialization
│   ├── add.py              # Add task functionality
│   ├── list.py             # List tasks functionality
│   └── remove.py           # Remove task functionality
├── data/
│   └── todo.json           # Local JSON data storage
└── utils/
    ├── styles.py           # Terminal styling utilities
    ├── menu.py             # Menu display utilities
    └── compatibility.py    # Cross-platform compatibility
```

---

## 🛠 How It Works

1. **Parser**: `parser.py` handles command line arguments
2. **Dispatcher**: `dispatcher.py` routes commands to the right functions
3. **Commands**: Individual command modules handle specific functionality
4. **Data Storage**: Tasks are stored in `data/todo.json` in JSON format
5. **Utilities**: Helper functions for styling and cross-platform compatibility

### Data Format
Tasks are stored as JSON objects with the following structure:
```json
[
  {
    "id": 1,
    "title": "Task description",
    "completed": false
  }
]
```

---

## � Requirements

- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

Potential features to add:
- Task completion/checking functionality
- Task editing/renaming
- Due dates for tasks
- Task categories or tags
- Search functionality
- Export/import features

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Created by [Aniket Gawande](https://github.com/Aniketgawande1)

If you found this useful, feel free to ⭐ the repo and share it with others!

If you found this useful, feel free to ⭐ the repo and share it with others!
Pull requests are welcome.

---

```

---

## ✅ Want More Polish?

Let me know if you want me to:
- Add **demo GIFs or terminal screenshots**
- Include **badges** (Python version, License, GitHub stars, etc.)
- Write a **minimal Hindi version** too
- Add an **interactive CLI menu**

Just say the word, and I’ll help you level this up for your GitHub profile!
```
