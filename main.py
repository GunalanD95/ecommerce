from fastapi import FastAPI
import  models
from database import engine 
from fastapi.templating import Jinja2Templates

import sys
sys.path.append(r"C:\Users\admin\Desktop\FASTAPI-TUT\fastapi-env\ecommerce")

from ecom.routers import product


models.Base.metadata.create_all(bind=engine)


app = FastAPI()
# app.include_router(product.router) 

templates = Jinja2Templates(directory="templates")

