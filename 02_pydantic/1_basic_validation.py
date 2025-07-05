from pydantic import BaseModel, EmailStr, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    
    name: Annotated[str, Field(max_length=60, title="Name of the patient", description="provide the patient name in lessthan 60 characters", examples=["Ajay","Rohit"])]
    email: EmailStr
    age : int = Field(gt=0, lt=100)
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=None,description="Is the patient married or not")]
    allergies: Annotated[Optional[List[str]], Field(default=None,emax_length=5)]
    contact_details: Dict[str, str]

def insert_patient_data(patient: Patient):
    # print(patient.name)
    # print(patient.age)
    # print(patient.weight)
    # print(type(patient))
    print(patient)
    print("inserted")


patient_data = {'name':"Ajay","email":"a.kumar01c@gmail.com", "age": 24,"weight": 80,"allergies":["dust"], "contact_details":{"phone": "9090909090"}}

patient1 = Patient(**patient_data)

insert_patient_data(patient1)