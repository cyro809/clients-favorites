import pytest

@pytest.mark.asyncio
async def test_should_signup_client(async_client):
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