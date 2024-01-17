from .todo_manager import TodoManager
from .models.todo import Todo
from .models.todo_type import TodoIU, TodoINU
import datetime
import time
import os
import asyncio
class TodoProm:
    def __init__(self):
        self.manager = TodoManager()
        self.todo_promp()
    def help():
        print(
            "exit       ->  Exit the program\n"+
            "create     ->  Create 1 new task\n"+
            "cls -a     ->  Delete all tasks\n"+
            "f -1       ->  Find 1 task\n"+
            "show -a    ->  See all tasks\n"+
            "ok - 1     ->  change the state of one task\n"
        )
    def categories():
        print(
            "N   -> Normal \n"+
            "IU  -> ImportantUrgent\n"
            "INU -> ImportantNotUrgent\n"
        )
    def add_task(self, category):
        state = False
        title = input("Title: ")
        description = input("Description: ")
        if category == "IU":
            start_time_str = input("Start Time(DD-MM-YY HH:MM): ")
            end_time_str = input("End Time(DD-MM-YY HH:MM): ")
            try:
                start_time = datetime.datetime.strptime(start_time_str, "%d-%m-%Y %H:%M")
                start_menssage = f"Start: {title}"
                asyncio.create_task(self.alarm(start_time, start_menssage))
                await 
            except ValueError:
                print("wrong format, play  again : " + start_time_str + ", or:"+end_time_str)

            try:
                end_time = datetime.datetime.strptime(end_time_str, "%d-%m-%Y %H:%M")
                end_menssage = f"End: {title}"
                self.alarm(end_time, end_menssage)
                new_todo = TodoIU(title, description, category, state, start_time_str, end_time_str)
                self.manager.add_todo(new_todo)
            except ValueError: 
                print("wrong format, play  again : " + start_time_str + ", or:"+end_time_str)
        elif category == "INU":
            start_time = input("Start Time(DD-MM-YY HH:MM): ")
            new_todo = TodoINU(title, description, category, state, start_time)
            self.manager.add_todo(new_todo)
        elif category == "N":
            new_todo = Todo(title, description, category, state)
            self.manager.add_todo(new_todo)
        else:
            print("Warnig, Wrong category")
    async def alarm(self, date, mensaje="Alarm!"):
        now = datetime.datetime.now()
        restar_time = date - now
        if  restar_time.total_seconds() > 0:
            print(f"the alarm sound at {restar_time}")
            await asyncio.sleep(restar_time.total_seconds())
            print(mensaje)
        
    def todo_promp(self):
        self.manager.read_to_file()
        if(self.manager.read_to_file == None):
            self.manager.save_to_file()      
        sw = 1
        while True:
            if sw == 1:
                self.manager.show_tasks()
            else:
                print("----------")
            inp = input(">")
            if inp == "show -a":
                self.manager.show_tasks()
            if inp == "exit":
                break
            if inp == "cls -a":
                self.manager.clear_todos()
                self.manager.save_to_file()
                print("all clear")
            if inp == "create":
                TodoProm.categories()
                category = input("write category of task:\n")
                asyncio.run(self.add_task(category))
                self.manager.save_to_file()
            if inp == "ok -1":
                id = input("Id of task: ")
                self.manager.completeTask(int(id))
            if inp == "help":
                TodoProm.help()
            print("----------")
            sw = 0
    
