# This file was auto-generated by Fern from our API Definition.

import typing

from ...types.assistant_input import AssistantInput
from ...types.audio_input import AudioInput
from ...types.pause_assistant_message import PauseAssistantMessage
from ...types.resume_assistant_message import ResumeAssistantMessage
from ...types.session_settings import SessionSettings
from ...types.tool_error_message import ToolErrorMessage
from ...types.tool_response_message import ToolResponseMessage
from ...types.user_input import UserInput

PublishEvent = typing.Union[
    AudioInput,
    SessionSettings,
    UserInput,
    AssistantInput,
    ToolResponseMessage,
    ToolErrorMessage,
    PauseAssistantMessage,
    ResumeAssistantMessage,
]
