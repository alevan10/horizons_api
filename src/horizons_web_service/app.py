from fastapi import FastAPI

from blueprint import horizons_router


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(horizons_router)
    return app


app = create_app()
