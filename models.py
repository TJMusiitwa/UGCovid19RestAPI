import datetime
from sqlalchemy import Column, String,Integer, DateTime
from sqlalchemy.sql.schema import FetchedValue
from .database import Base

class Summary(Base):
    __tablename__ = 'summary'

    id = Column(Integer, primary_key=True,default=1)
    cases = Column(Integer, nullable=False)
    deaths = Column(Integer, nullable=False)
    recoveries = Column(Integer, nullable=False)
    lastUpdated = Column(DateTime,nullable=False, default=datetime.datetime.now,onupdate=datetime.datetime.now)

# class User(Base):
#     __tablename__ = "users"
#     email = Column(String,unique=True,index=True)
#     hashed_password = Column(String)

class Timeline(Base):
    __tablename__ = "timeline"

    createdAt = Column(DateTime, unique=True, nullable=True,index=True,primary_key=True)
    cases = Column(Integer, nullable=False)
    deaths = Column(Integer, nullable=False)
    recoveries = Column(Integer, nullable=False)  

class HospitalCases(Base):
    __tablename__ = "hospitalCases"

    hospitalName = Column('hospital',String,unique=True,index=True,primary_key=True,nullable=False)
    admissions = Column(Integer, nullable=False)
    discharge = Column(Integer, nullable=False)
    deaths = Column(Integer, nullable=False)
    lastUpdated = Column(DateTime,nullable=False, default=datetime.datetime.now,onupdate=datetime.datetime.now)

def calcTotal(context):
    return context.get_current_parameters()['females'] + context.get_current_parameters()['males']

class AgeGender(Base):
    __tablename__ = "age_gender"

    ageGroup = Column(String)
    females = Column(Integer)
    males = Column(Integer)
    totalAgeGroup = Column(Integer,default=calcTotal,onupdate=calcTotal)
    lastUpdated = Column(DateTime,nullable=False, default=datetime.datetime.now,onupdate=datetime.datetime.now)

class DistrictCases(Base):
    __tablename__ = 'district_cases'

    districtName = Column('district',String,unique=True,index=True,nullable=False)
    region = Column(String,index=True)
    cases = Column(Integer, nullable=False)
    deaths = Column(Integer, nullable=False)
    recoveries = Column(Integer, nullable=False)
    lastUpdated = Column(DateTime,nullable=False, default=datetime.datetime.now,onupdate=datetime.datetime.now)

