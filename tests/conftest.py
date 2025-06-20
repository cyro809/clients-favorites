import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app
import pytest_asyncio
from sqlalchemy import text
from app.core.database import async_session


@pytest_asyncio.fixture(autouse=True)
async def async_session_fixture():
    async with async_session() as session:
        yield session

@pytest_asyncio.fixture
async def async_client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client

@pytest_asyncio.fixture(autouse=True)
async def clean_db(async_session_fixture):
    yield
    await async_session_fixture.execute(text("TRUNCATE TABLE favorites, clients RESTART IDENTITY CASCADE"))
    print("TRUNCATE========")
    await async_session_fixture.commit()