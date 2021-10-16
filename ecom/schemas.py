from pydantic import BaseModel
from typing import Text
from datetime import date, datetime, time, timedelta


class Shop(BaseModel):
    title:str
    description:str
    price:int

    class Config:
        orm_mode = True

class Product(BaseModel):
    name :str
    description :Text
    # url : url
    # price :int
    # available : bool
    # create_date :datetime.date
    # updated_date = Column(DateTime,onupdate=datetime.datetime.now())
    # slug = Column(String,unique=True)
    # category_id = Column(Integer, ForeignKey("category.id"))
    # category = relationship("Category", back_populates="product_category")