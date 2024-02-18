class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def delete_task(self, index):
        del self.tasks[index]

    def mark_completed(self, index):
        self.tasks[index]["completed"] = True

    def display_tasks(self):
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}. [{'X' if task['completed'] else ' '}] {task['task']}")


def main():
    todo_list = TodoList()

    while True:
        print("\nTODO LIST\n")
        todo_list.display_tasks()
        
        print("\nOptions:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == "2":
            index = int(input("Enter task number to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == "3":
            index = int(input("Enter task number to mark as completed: ")) - 1
            todo_list.mark_completed(index)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
