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
from . cart import Cart
templates = Jinja2Templates(directory=str(BASE_PATH / "templates"))


router = APIRouter(
    prefix="/cart"
)

@router.get("/")
def cart_detail(request: Request, db: Session = Depends(get_db)):
    cart = Cart(Request,db)
    return templates.TemplateResponse("cart.html", {"request": request,
                                                     "cart": cart  })
