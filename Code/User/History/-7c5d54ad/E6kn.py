#todo_manager.py
from start_todo.todo import Todo
import json
class TodoManager:
    def __init__(self):
        self.todos = []
   """
   
   """ 
        todo = Todo(title, description, category, state)
        self.todos.append(todo)
    def clear_todos(self):
        self.todos = []
    def save_to_file(self):
        with open('Todos.json', 'w') as file:
            json.dump(self.todos, file, default=lambda obj: obj.__dict__, indent=2)
    def show_tasks(self):
        for todo in self.todos:
            print(todo.__str__())
    def read_to_file(self):
        with open('Todos.json', 'r') as file:
            todo_data= json.load(file)
            for todo in todo_data:
                task = Todo(todo.get('title', ''), todo.get('description', ''), todo.get('category',''), todo.get('e¿state',''))
                self.todos.append(task)