# This file was auto-generated by Fern from our API Definition.

from hume import HumeClient
from hume import AsyncHumeClient
import typing
from ..utilities import validate_response


async def test_get_chat_group(client: HumeClient, async_client: AsyncHumeClient) -> None:
    expected_response: typing.Any = {
        "id": "369846cf-6ad5-404d-905e-a8acb5cdfc78",
        "first_start_timestamp": 1712334213647,
        "most_recent_start_timestamp": 1712334213647,
        "num_chats": 1,
        "page_number": 0,
        "page_size": 1,
        "total_pages": 1,
        "pagination_direction": "ASC",
        "chats_page": [
            {
                "id": "6375d4f8-cd3e-4d6b-b13b-ace66b7c8aaa",
                "chat_group_id": "369846cf-6ad5-404d-905e-a8acb5cdfc78",
                "status": "USER_ENDED",
                "start_timestamp": 1712334213647,
                "end_timestamp": 1712334332571,
                "event_count": 0,
                "metadata": None,
                "config": None,
            }
        ],
        "active": False,
    }
    expected_types: typing.Any = {
        "id": None,
        "first_start_timestamp": None,
        "most_recent_start_timestamp": None,
        "num_chats": "integer",
        "page_number": "integer",
        "page_size": "integer",
        "total_pages": "integer",
        "pagination_direction": None,
        "chats_page": (
            "list",
            {
                0: {
                    "id": None,
                    "chat_group_id": None,
                    "status": None,
                    "start_timestamp": None,
                    "end_timestamp": None,
                    "event_count": None,
                    "metadata": None,
                    "config": None,
                }
            },
        ),
        "active": None,
    }
    response = client.empathic_voice.chat_groups.get_chat_group(
        id="697056f0-6c7e-487d-9bd8-9c19df79f05f", page_number=0, page_size=1, ascending_order=True
    )
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.empathic_voice.chat_groups.get_chat_group(
        id="697056f0-6c7e-487d-9bd8-9c19df79f05f", page_number=0, page_size=1, ascending_order=True
    )
    validate_response(async_response, expected_response, expected_types)


async def test_get_audio(client: HumeClient, async_client: AsyncHumeClient) -> None:
    expected_response: typing.Any = {
        "id": "369846cf-6ad5-404d-905e-a8acb5cdfc78",
        "user_id": "e6235940-cfda-3988-9147-ff531627cf42",
        "num_chats": 1,
        "page_number": 0,
        "page_size": 10,
        "total_pages": 1,
        "pagination_direction": "ASC",
        "audio_reconstructions_page": [
            {
                "id": "470a49f6-1dec-4afe-8b61-035d3b2d63b0",
                "user_id": "e6235940-cfda-3988-9147-ff531627cf42",
                "status": "COMPLETE",
                "filename": "e6235940-cfda-3988-9147-ff531627cf42/470a49f6-1dec-4afe-8b61-035d3b2d63b0/reconstructed_audio.mp4",
                "modified_at": 1729875432555,
                "signed_audio_url": "https://storage.googleapis.com/...etc.",
                "signed_url_expiration_timestamp_millis": 1730232816964,
            }
        ],
    }
    expected_types: typing.Any = {
        "id": None,
        "user_id": None,
        "num_chats": "integer",
        "page_number": "integer",
        "page_size": "integer",
        "total_pages": "integer",
        "pagination_direction": None,
        "audio_reconstructions_page": (
            "list",
            {
                0: {
                    "id": None,
                    "user_id": None,
                    "status": None,
                    "filename": None,
                    "modified_at": None,
                    "signed_audio_url": None,
                    "signed_url_expiration_timestamp_millis": None,
                }
            },
        ),
    }
    response = client.empathic_voice.chat_groups.get_audio(
        id="369846cf-6ad5-404d-905e-a8acb5cdfc78", page_number=0, page_size=10, ascending_order=True
    )
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.empathic_voice.chat_groups.get_audio(
        id="369846cf-6ad5-404d-905e-a8acb5cdfc78", page_number=0, page_size=10, ascending_order=True
    )
    validate_response(async_response, expected_response, expected_types)
