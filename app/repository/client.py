from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.client import Client
from app.schemas.client import ClientInputDatabase, ClientUpdateInput

async def create_client(db: AsyncSession, client_input: ClientInputDatabase):
    db_client = Client(
        name=client_input.name,
        email=client_input.email,
        hashed_password=client_input.hashed_password
    )
    db.add(db_client)
    await db.commit()
    await db.refresh(db_client)
    return db_client

async def get_client(db: AsyncSession, client_id: int):
    result = await db.execute(select(Client).where(Client.id == client_id))
    return result.scalars().first()

async def get_client_by_email(db: AsyncSession, client_email: str):
    result = await db.execute(select(Client).where(Client.email == client_email))
    return result.scalars().first()

async def update_client(db: AsyncSession, client_id: int, client_input: ClientUpdateInput):
    db_client = await get_client(db, client_id)
    if not db_client:
        return None
    
    if client_input.name:
        db_client.name = client_input.name
    if client_input.email:
        db_client.email = client_input.email

    await db.commit()
    await db.refresh(db_client)
    return db_client

async def delete_client(db: AsyncSession, client_id: int):
    db_client = await get_client(db, client_id)
    if db_client:
        await db.delete(db_client)
        await db.commit()
    return db_client