from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# se importa los encirptadores
# Jwt es el que genera el token
from jose import jwt, JWTError

# passlib es el que da el contexto de la cryptografica
from passlib.context import CryptContext

# se importa el data time ya que se necesita manejar el tiempo
from datetime import datetime, timedelta

# Se pone el contexto que se va a utilizar en el algoritmo de encritación
ALGORITHM = "HS256"

# Se agrega el tiempo de activación de cada token '1 = 1 minuto'
ACCESS_TOKEN_DURATION = 1440

# Se pone el secreto por 'openssl rand -hex 32' => ese codigo se pone el bash
SECRET = "4bd3cad5e8118195a55fcf086d8710fa65d44a2f571d58d9809858dd234847ce"

""" Aqui se agrupa los enpoints 
  El prefix es la ruta por defecto y el tags es la etiqueta que agrupa los enpoins
  hechos en este modulo
"""
login_auth_jwt = APIRouter(prefix="/jwt", tags=["Login JWT"])


# Este es el que envia los criterios de autenticación a cualquier enpoint
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

# Se pone el contesto que se utilizara en la criptografia
crypt = CryptContext(schemes=["bcrypt"])


"""
Autenticacion: Es cuando estes registrado en una plataforma
Autorizacion: Es cuando tienes permisos en dicha plataforma 
"""

# Modelos de la base de datos
class User(BaseModel):
  username: str
  full_name: str
  email: str
  disable: bool

class UserDB(User):
  password:str

class AuthUser(BaseModel):
  username: str
  password: str  


# Base de datos
users_list = {
  "Jhojan": {
    "username": "Jhojan",
    "full_name": "jhojan Toro",
    "email": "jhojan@email.com",
    "disable": False,
    "password": "$2a$12$RtZ2xJ4jSX/ejSRB/zE9le6FrK6mE3nuyVSrJnDdnlwzWpNtr1Xf."
  }, 
  "Jhojan2":{
    "username": "Jhojan2",
    "full_name": "jhojan2 Toro",
    "email": "jhojan2@email.com",
    "disable": True,
    "password": "$2a$12$EIEZpQ2yeWwVrvlQZVCw6ee9TAtxWJd7fhxto4PyDCduA8sSDDB5W"
  },
}


def search_data(username: str):
  if username in users_list:
    user_data = users_list[username]
    return AuthUser(username=str(user_data["username"]), password=str(user_data["password"]))
    
def search_user(username: str):
  if username in users_list:
    user_data = users_list[username]
    return User(
      username=str(user_data["username"]),
      full_name=str(user_data["full_name"]),
      email=str(user_data["email"]),
      disable=bool(user_data["disable"]),
    )

async def auth_user(token: str =Depends(oauth2)):
  exception= HTTPException(
          status_code=status.HTTP_401_UNAUTHORIZED, 
          detail="User not Authorized",
          headers={"WWW-Authenticate":"Bearer"}
        )
  try:
    username = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
    if username is None:
      raise exception 
  except JWTError:
      raise exception
    
  return search_user(username["sub"])
    

async def current_user(user: User = Depends(auth_user)):
  
  if user.disable:
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, 
        detail="User Inactive",
      ) 
  return user
 
@login_auth_jwt.post("/login")
async def authentication(form: OAuth2PasswordRequestForm = Depends()):
  user_db= users_list.get(form.username)
  if not user_db:
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, 
        detail="User not found"
      )
  user = search_data(form.username)
  if not crypt.verify(form.password, user.password):
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, 
        detail="password is incorrect"
      )
 
  access_token = {
    "sub": user.username,
    "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)
  } 

  # el token es algo que es encriptado
  return {"access_token": jwt.encode(access_token, SECRET , algorithm=ALGORITHM,), "token_type":"bearer"}

@login_auth_jwt.get("/users/me")
async def me(user: User = Depends(current_user)):
  return user
  