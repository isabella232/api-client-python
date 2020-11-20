# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 3.9.0
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from launchdarkly_api.models.link import Link  # noqa: F401,E501


class UsageLinks(object):
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
        'parent': 'Link',
        '_self': 'Link',
        'subseries': 'list[Link]'
    }

    attribute_map = {
        'parent': 'parent',
        '_self': 'self',
        'subseries': 'subseries'
    }

    def __init__(self, parent=None, _self=None, subseries=None):  # noqa: E501
        """UsageLinks - a model defined in Swagger"""  # noqa: E501

        self._parent = None
        self.__self = None
        self._subseries = None
        self.discriminator = None

        if parent is not None:
            self.parent = parent
        if _self is not None:
            self._self = _self
        if subseries is not None:
            self.subseries = subseries

    @property
    def parent(self):
        """Gets the parent of this UsageLinks.  # noqa: E501


        :return: The parent of this UsageLinks.  # noqa: E501
        :rtype: Link
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this UsageLinks.


        :param parent: The parent of this UsageLinks.  # noqa: E501
        :type: Link
        """

        self._parent = parent

    @property
    def _self(self):
        """Gets the _self of this UsageLinks.  # noqa: E501


        :return: The _self of this UsageLinks.  # noqa: E501
        :rtype: Link
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this UsageLinks.


        :param _self: The _self of this UsageLinks.  # noqa: E501
        :type: Link
        """

        self.__self = _self

    @property
    def subseries(self):
        """Gets the subseries of this UsageLinks.  # noqa: E501

        The following links that are in the response.  # noqa: E501

        :return: The subseries of this UsageLinks.  # noqa: E501
        :rtype: list[Link]
        """
        return self._subseries

    @subseries.setter
    def subseries(self, subseries):
        """Sets the subseries of this UsageLinks.

        The following links that are in the response.  # noqa: E501

        :param subseries: The subseries of this UsageLinks.  # noqa: E501
        :type: list[Link]
        """

        self._subseries = subseries

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
        if issubclass(UsageLinks, dict):
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
        if not isinstance(other, UsageLinks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
