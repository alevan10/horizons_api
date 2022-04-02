import pytest
from httpx import AsyncClient
from horizons_web_service.app import app


@pytest.fixture
def test_client() -> AsyncClient:
    yield AsyncClient(app=app, base_url="http://levan.home")
