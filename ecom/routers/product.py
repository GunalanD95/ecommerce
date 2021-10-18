from fastapi import APIRouter
from ..database import get_db,BASE_PATH
from sqlalchemy.orm import Session
from sqlalchemy import engine
from sqlalchemy.sql.functions import mode
from fastapi.responses import HTMLResponse
from starlette.responses import RedirectResponse
from ..import models
from fastapi import FastAPI ,Response , Request ,Depends, Form ,status
from ..database import SessionLocal, engine , get_db
from sqlalchemy.orm.session import Session
from ..repos import product
from .. import schemas , models , database
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException

templates = Jinja2Templates(directory=str(BASE_PATH / "templates"))


router = APIRouter()

# @router.post('/create',response_class=HTMLResponse)
# def create_prod(request:Request,title:str=Form(...),description:str=Form(...),price:int=Form(...),db: Session= Depends(get_db)):
#     product.create_product(title=title,description=description,price=price,db=db)
#     return RedirectResponse(url="/get_product",status_code=status.HTTP_303_SEE_OTHER)


@router.get('/{category_slug}')
def get_prod(request:Request,category_slug:str,db: Session= Depends(get_db), page: int=1):
    products = product.list_product(request,category_slug=category_slug,db =db)[16*(page-1): 16*(page)]
    categories = db.query(models.Category).all()
    category = db.query(models.Category).filter_by(slug=category_slug).first()
    return templates.TemplateResponse("list.html", {"request": request,
                                                    "page": page,
                                                    "product": jsonable_encoder(products),
                                                    "category":jsonable_encoder(category),
                                                    "categories":jsonable_encoder(categories),})


@router.get('/{product_id}/{product_slug}')
def prod_details(request:Request,product_id:int,product_slug:str,db: Session= Depends(get_db)):
    products = jsonable_encoder(product.product_details(id=product_id,slug=product_slug,db =db))
    if products is None:
        raise HTTPException(status_code=404,detail="product does not exit")
    return templates.TemplateResponse("detail.html",  {"request": request,
                                                       "product": jsonable_encoder(products),})