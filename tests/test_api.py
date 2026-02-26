
import pytest
from httpx import AsyncClient, ASGITransport

from test1 import app

@pytest.mark.asyncio
async def test_post_cars():
    async with AsyncClient(transport=ASGITransport(app=app),
                           base_url="http://test") as ac:
        response = await ac.post("/cars",
                            json={
                            "car_model": "FFFFFF",
                            "year": 2016,
                            "country": "Russia"})
        assert response.status_code == 200
        data = response.json()
        print(data)
        assert data == {"success": "True"}


@pytest.mark.asyncio
async def test_get_cars():
    async with AsyncClient(transport=ASGITransport(app=app),
                           base_url="http://test") as ac:
        response = await ac.get("/cars")
        assert response.status_code == 200
        data = response.json()
        print(data)
        assert len(data) == 3

