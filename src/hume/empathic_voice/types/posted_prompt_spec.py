# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class PostedPromptSpec(UniversalBaseModel):
    """
    A Prompt associated with this Config.
    """

    id: str = pydantic.Field()
    """
    Identifier for a Prompt. Formatted as a UUID.
    """

    version: typing.Optional[int] = pydantic.Field(default=None)
    """
    Version number for a Prompt.
    
    Prompts, as well as Configs and Tools, are versioned. This versioning system supports iterative development, allowing you to progressively refine prompts and revert to previous versions if needed.
    
    Version numbers are integer values representing different iterations of the Prompt. Each update to the Prompt increments its version number.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
