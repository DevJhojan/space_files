class Todo:
    def __init__(self, title, description, type):
        self.tile = title
        self.description = description
        self.type = type
        
    def __str__(self):
        return f"Title: {self.tile}\nDescription: {self.description}\nType: {self.type}"