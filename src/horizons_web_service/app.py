from blueprint import horizons_router
from fastapi import FastAPI


def create_app() -> FastAPI:
    horizons_app = FastAPI()
    horizons_app.include_router(horizons_router)
    return horizons_app


app = create_app()
