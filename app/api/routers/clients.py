from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db

router = APIRouter()

@router.post("/")
async def create_client(db: AsyncSession = Depends(get_db)):
    return {"msg": "Client created"}

@router.get("/{client_id}")
async def get_client(client_id: int, db: AsyncSession = Depends(get_db)):
    return {"msg": f"get client {client_id}"}

@router.put("/{client_id}")
async def update_client(client_id: int, db: AsyncSession = Depends(get_db)):
    return {"msg": f"update client {client_id}"}

@router.delete("/{client_id}")
async def delete_client(client_id: int, db: AsyncSession = Depends(get_db)):
    return {"msg": f"delete client {client_id}"}