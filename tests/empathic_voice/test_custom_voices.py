# This file was auto-generated by Fern from our API Definition.

from hume import HumeClient
from hume import AsyncHumeClient
import typing
from ..utilities import validate_response


async def test_list_custom_voices(client: HumeClient, async_client: AsyncHumeClient) -> None:
    expected_response: typing.Any = {
        "page_number": 1,
        "page_size": 1,
        "total_pages": 1,
        "custom_voices_page": [
            {
                "id": "id",
                "version": 1,
                "name": "name",
                "created_on": 1000000,
                "modified_on": 1000000,
                "base_voice": "ITO",
                "parameter_model": "20241004-11parameter",
                "parameters": {},
            }
        ],
    }
    expected_types: typing.Any = {
        "page_number": "integer",
        "page_size": "integer",
        "total_pages": "integer",
        "custom_voices_page": (
            "list",
            {
                0: {
                    "id": None,
                    "version": "integer",
                    "name": None,
                    "created_on": None,
                    "modified_on": None,
                    "base_voice": None,
                    "parameter_model": None,
                    "parameters": {},
                }
            },
        ),
    }
    response = client.empathic_voice.custom_voices.list_custom_voices()
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.empathic_voice.custom_voices.list_custom_voices()
    validate_response(async_response, expected_response, expected_types)


async def test_create_custom_voice(client: HumeClient, async_client: AsyncHumeClient) -> None:
    expected_response: typing.Any = {
        "id": "id",
        "version": 1,
        "name": "name",
        "created_on": 1000000,
        "modified_on": 1000000,
        "base_voice": "ITO",
        "parameter_model": "20241004-11parameter",
        "parameters": {
            "gender": 1,
            "articulation": 1,
            "assertiveness": 1,
            "buoyancy": 1,
            "confidence": 1,
            "enthusiasm": 1,
            "nasality": 1,
            "relaxedness": 1,
            "smoothness": 1,
            "tepidity": 1,
            "tightness": 1,
        },
    }
    expected_types: typing.Any = {
        "id": None,
        "version": "integer",
        "name": None,
        "created_on": None,
        "modified_on": None,
        "base_voice": None,
        "parameter_model": None,
        "parameters": {
            "gender": "integer",
            "articulation": "integer",
            "assertiveness": "integer",
            "buoyancy": "integer",
            "confidence": "integer",
            "enthusiasm": "integer",
            "nasality": "integer",
            "relaxedness": "integer",
            "smoothness": "integer",
            "tepidity": "integer",
            "tightness": "integer",
        },
    }
    response = client.empathic_voice.custom_voices.create_custom_voice(name="name", base_voice="ITO")
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.empathic_voice.custom_voices.create_custom_voice(name="name", base_voice="ITO")
    validate_response(async_response, expected_response, expected_types)


async def test_get_custom_voice(client: HumeClient, async_client: AsyncHumeClient) -> None:
    expected_response: typing.Any = {
        "id": "id",
        "version": 1,
        "name": "name",
        "created_on": 1000000,
        "modified_on": 1000000,
        "base_voice": "ITO",
        "parameter_model": "20241004-11parameter",
        "parameters": {
            "gender": 1,
            "articulation": 1,
            "assertiveness": 1,
            "buoyancy": 1,
            "confidence": 1,
            "enthusiasm": 1,
            "nasality": 1,
            "relaxedness": 1,
            "smoothness": 1,
            "tepidity": 1,
            "tightness": 1,
        },
    }
    expected_types: typing.Any = {
        "id": None,
        "version": "integer",
        "name": None,
        "created_on": None,
        "modified_on": None,
        "base_voice": None,
        "parameter_model": None,
        "parameters": {
            "gender": "integer",
            "articulation": "integer",
            "assertiveness": "integer",
            "buoyancy": "integer",
            "confidence": "integer",
            "enthusiasm": "integer",
            "nasality": "integer",
            "relaxedness": "integer",
            "smoothness": "integer",
            "tepidity": "integer",
            "tightness": "integer",
        },
    }
    response = client.empathic_voice.custom_voices.get_custom_voice(id="id")
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.empathic_voice.custom_voices.get_custom_voice(id="id")
    validate_response(async_response, expected_response, expected_types)


async def test_create_custom_voice_version(client: HumeClient, async_client: AsyncHumeClient) -> None:
    expected_response: typing.Any = {
        "id": "id",
        "version": 1,
        "name": "name",
        "created_on": 1000000,
        "modified_on": 1000000,
        "base_voice": "ITO",
        "parameter_model": "20241004-11parameter",
        "parameters": {
            "gender": 1,
            "articulation": 1,
            "assertiveness": 1,
            "buoyancy": 1,
            "confidence": 1,
            "enthusiasm": 1,
            "nasality": 1,
            "relaxedness": 1,
            "smoothness": 1,
            "tepidity": 1,
            "tightness": 1,
        },
    }
    expected_types: typing.Any = {
        "id": None,
        "version": "integer",
        "name": None,
        "created_on": None,
        "modified_on": None,
        "base_voice": None,
        "parameter_model": None,
        "parameters": {
            "gender": "integer",
            "articulation": "integer",
            "assertiveness": "integer",
            "buoyancy": "integer",
            "confidence": "integer",
            "enthusiasm": "integer",
            "nasality": "integer",
            "relaxedness": "integer",
            "smoothness": "integer",
            "tepidity": "integer",
            "tightness": "integer",
        },
    }
    response = client.empathic_voice.custom_voices.create_custom_voice_version(id="id", name="name", base_voice="ITO")
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.empathic_voice.custom_voices.create_custom_voice_version(
        id="id", name="name", base_voice="ITO"
    )
    validate_response(async_response, expected_response, expected_types)


async def test_delete_custom_voice(client: HumeClient, async_client: AsyncHumeClient) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert (
        client.empathic_voice.custom_voices.delete_custom_voice(id="id")  # type: ignore[func-returns-value]
        is None
    )

    assert (
        await async_client.empathic_voice.custom_voices.delete_custom_voice(id="id")  # type: ignore[func-returns-value]
        is None
    )
