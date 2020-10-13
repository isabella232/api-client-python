# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 3.7.1
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from launchdarkly_api.models.feature_flag_scheduled_change import FeatureFlagScheduledChange  # noqa: F401,E501
from launchdarkly_api.models.links import Links  # noqa: F401,E501


class FeatureFlagScheduledChanges(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'links': 'Links',
        'items': 'list[FeatureFlagScheduledChange]'
    }

    attribute_map = {
        'links': '_links',
        'items': 'items'
    }

    def __init__(self, links=None, items=None):  # noqa: E501
        """FeatureFlagScheduledChanges - a model defined in Swagger"""  # noqa: E501

        self._links = None
        self._items = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if items is not None:
            self.items = items

    @property
    def links(self):
        """Gets the links of this FeatureFlagScheduledChanges.  # noqa: E501


        :return: The links of this FeatureFlagScheduledChanges.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this FeatureFlagScheduledChanges.


        :param links: The links of this FeatureFlagScheduledChanges.  # noqa: E501
        :type: Links
        """

        self._links = links

    @property
    def items(self):
        """Gets the items of this FeatureFlagScheduledChanges.  # noqa: E501


        :return: The items of this FeatureFlagScheduledChanges.  # noqa: E501
        :rtype: list[FeatureFlagScheduledChange]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this FeatureFlagScheduledChanges.


        :param items: The items of this FeatureFlagScheduledChanges.  # noqa: E501
        :type: list[FeatureFlagScheduledChange]
        """

        self._items = items

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(FeatureFlagScheduledChanges, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FeatureFlagScheduledChanges):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
