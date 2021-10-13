from sqlalchemy import engine
from sqlalchemy.sql.functions import mode
from fastapi.responses import HTMLResponse
from starlette.responses import RedirectResponse
import models
from fastapi import FastAPI ,Response , Request ,Depends, Form ,status
from database import SessionLocal, engine , get_db
from sqlalchemy.orm.session import Session
import schemas
from repos import product
from fastapi.templating import Jinja2Templates

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

templates = Jinja2Templates(directory="templates")




# @app.post('/create')
# def create_prod(request: schemas.Shop,db: Session= Depends(get_db)):
#     return product.create_product(request,db)


# @app.get('/get_product')
# def get_prod(db: Session= Depends(get_db)):
#     return product.list_product(db)


@app.post('/create',response_class=HTMLResponse)
def create_prod(request:Request,title:str=Form(...),description:str=Form(...),price:int=Form(...),db: Session= Depends(get_db)):
    product.create_product(title=title,description=description,price=price,db=db)
    return RedirectResponse(url="/get_product",status_code=status.HTTP_303_SEE_OTHER)


@app.get('/get_product',response_class=HTMLResponse)
def get_prod(request:Request,db: Session= Depends(get_db)):
    products = product.list_product(db)
    return templates.TemplateResponse("index.html",{"request": request,"products": products})