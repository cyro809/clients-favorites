from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.settings import settings

DATABASE_URL = settings.DATABASE_URL.replace('postgresql+psycopg2', 'postgresql+asyncpg')

engine = create_async_engine(DATABASE_URL, pool_size=5, max_overflow=10, future=True, echo=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

Base = declarative_base()

async def get_db():
    async with async_session() as session:
        yield session