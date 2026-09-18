import sys
from datetime import datetime
import json
import os
from task_manager import add, list, update, delete, mark_in_progress, mark_done, invalid

if(len(sys.argv) == 1):
    print("No command provided. Please enter a command.")
else:
    command = sys.argv[1]
    if(command == "add"):
        if(len(sys.argv) < 3):
            print("You need to add something.")
        else:
            title = sys.argv[2]
            add(title)

    elif(command == "list"):
        list()

    elif(command == "update"):
        if(len(sys.argv) < 4):
            print("You need to update something.")
        else:
            try:
                update_id = int(sys.argv[2])
                newtitle = sys.argv[3]
                update(update_id, newtitle)
            except ValueError:
                print("Invalid ID. Please input the ID as a number.")

    elif(command == "delete"):
        if(len(sys.argv) <= 2):
                print("You need to delete something (Insert task ID).")
        else:
            try:
                delete_id = int(sys.argv[2])
                delete(delete_id)
            except ValueError:
                print("Invalid ID. Please input the ID as a number.")

    elif(command == "mark_in_progress"):
        if(len(sys.argv) <= 2):
            print("You need to insert something to change the status (Insert task ID).")
        else:
            try:
                change_id = int(sys.argv[2])
                mark_in_progress(change_id)
            except ValueError:
                print("Invalid ID. Please input the ID as a number.")

    elif(command == "mark_done"):
        if(len(sys.argv) <= 2):
            print("You need to insert something to change the status (Insert task ID).")
        else:
            try:
                change_id = int(sys.argv[2])
                mark_done(change_id)
            except ValueError:
                print("Invalid ID. Please input the ID as a number.")

    else:
        invalid()