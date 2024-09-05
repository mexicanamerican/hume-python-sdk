# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2


class StreamModelsEndpointPayloadModelsFace(UniversalBaseModel):
    """
    Configuration for the facial expression emotion model.

    Note: Using the `reset_stream` parameter does not have any effect on face identification. A single face identifier cache is maintained over a full session whether `reset_stream` is used or not.
    """

    facs: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    Configuration for FACS predictions. If missing or null, no FACS predictions will be generated.
    """

    descriptions: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    Configuration for Descriptions predictions. If missing or null, no Descriptions predictions will be generated.
    """

    identify_faces: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to return identifiers for faces across frames. If true, unique identifiers will be assigned to face bounding boxes to differentiate different faces. If false, all faces will be tagged with an "unknown" ID.
    """

    fps_pred: typing.Optional[float] = pydantic.Field(default=None)
    """
    Number of frames per second to process. Other frames will be omitted from the response.
    """

    prob_threshold: typing.Optional[float] = pydantic.Field(default=None)
    """
    Face detection probability threshold. Faces detected with a probability less than this threshold will be omitted from the response.
    """

    min_face_size: typing.Optional[float] = pydantic.Field(default=None)
    """
    Minimum bounding box side length in pixels to treat as a face. Faces detected with a bounding box side length in pixels less than this threshold will be omitted from the response.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
