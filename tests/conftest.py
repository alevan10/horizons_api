from datetime import datetime, timedelta
from typing import Generator

import pytest
from httpx import AsyncClient

from horizons_web_service.app import app


@pytest.fixture
def client_generator() -> Generator[AsyncClient, None, None]:
    def _generator(url: str = "levan.home") -> AsyncClient:
        return AsyncClient(app=app, base_url=f"http://{url}")

    yield _generator


@pytest.fixture
def test_client(client_generator) -> AsyncClient:
    yield client_generator()


@pytest.fixture
def test_start_time() -> datetime:
    yield datetime.utcnow()


@pytest.fixture
def test_end_time(test_start_time) -> datetime:
    yield test_start_time + timedelta(hours=1)
