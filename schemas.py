from pydantic import BaseModel
from datetime import  datetime

class Summary(BaseModel):
    id:int
    cases:int
    deaths:int
    recoveries:int
    lastUpdated:datetime

    class Config:
        orm_mode = True

class Timeline(BaseModel):
    createdAt:datetime
    cases:int
    deaths:int
    recoveries:int

    class Config:
        orm_mode = True

class HospitalCases(BaseModel):
    hospitalName:str
    admissions:int
    discharge:int
    deaths:int
    lastUpdated:datetime

    class Config:
        orm_mode = True

class HospitalCasesCreate(HospitalCases):
    pass

class AgeGender(BaseModel):
    ageGroup:str
    females:int
    males:int
    totalAgeGroup:int
    lastUpdated:datetime

    class Config:
        orm_mode = True

class DistrictCases(BaseModel):
    districtName:str
    region:str
    cases:int
    deaths:int
    recoveries:int
    lastUpdated:datetime

    class Config:
        orm_mode = True