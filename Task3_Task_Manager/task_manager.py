# Cognifyz Technologies - Software Development Internship
# Level 2 - Task 3: Console CRUD Task Manager


class Task:
    def __init__(self, task_id, title, description, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = status

    def display(self):
        print(f"\nTask ID     : {self.task_id}")
        print(f"Title       : {self.title}")
        print(f"Description : {self.description}")
        print(f"Status      : {self.status}")


tasks = []


def create_task():
    task_id = len(tasks) + 1

    title = input("Enter task title: ")
    description = input("Enter task description: ")

    task = Task(task_id, title, description)
    tasks.append(task)

    print("\nTask created successfully!")


def read_tasks():
    if not tasks:
        print("\nNo tasks available.")
        return

    print("\n========== TASK LIST ==========")

    for task in tasks:
        task.display()

    print("\n==============================")


def update_task():
    if not tasks:
        print("\nNo tasks available to update.")
        return

    read_tasks()

    try:
        task_id = int(input("\nEnter Task ID to update: "))
    except ValueError:
        print("Please enter a valid Task ID.")
        return

    for task in tasks:
        if task.task_id == task_id:
            print("\nLeave a field empty to keep the existing value.")

            new_title = input(f"Enter new title [{task.title}]: ")
            new_description = input(
                f"Enter new description [{task.description}]: "
            )
            new_status = input(
                f"Enter new status [{task.status}]: "
            )

            if new_title:
                task.title = new_title

            if new_description:
                task.description = new_description

            if new_status:
                task.status = new_status

            print("\nTask updated successfully!")
            return

    print("\nTask not found.")


def delete_task():
    if not tasks:
        print("\nNo tasks available to delete.")
        return

    read_tasks()

    try:
        task_id = int(input("\nEnter Task ID to delete: "))
    except ValueError:
        print("Please enter a valid Task ID.")
        return

    for task in tasks:
        if task.task_id == task_id:
            tasks.remove(task)
            print("\nTask deleted successfully!")
            return

    print("\nTask not found.")


def main():
    while True:
        print("\n================================")
        print("          TASK MANAGER")
        print("================================")
        print("1. Create Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        print("================================")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            create_task()

        elif choice == "2":
            read_tasks()

        elif choice == "3":
            update_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            print("\nThank you for using Task Manager!")
            break

        else:
            print("\nInvalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()