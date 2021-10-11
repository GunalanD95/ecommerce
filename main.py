from sqlalchemy import engine
from sqlalchemy.sql.functions import mode
import models
from fastapi import FastAPI ,Response , Request ,Depends
from database import SessionLocal, engine , get_db
from sqlalchemy.orm.session import Session
import schemas
from repos import product


models.Base.metadata.create_all(bind=engine)


app = FastAPI()

@app.post('/create')
def create_prod(request: schemas.Shop,db: Session= Depends(get_db)):
    return product.create_product(request,db)


@app.get('/get_product')
def get_prod(db: Session= Depends(get_db)):
    return product.list_product(db)

