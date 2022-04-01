import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_health_endpoint(test_client: AsyncClient):
    res = await test_client.get("/health")
    assert res.status_code == 200

