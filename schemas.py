from pydantic import BaseModel

class Shop(BaseModel):
    title:str
    description:str
    price:int

    class Config:
        orm_mode = True