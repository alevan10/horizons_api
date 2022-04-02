from fastapi import APIRouter

horizons_router = APIRouter()


@horizons_router.get("/health")
async def health_endpoint() -> str:
    return "pong"
