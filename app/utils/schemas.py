from typing import List, Union

from pydantic import BaseModel


class ProductBase(BaseModel):
    brand: str
    name: str
    price: float

    class Config:
        orm_mode = True


class Product(ProductBase):
    id: int
    # owner_id: int




class ProductCreate(ProductBase):
    pass

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    products: List[Product] = []

    class Config:
        orm_mode = True
