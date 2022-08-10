from typing import List

import uvicorn
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from utils import crud, models, schemas
from utils.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/products/", response_model=List[schemas.Product])
def get_all_products(db: Session = Depends(get_db)):
    return crud.get_products(db)


@app.post("/create/product/", response_model=schemas.Product)
def create_product(
    product: schemas.ProductCreate, db: Session = Depends(get_db)
):

    return crud.create_user_product(db=db, product=product)


# mag nooit weg!
if __name__ == '__main__':
    uvicorn.run(app="main:app", reload=True)
