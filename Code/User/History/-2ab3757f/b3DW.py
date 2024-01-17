#todo.py
class Todo:
    _id_counter = 0
    def __init__(self, title, description, category, estado):
        Todo._id_counter += 1
        self.id =  Todo._id_counter
        self.title = title
        self.description = description
        self.category = category
        self.estado = estado

    def __str__(self):
        return f"----------\nid:{self.id},\n{self.title},\n{self.description},\ncategoria{self.category}\nestado:{self.estado}\n----------"
    