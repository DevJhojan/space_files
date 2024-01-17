from todo import todo_manager, todo

def main():
    todo_manager = TodoManager()
    while True:
        print("1. Add Todo")
        print("2. Show Todo")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            title = input("Enter title: ")
            description = input("Enter description: ")
            type = input("Enter type: ")
            todo = Todo(title, description, type)
            todo_manager.add_todo(todo)
        elif choice == 2:
            todo_manager.show_todo()
        elif choice == 3:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()