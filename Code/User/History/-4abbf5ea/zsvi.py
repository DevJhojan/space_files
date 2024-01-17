from fastapi import APIRouter
from enum import Enum
from pydantic import BaseModel

user = APIRouter()


# ! Path and Query
"""
  ? Path, cuando se sabe que un parametro es fijo
  ? Query, Cuando no hay parametros que nos se saben ni el tipo
  ! Las buenas practivas es cuando todo sea fijo
"""
# user Data
user_list = [
 User( id=1, name= "admin", age=2),
 User( id=2, name= "Marco", age=4)
]

#path
@my_steeps.get("/user/{id}")
async def user(id: int):
  return search_user(id)

#querry
@my_steeps.get("/userquery/")
async def userquerry(id: int):
  return search_user(id)

def search_user(id:int):
  users = filter(lambda user: user.id == id, user_list)
  try:
    return list(users)[0]
  except:
    return {"error": "User not found"}

"""CRUD"""
@my_steeps.post("/user/")
async def user_post(user: User):
  if type(search_user(user.id)) == User:
    return {"messages": "User al ready exist"}
  else:
    user_list.append(user)
    return {"messages": "User added", "body": user}
   


@my_steeps.put("/user/")
async def user_put(user: User):
  found =False
  for index, save_user in enumerate(user_list):
    if save_user.id == user.id:
      user_list[index] = user
      found = True
      return {"messages": "User update", "body": user}
  
  if not found:
    return {"messages": "User not found"}
  

@my_steeps.delete("/user/{id}")
async def user_delete(id: int):
  found = False
  for index, save_user in enumerate(user_list):
    if save_user.id == id:
      del user_list[index]
      found = True
      return {"messages": "User deleted", "list": user_list}
    
  if not found:
    return {"messages": "User not found"}
  