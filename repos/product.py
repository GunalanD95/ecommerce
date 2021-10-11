import models
from fastapi import FastAPI ,Response , Request ,Depends
from database import SessionLocal, engine , get_db
from sqlalchemy.orm.session import Session
import schemas


def create_product(request,db):
    new_prod = models.Shop(title=request.title,description=request.description,price=request.price)
    db.add(new_prod)
    db.commit()
    db.refresh(new_prod)
    return new_prod    

def list_product(db):
    all_prods = db.query(models.Shop).all()
    return all_prods   