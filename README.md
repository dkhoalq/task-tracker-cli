# Task Tracker CLI

A simple command-line task tracker built with Python: https://roadmap.sh/projects/task-tracker

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
├── .gitignore
└── pyproject.toml
```

### Files

- `task_cli.py` — handles command-line input and commands
- `task_manager.py` — contains task management logic
- `storage.py` — handles loading and saving tasks
- `tasks.json` — stores the tasks
- `README.md` — project documentation
- `.gitignore` — specifies files that Git should ignore
- `pyproject.toml` — allows usage of customized commands

## Requirements

- Python 3.x

No external Python packages are required.

## Usage

Run the program using:

```bash
task-cli <command> [arguments]
```

### Add a task

```bash
task-cli add "Learn Python"
```

### List all tasks

```bash
task-cli list
```

### List tasks by status

```bash
task-cli list todo
task-cli list in-progress
task-cli list done
```

### Update a task

```bash
task-cli update 1 "Learn advanced Python"
```

### Mark a task as in progress

```bash
task-cli mark-in-progress 1
```

### Mark a task as done

```bash
task-cli mark-done 1
```

### Delete a task

```bash
task-cli delete 1
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