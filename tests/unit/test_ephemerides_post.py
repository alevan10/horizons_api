import pytest


@pytest.mark.usefixtures("patch_horizons_client")
@pytest.mark.asyncio
async def test_successful_post(test_client, test_request, test_response):
    res = await test_client.post("/ephemerides", json=test_request)
    assert res.status_code == 200
    api_data = res.json()
    mars_data = api_data.get(test_request[0]["target"])
    assert mars_data
    assert len(mars_data) == 2
    assert mars_data[0]["date"] == str(test_response[0].date).replace(" ", "T")
    assert mars_data[1]["date"] == str(test_response[1].date).replace(" ", "T")


@pytest.mark.usefixtures("patch_horizons_client")
@pytest.mark.asyncio
async def test_422_repeated_target_post(test_client, test_request):
    bad_requests = [test_request[0], test_request[0]]
    res = await test_client.post("/ephemerides", json=bad_requests)
    assert res.status_code == 422
