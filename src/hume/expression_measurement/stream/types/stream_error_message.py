# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from .job_details import JobDetails
from ....core.pydantic_utilities import IS_PYDANTIC_V2


class StreamErrorMessage(UniversalBaseModel):
    """
    Error message
    """

    error: typing.Optional[str] = pydantic.Field(default=None)
    """
    Error message text.
    """

    code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for the error.
    """

    payload_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    If a payload ID was passed in the request, the same payload ID will be sent back in the response body.
    """

    job_details: typing.Optional[JobDetails] = pydantic.Field(default=None)
    """
    If the job_details flag was set in the request, details about the current streaming job will be returned in the response body.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
