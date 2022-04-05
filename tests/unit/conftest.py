from typing import Any, Union
from unittest import mock
from unittest.mock import AsyncMock, MagicMock

import pytest
from horizons_client.entities.enums import Planets, ResponseOptions
from horizons_client.services.horizons_request_service import HorizonsRequestService
from horizons_client.services.response_object import ResponseObject


@pytest.fixture
def test_request(test_start_time, test_end_time) -> list[dict[str, Any]]:
    yield [
        {
            "target": f"{Planets.MARS}",
            "startTime": str(test_start_time),
            "endTime": str(test_end_time),
        }
    ]


@pytest.fixture
def test_response(test_start_time, test_end_time) -> list[ResponseObject]:
    base_response = {
        f"{ResponseOptions.RA_ICRF}": 300.765,
        f"{ResponseOptions.DEC_ICRF}": -12.8,
    }
    yield [
        ResponseObject(
            {**base_response, f"{ResponseOptions.DATE}": str(test_start_time)}
        ),
        ResponseObject(
            {**base_response, f"{ResponseOptions.DATE}": str(test_end_time)}
        ),
    ]


@pytest.fixture
def patch_horizons_client(test_response) -> Union[MagicMock, AsyncMock]:
    with mock.patch.object(HorizonsRequestService, "make_request") as mock_svc:
        mock_svc.return_value = test_response
        yield mock_svc
