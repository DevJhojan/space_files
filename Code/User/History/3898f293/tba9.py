from todo.todo_manager import TodoManager
from todo.todo import Todo

def main():
    manager = TodoManager()

    while True:
        print("1. Add Todo")
        print("2. Show Todo")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            title = input("Enter title: ")
            description = input("Enter description: ")
            type = input("Enter type: ")
            new_todo = Todo(title, description, type)
            manager.add_todo(new_todo)
        elif choice == 2:
            manager.show_todo()
        elif choice == 3:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()