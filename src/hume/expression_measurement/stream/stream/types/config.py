# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from .....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .stream_face import StreamFace
from .stream_language import StreamLanguage


class Config(UniversalBaseModel):
    """
    Configuration used to specify which models should be used and with what settings.
    """

    burst: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    Configuration for the vocal burst emotion model.
    
    Note: Model configuration is not currently available in streaming.
    
    Please use the default configuration by passing an empty object `{}`.
    """

    face: typing.Optional[StreamFace] = pydantic.Field(default=None)
    """
    Configuration for the facial expression emotion model.
    
    Note: Using the `reset_stream` parameter does not have any effect on face identification. A single face identifier cache is maintained over a full session whether `reset_stream` is used or not.
    """

    facemesh: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    Configuration for the facemesh emotion model.
    
    Note: Model configuration is not currently available in streaming.
    
    Please use the default configuration by passing an empty object `{}`.
    """

    language: typing.Optional[StreamLanguage] = pydantic.Field(default=None)
    """
    Configuration for the language emotion model.
    """

    prosody: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    Configuration for the speech prosody emotion model.
    
    Note: Model configuration is not currently available in streaming.
    
    Please use the default configuration by passing an empty object `{}`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
