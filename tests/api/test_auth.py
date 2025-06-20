import pytest
from app.models.client import Client
from app.core.security import get_password_hash

@pytest.mark.asyncio
async def test_signup_client_should_signup_client_succesfully(async_client):
    payload = {
        "name": "Cyro",
        "email": "cyro@email.com",
        "password": "123456"
    }
    response = await async_client.post("/api/auth/signup", json=payload)

    assert response.status_code == 201
    response_json = response.json()
    assert response_json["email"] == "cyro@email.com"
    assert response_json["name"] == "Cyro"

@pytest.mark.asyncio
async def test_signup_client_should_raise_error_if_email_already_registered(async_client, db_session):
    # Insere diretamente no banco para simular cliente já cadastrado
    hashed_password = get_password_hash("123456")
    existing_client = Client(name="Cyro", email="cyro@email.com", hashed_password=hashed_password)
    db_session.add(existing_client)
    await db_session.commit()

    payload = {
        "name": "Cyro",
        "email": "cyro@email.com",
        "password": "123456"
    }
    response = await async_client.post("/api/auth/signup", json=payload)

    assert response.status_code == 400
