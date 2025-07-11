# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .posted_event_message_spec import PostedEventMessageSpec


class PostedEventMessageSpecs(UniversalBaseModel):
    """
    Collection of event messages returned by the server.

    Event messages are sent by the server when specific events occur during a chat session. These messages are used to configure behaviors for EVI, such as controlling how EVI starts a new conversation.
    """

    on_new_chat: typing.Optional[PostedEventMessageSpec] = pydantic.Field(default=None)
    """
    Specifies the initial message EVI provides when a new chat is started, such as a greeting or welcome message.
    """

    on_inactivity_timeout: typing.Optional[PostedEventMessageSpec] = pydantic.Field(default=None)
    """
    Specifies the message EVI provides when the chat is about to be disconnected due to a user inactivity timeout, such as a message mentioning a lack of user input for a period of time.
    
    Enabling an inactivity message allows developers to use this message event for "checking in" with the user if they are not responding to see if they are still active.
    
    If the user does not respond in the number of seconds specified in the `inactivity_timeout` field, then EVI will say the message and the user has 15 seconds to respond. If they respond in time, the conversation will continue; if not, the conversation will end.
    
    However, if the inactivity message is not enabled, then reaching the inactivity timeout will immediately end the connection.
    """

    on_max_duration_timeout: typing.Optional[PostedEventMessageSpec] = pydantic.Field(default=None)
    """
    Specifies the message EVI provides when the chat is disconnected due to reaching the maximum chat duration, such as a message mentioning the time limit for the chat has been reached.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
