import os
from typing import Any

import pytest
from aiohttp import ClientSession
from horizons_client.entities.enums import Planets

HORIZONS_API_URL = os.environ.get("HORIZONS_API_URL", "http://levan.home/api/v1")


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
                "observer": "@10",
            }
        )
    yield requests


@pytest.mark.asyncio
async def test_successful_post(test_client, test_full_request, test_planets):
    async with ClientSession() as session:
        async with session.post(
            url=f"{HORIZONS_API_URL}/ephemerides", json=test_full_request
        ) as resp:
            assert resp.ok
            planets_data = await resp.json()
            for planet in test_planets:
                ephems = planets_data.get(planet)
                assert ephems and len(ephems) == 2
                for ephem in ephems:
                    assert ephem.get("date")
                    assert ephem.get("raIcrf")
                    assert isinstance(ephem.get("raIcrf"), float)


@pytest.mark.parametrize(
    "return_options",
    [
        {"angleFormat": "DEG"},
        {"stepSize": "hour"},
        {"angleFormat": "DEG", "stepSize": "hour"},
    ],
)
@pytest.mark.asyncio
async def test_successful_post_with_options(
    test_client, test_full_request, return_options
):
    for request in test_full_request:
        request.update({"returnOptions": return_options})
        async with ClientSession() as session:
            async with session.post(
                url=f"{HORIZONS_API_URL}/ephemerides", json=[request]
            ) as resp:
                assert resp.ok
                planet_data = await resp.json()
                ephems = planet_data.get(request.get("target"))
                assert ephems and len(ephems) == 2
                for ephem in ephems:
                    assert ephem.get("date")
                    assert ephem.get("raIcrf")
                    assert isinstance(ephem.get("raIcrf"), float)


@pytest.mark.asyncio
async def test_successful_post_with_known_request(test_client, known_request):
    async with ClientSession() as session:
        async with session.post(
            url=f"{HORIZONS_API_URL}/ephemerides", json=known_request
        ) as resp:
            assert resp.ok
            planets_data = await resp.json()
            for target in [planet.get("target") for planet in known_request]:
                ephems = planets_data.get(target)
                assert ephems and len(ephems) == 2
                for ephem in ephems:
                    assert ephem.get("date")
                    assert ephem.get("raIcrf")
                    assert isinstance(ephem.get("raIcrf"), float)
