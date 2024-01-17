from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

login_auth = APIRouter(prefix="/login", tags=["Login"])

oauth2 = OAuth2PasswordBearer(tokenUrl="auth")
"""
Autenticacion: Es cuando estes registrado en una plataforma
Autorizacion: Es cuando tienes permisos en dicha plataforma 
"""



class User(BaseModel):
  username: str
  full_name: str
  email: str
  disable: bool

class UserDB(User):
  password:str
  

users_list = {
  "Jhojan": {
    "username": "Jhojan",
    "full_name": "jhojan Toro",
    "email": "jhojan@email.com",
    "disable": False,
    "password": "root"
  }, 
  "Jhojan2":{
    "username": "Jhojan2",
    "full_name": "jhojan2 Toro",
    "email": "jhojan2@email.com",
    "disable": False,
    "password": "root2"
  },
}

def search_user(username: str):
  if username in users_list:
    user_data = users_list[username]
    return UserDB(
      username=str(user_data["username"]),
      full_name=str(user_data["full_name"]),
      email=str(user_data["email"]),
      disable=bool(user_data["disable"]),
      password=str(user_data["password"])
    )

async def current_user(token: str = Depends(oauth2)):
  user = search_user(token)
  if not user:
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, 
        detail="User not Authorized",
        headers={"WWW-Authenticate":"Bearer"}
      )
  return user
 
@login_auth.post("/auth")
async def authentication(form: OAuth2PasswordRequestForm = Depends()):
  user_db= users_list.get(form.username)
  if not user_db:
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, 
        detail="User not found"
      )
  user = search_user(form.username)
  if not form.password == user.password:
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, 
        detail="password is incorrect"
      )
  # el token es algo que es encriptado
  return {"access_token": user.username, "token_type":"bearer"}

@login_auth.get("/users/me")
async def me(user: User = Depends()):
  return user
  