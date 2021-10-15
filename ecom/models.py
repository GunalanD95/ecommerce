from pydantic import BaseModel
from .database import Base
from sqlalchemy import Column,String,Text, Integer, Boolean , DECIMAL
import datetime

class Category(Base):
    __tablename__ = "category"

    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    description = Column(Text)
    price = Column(Integer)


