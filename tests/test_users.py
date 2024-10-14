import pytest
from httpx import AsyncClient
from src.users.schemas import UserCreate


@pytest.mark.anyio
async def test_users_create(client: AsyncClient):
    user = UserCreate(email="test@email.com", password="abcdefghijkl")
    response = await client.post("/users", data=user.model_dump_json())

    print(user.model_dump_json())

    assert response.status_code == 201
    assert response.json()["message"] == f"User {user.email}  successfully registered!"