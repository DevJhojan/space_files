#todo.py
class Todo:
    _id_counter = 0
    def __init__(self, title, description, category):
        Todo._id_counter += 1
        self.id =  Todo._id_counter
        self.title = title
        self.description = description
        self.category = category

    def __str__(self):
        return f"Todo(id={self.id}, \n title={self.title},\n description={self.description},\n category={self.category})"
    