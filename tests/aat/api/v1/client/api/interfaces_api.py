# coding: utf-8

"""
    OpenPerf API

    REST API interface for OpenPerf  # noqa: E501

    OpenAPI spec version: 1
    Contact: support@spirent.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from client.api_client import ApiClient


class InterfacesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def bulk_create_interfaces(self, create, **kwargs):  # noqa: E501
        """Bulk create network interfaces  # noqa: E501

        Create multiple network interfaces. Requests are processed in an all-or-nothing manner, i.e. a single network interface creation failure causes all network interface creations for this request to fail.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.bulk_create_interfaces(create, async=True)
        >>> result = thread.get()

        :param async bool
        :param BulkCreateInterfacesRequest create: Bulk creation (required)
        :return: BulkCreateInterfacesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.bulk_create_interfaces_with_http_info(create, **kwargs)  # noqa: E501
        else:
            (data) = self.bulk_create_interfaces_with_http_info(create, **kwargs)  # noqa: E501
            return data

    def bulk_create_interfaces_with_http_info(self, create, **kwargs):  # noqa: E501
        """Bulk create network interfaces  # noqa: E501

        Create multiple network interfaces. Requests are processed in an all-or-nothing manner, i.e. a single network interface creation failure causes all network interface creations for this request to fail.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.bulk_create_interfaces_with_http_info(create, async=True)
        >>> result = thread.get()

        :param async bool
        :param BulkCreateInterfacesRequest create: Bulk creation (required)
        :return: BulkCreateInterfacesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['create']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method bulk_create_interfaces" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'create' is set
        if ('create' not in params or
                params['create'] is None):
            raise ValueError("Missing the required parameter `create` when calling `bulk_create_interfaces`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create' in params:
            body_params = params['create']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/interfaces/x/bulk-create', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BulkCreateInterfacesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def bulk_delete_interfaces(self, delete, **kwargs):  # noqa: E501
        """Bulk delete network interfaces  # noqa: E501

        Best-effort delete multiple network interfaces. Non-existent interface ids do not cause errors. Idempotent.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.bulk_delete_interfaces(delete, async=True)
        >>> result = thread.get()

        :param async bool
        :param BulkDeleteInterfacesRequest delete: Bulk delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.bulk_delete_interfaces_with_http_info(delete, **kwargs)  # noqa: E501
        else:
            (data) = self.bulk_delete_interfaces_with_http_info(delete, **kwargs)  # noqa: E501
            return data

    def bulk_delete_interfaces_with_http_info(self, delete, **kwargs):  # noqa: E501
        """Bulk delete network interfaces  # noqa: E501

        Best-effort delete multiple network interfaces. Non-existent interface ids do not cause errors. Idempotent.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.bulk_delete_interfaces_with_http_info(delete, async=True)
        >>> result = thread.get()

        :param async bool
        :param BulkDeleteInterfacesRequest delete: Bulk delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['delete']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method bulk_delete_interfaces" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'delete' is set
        if ('delete' not in params or
                params['delete'] is None):
            raise ValueError("Missing the required parameter `delete` when calling `bulk_delete_interfaces`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'delete' in params:
            body_params = params['delete']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/interfaces/x/bulk-delete', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_interface(self, interface, **kwargs):  # noqa: E501
        """Create a network interface  # noqa: E501

        Create a new network interface.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_interface(interface, async=True)
        >>> result = thread.get()

        :param async bool
        :param Interface interface: New network interface (required)
        :return: Interface
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_interface_with_http_info(interface, **kwargs)  # noqa: E501
        else:
            (data) = self.create_interface_with_http_info(interface, **kwargs)  # noqa: E501
            return data

    def create_interface_with_http_info(self, interface, **kwargs):  # noqa: E501
        """Create a network interface  # noqa: E501

        Create a new network interface.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_interface_with_http_info(interface, async=True)
        >>> result = thread.get()

        :param async bool
        :param Interface interface: New network interface (required)
        :return: Interface
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['interface']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_interface" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'interface' is set
        if ('interface' not in params or
                params['interface'] is None):
            raise ValueError("Missing the required parameter `interface` when calling `create_interface`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'interface' in params:
            body_params = params['interface']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/interfaces', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Interface',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_interface(self, id, **kwargs):  # noqa: E501
        """Delete a network interface  # noqa: E501

        Deletes an existing interface. Idempotent.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_interface(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: Unique resource identifier (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_interface_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_interface_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def delete_interface_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete a network interface  # noqa: E501

        Deletes an existing interface. Idempotent.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_interface_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: Unique resource identifier (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_interface" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_interface`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/interfaces/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_interface(self, id, **kwargs):  # noqa: E501
        """Get a network interface  # noqa: E501

        Returns a network interface, by id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_interface(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: Unique resource identifier (required)
        :return: Interface
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_interface_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_interface_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_interface_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get a network interface  # noqa: E501

        Returns a network interface, by id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_interface_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: Unique resource identifier (required)
        :return: Interface
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_interface" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_interface`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/interfaces/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Interface',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_interfaces(self, **kwargs):  # noqa: E501
        """List network interfaces  # noqa: E501

        The `interfaces` endpoint returns all network interfaces that are available for use as stack entry/exit points.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_interfaces(async=True)
        >>> result = thread.get()

        :param async bool
        :param str port_id: Filter by port id
        :param str eth_mac_address: Filter by Ethernet MAC address
        :param str ipv4_address: Filter by IPv4 address
        :return: list[Interface]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_interfaces_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_interfaces_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_interfaces_with_http_info(self, **kwargs):  # noqa: E501
        """List network interfaces  # noqa: E501

        The `interfaces` endpoint returns all network interfaces that are available for use as stack entry/exit points.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_interfaces_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str port_id: Filter by port id
        :param str eth_mac_address: Filter by Ethernet MAC address
        :param str ipv4_address: Filter by IPv4 address
        :return: list[Interface]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['port_id', 'eth_mac_address', 'ipv4_address']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_interfaces" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'port_id' in params:
            query_params.append(('port_id', params['port_id']))  # noqa: E501
        if 'eth_mac_address' in params:
            query_params.append(('eth_mac_address', params['eth_mac_address']))  # noqa: E501
        if 'ipv4_address' in params:
            query_params.append(('ipv4_address', params['ipv4_address']))  # noqa: E501

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/interfaces', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Interface]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
