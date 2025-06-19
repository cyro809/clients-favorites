from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.favorite import Favorite
from app.schemas.favorite import FavoriteCreateInput

async def add_favorite_product(db: AsyncSession, client_id: int, favorite_input: FavoriteCreateInput):
    db_favorite = Favorite(
        client_id=client_id,
        product_id=favorite_input.product_id,
        title=favorite_input.title,
        image=favorite_input.image,
        price=favorite_input.price
    )
    await db.add(db_favorite)
    await db.commit()
    await db.refresh(db_favorite)
    return db_favorite

async def get_favorites_by_client(db: AsyncSession, client_id: int):
    result = await db.execute(select(Favorite).where(Favorite.client_id == client_id))
    return result.scalars().all()

async def get_favorite_product(db: AsyncSession, client_id: int, product_id: int):
    result = await db.execute(select(Favorite).where(Favorite.client_id == client_id, Favorite.product_id == product_id))
    return result.scalars().first()

async def delete_favorite_product(db: AsyncSession, client_id: int, product_id: int):
    db_favorite = await get_favorite_product(db, client_id, product_id)

    if db_favorite:
        await db.delete(db_favorite)
        await db.commit()
        await db.refresh(db_favorite)
    return db_favorite