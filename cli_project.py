import json
import os

filename = "tasks.json"

def load_tasks():
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return {}

def save_tasks(tasks):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks, task_name):
    tasks[task_name] = "pending"
    save_tasks(tasks)
    print(f"Task ' {task_name}' added.")

def delete_task(tasks, task_name):
    if task_name in tasks:
        del tasks[task_name]
        save_tasks(tasks)
        print(f"Task ' {task_name}' deleted.")
    else:
        print(f"Task ' {task_name}' not found.")

def list_tasks(tasks):
    if tasks:
        print("Tasks:")
        for name, status in tasks.items():
             print(f"- {name} [{status}]")
            
    else:
        print("No tasks found.")

def mark_done(tasks, task_name):
    if task_name in tasks:
        tasks[task_name] = "done"
        save_tasks(tasks)
        print(f"Task ' {task_name}' marked as done.")
    else:
        print(f"Task ' {task_name}' not found.")

def main():
    tasks = load_tasks()

    while True:
        command = input("Enter command (add, delete, list, done, exit): ").strip().lower()
        if command == "add":
            task_name = input("Enter task name: ")
            add_task(tasks, task_name)

        elif command == "delete":
            task_name = input("Enter task name: ")
            delete_task(task_name)
        
        elif command == "list":
            list_tasks(tasks)

        elif command == "done":
            task_name = input("Enter task name: ")
            mark_done(task_name)

        elif command == "exit":
            print("Exiting...")
            break
        else:
            print("Invalid command. Please try again.")


main()