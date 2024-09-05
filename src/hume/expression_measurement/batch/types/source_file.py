# This file was auto-generated by Fern from our API Definition.

from .file import File
import typing
from ....core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class SourceFile(File):
    type: typing.Literal["file"] = "file"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
