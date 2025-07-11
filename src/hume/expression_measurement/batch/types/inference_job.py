# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2
from .job_inference import JobInference


class InferenceJob(JobInference):
    type: str = pydantic.Field()
    """
    Denotes the job type.
    
    Jobs created with the Expression Measurement API will have this field set to `INFERENCE`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
