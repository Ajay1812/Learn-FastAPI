from pydantic import BaseModel

class Address(BaseModel):
    
    city: str
    state: str
    pincode: str

class Patient(BaseModel):
    
    name: str
    gender: str
    age: int
    address: Address

address_dict = {"city": "gurgaon", "state":"haryana", "pincode":"122002"}

address1 = Address(**address_dict)

patient_dict = {
    "name":"Ajay",
    "gender": "M",
    "age": 24,
    "address": address1
}

patient1 = Patient(**patient_dict)
print(patient1)
print(patient1.address.pincode)