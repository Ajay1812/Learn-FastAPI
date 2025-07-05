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

temp = patient1.model_dump(include=["name","age"]) # convert pydantic object to python dict
print(temp)
print(type(temp))

temp1 = patient1.model_dump_json() # to json
print(temp1)
print(type(temp1)) # python treat as str

temp2 = patient1.model_dump(exclude={"address": ["pincode"]})
print(temp2)