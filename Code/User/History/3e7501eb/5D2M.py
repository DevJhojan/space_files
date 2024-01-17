from start_todo.todo_manager import TodoManager
from start_todo.todo import Todo
def help():
    print(
        "exit       ->  Exit the program\n"+
        "create     ->  Create 1 new task\n"+
        "cls -a     ->  Delete all tasks\n"+
        "f -1       ->  Find 1 task\n"+
        "show -a    ->  See all tasks\n"+
        "ok - 1     ->  Complete 1 task"
    )
def main():
    manager = TodoManager()
    manager.read_to_file()
    sw = 1
    while True:
        if sw == 1:
            manager.show_tasks()
        else:
            print("----------")
        print("----------")
        inp = input(">")
        if inp == "show -a":
            manager.show_tasks()
        if inp == "exit":
            break
        if inp == "cls -a":
            manager.clear_todos()
            manager.save_to_file()
            print("all clear")
        if inp == "create":
            state = False
            title = input("Title: ")
            description = input("Description: ")
            category = input("Category: ")
            new_todo = Todo(title, description, category, state)
            manager.add_todo(new_todo)
            manager.save_to_file()
        if inp == "ok -1":
            id = input("Id of task: ")
            manager.completeTask(int(id))
        if inp == "help":
            help()
        print("----------")
        sw = 0

if __name__ == "__main__":
    main()
