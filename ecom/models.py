from pydantic import BaseModel
from sqlalchemy.sql.schema import ForeignKey
from .database import Base
from sqlalchemy import Column,String,Text, Integer, Boolean , DECIMAL ,Date,DateTime 
import datetime
from datetime import date
from slugify import slugify
from sqlalchemy_utils import URLType
from sqlalchemy.orm import relationship




class Category(Base):
    __tablename__ = "category"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    slug = Column(String,unique=True)

    def __init__(self,*args,**kwargs):
        if not 'slug' in kwargs:
            kwargs['slug'] = slugify(kwargs.get('name',''))
        super(Category,self).__init__(self,*args,**kwargs)

    product_category = relationship("Product", back_populates="category")


class Product(Base):
    __tablename__ = "product"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    description = Column(Text)
    url = Column(URLType)
    price = Column(DECIMAL(scale=2))
    available = Column(Boolean,default=True)
    create_date = Column(Date,default=date.today())
    updated_date = Column(DateTime,onupdate=datetime.datetime.now())
    slug = Column(String,unique=True)
    category_id = Column(Integer, ForeignKey("category.id"))
    category = relationship("Category", back_populates="product_category")

    def __init__(self,*args,**kwargs):
        if not 'slug' in kwargs:
            kwargs['slug'] = slugify(kwargs.get('name',''))
        super(Product,self).__init__(self,*args,**kwargs)

