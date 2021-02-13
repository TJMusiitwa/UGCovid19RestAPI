from fastapi import Depends,status
from starlette.status import HTTP_200_OK
from main import app, get_db
import crud, models, schemas
from sqlalchemy.orm import Session

#Get the summary
@app.get('/summary', response_model=schemas.Summary, status_code=status.HTTP_200_OK)
async def getSummary(db: Session = Depends(get_db)):
    summary = crud.get_summary(db=db)
    return summary

#Update Summary
@app.put('/summary', response_model=schemas.Summary)
async def updateSummary(db:Session=Depends(get_db)):
    newSummary = crud.add_summary(db=db)
    return newSummary 

#Get Timeline
@app.get('/timeline', status_code=status.HTTP_200_OK, response_model=schemas.Timeline)
async def getTimeline(db:Session=Depends(get_db)):
    fetchTimeline = crud.get_timeline(db)
    return fetchTimeline

#Add new Timeline Entry
@app.post('/timeline', status_code=status.HTTP_201_CREATED, response_model=schemas.Timeline)
async def addToTimeline(db:Session=Depends(get_db)):
    newTimelineEntry = crud.get_timeline(db)
    return newTimelineEntry

#Get all hospital data
@app.get('/hospitals', response_model=schemas.HospitalCases)
async def getHospitals(db:Session=Depends(get_db)):
    return

#Get all data for one hospital
@app.get('/hospitals/{hospital_name}', response_model=schemas.HospitalCases)
async def getByHospitalName(hospital_name:str,db:Session=Depends(get_db)):
    return crud.oneHospital(db=db,hospital_name=hospital_name)

#Add a new hospital
@app.post('/hospitals', response_model=schemas.HospitalCases)
def create_hospital(hospital:schemas.HospitalCasesCreate, db:Session=Depends(get_db)):
    return crud.addHospital(db,hospital)

# Update one hospital
@app.put('/hospitals/{hospital_name}', response_model=schemas.HospitalCases)
async def update_hospital(hospital_name:str, hospital:schemas.HospitalCasesUpdate,db:Session=Depends(get_db)):  
    return crud.updateHospital(db,hospital)


#Fetch District Cases
@app.get('/districts', response_model=schemas.DistrictCases)
async def get_districts(db:Session=Depends(get_db)):
    return crud.allDistricts(db)

#Fetch One District 
@app.get('/districts/{district_name}', response_model=schemas.DistrictCases)
async def get_one_district(district_name:str, db:Session=Depends(get_db)):
    return crud.oneDistrict(db,district_name)

#Fetch Districts By Region 
@app.get('/districts/{region}', response_model=schemas.DistrictCases)
async def get_district_by_region(region:str, db:Session=Depends(get_db)):
    return crud.getDistristsByRegion(db,region)

#Add new District Entry
@app.post('/districts', status_code=status.HTTP_201_CREATED, response_model=schemas.DistrictCases)
async def addDistrict(district:schemas.DistrictCreate,db:Session=Depends(get_db)):
    newTimelineEntry = crud.addDistrict(db,district)
    return newTimelineEntry

#Update district information
@app.put('/districts/{district_name}', response_model=schemas.DistrictCases)
async def update_one_district(district:schemas.DistrictUpdate,db:Session=Depends(get_db)):
    return crud.update_district(db,district)


#Fetch all Age Gender Data
@app.get('/age_gender', response_model=schemas.AgeGender)
async def getAgeGender(db:Session=Depends(get_db)):
    return crud.allAgeGender(db)

#Fetch Specific Age Gender Data
@app.get('/age_gender/{age_group}', response_model=schemas.AgeGender)
async def getOneAgeGroup(ageGroup:str,db:Session=Depends(get_db)):
    return crud.oneAgeGender(db,ageGroup)

#Update Specific Age Gender Data
@app.put('/age_gender/{age_group}', response_model=schemas.AgeGender)
async def updateOneAgeGroup(ageGroup:schemas.AgeGenderUpdate,db:Session=Depends(get_db)):
    return crud.update_ageGroup(db,ageGroup)

#Add new Age Gender Data
@app.post('/age_gender', response_model=schemas.AgeGender)
async def newAgeGroup(ageGroup:schemas.AgeGenderCreate,db:Session=Depends(get_db)):
    return crud.newAgeGender(db,ageGroup)