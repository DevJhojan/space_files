from fastapi import APIRouter
from enum import Enum
from pydantic import BaseModel

product = APIRouter()


@product.get("/product/")
async def get_product():
  try:
    return "Funciona"
  except:
    return "not funciona"