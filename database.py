from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DB_URL = "postgresql://user:password@postgresserver/db"

metadata = MetaData()

db_engine = create_engine(SQLALCHEMY_DB_URL)
SessionLocal = sessionmaker(bind=db_engine, autocommit=False, autoflush=False)

Base = declarative_base()

metadata.create_all(db_engine)