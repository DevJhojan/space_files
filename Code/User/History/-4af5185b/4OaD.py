from todo import Todo
import json
class TodoManager:
    def __init__(self):
        self.todos = []
    def add_todo(self, todo):
        todo = Todo(todo)
        self.todos.append(todo)
        with open('todos.json','w') as file:
            json.dump(self.todos , file)
        print(f"Added todo '{todo.title}'")
    def show_todo(self):
        if not self.todos:
            print("There are no Task")
        else:
            for i, todo in enumerate(self.todos, 1):
                print(f"{todo.__str__}")