from typing import List

import uvicorn
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from utils import crud, models, schemas
from utils.crud import get_items
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


@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/products")
def get_products():

    return get_items(Session)
    return {
        "test": "testmessage",
        "test2": "testmessage2",
        "test3": "testmessage3"
    }


@app.get("/test")
def read_test():
    return {"test": "testmessage"}


# mag nooit weg!
if __name__ == '__main__':
    uvicorn.run(app="main:app", reload=True)
