# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class DescriptionsScore(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    Name of the descriptive feature being expressed.
    """

    score: float = pydantic.Field()
    """
    Embedding value for the descriptive feature being expressed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
