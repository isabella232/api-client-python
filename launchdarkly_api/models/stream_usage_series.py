# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 2.0.33
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class StreamUsageSeries(object):
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
        '_0': 'float',
        'time': 'float'
    }

    attribute_map = {
        '_0': '0',
        'time': 'time'
    }

    def __init__(self, _0=None, time=None):  # noqa: E501
        """StreamUsageSeries - a model defined in Swagger"""  # noqa: E501

        self.__0 = None
        self._time = None
        self.discriminator = None

        if _0 is not None:
            self._0 = _0
        if time is not None:
            self.time = time

    @property
    def _0(self):
        """Gets the _0 of this StreamUsageSeries.  # noqa: E501

        A key corresponding to a time series data point.  # noqa: E501

        :return: The _0 of this StreamUsageSeries.  # noqa: E501
        :rtype: float
        """
        return self.__0

    @_0.setter
    def _0(self, _0):
        """Sets the _0 of this StreamUsageSeries.

        A key corresponding to a time series data point.  # noqa: E501

        :param _0: The _0 of this StreamUsageSeries.  # noqa: E501
        :type: float
        """

        self.__0 = _0

    @property
    def time(self):
        """Gets the time of this StreamUsageSeries.  # noqa: E501

        A unix epoch time in milliseconds specifying the creation time of this flag.  # noqa: E501

        :return: The time of this StreamUsageSeries.  # noqa: E501
        :rtype: float
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this StreamUsageSeries.

        A unix epoch time in milliseconds specifying the creation time of this flag.  # noqa: E501

        :param time: The time of this StreamUsageSeries.  # noqa: E501
        :type: float
        """

        self._time = time

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
        if issubclass(StreamUsageSeries, dict):
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
        if not isinstance(other, StreamUsageSeries):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
