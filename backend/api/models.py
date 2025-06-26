from pydantic import BaseModel

def to_camel(string: str) -> str:
    parts = string.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

class Vehicle(BaseModel):
    id: int
    name: str
    status: str

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True

class VehicleSyncRequest(BaseModel):
    start_mode: int

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True