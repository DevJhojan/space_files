class TodoIU:
    _id_counter = 0
    def __init__(self, title, description, category, state, start_time, end_time):
        TodoIU._id_counter += 1
        self.id =  TodoIU._id_counter
        self.title = title
        self.description = description
        self.category = category
        self.state = state
        self.start_time = start_time
        self.end_time = end_time

    @property
    def get_id(self):
        return self.id
    
    def __str__(self):
        return f"----------\nid:{self.id}\n{self.title}\n{self.description}\ncategoria: {self.category}\nestado:{self.state}\nstart time:{self.start_time}\nend time:{self.end_time}----------"

class TodoINU:
    _id_counter = 0
    def __init__(self, title, description, category, state, start_time ):
        TodoINU._id_counter += 1
        self.id =  TodoINU._id_counter
        self.title = title
        self.description = description
        self.category = category
        self.state = state
        self.start_time = start_time

    @property
    def get_id(self):
        return self.id
    
    def __str__(self):
        return f"----------\nid:{self.id}\n{self.title}\n{self.description}\ncategoria: {self.category}\nestado:{self.state}\nstart_time:{self.start_time}----------"

