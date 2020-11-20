# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 3.9.0
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import launchdarkly_api
from launchdarkly_api.api.integrations_api import IntegrationsApi  # noqa: E501
from launchdarkly_api.rest import ApiException


class TestIntegrationsApi(unittest.TestCase):
    """IntegrationsApi unit test stubs"""

    def setUp(self):
        self.api = launchdarkly_api.api.integrations_api.IntegrationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_integration_subscription(self):
        """Test case for delete_integration_subscription

        Delete an integration subscription by ID.  # noqa: E501
        """
        pass

    def test_get_integration_subscription(self):
        """Test case for get_integration_subscription

        Get a single integration subscription by ID.  # noqa: E501
        """
        pass

    def test_get_integration_subscriptions(self):
        """Test case for get_integration_subscriptions

        Get a list of all configured integrations of a given kind.  # noqa: E501
        """
        pass

    def test_get_integrations(self):
        """Test case for get_integrations

        Get a list of all configured audit log event integrations associated with this account.  # noqa: E501
        """
        pass

    def test_patch_integration_subscription(self):
        """Test case for patch_integration_subscription

        Modify an integration subscription by ID.  # noqa: E501
        """
        pass

    def test_post_integration_subscription(self):
        """Test case for post_integration_subscription

        Create a new integration subscription of a given kind.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
