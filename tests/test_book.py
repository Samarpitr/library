from fastapi.testclient import TestClient
from app.main import app 
from app.models.books import Book
from app.db.db_setup import get_session
from httpx import AsyncClient, ASGITransport
import random, string


import pytest
from httpx import AsyncClient

@pytest.fixture
def anyio_backend():
    return 'asyncio'


@pytest.mark.anyio
async def test_book_create():
    title = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=7))
    payload = {'title': title, 'author' : 'Test1', 'publication_year': 2024}
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post("/books", json=payload)
    assert response.status_code == 200
