# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error_level import ErrorLevel
from .tool_type import ToolType


class ToolErrorMessage(UniversalBaseModel):
    """
    When provided, the output is a function call error.
    """

    code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Error code. Identifies the type of error encountered.
    """

    content: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional text passed to the supplemental LLM in place of the tool call result. The LLM then uses this text to generate a response back to the user, ensuring continuity in the conversation if the tool errors.
    """

    custom_session_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Used to manage conversational state, correlate frontend and backend data, and persist conversations across EVI sessions.
    """

    error: str = pydantic.Field()
    """
    Error message from the tool call, not exposed to the LLM or user.
    """

    level: typing.Optional[ErrorLevel] = pydantic.Field(default=None)
    """
    Indicates the severity of an error; for a Tool Error message, this must be `warn` to signal an unexpected event.
    """

    tool_call_id: str = pydantic.Field()
    """
    The unique identifier for a specific tool call instance.
    
    This ID is used to track the request and response of a particular tool invocation, ensuring that the Tool Error message is linked to the appropriate tool call request. The specified `tool_call_id` must match the one received in the [Tool Call message](/reference/empathic-voice-interface-evi/chat/chat#receive.ToolCallMessage.type).
    """

    tool_type: typing.Optional[ToolType] = pydantic.Field(default=None)
    """
    Type of tool called. Either `builtin` for natively implemented tools, like web search, or `function` for user-defined tools.
    """

    type: typing.Literal["tool_error"] = pydantic.Field(default="tool_error")
    """
    The type of message sent through the socket; for a Tool Error message, this must be `tool_error`.
    
    Upon receiving a [Tool Call message](/reference/empathic-voice-interface-evi/chat/chat#receive.ToolCallMessage.type) and failing to invoke the function, this message is sent to notify EVI of the tool's failure.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
