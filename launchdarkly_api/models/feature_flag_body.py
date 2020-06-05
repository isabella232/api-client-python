# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 3.3.2
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from launchdarkly_api.models.defaults import Defaults  # noqa: F401,E501
from launchdarkly_api.models.variation import Variation  # noqa: F401,E501


class FeatureFlagBody(object):
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
        'name': 'str',
        'key': 'str',
        'description': 'str',
        'variations': 'list[Variation]',
        'temporary': 'bool',
        'tags': 'list[str]',
        'include_in_snippet': 'bool',
        'defaults': 'Defaults'
    }

    attribute_map = {
        'name': 'name',
        'key': 'key',
        'description': 'description',
        'variations': 'variations',
        'temporary': 'temporary',
        'tags': 'tags',
        'include_in_snippet': 'includeInSnippet',
        'defaults': 'defaults'
    }

    def __init__(self, name=None, key=None, description=None, variations=None, temporary=None, tags=None, include_in_snippet=None, defaults=None):  # noqa: E501
        """FeatureFlagBody - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._key = None
        self._description = None
        self._variations = None
        self._temporary = None
        self._tags = None
        self._include_in_snippet = None
        self._defaults = None
        self.discriminator = None

        self.name = name
        self.key = key
        if description is not None:
            self.description = description
        self.variations = variations
        if temporary is not None:
            self.temporary = temporary
        if tags is not None:
            self.tags = tags
        if include_in_snippet is not None:
            self.include_in_snippet = include_in_snippet
        if defaults is not None:
            self.defaults = defaults

    @property
    def name(self):
        """Gets the name of this FeatureFlagBody.  # noqa: E501

        A human-friendly name for the feature flag. Remember to note if this flag is intended to be temporary or permanent.  # noqa: E501

        :return: The name of this FeatureFlagBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FeatureFlagBody.

        A human-friendly name for the feature flag. Remember to note if this flag is intended to be temporary or permanent.  # noqa: E501

        :param name: The name of this FeatureFlagBody.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def key(self):
        """Gets the key of this FeatureFlagBody.  # noqa: E501

        A unique key that will be used to reference the flag in your code.  # noqa: E501

        :return: The key of this FeatureFlagBody.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this FeatureFlagBody.

        A unique key that will be used to reference the flag in your code.  # noqa: E501

        :param key: The key of this FeatureFlagBody.  # noqa: E501
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def description(self):
        """Gets the description of this FeatureFlagBody.  # noqa: E501

        A description of the feature flag.  # noqa: E501

        :return: The description of this FeatureFlagBody.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FeatureFlagBody.

        A description of the feature flag.  # noqa: E501

        :param description: The description of this FeatureFlagBody.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def variations(self):
        """Gets the variations of this FeatureFlagBody.  # noqa: E501

        An array of possible variations for the flag.  # noqa: E501

        :return: The variations of this FeatureFlagBody.  # noqa: E501
        :rtype: list[Variation]
        """
        return self._variations

    @variations.setter
    def variations(self, variations):
        """Sets the variations of this FeatureFlagBody.

        An array of possible variations for the flag.  # noqa: E501

        :param variations: The variations of this FeatureFlagBody.  # noqa: E501
        :type: list[Variation]
        """
        if variations is None:
            raise ValueError("Invalid value for `variations`, must not be `None`")  # noqa: E501

        self._variations = variations

    @property
    def temporary(self):
        """Gets the temporary of this FeatureFlagBody.  # noqa: E501

        Whether or not the flag is a temporary flag.  # noqa: E501

        :return: The temporary of this FeatureFlagBody.  # noqa: E501
        :rtype: bool
        """
        return self._temporary

    @temporary.setter
    def temporary(self, temporary):
        """Sets the temporary of this FeatureFlagBody.

        Whether or not the flag is a temporary flag.  # noqa: E501

        :param temporary: The temporary of this FeatureFlagBody.  # noqa: E501
        :type: bool
        """

        self._temporary = temporary

    @property
    def tags(self):
        """Gets the tags of this FeatureFlagBody.  # noqa: E501

        Tags for the feature flag.  # noqa: E501

        :return: The tags of this FeatureFlagBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this FeatureFlagBody.

        Tags for the feature flag.  # noqa: E501

        :param tags: The tags of this FeatureFlagBody.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def include_in_snippet(self):
        """Gets the include_in_snippet of this FeatureFlagBody.  # noqa: E501

        Whether or not this flag should be made available to the client-side JavaScript SDK.  # noqa: E501

        :return: The include_in_snippet of this FeatureFlagBody.  # noqa: E501
        :rtype: bool
        """
        return self._include_in_snippet

    @include_in_snippet.setter
    def include_in_snippet(self, include_in_snippet):
        """Sets the include_in_snippet of this FeatureFlagBody.

        Whether or not this flag should be made available to the client-side JavaScript SDK.  # noqa: E501

        :param include_in_snippet: The include_in_snippet of this FeatureFlagBody.  # noqa: E501
        :type: bool
        """

        self._include_in_snippet = include_in_snippet

    @property
    def defaults(self):
        """Gets the defaults of this FeatureFlagBody.  # noqa: E501


        :return: The defaults of this FeatureFlagBody.  # noqa: E501
        :rtype: Defaults
        """
        return self._defaults

    @defaults.setter
    def defaults(self, defaults):
        """Sets the defaults of this FeatureFlagBody.


        :param defaults: The defaults of this FeatureFlagBody.  # noqa: E501
        :type: Defaults
        """

        self._defaults = defaults

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
        if issubclass(FeatureFlagBody, dict):
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
        if not isinstance(other, FeatureFlagBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
