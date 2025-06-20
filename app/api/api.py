from fastapi import APIRouter
from app.api.routers import clients
from app.api.routers import favorites
from app.api.routers import auth

api_router = APIRouter()
api_router.include_router(clients.router, prefix="/clients", tags=["clients"])
api_router.include_router(favorites.router, prefix="/clients/{client_id}/favorites", tags=["favorites"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])