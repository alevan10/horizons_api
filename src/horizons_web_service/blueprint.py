from fastapi import APIRouter

horizons_router = APIRouter()


@horizons_router.get("/health")
async def health_endpoint() -> str:
    return "pong"


@horizons_router.post("/ephemerides")
async def ephemerides_endpoint() -> str:
    return "pong"
