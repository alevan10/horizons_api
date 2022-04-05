from fastapi import HTTPException

from horizons_web_service.models import EphemerideRequest


def validate_horizons_requests(
    requests: list[EphemerideRequest],
) -> list[EphemerideRequest]:
    targets = [request.target for request in requests]
    target_set = set(targets)
    if not len(target_set) == len(targets):
        raise HTTPException(
            status_code=422, detail="Request objects must have unique targets."
        )
    return requests
