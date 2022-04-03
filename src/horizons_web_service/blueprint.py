from typing import Union

from fastapi import APIRouter
from horizons_client.entities.enums import Moons, Planets
from horizons_client.services.horizons_request_service import HorizonsRequestService

from horizons_web_service.models import EphemerideRequest, EphemerideResponse

horizons_router = APIRouter()


@horizons_router.get("/health")
async def health_endpoint() -> str:
    return "pong"


@horizons_router.post("/ephemerides")
async def ephemerides_endpoint(
    requests: list[EphemerideRequest],
) -> dict[Union[Planets, Moons] : list[EphemerideResponse]]:
    responses = {}
    for request in requests:
        horizons_svc = HorizonsRequestService(request.to_horizons_request())
        horizons_res = await horizons_svc.make_request()
        responses.update({request.target: [EphemerideResponse(**dict(res)) for res in horizons_res]})
    return "pong"
