# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .granularity import Granularity
from .window import Window


class Prosody(UniversalBaseModel):
    """
    The Speech Prosody model analyzes the intonation, stress, and rhythm of spoken word.

    Recommended input file types: `.wav`, `.mp3`, `.mp4`
    """

    granularity: typing.Optional[Granularity] = None
    window: typing.Optional[Window] = None
    identify_speakers: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to return identifiers for speakers over time. If `true`, unique identifiers will be assigned to spoken words to differentiate different speakers. If `false`, all speakers will be tagged with an `unknown` ID.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
