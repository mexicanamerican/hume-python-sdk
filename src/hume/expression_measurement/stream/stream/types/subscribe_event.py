# This file was auto-generated by Fern from our API Definition.

import typing

from .stream_error_message import StreamErrorMessage
from .stream_model_predictions import StreamModelPredictions
from .stream_warning_message import StreamWarningMessage

SubscribeEvent = typing.Union[StreamModelPredictions, StreamErrorMessage, StreamWarningMessage]
