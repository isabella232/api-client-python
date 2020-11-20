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


class FeatureFlagCopyObject(object):
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
        'key': 'str',
        'current_version': 'int'
    }

    attribute_map = {
        'key': 'key',
        'current_version': 'currentVersion'
    }

    def __init__(self, key=None, current_version=None):  # noqa: E501
        """FeatureFlagCopyObject - a model defined in Swagger"""  # noqa: E501

        self._key = None
        self._current_version = None
        self.discriminator = None

        self.key = key
        if current_version is not None:
            self.current_version = current_version

    @property
    def key(self):
        """Gets the key of this FeatureFlagCopyObject.  # noqa: E501

        The environment key to be used.  # noqa: E501

        :return: The key of this FeatureFlagCopyObject.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this FeatureFlagCopyObject.

        The environment key to be used.  # noqa: E501

        :param key: The key of this FeatureFlagCopyObject.  # noqa: E501
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def current_version(self):
        """Gets the current_version of this FeatureFlagCopyObject.  # noqa: E501

        If the latest version of the flag matches provided version it will copy, otherwise it will return a conflict.  # noqa: E501

        :return: The current_version of this FeatureFlagCopyObject.  # noqa: E501
        :rtype: int
        """
        return self._current_version

    @current_version.setter
    def current_version(self, current_version):
        """Sets the current_version of this FeatureFlagCopyObject.

        If the latest version of the flag matches provided version it will copy, otherwise it will return a conflict.  # noqa: E501

        :param current_version: The current_version of this FeatureFlagCopyObject.  # noqa: E501
        :type: int
        """

        self._current_version = current_version

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
        if issubclass(FeatureFlagCopyObject, dict):
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
        if not isinstance(other, FeatureFlagCopyObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
