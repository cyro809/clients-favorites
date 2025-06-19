from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.repository import favorite as favorite_repository
from app.repository import client as client_repository
from app.schemas.favorite import FavoriteOutput, FavoriteCreateInput, FavoriteBase
from app.schemas.client import ClientOutput
from app.services.fakestore_api_service import FakeStoreApiService
from typing import List


FAKESTORE_API_URL = "https://fakestoreapi.com"
router = APIRouter()

@router.get("/", response_model=List[FavoriteOutput], status_code=200)
async def get_client_favorites(client_id: int, db: AsyncSession = Depends(get_db)):
    client = await client_repository.get_client(db, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")

    client_favorites = await favorite_repository.get_favorites_by_client(db, client_id)
    return client_favorites


@router.post("/", response_model=FavoriteOutput, status_code=201)
async def add_client_favorite(client_id: int, favorite_input: FavoriteCreateInput, db: AsyncSession = Depends(get_db)):
    fakestore_service = FakeStoreApiService(FAKESTORE_API_URL)
    favorite_product = await fakestore_service.get_product_by_id(favorite_input.product_id)
    if not favorite_product:
        raise HTTPException(status_code=404, detail="Product not found")
    print(favorite_product)
    favorite_product_input = FavoriteBase(
        product_id=favorite_product["id"],
        title=favorite_product["title"],
        image=favorite_product["image"],
        price=favorite_product["price"],
        rating=favorite_product.get("rating", {}).get("rate")
    )
    db_favorite_product = await favorite_repository.add_favorite_product(db, client_id, favorite_product_input)

    return db_favorite_product
    

