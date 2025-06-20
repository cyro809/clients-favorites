from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.core.security import get_current_client
from app.models.client import Client
from app.repository import client as client_repository
from app.repository import favorite as favorite_repository
from app.schemas.client import ClientOutput, ClientCreateInput, ClientUpdateInput

router = APIRouter()

@router.get("/{client_id}", response_model=ClientOutput, status_code=200)
async def get_client(client_id: int, current_client: Client = Depends(get_current_client), db: AsyncSession = Depends(get_db)):
    if client_id != current_client.id:
        raise HTTPException(status_code=403, detail="Forbidden")
    client = await client_repository.get_client(db, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@router.put("/{client_id}", response_model=ClientOutput)
async def update_client(client_id: int, client_input: ClientUpdateInput, current_client: Client = Depends(get_current_client), db: AsyncSession = Depends(get_db)):
    if client_id != current_client.id:
        raise HTTPException(status_code=403, detail="Forbidden")
    client = await client_repository.update_client(db, client_id, client_input)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    
    return client
    

@router.delete("/{client_id}", status_code=204)
async def delete_client(client_id: int, current_client: Client = Depends(get_current_client), db: AsyncSession = Depends(get_db)):
    if client_id != current_client.id:
        raise HTTPException(status_code=403, detail="Forbidden")
    client = await client_repository.delete_client(db, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")