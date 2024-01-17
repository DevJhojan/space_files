from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from enum import Enum
from pydantic import BaseModel
from routers import products
from users import user

class ModelName(str, Enum):
  xuning = "xuning"
  resnet = "resnet"

my_steeps = FastAPI()

my_steeps.include_router(products.product)

my_steeps.include_router(user.user)

my_steeps.mount("/static", StaticFiles(directory="Static"), name="static")

@my_steeps.get("/")
async def hello_world():
  return {"message": "Hello, world!"}

@my_steeps.get("/item/{item_id}")
async def read_item(item_id:int):
  return {"item_id": item_id}


@my_steeps.get("/item/{model_name}") #! esto tiene un error enorme
async def read_model(model_name: ModelName):
  return {"model": model_name, "message": "Unknown model"}

  