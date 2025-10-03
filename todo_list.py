# Unique To-Do List App 📝
# Features: Save tasks, priority levels, completion timestamp

import json
from datetime import datetime

# Load tasks from file if it exists
try:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Mark task as done")
    print("4. Delete a task")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("\nNo tasks yet!")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "✅" if task["done"] else "❌"
            timestamp = f"(Completed: {task['completed_at']})" if task["done"] else ""
            print(f"{i}. {task['name']} | Priority: {task['priority']} {status} {timestamp}")

def add_task():
    name = input("\nEnter a new task: ")
    priority = input("Enter priority (High/Medium/Low): ").capitalize()
    tasks.append({"name": name, "priority": priority, "done": False, "completed_at": ""})
    save_tasks()
    print(f"Added: {name} with priority {priority}")

def mark_done():
    view_tasks()
    task_num = int(input("\nEnter task number to mark as done: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]["done"] = True
        tasks[task_num]["completed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
        save_tasks()
        print(f"Marked '{tasks[task_num]['name']}' as done ✅")
    else:
        print("Invalid number!")

def delete_task():
    view_tasks()
    task_num = int(input("\nEnter task number to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        removed = tasks.pop(task_num)
        save_tasks()
        print(f"Deleted: {removed['name']}")
    else:
        print("Invalid number!")

# Main loop
while True:
    show_menu()
    choice = input("\nEnter your choice: ")
    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye 👋")
        break
    else:
        print("Invalid choice, try again.")
