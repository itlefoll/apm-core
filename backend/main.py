from fastapi import FastAPI, Body
from typing import List
from backend.api.loop_client import get_vehicles, get_vehicles_mock
from backend.api.models import Vehicle, VehicleSyncRequest

app = FastAPI()

@app.get("/vehicles", response_model=List[Vehicle])
async def read_vehicles(mock: bool = False):
    """
    Devuelve la lista de vehículos desde Loop (mock si ?mock=true)
    """
    if mock:
        return await get_vehicles_mock()
    return await get_vehicles_mock()




@app.post("/vehicles/sync", response_model=List[Vehicle])
async def sync_vehicles(
    dto: VehicleSyncRequest = Body(...),
    mock: bool = False
):
    """
    Devuelve la lista de vehículos desde Loop (mock si ?mock=true)
    """
    if mock:
        result = await get_vehicles_mock(dto)
        return result
    return await get_vehicles(dto)



