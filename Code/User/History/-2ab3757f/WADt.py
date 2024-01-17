class Todo:
    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category

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
    def category(self):
        return self.category
    
    @category.setter
    def category(self, category):
        self.category = category

    def __str__() -> str:
        return f"Title: {self.title}\nDescription: {self.description}\nCategory: {self.category}"