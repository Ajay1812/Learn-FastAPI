from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):
    name: str
    email: EmailStr
    age : int
    weight: float # kg
    height: float # mtr
    married: bool = False
    allergies: List[str]
    contact_details: Dict[str, str]
    
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/self.height**2,2)
        return bmi
    
def insert_patient_data(patient: Patient):
    print(patient)
    print("BMI: ", patient.bmi)
    print("inserted")

patient_data = {
    'name':"Ajay",
    "email":"a.kumar01c@hdfc.com",
    "age": 64,
    "weight": 80,
    "height" : 1.65,
    "allergies":["dust"],
    "contact_details":{
            "phone": "9090909090",
            "emergency": "8989898989"
    }}

patient1 = Patient(**patient_data) # validation -> type coercion
insert_patient_data(patient1)