from fastapi import Depends,status
from starlette.status import HTTP_200_OK
from .main import app, get_db
from . import crud, models, schemas
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
@app.get('hospitals', response_model=schemas.HospitalCases)
async def getHospitals(db:Session=Depends(get_db)):
    return

#Get all data for one hospital
@app.get('hospitals/{hospital_name}', response_model=schemas.HospitalCases)
async def getByHospitalName(hospital_name:str,db:Session=Depends(get_db)):
    return

#Add a  new hospital
@app.post('/hospitals', response_model=schemas.HospitalCases)
def create_hospital(hospital:schemas.HospitalCasesCreate, db:Session=Depends(get_db)):
    return crud.addHospital(db,hospital)