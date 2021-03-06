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
from launchdarkly_api.api.webhooks_api import WebhooksApi  # noqa: E501
from launchdarkly_api.rest import ApiException


class TestWebhooksApi(unittest.TestCase):
    """WebhooksApi unit test stubs"""

    def setUp(self):
        self.api = launchdarkly_api.api.webhooks_api.WebhooksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_webhook(self):
        """Test case for delete_webhook

        Delete a webhook by ID.  # noqa: E501
        """
        pass

    def test_get_webhook(self):
        """Test case for get_webhook

        Get a webhook by ID.  # noqa: E501
        """
        pass

    def test_get_webhooks(self):
        """Test case for get_webhooks

        Fetch a list of all webhooks.  # noqa: E501
        """
        pass

    def test_patch_webhook(self):
        """Test case for patch_webhook

        Modify a webhook by ID.  # noqa: E501
        """
        pass

    def test_post_webhook(self):
        """Test case for post_webhook

        Create a webhook.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
