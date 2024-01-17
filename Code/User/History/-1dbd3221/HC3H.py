from fastapi import APIRouter
from enum import Enum
from pydantic import BaseModel

product = APIRouter(prefix="/products", tags=["Products", "dame"])


@product.get("/")
async def get_product():
  try:
    return "Funciona"
  except:
    return "not funciona"