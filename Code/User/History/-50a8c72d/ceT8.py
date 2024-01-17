class Todo:
    def __init__(self, title, description, type):
        self.tile = title
        self.description = description
        self.type = type

    @property
    def title(self):
        return self.tile
    @property
    def description(self):
        return self.description
    def __str__(self):
        return f"Title: {self.tile}\nDescription: {self.description}\nType: {self.type}"