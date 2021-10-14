from fastapi import FastAPI
from . import  models
from .database import engine 
from fastapi.templating import Jinja2Templates
from . routers import product

models.Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(product.router) 

templates = Jinja2Templates(directory="templates")

