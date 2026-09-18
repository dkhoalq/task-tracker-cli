import json
def load_tasks():
    with open("tasks.json", "r", encoding="utf-8") as file:
        return json.load(file)

def save_tasks(tasks):
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)