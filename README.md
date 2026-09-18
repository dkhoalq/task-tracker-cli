# Task Tracker CLI

A simple command-line task tracker built with Python.

This project was created as a learning project to practice Python, command-line arguments, JSON file handling, functions, modules, and error handling.

## Features

- Add new tasks
- List tasks
- Update task descriptions
- Mark tasks as `in-progress`
- Mark tasks as `done`
- Delete tasks
- Store tasks persistently in a JSON file
- Handle invalid user input

## Project Structure

```text
task-tracker/
├── task_cli.py
├── task_manager.py
├── storage.py
├── tasks.json
├── README.md
└── .gitignore
```

### Files

- `task_cli.py` — handles command-line input and commands
- `task_manager.py` — contains task management logic
- `storage.py` — handles loading and saving tasks
- `tasks.json` — stores the tasks
- `README.md` — project documentation
- `.gitignore` — specifies files that Git should ignore

## Requirements

- Python 3.x

No external Python packages are required.

## Usage

Run the program using:

```bash
python task_cli.py <command> [arguments]
```

### Add a task

```bash
python task_cli.py add "Learn Python"
```

### List all tasks

```bash
python task_cli.py list
```

### List tasks by status

```bash
python task_cli.py list todo
python task_cli.py list in-progress
python task_cli.py list done
```

### Update a task

```bash
python task_cli.py update 1 "Learn advanced Python"
```

### Mark a task as in progress

```bash
python task_cli.py mark-in-progress 1
```

### Mark a task as done

```bash
python task_cli.py mark-done 1
```

### Delete a task

```bash
python task_cli.py delete 1
```

## Data Storage

Tasks are stored locally in `tasks.json`.

Each task contains information such as:

- ID
- Title
- Status
- Creation time
- Last updated time

## Technologies

- Python
- JSON
- Git / GitHub

## Project Status

This project is currently being developed as a learning project.