from ..import models
from fastapi import FastAPI ,Response , Request ,Depends
from ..database import SessionLocal, engine , get_db
from sqlalchemy.orm.session import Session
from ..import schemas


def list_product(request: schemas.Product,db: Session= Depends(get_db),category_slug: str = None):
    if category_slug:
        category = db.query(models.Category).filter_by(slug=category_slug).first()
        return db.query(models.Product).filter_by(category=category).all()

    return db.query(models.Product).all()
