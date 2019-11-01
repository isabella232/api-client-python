# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 2.0.20
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from launchdarkly_api.api_client import ApiClient


class UsageApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_evaluations(self, env_id, flag_key, **kwargs):  # noqa: E501
        """[BETA] Get events usage by event id and the feature flag key.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_evaluations(env_id, flag_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str env_id: The environment id for the flag evaluations in question. (required)
        :param str flag_key: The key of the flag we want metrics for. (required)
        :return: StreamSDKVersion
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_evaluations_with_http_info(env_id, flag_key, **kwargs)  # noqa: E501
        else:
            (data) = self.get_evaluations_with_http_info(env_id, flag_key, **kwargs)  # noqa: E501
            return data

    def get_evaluations_with_http_info(self, env_id, flag_key, **kwargs):  # noqa: E501
        """[BETA] Get events usage by event id and the feature flag key.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_evaluations_with_http_info(env_id, flag_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str env_id: The environment id for the flag evaluations in question. (required)
        :param str flag_key: The key of the flag we want metrics for. (required)
        :return: StreamSDKVersion
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['env_id', 'flag_key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_evaluations" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'env_id' is set
        if ('env_id' not in params or
                params['env_id'] is None):
            raise ValueError("Missing the required parameter `env_id` when calling `get_evaluations`")  # noqa: E501
        # verify the required parameter 'flag_key' is set
        if ('flag_key' not in params or
                params['flag_key'] is None):
            raise ValueError("Missing the required parameter `flag_key` when calling `get_evaluations`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'env_id' in params:
            path_params['envId'] = params['env_id']  # noqa: E501
        if 'flag_key' in params:
            path_params['flagKey'] = params['flag_key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/usage/evaluations/{envId}/{flagKey}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StreamSDKVersion',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_event(self, type, **kwargs):  # noqa: E501
        """[BETA] Get events usage by event type.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_event(type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str type: The type of event we would like to track. (required)
        :return: StreamSDKVersion
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_event_with_http_info(type, **kwargs)  # noqa: E501
        else:
            (data) = self.get_event_with_http_info(type, **kwargs)  # noqa: E501
            return data

    def get_event_with_http_info(self, type, **kwargs):  # noqa: E501
        """[BETA] Get events usage by event type.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_event_with_http_info(type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str type: The type of event we would like to track. (required)
        :return: StreamSDKVersion
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_event" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'type' is set
        if ('type' not in params or
                params['type'] is None):
            raise ValueError("Missing the required parameter `type` when calling `get_event`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'type' in params:
            path_params['type'] = params['type']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/usage/events/{type}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StreamSDKVersion',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_events(self, **kwargs):  # noqa: E501
        """[BETA] Get events usage endpoints.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_events(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Events
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_events_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_events_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_events_with_http_info(self, **kwargs):  # noqa: E501
        """[BETA] Get events usage endpoints.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_events_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Events
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_events" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/usage/events', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Events',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_mau(self, **kwargs):  # noqa: E501
        """[BETA] Get monthly active user data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_mau(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: MAU
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_mau_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_mau_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_mau_with_http_info(self, **kwargs):  # noqa: E501
        """[BETA] Get monthly active user data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_mau_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: MAU
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_mau" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/usage/mau', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MAU',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_mau_by_category(self, **kwargs):  # noqa: E501
        """[BETA] Get monthly active user data by category.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_mau_by_category(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: MAUbyCategory
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_mau_by_category_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_mau_by_category_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_mau_by_category_with_http_info(self, **kwargs):  # noqa: E501
        """[BETA] Get monthly active user data by category.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_mau_by_category_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: MAUbyCategory
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_mau_by_category" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/usage/mau/bycategory', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MAUbyCategory',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_stream(self, source, **kwargs):  # noqa: E501
        """[BETA] Get a stream endpoint and return timeseries data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_stream(source, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str source: The source of where the stream comes from. (required)
        :return: Stream
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_stream_with_http_info(source, **kwargs)  # noqa: E501
        else:
            (data) = self.get_stream_with_http_info(source, **kwargs)  # noqa: E501
            return data

    def get_stream_with_http_info(self, source, **kwargs):  # noqa: E501
        """[BETA] Get a stream endpoint and return timeseries data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_stream_with_http_info(source, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str source: The source of where the stream comes from. (required)
        :return: Stream
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['source']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_stream" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'source' is set
        if ('source' not in params or
                params['source'] is None):
            raise ValueError("Missing the required parameter `source` when calling `get_stream`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'source' in params:
            path_params['source'] = params['source']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/usage/streams/{source}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Stream',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_stream_by_sdk(self, source, **kwargs):  # noqa: E501
        """[BETA] Get a stream timeseries data by source show sdk version metadata.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_stream_by_sdk(source, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str source: The source of where the stream comes from. (required)
        :return: StreamBySDK
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_stream_by_sdk_with_http_info(source, **kwargs)  # noqa: E501
        else:
            (data) = self.get_stream_by_sdk_with_http_info(source, **kwargs)  # noqa: E501
            return data

    def get_stream_by_sdk_with_http_info(self, source, **kwargs):  # noqa: E501
        """[BETA] Get a stream timeseries data by source show sdk version metadata.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_stream_by_sdk_with_http_info(source, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str source: The source of where the stream comes from. (required)
        :return: StreamBySDK
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['source']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_stream_by_sdk" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'source' is set
        if ('source' not in params or
                params['source'] is None):
            raise ValueError("Missing the required parameter `source` when calling `get_stream_by_sdk`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'source' in params:
            path_params['source'] = params['source']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/usage/streams/{source}/bysdkversion', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StreamBySDK',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_stream_sdk_version(self, source, **kwargs):  # noqa: E501
        """[BETA] Get a stream timeseries data by source and show all sdk version associated.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_stream_sdk_version(source, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str source: The source of where the stream comes from. (required)
        :return: StreamSDKVersion
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_stream_sdk_version_with_http_info(source, **kwargs)  # noqa: E501
        else:
            (data) = self.get_stream_sdk_version_with_http_info(source, **kwargs)  # noqa: E501
            return data

    def get_stream_sdk_version_with_http_info(self, source, **kwargs):  # noqa: E501
        """[BETA] Get a stream timeseries data by source and show all sdk version associated.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_stream_sdk_version_with_http_info(source, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str source: The source of where the stream comes from. (required)
        :return: StreamSDKVersion
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['source']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_stream_sdk_version" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'source' is set
        if ('source' not in params or
                params['source'] is None):
            raise ValueError("Missing the required parameter `source` when calling `get_stream_sdk_version`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'source' in params:
            path_params['source'] = params['source']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/usage/streams/{source}/sdkversions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StreamSDKVersion',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_streams(self, **kwargs):  # noqa: E501
        """[BETA] Returns a list of all streams.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_streams(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Streams
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_streams_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_streams_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_streams_with_http_info(self, **kwargs):  # noqa: E501
        """[BETA] Returns a list of all streams.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_streams_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Streams
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_streams" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/usage/streams', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Streams',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_usage(self, **kwargs):  # noqa: E501
        """[BETA] Returns of the usage endpoints available.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_usage(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Usage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_usage_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_usage_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_usage_with_http_info(self, **kwargs):  # noqa: E501
        """[BETA] Returns of the usage endpoints available.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_usage_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Usage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_usage" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/usage', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Usage',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
