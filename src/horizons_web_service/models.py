from datetime import datetime, timedelta
from typing import Optional, Union

from horizons_client.entities.enums import (
    AngleFormat,
    EphemerideOptions,
    Moons,
    Observers,
    Planets,
    ResponseOptions,
    StepSize,
)
from horizons_client.services.request_objects import (
    BaseRequestObject,
    CenterRequestObject,
    CommandRequestObject,
    StartTimeRequest,
    StopTimeRequest,
)
from pydantic import BaseModel, Field


class EphemerideOptionsRequest(BaseModel):
    angle_format: AngleFormat = Field(default=AngleFormat.DEG)
    step_site: StepSize = Field(default=StepSize.HOUR)
    options: list[EphemerideOptions] = Field(
        default=[EphemerideOptions.APPARENT_RA_AND_DEC]
    )


class EphemerideRequest(BaseModel):
    target: Union[Planets, Moons]
    observer: Observers = Field(default=Observers.SUN)
    return_options: EphemerideOptionsRequest
    start_time: datetime = Field(default=datetime.utcnow())
    end_time: datetime = Field(default=datetime.utcnow() + timedelta(days=1))

    def to_horizons_request(self) -> list[BaseRequestObject]:
        command = CommandRequestObject(value=self.target)
        center = CenterRequestObject(value=self.observer)
        start = StartTimeRequest(value=self.start_time)
        stop = StopTimeRequest(value=self.end_time)
        return [command, center, start, stop]


class EphemerideResponse(BaseModel):
    date: datetime
    ra_icrf: float
    dec_icrf: float
    dev_a_app: float
    d_ra: float
    ap_mag: float
    s_brt: float
    delta: float
    deldot: float
