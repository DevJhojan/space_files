class Person: 
    def __init__(self, names,  age, last_names="", gender=""):
        self.name= names
        self.last_names = last_names
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"Names:{self.names},\nLast Names:{self.last_names},\nAge:{self.age},\ngender:{self.gender}" 



