import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Generator

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


@pytest.fixture
def known_request() -> list[dict[str, Any]]:
    with open(
        Path.cwd().parent.joinpath("horizons_request.json"), encoding="utf8"
    ) as json_file:
        yield json.load(json_file)
