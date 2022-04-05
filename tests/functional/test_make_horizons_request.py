from typing import Any

import pytest
from horizons_client.entities.enums import Planets


@pytest.fixture
def test_planets() -> list[Planets]:
    yield [f"{planet}" for planet in list(Planets)]


@pytest.fixture
def test_full_request(
    test_planets, test_start_time, test_end_time
) -> list[dict[str, Any]]:
    requests = []
    for planet in test_planets:
        requests.append(
            {
                "target": planet,
                "startTime": str(test_start_time),
                "endTime": str(test_end_time),
            }
        )
    yield requests


@pytest.mark.asyncio
async def test_successful_post(test_client, test_full_request, test_planets):
    res = await test_client.post("/ephemerides", json=test_full_request)
    assert res.status_code == 200
    planets_data = res.json()
    for planet in test_planets:
        ephems = planets_data.get(planet)
        assert ephems and len(ephems) == 2
        for ephem in ephems:
            assert ephem.get("date")
            assert ephem.get("raIcrf")
