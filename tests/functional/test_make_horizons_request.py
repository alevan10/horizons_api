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
                "observer": "@10",
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
        res = await test_client.post("/ephemerides", json=[request])
        assert res.status_code == 200
        planet_data = res.json()
        ephems = planet_data.get(request.get("target"))
        assert ephems and len(ephems) == 2
        for ephem in ephems:
            assert ephem.get("date")
            assert ephem.get("raIcrf")


@pytest.mark.asyncio
async def test_successful_post_with_known_request(test_client, known_request):
    res = await test_client.post("/ephemerides", json=known_request)
    assert res.status_code == 200
    planets_data = res.json()
    for target in [planet.get("target") for planet in known_request]:
        ephems = planets_data.get(target)
        assert ephems and len(ephems) == 2
        for ephem in ephems:
            assert ephem.get("date")
            assert ephem.get("raIcrf")
