# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 3.8.0
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from launchdarkly_api.models.semantic_patch_instruction import SemanticPatchInstruction  # noqa: F401,E501


class FeatureFlagScheduledChange(object):
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
        'execution_date': 'int',
        'version': 'int',
        'id': 'str',
        'instructions': 'SemanticPatchInstruction'
    }

    attribute_map = {
        'execution_date': 'executionDate',
        'version': '_version',
        'id': '_id',
        'instructions': 'instructions'
    }

    def __init__(self, execution_date=None, version=None, id=None, instructions=None):  # noqa: E501
        """FeatureFlagScheduledChange - a model defined in Swagger"""  # noqa: E501

        self._execution_date = None
        self._version = None
        self._id = None
        self._instructions = None
        self.discriminator = None

        if execution_date is not None:
            self.execution_date = execution_date
        if version is not None:
            self.version = version
        if id is not None:
            self.id = id
        if instructions is not None:
            self.instructions = instructions

    @property
    def execution_date(self):
        """Gets the execution_date of this FeatureFlagScheduledChange.  # noqa: E501

        A unix epoch time in milliseconds specifying the date the scheduled changes will be applied  # noqa: E501

        :return: The execution_date of this FeatureFlagScheduledChange.  # noqa: E501
        :rtype: int
        """
        return self._execution_date

    @execution_date.setter
    def execution_date(self, execution_date):
        """Sets the execution_date of this FeatureFlagScheduledChange.

        A unix epoch time in milliseconds specifying the date the scheduled changes will be applied  # noqa: E501

        :param execution_date: The execution_date of this FeatureFlagScheduledChange.  # noqa: E501
        :type: int
        """

        self._execution_date = execution_date

    @property
    def version(self):
        """Gets the version of this FeatureFlagScheduledChange.  # noqa: E501


        :return: The version of this FeatureFlagScheduledChange.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this FeatureFlagScheduledChange.


        :param version: The version of this FeatureFlagScheduledChange.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def id(self):
        """Gets the id of this FeatureFlagScheduledChange.  # noqa: E501


        :return: The id of this FeatureFlagScheduledChange.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FeatureFlagScheduledChange.


        :param id: The id of this FeatureFlagScheduledChange.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def instructions(self):
        """Gets the instructions of this FeatureFlagScheduledChange.  # noqa: E501


        :return: The instructions of this FeatureFlagScheduledChange.  # noqa: E501
        :rtype: SemanticPatchInstruction
        """
        return self._instructions

    @instructions.setter
    def instructions(self, instructions):
        """Sets the instructions of this FeatureFlagScheduledChange.


        :param instructions: The instructions of this FeatureFlagScheduledChange.  # noqa: E501
        :type: SemanticPatchInstruction
        """

        self._instructions = instructions

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
        if issubclass(FeatureFlagScheduledChange, dict):
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
        if not isinstance(other, FeatureFlagScheduledChange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
