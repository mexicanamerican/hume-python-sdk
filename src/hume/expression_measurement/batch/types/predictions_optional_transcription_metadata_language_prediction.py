# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .grouped_predictions_language_prediction import GroupedPredictionsLanguagePrediction
from .transcription_metadata import TranscriptionMetadata


class PredictionsOptionalTranscriptionMetadataLanguagePrediction(UniversalBaseModel):
    metadata: typing.Optional[TranscriptionMetadata] = None
    grouped_predictions: typing.List[GroupedPredictionsLanguagePrediction]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
