from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import base
from sqlalchemy.orm.session import Session, sessionmaker
from pathlib import Path




DATABASE_URL = "sqlite:///ecom/sql.db"

engine = create_engine(DATABASE_URL,connect_args={"check_same_thread": False})


BASE_PATH = Path(__file__).resolve().parent



SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

