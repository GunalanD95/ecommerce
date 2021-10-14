from ..import models
from fastapi import FastAPI ,Response , Request ,Depends
from ..database import SessionLocal, engine , get_db
from sqlalchemy.orm.session import Session
from ..import schemas


def create_product(title,description,price,db):
    new_prod = models.Shop(title=title,description=description,price=price)
    db.add(new_prod)
    db.commit()
    db.refresh(new_prod)
    return new_prod    

def list_product(db):
    all_prods = db.query(models.Shop).all()
    return all_prods   