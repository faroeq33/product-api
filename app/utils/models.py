from operator import index
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from utils.database import Base


# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=True)

#     products = relationship("Product", back_populates="owner")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String, index=True)
    name = Column(String, index=True)
    price = Column(Integer, index=True)

    class Config:
        orm_mode = True
