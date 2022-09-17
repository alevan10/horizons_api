import os

from blueprint import horizons_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# import uvicorn


default_origins = [
    "http://levan.home",
    "https://levan.home",
    "http://localhost",
    "http://localhost:8080",
]


def create_app() -> FastAPI:
    horizons_app = FastAPI()
    horizons_app.include_router(horizons_router)
    default_origins.extend(os.environ.get("ALLOWED_ORIGINS", []))
    horizons_app.add_middleware(
        CORSMiddleware,
        allow_origins=default_origins,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return horizons_app


app = create_app()

# Uncomment for local development
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8081)
