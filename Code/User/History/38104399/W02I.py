class TodoUrgen:
    _id_counter = 0
    def __init__(self, title, description, category, state, start_time, end_time):
        TodoUrgen._id_counter += 1
        self.id =  TodoUrgen._id_counter
        self.title = title
        self.description = description
        self.category = category
        self.state = state

    @property
    def get_id(self):
        return self.id
    def __str__(self):
        return f"----------\nid:{self.id}\n{self.title}\n{self.description}\ncategoria: {self.category}\nestado:{self.state}\n----------"

