import os

def display_tasks(tasks):
    print("Your To-Do List:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

def add_task(tasks, new_task):
    tasks.append(new_task)
    print("Task added successfully!")

def remove_task(tasks, index):
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        print(f"Task '{removed_task}' removed successfully!")
    else:
        print("Invalid task index!")

def save_tasks_to_file(tasks, filename="todo_list.txt"):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def load_tasks_from_file(filename="todo_list.txt"):
    tasks = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    return tasks

def main():
    tasks = load_tasks_from_file()

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark as Completed")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            new_task = input("Enter the new task: ")
            add_task(tasks, new_task)
        elif choice == "2":
            display_tasks(tasks)
        elif choice == "3":
            display_tasks(tasks)
            index = int(input("Enter the index of the completed task: "))
            remove_task(tasks, index)
        elif choice == "4":
            save_tasks_to_file(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()