#todo_manager.py
from .models.todo import Todo
from .models.todo_type import TodoINU, TodoIU
import json
class TodoManager:
    def __init__(self):
        self.todos = []
    def add_todo(self, new_todo):
        self.todos.append(new_todo)
    def completeTask(self, id):
        for todo in self.todos:
            print(type(todo.get_id))
            if todo.get_id == id:
                print('Before:\n',todo.__str__())
                if(todo.state != True):
                    todo.state = True
                else:
                    todo.state = False
                print('After:\n',todo.__str__())
                self.save_to_file()
                break
            else:
                print("todo not found")
    def clear_todos(self):
        self.todos = []
    def save_to_file(self):
        with open('./src/data/Todos.json', 'w') as file:
            json.dump(self.todos, file, default=lambda obj: obj.__dict__, indent=2)
    def show_tasks(self):
        for todo in self.todos:
            print(todo.__str__())
    def read_to_file(self):
        try:
            with open('./src/data/Todos.json', 'r') as file:
                todo_data = json.load(file)

                for todo in todo_data:
                    if todo.get('category') == 'N':
                        task = Todo(todo.get('title', ''), todo.get('description', ''), todo.get('category',''), todo.get('state',bool))
                        self.todos.append(task)
                    if todo.get('category') == 'IU':
                        task = TodoIU(todo.get('title', ''), todo.get('description', ''), todo.get('category',''), todo.get('state',bool), todo.get('start_time',str), todo.get('end_time',str))
                        self.todos.append(task)
                return True
        except FileNotFoundError:
            print("File not found")
            return None
            

