from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    
    name: str
    email: EmailStr
    age : int
    weight: float
    married: bool = False
    allergies: List[str]
    contact_details: Dict[str, str]
    
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domain = ["hdfc.com","icici.com"]
        # abc@gmail.com
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domain:
            raise ValueError("Not a valid domain")
        return value
    
    @field_validator("name") 
    @classmethod
    def name_validator(cls, value):
        return value.upper()
    
    @field_validator('age', mode='before') #by default mode=after
    @classmethod
    def age_validator(cls, value):
        if 0 < value < 100:
            return value
        raise ValueError("Age value should be in between 0 - 100")

def insert_patient_data(patient: Patient):
    print(patient)
    print("inserted")


patient_data = {
    'name':"Ajay",
    "email":"a.kumar01c@hdfc.com",
    "age": 24,
    "weight": 80,
    "allergies":["dust"],
    "contact_details":{
            "phone": "9090909090"
    }}

patient1 = Patient(**patient_data) # validation -> type coercion

insert_patient_data(patient1)