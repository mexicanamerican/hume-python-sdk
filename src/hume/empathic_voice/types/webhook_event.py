# This file was auto-generated by Fern from our API Definition.

import typing

from .webhook_event_chat_ended import WebhookEventChatEnded
from .webhook_event_chat_started import WebhookEventChatStarted

WebhookEvent = typing.Union[WebhookEventChatStarted, WebhookEventChatEnded]
