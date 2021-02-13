from fastapi import FastAPI
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

import models
from database import SessionLocal, db_engine

models.Base.metadata.create_all(bind=db_engine)

app = FastAPI(
    title="Uganda Covid-19 REST API",  
)

# @app.on_event("startup")
# async def startup():
#     #await db_engine.connect()


# @app.on_event("shutdown")
# async def shutdown():
#     #await database.disconnect()

#Dependency
def get_db():
    db_engine = SessionLocal()
    try:
        yield db_engine
    finally:
        db_engine.close()    


@app.get("/", include_in_schema=False)
async def index():
    return RedirectResponse("/docs")