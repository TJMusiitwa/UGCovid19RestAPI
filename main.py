from fastapi import FastAPI
from sqlalchemy.orm import Session

from . import models, schemas
from .database import SessionLocal, db_engine

models.Base.metadata.create_all(bind=db_engine)

app = FastAPI(
    title="Uganda Covid-19 REST API",  
)

#Dependency
def get_db():
    db_engine = SessionLocal()
    try:
        yield db_engine
    finally:
        db_engine.close()    


@app.get('/')
async def root():
    return {"Message": "This proves that it works as expected"}