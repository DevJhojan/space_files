from todo import Todo

class TodoManager:
    def __init__(self):
        self.todos = []
    def add_todo(self, todo):
        self.todos.append(todo)
