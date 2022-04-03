from typing import Union

from horizons_client.entities.enums import Moons, Planets, ResponseOptions
from pydantic import BaseModel


class EphemerideOptionsRequest(BaseModel):
    pass


class EphemerideRequest(BaseModel):

    target = Union[Planets, Moons]
    options = list(ResponseOptions)
