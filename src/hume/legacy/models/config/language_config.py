"""Configuration for the language emotion model."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from hume.legacy.models import ModelType
from hume.legacy.models.config.model_config_base import ModelConfigBase


@dataclass
class LanguageConfig(ModelConfigBase):
    """Configuration for the language emotion model.

    Args:
        granularity (str | None): The granularity at which to generate predictions.
            Accepted values are `word`, `sentence`, `utterance`, or `conversational_turn`.
            The default is `utterance`.
            `utterance` corresponds to a natural pause or break in conversation
            `conversational_turn` corresponds to a change in speaker.
            This configuration is available for the streaming API, but only with values `word` and `sentence`.
        identify_speakers (bool | None): Whether to return identifiers for speakers over time.
            If true, unique identifiers will be assigned to spoken words to differentiate different speakers.
            If false, all speakers will be tagged with an "unknown" ID.
            This configuration is only available for the batch API.
        sentiment (dict[str, Any] | None): Configuration for Sentiment predictions.
            Sentiment prediction can be enabled by setting "sentiment": {}.
            Currently, Sentiment prediction cannot be further configured with any parameters.
            If missing or null, no sentiment predictions will be generated.
        toxicity (dict[str, Any] | None): Configuration for Toxicity predictions.
            Toxicity prediction can be enabled by setting "toxicity": {}.
            Currently, Toxicity prediction cannot be further configured with any parameters.
            If missing or null, no toxicity predictions will be generated.
    """

    granularity: str | None = None
    identify_speakers: bool | None = None
    sentiment: dict[str, Any] | None = None
    toxicity: dict[str, Any] | None = None

    @classmethod
    def get_model_type(cls) -> ModelType:
        """Get the configuration model type.

        Returns:
            ModelType: Model type.
        """
        return ModelType.LANGUAGE
