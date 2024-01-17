from todo import Todo

class TodoManager:
    def __init__(self):
        self.todos = []
    def add_todo(self, todo):
        todo = Todo(todo)
        self.todos.append(todo)
        print(f"Added todo '{todo.name}'")
    def show_todo(self):
        if not self.todos:
            print("No todos")