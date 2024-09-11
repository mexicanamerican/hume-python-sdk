# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import pydantic
from .return_prompt_version_type import ReturnPromptVersionType
import typing
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class ReturnPrompt(UniversalBaseModel):
    """
    A Prompt associated with this Config.
    """

    id: str = pydantic.Field()
    """
    Identifier for a Prompt. Formatted as a UUID.
    """

    version: int = pydantic.Field()
    """
    Version number for a Prompt.
    
    Prompts, as well as Configs and Tools, are versioned. This versioning system supports iterative development, allowing you to progressively refine prompts and revert to previous versions if needed.
    
    Version numbers are integer values representing different iterations of the Prompt. Each update to the Prompt increments its version number.
    """

    version_type: ReturnPromptVersionType = pydantic.Field()
    """
    Versioning method for a Prompt. Either `FIXED` for using a fixed version number or `LATEST` for auto-updating to the latest version.
    """

    version_description: typing.Optional[str] = pydantic.Field(default=None)
    """
    An optional description of the Prompt version.
    """

    name: str = pydantic.Field()
    """
    Name applied to all versions of a particular Prompt.
    """

    created_on: int = pydantic.Field()
    """
    Time at which the Prompt was created. Measured in seconds since the Unix epoch.
    """

    modified_on: int = pydantic.Field()
    """
    Time at which the Prompt was last modified. Measured in seconds since the Unix epoch.
    """

    text: str = pydantic.Field()
    """
    Instructions used to shape EVI’s behavior, responses, and style.
    
    You can use the Prompt to define a specific goal or role for EVI, specifying how it should act or what it should focus on during the conversation. For example, EVI can be instructed to act as a customer support representative, a fitness coach, or a travel advisor, each with its own set of behaviors and response styles.
    
    For help writing a system prompt, see our [Prompting Guide](/docs/empathic-voice-interface-evi/prompting).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow