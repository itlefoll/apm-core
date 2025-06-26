

# loop_client.py
import httpx
from typing import List
from fastapi import FastAPI  # Import FastAPI
from .models import Vehicle, VehicleSyncRequest  # Asegúrate que el import sea correcto según tu estructura

app = FastAPI()  # Define the FastAPI app instance

LOOP_API_BASE_URL = "https://integration.loop4.io/api/sync"
COMPANY_TOKEN = "TU_TOKEN_AQUI"  # Reemplaza esto con tu token real


async def get_vehicles(dto: VehicleSyncRequest) -> List[Vehicle]:
    url = f"{LOOP_API_BASE_URL}/vehicles"
    headers = {"token": COMPANY_TOKEN}
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        response.raise_for_status()
        vehicles_data = response.json()
        return [Vehicle(**item) for item in vehicles_data]

async def get_vehicles_mock(dto: VehicleSyncRequest) -> List[Vehicle]:
    return [
        Vehicle(id=1, name="Truck 1", status="active"),
        Vehicle(id=2, name="Truck 2", status="maintenance"),
    ]


