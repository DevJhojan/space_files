#todo.py
class Todo:
    _id_counter = 0
    def __init__(self, idt, title, description, category):
        Todo._id_counter += 1
        self.id =  Todo._id_counter
        self.title = title
        self.description = description
        self.category = category

    