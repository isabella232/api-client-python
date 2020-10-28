# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 3.8.0
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import launchdarkly_api
from launchdarkly_api.api.customer_metrics_api import CustomerMetricsApi  # noqa: E501
from launchdarkly_api.rest import ApiException


class TestCustomerMetricsApi(unittest.TestCase):
    """CustomerMetricsApi unit test stubs"""

    def setUp(self):
        self.api = launchdarkly_api.api.customer_metrics_api.CustomerMetricsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_evaluations(self):
        """Test case for get_evaluations

        Get events usage by event id and the feature flag key.  # noqa: E501
        """
        pass

    def test_get_event(self):
        """Test case for get_event

        Get events usage by event type.  # noqa: E501
        """
        pass

    def test_get_events(self):
        """Test case for get_events

        Get events usage endpoints.  # noqa: E501
        """
        pass

    def test_get_mau(self):
        """Test case for get_mau

        Get monthly active user data.  # noqa: E501
        """
        pass

    def test_get_mau_by_category(self):
        """Test case for get_mau_by_category

        Get monthly active user data by category.  # noqa: E501
        """
        pass

    def test_get_stream(self):
        """Test case for get_stream

        Get a stream endpoint and return timeseries data.  # noqa: E501
        """
        pass

    def test_get_stream_by_sdk(self):
        """Test case for get_stream_by_sdk

        Get a stream timeseries data by source show sdk version metadata.  # noqa: E501
        """
        pass

    def test_get_stream_sdk_version(self):
        """Test case for get_stream_sdk_version

        Get a stream timeseries data by source and show all sdk version associated.  # noqa: E501
        """
        pass

    def test_get_streams(self):
        """Test case for get_streams

        Returns a list of all streams.  # noqa: E501
        """
        pass

    def test_get_usage(self):
        """Test case for get_usage

        Returns of the usage endpoints available.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
