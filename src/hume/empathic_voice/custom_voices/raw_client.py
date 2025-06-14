# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.http_response import AsyncHttpResponse, HttpResponse
from ...core.jsonable_encoder import jsonable_encoder
from ...core.pagination import AsyncPager, BaseHttpResponse, SyncPager
from ...core.pydantic_utilities import parse_obj_as
from ...core.request_options import RequestOptions
from ...core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..types.error_response import ErrorResponse
from ..types.posted_custom_voice_base_voice import PostedCustomVoiceBaseVoice
from ..types.posted_custom_voice_parameters import PostedCustomVoiceParameters
from ..types.return_custom_voice import ReturnCustomVoice
from ..types.return_paged_custom_voices import ReturnPagedCustomVoices

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RawCustomVoicesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_custom_voices(
        self,
        *,
        page_number: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[ReturnCustomVoice]:
        """
        Fetches a paginated list of **Custom Voices**.

        Refer to our [voices guide](/docs/empathic-voice-interface-evi/configuration/voices) for details on creating a custom voice.

        Parameters
        ----------
        page_number : typing.Optional[int]
            Specifies the page number to retrieve, enabling pagination.

            This parameter uses zero-based indexing. For example, setting `page_number` to 0 retrieves the first page of results (items 0-9 if `page_size` is 10), setting `page_number` to 1 retrieves the second page (items 10-19), and so on. Defaults to 0, which retrieves the first page.

        page_size : typing.Optional[int]
            Specifies the maximum number of results to include per page, enabling pagination. The value must be between 1 and 100, inclusive.

            For example, if `page_size` is set to 10, each page will include up to 10 items. Defaults to 10.

        name : typing.Optional[str]
            Filter to only include custom voices with name.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[ReturnCustomVoice]
            Success
        """
        page_number = page_number if page_number is not None else 0

        _response = self._client_wrapper.httpx_client.request(
            "v0/evi/custom_voices",
            method="GET",
            params={
                "page_number": page_number,
                "page_size": page_size,
                "name": name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ReturnPagedCustomVoices,
                    parse_obj_as(
                        type_=ReturnPagedCustomVoices,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.custom_voices_page
                _has_next = True
                _get_next = lambda: self.list_custom_voices(
                    page_number=page_number + 1,
                    page_size=page_size,
                    name=name,
                    request_options=request_options,
                )
                return SyncPager(
                    has_next=_has_next, items=_items, get_next=_get_next, response=BaseHttpResponse(response=_response)
                )
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_custom_voice(
        self,
        *,
        name: str,
        base_voice: PostedCustomVoiceBaseVoice,
        parameters: typing.Optional[PostedCustomVoiceParameters] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ReturnCustomVoice]:
        """
        Creates a **Custom Voice** that can be added to an [EVI configuration](/reference/empathic-voice-interface-evi/configs/create-config).

        Refer to our [voices guide](/docs/empathic-voice-interface-evi/configuration/voices) for details on creating a custom voice.

        Parameters
        ----------
        name : str
            The name of the Custom Voice. Maximum length of 75 characters. Will be converted to all-uppercase. (e.g., "sample voice" becomes "SAMPLE VOICE")

        base_voice : PostedCustomVoiceBaseVoice
            Specifies the base voice used to create the Custom Voice.

        parameters : typing.Optional[PostedCustomVoiceParameters]
            The specified attributes of a Custom Voice.

            If no parameters are specified then all attributes will be set to their defaults, meaning no modfications will be made to the base voice.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ReturnCustomVoice]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/evi/custom_voices",
            method="POST",
            json={
                "name": name,
                "base_voice": base_voice,
                "parameters": convert_and_respect_annotation_metadata(
                    object_=parameters, annotation=PostedCustomVoiceParameters, direction="write"
                ),
                "parameter_model": "20241004-11parameter",
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ReturnCustomVoice,
                    parse_obj_as(
                        type_=ReturnCustomVoice,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_custom_voice(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ReturnCustomVoice]:
        """
        Fetches a specific **Custom Voice** by ID.

        Refer to our [voices guide](/docs/empathic-voice-interface-evi/configuration/voices) for details on creating a custom voice.

        Parameters
        ----------
        id : str
            Identifier for a Custom Voice. Formatted as a UUID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ReturnCustomVoice]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/evi/custom_voices/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ReturnCustomVoice,
                    parse_obj_as(
                        type_=ReturnCustomVoice,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_custom_voice_version(
        self,
        id: str,
        *,
        name: str,
        base_voice: PostedCustomVoiceBaseVoice,
        parameters: typing.Optional[PostedCustomVoiceParameters] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ReturnCustomVoice]:
        """
        Updates a **Custom Voice** by creating a new version of the **Custom Voice**.

        Refer to our [voices guide](/docs/empathic-voice-interface-evi/configuration/voices) for details on creating a custom voice.

        Parameters
        ----------
        id : str
            Identifier for a Custom Voice. Formatted as a UUID.

        name : str
            The name of the Custom Voice. Maximum length of 75 characters. Will be converted to all-uppercase. (e.g., "sample voice" becomes "SAMPLE VOICE")

        base_voice : PostedCustomVoiceBaseVoice
            Specifies the base voice used to create the Custom Voice.

        parameters : typing.Optional[PostedCustomVoiceParameters]
            The specified attributes of a Custom Voice.

            If no parameters are specified then all attributes will be set to their defaults, meaning no modfications will be made to the base voice.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ReturnCustomVoice]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/evi/custom_voices/{jsonable_encoder(id)}",
            method="POST",
            json={
                "name": name,
                "base_voice": base_voice,
                "parameters": convert_and_respect_annotation_metadata(
                    object_=parameters, annotation=PostedCustomVoiceParameters, direction="write"
                ),
                "parameter_model": "20241004-11parameter",
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ReturnCustomVoice,
                    parse_obj_as(
                        type_=ReturnCustomVoice,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_custom_voice(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Deletes a **Custom Voice** and its versions.

        Refer to our [voices guide](/docs/empathic-voice-interface-evi/configuration/voices) for details on creating a custom voice.

        Parameters
        ----------
        id : str
            Identifier for a Custom Voice. Formatted as a UUID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/evi/custom_voices/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_custom_voice_name(
        self, id: str, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[str]:
        """
        Updates the name of a **Custom Voice**.

        Refer to our [voices guide](/docs/empathic-voice-interface-evi/configuration/voices) for details on creating a custom voice.

        Parameters
        ----------
        id : str
            Identifier for a Custom Voice. Formatted as a UUID.

        name : str
            The name of the Custom Voice. Maximum length of 75 characters. Will be converted to all-uppercase. (e.g., "sample voice" becomes "SAMPLE VOICE")

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/evi/custom_voices/{jsonable_encoder(id)}",
            method="PATCH",
            json={
                "name": name,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawCustomVoicesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_custom_voices(
        self,
        *,
        page_number: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[ReturnCustomVoice]:
        """
        Fetches a paginated list of **Custom Voices**.

        Refer to our [voices guide](/docs/empathic-voice-interface-evi/configuration/voices) for details on creating a custom voice.

        Parameters
        ----------
        page_number : typing.Optional[int]
            Specifies the page number to retrieve, enabling pagination.

            This parameter uses zero-based indexing. For example, setting `page_number` to 0 retrieves the first page of results (items 0-9 if `page_size` is 10), setting `page_number` to 1 retrieves the second page (items 10-19), and so on. Defaults to 0, which retrieves the first page.

        page_size : typing.Optional[int]
            Specifies the maximum number of results to include per page, enabling pagination. The value must be between 1 and 100, inclusive.

            For example, if `page_size` is set to 10, each page will include up to 10 items. Defaults to 10.

        name : typing.Optional[str]
            Filter to only include custom voices with name.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[ReturnCustomVoice]
            Success
        """
        page_number = page_number if page_number is not None else 0

        _response = await self._client_wrapper.httpx_client.request(
            "v0/evi/custom_voices",
            method="GET",
            params={
                "page_number": page_number,
                "page_size": page_size,
                "name": name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ReturnPagedCustomVoices,
                    parse_obj_as(
                        type_=ReturnPagedCustomVoices,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.custom_voices_page
                _has_next = True

                async def _get_next():
                    return await self.list_custom_voices(
                        page_number=page_number + 1,
                        page_size=page_size,
                        name=name,
                        request_options=request_options,
                    )

                return AsyncPager(
                    has_next=_has_next, items=_items, get_next=_get_next, response=BaseHttpResponse(response=_response)
                )
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_custom_voice(
        self,
        *,
        name: str,
        base_voice: PostedCustomVoiceBaseVoice,
        parameters: typing.Optional[PostedCustomVoiceParameters] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ReturnCustomVoice]:
        """
        Creates a **Custom Voice** that can be added to an [EVI configuration](/reference/empathic-voice-interface-evi/configs/create-config).

        Refer to our [voices guide](/docs/empathic-voice-interface-evi/configuration/voices) for details on creating a custom voice.

        Parameters
        ----------
        name : str
            The name of the Custom Voice. Maximum length of 75 characters. Will be converted to all-uppercase. (e.g., "sample voice" becomes "SAMPLE VOICE")

        base_voice : PostedCustomVoiceBaseVoice
            Specifies the base voice used to create the Custom Voice.

        parameters : typing.Optional[PostedCustomVoiceParameters]
            The specified attributes of a Custom Voice.

            If no parameters are specified then all attributes will be set to their defaults, meaning no modfications will be made to the base voice.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ReturnCustomVoice]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/evi/custom_voices",
            method="POST",
            json={
                "name": name,
                "base_voice": base_voice,
                "parameters": convert_and_respect_annotation_metadata(
                    object_=parameters, annotation=PostedCustomVoiceParameters, direction="write"
                ),
                "parameter_model": "20241004-11parameter",
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ReturnCustomVoice,
                    parse_obj_as(
                        type_=ReturnCustomVoice,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_custom_voice(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ReturnCustomVoice]:
        """
        Fetches a specific **Custom Voice** by ID.

        Refer to our [voices guide](/docs/empathic-voice-interface-evi/configuration/voices) for details on creating a custom voice.

        Parameters
        ----------
        id : str
            Identifier for a Custom Voice. Formatted as a UUID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ReturnCustomVoice]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/evi/custom_voices/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ReturnCustomVoice,
                    parse_obj_as(
                        type_=ReturnCustomVoice,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_custom_voice_version(
        self,
        id: str,
        *,
        name: str,
        base_voice: PostedCustomVoiceBaseVoice,
        parameters: typing.Optional[PostedCustomVoiceParameters] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ReturnCustomVoice]:
        """
        Updates a **Custom Voice** by creating a new version of the **Custom Voice**.

        Refer to our [voices guide](/docs/empathic-voice-interface-evi/configuration/voices) for details on creating a custom voice.

        Parameters
        ----------
        id : str
            Identifier for a Custom Voice. Formatted as a UUID.

        name : str
            The name of the Custom Voice. Maximum length of 75 characters. Will be converted to all-uppercase. (e.g., "sample voice" becomes "SAMPLE VOICE")

        base_voice : PostedCustomVoiceBaseVoice
            Specifies the base voice used to create the Custom Voice.

        parameters : typing.Optional[PostedCustomVoiceParameters]
            The specified attributes of a Custom Voice.

            If no parameters are specified then all attributes will be set to their defaults, meaning no modfications will be made to the base voice.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ReturnCustomVoice]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/evi/custom_voices/{jsonable_encoder(id)}",
            method="POST",
            json={
                "name": name,
                "base_voice": base_voice,
                "parameters": convert_and_respect_annotation_metadata(
                    object_=parameters, annotation=PostedCustomVoiceParameters, direction="write"
                ),
                "parameter_model": "20241004-11parameter",
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ReturnCustomVoice,
                    parse_obj_as(
                        type_=ReturnCustomVoice,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_custom_voice(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Deletes a **Custom Voice** and its versions.

        Refer to our [voices guide](/docs/empathic-voice-interface-evi/configuration/voices) for details on creating a custom voice.

        Parameters
        ----------
        id : str
            Identifier for a Custom Voice. Formatted as a UUID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/evi/custom_voices/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_custom_voice_name(
        self, id: str, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        Updates the name of a **Custom Voice**.

        Refer to our [voices guide](/docs/empathic-voice-interface-evi/configuration/voices) for details on creating a custom voice.

        Parameters
        ----------
        id : str
            Identifier for a Custom Voice. Formatted as a UUID.

        name : str
            The name of the Custom Voice. Maximum length of 75 characters. Will be converted to all-uppercase. (e.g., "sample voice" becomes "SAMPLE VOICE")

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/evi/custom_voices/{jsonable_encoder(id)}",
            method="PATCH",
            json={
                "name": name,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
