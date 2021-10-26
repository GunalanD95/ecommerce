from fastapi import FastAPI
from . import  models
from .database import engine 
from fastapi.templating import Jinja2Templates
from . routers import product
import os
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
import itsdangerous
from . cart import main


models.Base.metadata.create_all(bind=engine)

secret_key = "cart"
middleware = [
    Middleware(SessionMiddleware,secret_key=secret_key)
]

app = FastAPI(middleware=middleware)
app.include_router(product.router) 
app.include_router(main.router) 



templates = Jinja2Templates(directory="templates")

BASE_PATH = Path(__file__).resolve().parent
app.mount(
    "/static",
    StaticFiles(directory=BASE_PATH/ "static"),
    name="static",
)

