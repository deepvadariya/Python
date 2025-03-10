import os

TODO_FILE = "todo.txt"

def load_tasks():
    try:
        with open(TODO_FILE, "r") as file:
            return [task.strip() for task in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(tasks):
    while True:
        task = input("Enter a new task: ").strip()
        if task:
            tasks.append(f"[ ] {task}")
            print("Task added successfully!")
            break
        else:
            print("Task cannot be empty.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def mark_completed(tasks):
    view_tasks(tasks)
    while True:
        try:
            task_num = int(input("Enter the task number to mark as completed: "))
            if 1 <= task_num <= len(tasks):
                task = tasks[task_num - 1]
                if "[ ]" in task:
                    tasks[task_num - 1] = task.replace("[ ]", "[X]")
                    print("Task marked as completed!")
                    break
                else:
                    print("Task is already completed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    while True:
        try:
            task_num = int(input("Enter the task number to delete: "))
            if 1 <= task_num <= len(tasks):
                deleted_task = tasks.pop(task_num - 1)
                print(f"Deleted task: {deleted_task}")
                break
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Your tasks have been saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
