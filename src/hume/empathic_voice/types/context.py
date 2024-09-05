# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
from .context_type import ContextType
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class Context(UniversalBaseModel):
    type: typing.Optional[ContextType] = pydantic.Field(default=None)
    """
    The persistence level of the injected context. Specifies how long the injected context will remain active in the session.
    
    There are three possible context types:
    
    - **Persistent**: The context is appended to all user messages for the duration of the session.
    
    - **Temporary**: The context is appended only to the next user message.
    
    - **Editable**: The original context is updated to reflect the new context.
    
    If the type is not specified, it will default to `temporary`.
    """

    text: str = pydantic.Field()
    """
    The context to be injected into the conversation. Helps inform the LLM's response by providing relevant information about the ongoing conversation.
    
    This text will be appended to the end of user messages based on the chosen persistence level. For example, if you want to remind EVI of its role as a helpful weather assistant, the context you insert will be appended to the end of user messages as `{Context: You are a helpful weather assistant}`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
