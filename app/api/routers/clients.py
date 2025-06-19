from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.repository import client as client_repository
from app.repository import favorite as favorite_repository
from app.schemas.client import ClientOutput, ClientCreateInput, ClientUpdateInput

router = APIRouter()

@router.post("/", response_model=ClientOutput, status_code=201)
async def create_client(client_input: ClientCreateInput, db: AsyncSession = Depends(get_db)):
    client = await client_repository.get_client_by_email(db, client_input.email)
    if client:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    client = await client_repository.create_client(db, client_input)
    return client

@router.get("/{client_id}", response_model=ClientOutput, status_code=200)
async def get_client(client_id: int, db: AsyncSession = Depends(get_db)):
    client = await client_repository.get_client(db, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@router.put("/{client_id}", response_model=ClientOutput)
async def update_client(client_id: int, client_input: ClientUpdateInput, db: AsyncSession = Depends(get_db)):
    client = await client_repository.update_client(db, client_id, client_input)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    
    return client
    

@router.delete("/{client_id}", status_code=204)
async def delete_client(client_id: int, db: AsyncSession = Depends(get_db)):
    client = await client_repository.delete_client(db, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")