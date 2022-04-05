from typing import Union

from fastapi import APIRouter, Depends
from horizons_client.entities.enums import Moons, Planets
from horizons_client.services.horizons_request_service import HorizonsRequestService

from horizons_web_service.models import EphemerideRequest, EphemerideResponse
from horizons_web_service.validators import validate_horizons_requests

horizons_router = APIRouter()


@horizons_router.get("/health")
async def health_endpoint() -> str:
    return "pong"


@horizons_router.post("/ephemerides")
async def ephemerides_endpoint(
    requests: list[EphemerideRequest] = Depends(validate_horizons_requests),
) -> dict[Union[Planets, Moons] : list[EphemerideResponse]]:
    responses = {}
    for request in requests:
        horizons_svc = HorizonsRequestService(request.to_horizons_request())
        horizons_res = await horizons_svc.make_request()
        responses.update(
            {
                request.target: [
                    EphemerideResponse(**res.__dict__) for res in horizons_res
                ]
            }
        )
    return responses
