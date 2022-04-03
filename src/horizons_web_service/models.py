from typing import Union

from horizons_client.entities.enums import Moons, Planets
from pydantic.main import BaseModel


class EphemerideRequest(BaseModel):

    target = Union[Planets, Moons]
