class Todo:
    def __init__(self, title, description, type):
        self.title = title
        self.description = description
        self.type = type

    @property
    def title(self):
        return self.title
    
    @title.setter
    def title(self, title):
        self.title = title
    @property
    def description(self):
        return self.description
    @description.setter
    def description(self, description):
        self.description = description
    @property
    def type(self):
        return self.type
    @type.setter
    def type(self, type):
        self.type = type
    def __str__(self):
        return f"Title: {self.tile}\nDescription: {self.description}\nType: {self.type}"