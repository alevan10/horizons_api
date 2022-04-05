from datetime import datetime, timedelta

import pytest
from httpx import AsyncClient

from horizons_web_service.app import app


@pytest.fixture
def test_client() -> AsyncClient:
    yield AsyncClient(app=app, base_url="http://levan.home")


@pytest.fixture
def test_start_time() -> datetime:
    yield datetime.utcnow()


@pytest.fixture
def test_end_time(test_start_time) -> datetime:
    yield test_start_time + timedelta(hours=1)
