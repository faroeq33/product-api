from pyexpat import model
from sqlalchemy.orm import Session

from utils import models, schemas


# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first()


# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()


# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()


# def create_product(db: Session, product: schemas.ProductCreate):
#     db_product = models.Product()
#     db.add(db_product)
#     db.commit()
#     db.refresh(db_product)
#     return db_product


# def create_user(db: Session, user: schemas.UserCreate):
#     fake_hashed_password = user.password + "notreallyhashed"
#     db_user = models.User(
#         email=user.email, hashed_password=fake_hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user


def get_products(db: Session, skip: int = 0, limit: int = 1000) -> object:
    return db.query(models.Product).offset(skip).limit(limit).all()


def create_user_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
