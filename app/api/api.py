from fastapi import APIRouter
from app.api.routers import clients
from app.api.routers import favorites

api_router = APIRouter()
api_router.include_router(clients.router, prefix="/clients", tags=["clients"])
api_router.include_router(favorites.router, prefix="/clients/{client_id}/favorites", tags=["favorites"])
