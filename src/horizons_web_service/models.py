from datetime import datetime, timedelta
from typing import Optional, Union

from horizons_client.entities.enums import (
    AngleFormat,
    EphemerideOptions,
    Moons,
    Observers,
    Planets,
    StepSize,
)
from horizons_client.services.request_objects import (
    BaseRequestObject,
    CenterRequestObject,
    CommandRequestObject,
    StartTimeRequest,
    StopTimeRequest,
)
from humps.camel import case
from pydantic import BaseModel, Field


def to_camel(string):
    return case(string)


class BaseEphemerideModel(BaseModel):
    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True


class EphemerideOptionsRequest(BaseEphemerideModel):
    angle_format: AngleFormat = Field(default=AngleFormat.DEG)
    step_site: StepSize = Field(default=StepSize.HOUR)
    options: list[EphemerideOptions] = Field(
        default=[EphemerideOptions.APPARENT_RA_AND_DEC]
    )


class EphemerideRequest(BaseEphemerideModel):
    target: Union[Planets, Moons]
    observer: Observers = Field(default=Observers.SUN)
    return_options: EphemerideOptionsRequest = Field(default=EphemerideOptionsRequest())
    start_time: datetime = Field(default=datetime.utcnow())
    end_time: datetime = Field(default=datetime.utcnow() + timedelta(days=1))

    def to_horizons_request(self) -> list[BaseRequestObject]:
        command = CommandRequestObject(value=self.target)
        center = CenterRequestObject(value=self.observer)
        start = StartTimeRequest(value=self.start_time)
        stop = StopTimeRequest(value=self.end_time)
        return [command, center, start, stop]


class EphemerideResponse(BaseEphemerideModel):
    date: datetime
    ra_icrf: Optional[Union[float, str]]
    dec_icrf: Optional[Union[float, str]]
    dev_a_app: Optional[float]
    d_ra: Optional[float]
    ap_mag: Optional[float]
    s_brt: Optional[float]
    delta: Optional[float]
    deldot: Optional[float]

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True
