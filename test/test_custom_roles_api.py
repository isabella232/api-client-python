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
from launchdarkly_api.api.custom_roles_api import CustomRolesApi  # noqa: E501
from launchdarkly_api.rest import ApiException


class TestCustomRolesApi(unittest.TestCase):
    """CustomRolesApi unit test stubs"""

    def setUp(self):
        self.api = launchdarkly_api.api.custom_roles_api.CustomRolesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_custom_role(self):
        """Test case for delete_custom_role

        Delete a custom role by key.  # noqa: E501
        """
        pass

    def test_get_custom_role(self):
        """Test case for get_custom_role

        Get one custom role by key.  # noqa: E501
        """
        pass

    def test_get_custom_roles(self):
        """Test case for get_custom_roles

        Return a complete list of custom roles.  # noqa: E501
        """
        pass

    def test_patch_custom_role(self):
        """Test case for patch_custom_role

        Modify a custom role by key.  # noqa: E501
        """
        pass

    def test_post_custom_role(self):
        """Test case for post_custom_role

        Create a new custom role.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
