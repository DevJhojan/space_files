class Person: 
    def __init__(self, names,  age, last_names="", gender="", number_contact=0):
        self.name= names
        self.last_names = last_names
        self.age = age
        self.gender = gender
        self.number_contact = number_contact

    def __str__(self):
        return f"Names:{self.names},\nLast Names:{self.last_names},\nAge:{self.age},\ngender:{self.gender},\nNumber contact:{self.number_contact}" 



