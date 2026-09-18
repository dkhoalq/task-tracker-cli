import os
import json
from datetime import datetime
import sys
from storage import load_tasks, save_tasks

now = datetime.now()
time_now = now.strftime("%m/%d/%Y, %H:%M:%S")

def find_task(tasks, task_id):
    if task_id <= len(tasks):
        for task in tasks:
            if task['ID'] == task_id:
                return task
    else:
        return {}


def add(title):
    if(len(sys.argv) == 2):
        print("You need to add something.")
    else:
        if os.path.exists("tasks.json"):
           tasks = load_tasks()
        else:
           tasks = []
    
        task_id = len(tasks) + 1
        new_task = {
            "ID" : task_id,
            "Title" : title,
            "Status" : "todo",
            "CreatedAt" : time_now,
            "UpdatedAt" : time_now
        }
        tasks.append(new_task)
        save_tasks(tasks)
        print(f"Task added successfully (ID: {task_id})")

def list():
    if os.path.exists("tasks.json"):
        tasks = load_tasks()
    if tasks == []:
        print("You are currently having no task.")
    else:
        if len(sys.argv) == 2:
            for dict in tasks:
                print(f"ID: {dict['ID']} - Title: {dict['Title']} - Status: {dict['Status']}")
                print(f"CreatedAt: {dict['CreatedAt']} - UpdatedAt: {dict['UpdatedAt']}")
                print()
        else:
            found = False
            for dict in tasks:
                if dict['Status'] == sys.argv[2]:
                    found = True
                    print(f"ID: {dict['ID']} - Title: {dict['Title']} - Status: {dict['Status']}")
                    print(f"CreatedAt: {dict['CreatedAt']} - UpdatedAt: {dict['UpdatedAt']}")
                    print()
            if found == False:
                print("No file found.")

def update(update_id, newtitle):
    try:
        if os.path.exists("tasks.json"):
            tasks = load_tasks()
            task = find_task(tasks, update_id)
            if task == {}:
                print(f"There is no task with ID {update_id}")
            else:
                task['Title'] = newtitle
                task['UpdatedAt'] = time_now
                save_tasks(tasks)
                print("Update successfully")
        else:
            print("You need to create a task tracker first.")
    except ValueError:
        print("Invalid ID. Please input the ID as a number.")

def delete(delete_id):
    tasks = load_tasks()
    task = find_task(tasks, delete_id)
    if task == {}:
        print(f"There is no task with ID {delete_id}")
    else:
        tasks.remove(task)
        for task in tasks:
            if(task['ID'] > delete_id):
                task['ID'] = task['ID'] - 1
        print("Delete successfully")
        save_tasks(tasks)

def mark_in_progress(change_id):
    tasks = load_tasks()
    task = find_task(tasks, change_id)
    if task == {}:
        print(f"There is no task with ID {change_id}")
    else:
        task['Status'] = "in-progress"
        task['UpdatedAt'] = time_now
        print("Change status successfully.")
        save_tasks(tasks)

def mark_done(change_id):
    tasks = load_tasks()
    task = find_task(tasks, change_id)
    if task == {}:
        print(f"There is no task with ID {change_id}")
    else:
        task['Status'] = "done"
        task['UpdatedAt'] = time_now
        print("Change status successfully.")
        save_tasks(tasks)

def invalid():
    print("Invalid command.")
    print("Please use the following commands:")
    print("'add' - To add a new task to the tracker.")
    print("'list' - To view all tasks in the tracker.")
    print("'update' - To update the name of an existing task.")
    print("'delete' - To delete an existing task.")
    print("'mark_in_progress' - To change an existing task's status to 'in-progress'")
    print("'make_done' - To change an existing task's status to 'done'")