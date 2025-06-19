from pydantic import BaseModel, EmailStr
from typing import Optional, List
from app.schemas.favorite import FavoriteOutput

class ClientBase(BaseModel):
    name: str
    email: EmailStr

class ClientCreateInput(ClientBase):
    password: str

class ClientInDatabase(ClientCreateInput):
    id: int
    hashed_password: str

class ClientUpdateInput(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None

class ClientOutput(ClientBase):
    id: int
    favorites: List[FavoriteOutput] = []

    model_config = {
        "from_attributes": True
    }