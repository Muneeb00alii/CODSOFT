class TODO_List:
    def __init__(self):
        self.todo_list = []

    def add_task(self, task):
        self.todo_list.append(task)

    def remove_task(self, task):
        self.todo_list.remove(task)

    def get_tasks(self):
        return self.todo_list

    def display_tasks(self):
        if self.todo_list:
            for task in self.todo_list:
                print("\nTask:", task)
                print("-" * 30)
        else:
            print("\nNo tasks found!")

if __name__ == "__main__":
    todo = TODO_List()
    while True:
        print("\nTODO List App")
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Exit")
        choice = input("\nEnter your choice: ")
        if choice == "1":
            task = input("\nEnter task: ")
            todo.add_task(task)
            print("\nTask added successfully!")
        elif choice == "2":
            task = input("\nEnter task to remove: ")
            if task in todo.todo_list:
                todo.remove_task(task)
                print("\nTask removed successfully!")
            else:
                print("\nTask not found!")
        elif choice == "3":
            todo.display_tasks()
        elif choice == "4":
            print("\nThanks for using the app!")
            break
        else:
            print("\nInvalid choice! Try again.")
            continue