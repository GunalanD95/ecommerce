from fastapi import FastAPI
from . import  models
from .database import engine 
from fastapi.templating import Jinja2Templates
from . routers import product
import os
from fastapi.staticfiles import StaticFiles
from pathlib import Path


models.Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(product.router) 

templates = Jinja2Templates(directory="templates")

BASE_PATH = Path(__file__).resolve().parent
app.mount(
    "/static",
    StaticFiles(directory=BASE_PATH/ "static"),
    name="static",
)

