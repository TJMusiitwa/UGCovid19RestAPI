from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DB_URL = "postgresql://user:password@postgresserver/db"

db_engine = create_engine(SQLALCHEMY_DB_URL)
SessionLocal = sessionmaker(bind=db_engine, autocommit=False, autoflush=False)

Base = declarative_base()