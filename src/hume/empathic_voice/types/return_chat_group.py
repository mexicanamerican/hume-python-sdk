# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .return_config_spec import ReturnConfigSpec


class ReturnChatGroup(UniversalBaseModel):
    """
    A description of chat_group and its status
    """

    id: str = pydantic.Field()
    """
    Identifier for the Chat Group. Any Chat resumed from this Chat Group will have the same `chat_group_id`. Formatted as a UUID.
    """

    first_start_timestamp: int = pydantic.Field()
    """
    Time at which the first Chat in this Chat Group was created. Measured in seconds since the Unix epoch.
    """

    most_recent_start_timestamp: int = pydantic.Field()
    """
    Time at which the most recent Chat in this Chat Group was created. Measured in seconds since the Unix epoch.
    """

    most_recent_chat_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The `chat_id` of the most recent Chat in this Chat Group. Formatted as a UUID.
    """

    most_recent_config: typing.Optional[ReturnConfigSpec] = None
    num_chats: int = pydantic.Field()
    """
    The total number of Chats in this Chat Group.
    """

    active: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Denotes whether there is an active Chat associated with this Chat Group.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
