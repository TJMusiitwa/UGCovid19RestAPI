from sqlalchemy.orm import Session
from . import models, schemas

#Get the summary from the db
def get_summary(db:Session):
    return db.query(models.Summary).one()

#Add the summary to the db
def add_summary(db:Session):
    db_summary = models.Summary()
    db.add(db_summary)
    db.commit()
    db.refresh(db_summary)
    return db_summary    

#Get the summary from the db
def get_timeline(db:Session):
    return db.query(models.Timeline)

#Add the summary to the db
def add_to_timeline(db:Session):
    db_timeline = models.Timeline()
    db.add(db_timeline)
    db.commit()
    db.refresh(db_timeline)
    return db_timeline 

#Get all hospitals
def allHospitals(db:Session):
    return db.query(models.HospitalCases).one()

#Get one hospitals
def oneHospital(db:Session, hospital_name:str):
    return db.query(models.HospitalCases).filter(models.HospitalCases.hospitalName == hospital_name).all() 

#Add one hospital
def addHospital(db:Session, hospital: schemas.HospitalCasesCreate):
    db_create_hospital = models.HospitalCases(hospitalName=hospital.hospitalName, addmissions=hospital.admissions, discharge=hospital.discharge, deaths=hospital.deaths)
    db.add(db_create_hospital)
    db.commit()
    db.refresh(db_create_hospital)
    return db_create_hospital

#Update one Hospital
#def updateHospital(db:Session, hospital_name:str):