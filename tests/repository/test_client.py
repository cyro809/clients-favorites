import pytest
from app.repository import client as client_repository
from app.models.client import Client
from app.schemas.client import ClientInputDatabase
from app.core.security import get_password_hash

@pytest.mark.asyncio
async def test_create_and_get_client(db_session):
    # Criar client input fake
    client_input = ClientInputDatabase(
        name="Test User",
        email="test@example.com",
        hashed_password=get_password_hash("test123")
    )

    # Criar no banco
    new_client = await client_repository.create_client(db_session, client_input)
    
    assert new_client.id is not None
    assert new_client.email == "test@example.com"

    # Buscar pelo email
    found_client = await client_repository.get_client_by_email(db_session, "test@example.com")
    
    assert found_client is not None
    assert found_client.email == "test@example.com"
