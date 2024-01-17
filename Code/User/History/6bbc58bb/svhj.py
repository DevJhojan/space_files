from fastapi import APIRouter, HTTPException, status
from conect_data_base.models.user import User
from conect_data_base.client import db_clien
from conect_data_base.schemas.user import user_schema, users_schema
from bson import ObjectId
""" Aqui se agrupa los enpoints 
  El prefix es la ruta por defecto y el tags es la etiqueta que agrupa los enpoins
  hechos en este modulo
"""
user_db = APIRouter(prefix="/users_db", tags=["Users DB"])

# Este es el modelo de usuarios
#este enpoint retorna por defecto los usuarios de la base de datos 
@user_db.get("/", response_model=list[User])
async def user_model():
  return users_schema(db_clien.local.users.find())



# ! Path and Query
"""
  ? Path, cuando se sabe que un parametro es fijo
  ? Query, Cuando no hay parametros que nos se saben ni el tipo
  ! Las buenas practivas es cuando todo sea fijo
"""
# user Data o base de datos
user_list = [""]

#path
# retorna el usuario buscado
@user_db.get("/{id}")
async def user_found(id: str):
  return search_user("_id", ObjectId(id))
  

#querry
#retorna el usuario buscado
@user_db.get("/userquery/")
async def userquerry(id: int):
  pass
  #return search_user_by_email(id)

# Busca los usuarios por el id
def search_user_by_email(email:str):
  try:
    user=db_clien.local.users.find_one({"email": email})
    return User(**user_schema(user))
  except:
    return {"error": "user not found"}
 
 
def search_user(field:str, key):
  try:
    user= db_clien.local.users.find_one({field: key})
    return User(**user_schema(user))
  except:
    return {"error": "user not found"}
    

"""CRUD
  ? este enpoint agrega los usuario
"""
@user_db.post("/add/")
async def user_post(user: User):
  if type(search_user("email", user.email))==User:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The user with this email alredy exist")
  
  user_dict = dict(user)
  del user_dict["id"]
  id = db_clien.local.users.insert_one(user_dict).inserted_id
  new_user=user_schema(db_clien.local.users.find_one({"_id": id}))
  return User(**new_user)
   
   

# este actualiza el usuario
@user_db.put("/update/")
async def user_put(user: User):
  found =False
  for index, save_user in enumerate(user_list):
    pass
  """AI is creating summary for user_put
    if save_user.id == user.id:
      user_list[index] = user
      found = True
      return {"messages": "User update", "body": user}
  """
  
  if not found:
    return {"messages": "User not found"}
  
#Este Elimina el usuario
@user_db.delete("/deleted/{id}")
async def user_delete(id: int):
  found = False
  for index, save_user in enumerate(user_list):
    pass
    """ 
    if save_user.id == id:
      del user_list[index]
      found = True
      return {"messages": "User deleted", "list": user_list}
    """
    
  if not found:
    return {"messages": "User not found"}
 