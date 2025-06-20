from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.models.client import Client
from app.core import security
from app.schemas.token import Token
from app.schemas.client import ClientCreateInput, ClientOutput, ClientInputDatabase
from app.repository import client as client_repository

router = APIRouter()

@router.post("/signup", response_model=ClientOutput, status_code=201)
async def signup(client_input: ClientCreateInput, db: AsyncSession = Depends(get_db)):
    db_client = await client_repository.get_client_by_email(db, client_input.email)
    if db_client:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = security.get_password_hash(client_input.password)
    db_client_input = ClientInputDatabase(
        name=client_input.name,
        email=client_input.email,
        hashed_password=hashed_password
    )
    new_client = await client_repository.create_client(db, db_client_input)
    return new_client

@router.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    db_client = await client_repository.get_client_by_email(db, form_data.username) 
    if not db_client or not security.verify_password(form_data.password, db_client.hashed_password):
        raise  HTTPException(status_code=401, detail="Wrong email or password")
    
    access_token = security.create_access_token(data={"sub": str(db_client.id)})
    return {"access_token": access_token, "token_type": "bearer"}