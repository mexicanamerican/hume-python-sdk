# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
from .predictions_optional_null_face_prediction import PredictionsOptionalNullFacePrediction
from .predictions_optional_null_burst_prediction import PredictionsOptionalNullBurstPrediction
from .predictions_optional_transcription_metadata_prosody_prediction import (
    PredictionsOptionalTranscriptionMetadataProsodyPrediction,
)
from .predictions_optional_transcription_metadata_language_prediction import (
    PredictionsOptionalTranscriptionMetadataLanguagePrediction,
)
from .predictions_optional_transcription_metadata_ner_prediction import (
    PredictionsOptionalTranscriptionMetadataNerPrediction,
)
from .predictions_optional_null_facemesh_prediction import PredictionsOptionalNullFacemeshPrediction
from ....core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ModelsPredictions(UniversalBaseModel):
    face: typing.Optional[PredictionsOptionalNullFacePrediction] = None
    burst: typing.Optional[PredictionsOptionalNullBurstPrediction] = None
    prosody: typing.Optional[PredictionsOptionalTranscriptionMetadataProsodyPrediction] = None
    language: typing.Optional[PredictionsOptionalTranscriptionMetadataLanguagePrediction] = None
    ner: typing.Optional[PredictionsOptionalTranscriptionMetadataNerPrediction] = None
    facemesh: typing.Optional[PredictionsOptionalNullFacemeshPrediction] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
