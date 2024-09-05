# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2


class TimeRange(UniversalBaseModel):
    """
    A time range with a beginning and end, measured in seconds.
    """

    begin: typing.Optional[float] = pydantic.Field(default=None)
    """
    Beginning of time range in seconds.
    """

    end: typing.Optional[float] = pydantic.Field(default=None)
    """
    End of time range in seconds.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
