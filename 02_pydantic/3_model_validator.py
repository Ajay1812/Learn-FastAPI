from pydantic import BaseModel, EmailStr, model_validator 
from typing import List, Dict

class Patient(BaseModel):
    name: str
    email: EmailStr
    age : int
    weight: float
    married: bool = False
    allergies: List[str]
    contact_details: Dict[str, str]
    
    @model_validator(mode="after")
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError("Patient older than 60 must have emergency contact")
        return model

def insert_patient_data(patient: Patient):
    print(patient)
    print("inserted")

patient_data = {
    'name':"Ajay",
    "email":"a.kumar01c@hdfc.com",
    "age": 64,
    "weight": 80,
    "allergies":["dust"],
    "contact_details":{
            "phone": "9090909090",
            "emergency": "8989898989"
    }}

patient1 = Patient(**patient_data) # validation -> type coercion
insert_patient_data(patient1)