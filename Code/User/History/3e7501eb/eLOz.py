from start_todo.todo_manager import TodoManager
from start_todo.todo import Todo
def main():
    manager = TodoManager()
    manager.read_to_file()  
    manager.show_tasks()
    while True:
        print("----------")
        inp = input("1.exit\n2.save file\n3:clear all\n4:add task\n")

        if inp == "1":
            break
        if inp == "2":
            manager.save_to_file()
            print("file save")
        if inp == "3":
            manager.clear_todos()
            print("all clear")
       
        if inp == "4":
            state = False
            title = input("Title: ")
            description = input("Description: ")
            category = input("Category: ")
            new_todo = Todo(title, description, category, state)
            manager.add_todo(new_todo)
        else:
            print("wrong input")
       
        

if __name__ == "__main__":
    main()
