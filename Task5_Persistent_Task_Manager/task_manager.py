
import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("tasks.json")


def load_tasks():
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            tasks = json.load(file)
            return tasks if isinstance(tasks, list) else []
    except (OSError, json.JSONDecodeError) as error:
        print(f"Could not load tasks: {error}")
        return []


def save_tasks(tasks):
    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4)
        return True
    except OSError as error:
        print(f"Could not save tasks: {error}")
        return False


def create_task(tasks):
    title = input("Task title: ").strip()
    description = input("Task description: ").strip()

    if not title:
        print("Title cannot be empty.")
        return

    next_id = max((task["id"] for task in tasks), default=0) + 1
    tasks.append({
        "id": next_id,
        "title": title,
        "description": description,
        "status": "Pending"
    })

    if save_tasks(tasks):
        print("Task created and saved successfully!")


def read_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    for task in tasks:
        print(f"\nID: {task['id']}")
        print(f"Title: {task['title']}")
        print(f"Description: {task['description']}")
        print(f"Status: {task['status']}")


def update_task(tasks):
    read_tasks(tasks)
    try:
        task_id = int(input("\nEnter task ID to update: "))
    except ValueError:
        print("Enter a valid numeric ID.")
        return

    for task in tasks:
        if task["id"] == task_id:
            title = input(f"New title [{task['title']}]: ").strip()
            description = input(
                f"New description [{task['description']}]: "
            ).strip()
            status = input(
                f"New status [{task['status']}]: "
            ).strip()

            if title:
                task["title"] = title
            if description:
                task["description"] = description
            if status:
                task["status"] = status

            if save_tasks(tasks):
                print("Task updated and saved!")
            return

    print("Task not found.")


def delete_task(tasks):
    read_tasks(tasks)
    try:
        task_id = int(input("\nEnter task ID to delete: "))
    except ValueError:
        print("Enter a valid numeric ID.")
        return

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            if save_tasks(tasks):
                print("Task deleted and changes saved!")
            return

    print("Task not found.")


def main():
    tasks = load_tasks()
    print("Persistent Task Manager")
    print(f"Loaded {len(tasks)} saved task(s).")

    while True:
        print("\n1. Create task")
        print("2. View tasks")
        print("3. Update task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose (1-5): ").strip()

        if choice == "1":
            create_task(tasks)
        elif choice == "2":
            read_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Tasks are saved. Goodbye!")
            break
        else:
            print("Invalid choice. Select 1-5.")


if __name__ == "__main__":
    main()
