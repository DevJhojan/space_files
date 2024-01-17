from person import Person
"""
TF:Termino fijo
TI:Termino indefinido
"""
class Employee(Person):
    def __init__(self, occupation, salary, type_of_contract="TF"):
        self.occupation = occupation
        self.salary = salary 
        self.type_of_contract

    def __str__():
        return f"Occupation: {self.occupation},\nSalary:{self.salary},\nType of contract:{self.type_of_contract}\n"

