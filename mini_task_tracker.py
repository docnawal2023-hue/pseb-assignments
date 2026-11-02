"""Mini Task Tracker - a menu-based task manager that saves to tasks.json."""

import json

FILENAME = "tasks.json"


def load_tasks():
    """Load tasks from tasks.json. Return an empty list if the file is missing or unreadable."""
    try:
        with open(FILENAME, "r") as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        print("Saved file has an unexpected format. Starting with an empty list.")
    except FileNotFoundError:
        print("No saved tasks found. Starting fresh.")
    except json.JSONDecodeError:
        print("Saved file is corrupted. Starting with an empty list.")
    return []


def save_tasks(tasks):
    """Write the task list to tasks.json."""
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(tasks):
    """Ask for a title and add it as a Pending task."""
    title = input("Task title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added.")


def view_tasks(tasks):
    """Print a numbered list of tasks with their status."""
    if not tasks:
        print("No tasks yet.")
        return
    for i, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Pending"
        print(f"{i}. {task['title']} [{status}]")


def get_task_index(tasks, prompt):
    """Ask for a task number and return its list index, or None if invalid."""
    if not tasks:
        print("No tasks yet.")
        return None
    raw = input(prompt).strip()
    try:
        number = int(raw)
    except ValueError:
        print("Please enter a valid number.")
        return None
    if number < 1 or number > len(tasks):
        print(f"Task number must be between 1 and {len(tasks)}.")
        return None
    return number - 1


def complete_task(tasks):
    """Mark the chosen task as done."""
    index = get_task_index(tasks, "Task number: ")
    if index is None:
        return
    tasks[index]["done"] = True
    save_tasks(tasks)
    print("Task completed.")


def delete_task(tasks):
    """Remove the chosen task."""
    index = get_task_index(tasks, "Task number: ")
    if index is None:
        return
    removed = tasks.pop(index)
    save_tasks(tasks)
    print(f"Deleted: {removed['title']}")


def main():
    tasks = load_tasks()

    while True:
        print("\n--- TASK TRACKER ---")
        print("1. Add 2. View 3. Complete 4. Delete 5. Exit")
        choice = input("Choice: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
