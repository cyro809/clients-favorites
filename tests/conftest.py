import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from app.main import app
from app.core.database import engine, Base, get_db
from app.models.client import Client
from app.core.security import get_password_hash

@pytest_asyncio.fixture(scope="function")
async def db_session():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

        async_session = sessionmaker(
            conn,
            expire_on_commit=False,
            class_=AsyncSession,
        )

        async with async_session() as session:
            async def override_get_db():
                yield session

            app.dependency_overrides[get_db] = override_get_db

            yield session

        app.dependency_overrides.clear()


@pytest_asyncio.fixture(scope="function")
async def async_client(db_session):
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client


@pytest_asyncio.fixture(autouse=True)
async def clean_db():
    print(">>> clean_db setup")
    yield
    print(">>> clean_db teardown")
    async with engine.connect() as conn:
        conn = conn.execution_options(isolation_level="AUTOCOMMIT")
        await conn.execute(text("TRUNCATE TABLE favorites, clients RESTART IDENTITY CASCADE"))

