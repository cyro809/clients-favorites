from fastapi import APIRouter
from app.api.routers import clients

api_router = APIRouter()
api_router.include_router(clients.router, prefix="/clients", tags=["clients"])
