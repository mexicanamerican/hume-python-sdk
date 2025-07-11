# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from .....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.emotion_embedding import EmotionEmbedding
from ...types.sentiment import Sentiment
from ...types.text_position import TextPosition
from ...types.toxicity import Toxicity


class StreamModelPredictionsLanguagePredictionsItem(UniversalBaseModel):
    text: typing.Optional[str] = pydantic.Field(default=None)
    """
    A segment of text (like a word or a sentence).
    """

    position: typing.Optional[TextPosition] = None
    emotions: typing.Optional[EmotionEmbedding] = None
    sentiment: typing.Optional[Sentiment] = None
    toxicity: typing.Optional[Toxicity] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
