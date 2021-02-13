from sqlalchemy.orm import Session
import models, schemas

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
def get_timeline(db:Session,skip: int = 0, limit: int = 100):
    return db.query(models.Timeline).offset(skip).limit(limit).all()

#Add the summary to the db
def add_to_timeline(db:Session):    
    db_timeline = models.Timeline()
    db.add(db_timeline)
    db.commit()
    db.refresh(db_timeline)
    return db_timeline 

#Get all hospitals
def allHospitals(db:Session):
    return db.query(models.HospitalCases).order_by(models.HospitalCases.hospitalName.asc).all()

#Get one hospitals
def oneHospital(db:Session, hospital_name:str):
    return db.query(models.HospitalCases).filter(models.HospitalCases.hospitalName == hospital_name).one()

#Add one hospital
def addHospital(db:Session, hospital: schemas.HospitalCasesCreate):
    db_create_hospital = models.HospitalCases(hospitalName=hospital.hospitalName, addmissions=hospital.admissions, discharge=hospital.discharge, deaths=hospital.deaths)
    db.add(db_create_hospital)
    db.commit()
    db.refresh(db_create_hospital)
    return db_create_hospital

#Update one Hospital
def updateHospital(db:Session, hospital:schemas.HospitalCasesUpdate):
    db_update_hospital = db.query(models.HospitalCases).filter(models.HospitalCases.hospitalName == hospital.hospitalName).update(hospital.dict(exclude_none=True))
    db.commit()
    return db_update_hospital

#Get all District Cases
def allDistricts(db:Session,skip: int = 0, limit: int = 20):
    return db.query(models.DistrictCases).order_by(models.DistrictCases.districtName.asc).offset(skip).limit(limit).all()

#Fetch one district
def oneDistrict(db:Session, district_name:str):
    return db.query(models.DistrictCases).filter(models.DistrictCases.districtName == district_name).one()

#Fetch districts by region
def getDistristsByRegion(db:Session, region:str,skip: int = 0, limit: int = 20):
    return db.query(models.DistrictCases).filter(models.DistrictCases.region == region).offset(skip).limit(limit).all()

#Add one district
def addDistrict(db:Session, district: schemas.DistrictCreate):
    db_create_district = models.DistrictCases(districtName=district.districtName,
    region=district.region,
     cases=district.cases,
    deaths=district.deaths,
     recoveries=district.recoveries)
    db.add(db_create_district)
    db.commit()
    db.refresh(db_create_district)
    return db_create_district

#Update one district
def update_district(db:Session, district:schemas.DistrictUpdate):
    db_update_district = db.query(models.DistrictCases).filter(models.DistrictCases.districtName == district.districtName).update(district.dict(exclude_none=True))
    db.commit()
    return db_update_district

#Get all age-gender cases
def allAgeGender(db:Session):
    return db.query(models.AgeGender).all()

#Get one age-gender group
def oneAgeGender(db:Session, ageGroup:str):
    return db.query(models.AgeGender).filter(models.AgeGender.ageGroup == ageGroup).one_or_none()

#Get add age-gender group
def newAgeGender(db:Session, agegroup:schemas.AgeGenderCreate):
    db_ageGroup = models.AgeGender(
        ageGroup = agegroup.ageGroup,
        females = agegroup.females,
        males = agegroup.males
    )
    db.add(db_ageGroup)
    db.commit()
    db.refresh(db_ageGroup)
    return db_ageGroup  

#Update age Group
def update_ageGroup(db:Session, ageGroup:schemas.AgeGenderUpdate):
    db_update_ageGroup = db.query(models.AgeGender).filter(models.AgeGender.ageGroup == ageGroup.ageGroup).update(ageGroup.dict(exclude_none=True))
    db.commit()
    return db_update_ageGroup