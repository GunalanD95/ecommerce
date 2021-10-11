from pydantic import BaseModel
from database import Base
from sqlalchemy import Column,String,Text, Integer


class Shop(Base):
    __tablename__ = "shop"

    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    description = Column(Text)
    price = Column(Integer)


