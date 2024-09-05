# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
from .return_user_defined_tool_tool_type import ReturnUserDefinedToolToolType
import pydantic
from .return_user_defined_tool_version_type import ReturnUserDefinedToolVersionType
import typing
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class ReturnUserDefinedTool(UniversalBaseModel):
    """
    A specific tool version returned from the server
    """

    tool_type: ReturnUserDefinedToolToolType = pydantic.Field()
    """
    Type of Tool. Either `BUILTIN` for natively implemented tools, like web search, or `FUNCTION` for user-defined tools.
    """

    id: str = pydantic.Field()
    """
    Identifier for a Tool. Formatted as a UUID.
    """

    version: int = pydantic.Field()
    """
    Version number for a Tool.
    
    Tools, as well as Configs and Prompts, are versioned. This versioning system supports iterative development, allowing you to progressively refine tools and revert to previous versions if needed.
    
    Version numbers are integer values representing different iterations of the Tool. Each update to the Tool increments its version number.
    """

    version_type: ReturnUserDefinedToolVersionType = pydantic.Field()
    """
    Versioning method for a Tool. Either `FIXED` for using a fixed version number or `LATEST` for auto-updating to the latest version.
    """

    version_description: typing.Optional[str] = pydantic.Field(default=None)
    """
    An optional description of the Tool version.
    """

    name: str = pydantic.Field()
    """
    Name applied to all versions of a particular Tool.
    """

    created_on: int = pydantic.Field()
    """
    Time at which the Tool was created. Measured in seconds since the Unix epoch.
    """

    modified_on: int = pydantic.Field()
    """
    Time at which the Tool was last modified. Measured in seconds since the Unix epoch.
    """

    fallback_content: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional text passed to the supplemental LLM in place of the tool call result. The LLM then uses this text to generate a response back to the user, ensuring continuity in the conversation if the Tool errors.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    An optional description of what the Tool does, used by the supplemental LLM to choose when and how to call the function.
    """

    parameters: str = pydantic.Field()
    """
    Stringified JSON defining the parameters used by this version of the Tool.
    
    These parameters define the inputs needed for the Tool’s execution, including the expected data type and description for each input field. Structured as a stringified JSON schema, this format ensures the tool receives data in the expected format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
