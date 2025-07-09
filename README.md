

 ✅ `README.md` — To-Do CLI App (Python)

````md
# ✅ To-Do CLI App — Manage Your Tasks from the Terminal

Hey there! 👋  
This is a beginner-friendly yet powerful **command-line To-Do list application** built with **Python**. You can add tasks, view them, mark as complete, remove them — all from your terminal 💻

---

## ⚙️ Features

- 📝 Add tasks via command line
- 📃 View all your tasks (pending & completed)
- ✅ Mark tasks as complete or incomplete
- ❌ Remove tasks by ID
- 🛠 Rename, search, toggle tasks
- 💾 Data stored locally in a `todos.json` file
- 🔧 Modular, well-structured code — easy to read and extend
- 🌱 Great for learning Python and contributing

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository:

```bash
git clone https://github.com/adityawarekar/todo-cli.git
cd todo-cli
````

### 2️⃣ Set up a Virtual Environment (recommended):

```bash
python -m venv venv
source venv/bin/activate        # For Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies (if using Typer/Rich):

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the App:

```bash
python todo/main.py add "Finish the Python CLI project"
python todo/main.py list
```

---

## 🧠 Available Commands

| Command   | Description                   |
| --------- | ----------------------------- |
| `add`     | Add a new task                |
| `list`    | List all tasks                |
| `remove`  | Remove a task by ID           |
| `check`   | Mark a task as completed      |
| `uncheck` | Mark a task as not completed  |
| `rename`  | Rename a task                 |
| `search`  | Search tasks by keyword       |
| `toggle`  | Toggle task completion status |

---

## 🗂 Project Structure

```
todo-cli/
├── todo/
│   ├── main.py             # App entry point
│   ├── parser.py           # Argument parser
│   ├── dispatcher.py       # Command dispatcher
│   ├── exceptions.py       # Custom error handling
│   ├── commands/           # All command modules
│   │   ├── add.py, list.py, remove.py, ...
│   ├── utils/              # Helpers and formatters
│   │   ├── styles.py, menu.py, compatibility.py
│   └── data/
│       └── todos.json      # Local JSON data file
```

---

## 📸 Screenshots / Demo (Optional)

> *(Insert a GIF or terminal screenshot of adding & listing tasks here)*

---

## 👨‍💻 Created by [Aniket Gawande](https://github.com/Aniketgawande1)

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
