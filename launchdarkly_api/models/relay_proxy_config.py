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

from launchdarkly_api.models.id import Id  # noqa: F401,E501
from launchdarkly_api.models.member import Member  # noqa: F401,E501
from launchdarkly_api.models.policy import Policy  # noqa: F401,E501


class RelayProxyConfig(object):
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
        'id': 'Id',
        'creator': 'Member',
        'name': 'str',
        'policy': 'list[Policy]',
        'full_key': 'str',
        'display_key': 'str',
        'creation_date': 'int',
        'last_modified': 'int'
    }

    attribute_map = {
        'id': '_id',
        'creator': '_creator',
        'name': 'name',
        'policy': 'policy',
        'full_key': 'fullKey',
        'display_key': 'displayKey',
        'creation_date': 'creationDate',
        'last_modified': 'lastModified'
    }

    def __init__(self, id=None, creator=None, name=None, policy=None, full_key=None, display_key=None, creation_date=None, last_modified=None):  # noqa: E501
        """RelayProxyConfig - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._creator = None
        self._name = None
        self._policy = None
        self._full_key = None
        self._display_key = None
        self._creation_date = None
        self._last_modified = None
        self.discriminator = None

        self.id = id
        self.creator = creator
        self.name = name
        self.policy = policy
        if full_key is not None:
            self.full_key = full_key
        self.display_key = display_key
        self.creation_date = creation_date
        self.last_modified = last_modified

    @property
    def id(self):
        """Gets the id of this RelayProxyConfig.  # noqa: E501


        :return: The id of this RelayProxyConfig.  # noqa: E501
        :rtype: Id
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RelayProxyConfig.


        :param id: The id of this RelayProxyConfig.  # noqa: E501
        :type: Id
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def creator(self):
        """Gets the creator of this RelayProxyConfig.  # noqa: E501


        :return: The creator of this RelayProxyConfig.  # noqa: E501
        :rtype: Member
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this RelayProxyConfig.


        :param creator: The creator of this RelayProxyConfig.  # noqa: E501
        :type: Member
        """
        if creator is None:
            raise ValueError("Invalid value for `creator`, must not be `None`")  # noqa: E501

        self._creator = creator

    @property
    def name(self):
        """Gets the name of this RelayProxyConfig.  # noqa: E501

        A human-friendly name for the relay proxy configuration  # noqa: E501

        :return: The name of this RelayProxyConfig.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RelayProxyConfig.

        A human-friendly name for the relay proxy configuration  # noqa: E501

        :param name: The name of this RelayProxyConfig.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def policy(self):
        """Gets the policy of this RelayProxyConfig.  # noqa: E501


        :return: The policy of this RelayProxyConfig.  # noqa: E501
        :rtype: list[Policy]
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this RelayProxyConfig.


        :param policy: The policy of this RelayProxyConfig.  # noqa: E501
        :type: list[Policy]
        """
        if policy is None:
            raise ValueError("Invalid value for `policy`, must not be `None`")  # noqa: E501

        self._policy = policy

    @property
    def full_key(self):
        """Gets the full_key of this RelayProxyConfig.  # noqa: E501

        Full secret key. Only included if creating or resetting the relay proxy configuration  # noqa: E501

        :return: The full_key of this RelayProxyConfig.  # noqa: E501
        :rtype: str
        """
        return self._full_key

    @full_key.setter
    def full_key(self, full_key):
        """Sets the full_key of this RelayProxyConfig.

        Full secret key. Only included if creating or resetting the relay proxy configuration  # noqa: E501

        :param full_key: The full_key of this RelayProxyConfig.  # noqa: E501
        :type: str
        """

        self._full_key = full_key

    @property
    def display_key(self):
        """Gets the display_key of this RelayProxyConfig.  # noqa: E501

        The last 4 digits of the unique secret key for this relay proxy configuration  # noqa: E501

        :return: The display_key of this RelayProxyConfig.  # noqa: E501
        :rtype: str
        """
        return self._display_key

    @display_key.setter
    def display_key(self, display_key):
        """Sets the display_key of this RelayProxyConfig.

        The last 4 digits of the unique secret key for this relay proxy configuration  # noqa: E501

        :param display_key: The display_key of this RelayProxyConfig.  # noqa: E501
        :type: str
        """
        if display_key is None:
            raise ValueError("Invalid value for `display_key`, must not be `None`")  # noqa: E501

        self._display_key = display_key

    @property
    def creation_date(self):
        """Gets the creation_date of this RelayProxyConfig.  # noqa: E501

        A unix epoch time in milliseconds specifying the creation time of this relay proxy configuration  # noqa: E501

        :return: The creation_date of this RelayProxyConfig.  # noqa: E501
        :rtype: int
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this RelayProxyConfig.

        A unix epoch time in milliseconds specifying the creation time of this relay proxy configuration  # noqa: E501

        :param creation_date: The creation_date of this RelayProxyConfig.  # noqa: E501
        :type: int
        """
        if creation_date is None:
            raise ValueError("Invalid value for `creation_date`, must not be `None`")  # noqa: E501

        self._creation_date = creation_date

    @property
    def last_modified(self):
        """Gets the last_modified of this RelayProxyConfig.  # noqa: E501

        A unix epoch time in milliseconds specifying the last time this relay proxy configuration was modified  # noqa: E501

        :return: The last_modified of this RelayProxyConfig.  # noqa: E501
        :rtype: int
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this RelayProxyConfig.

        A unix epoch time in milliseconds specifying the last time this relay proxy configuration was modified  # noqa: E501

        :param last_modified: The last_modified of this RelayProxyConfig.  # noqa: E501
        :type: int
        """
        if last_modified is None:
            raise ValueError("Invalid value for `last_modified`, must not be `None`")  # noqa: E501

        self._last_modified = last_modified

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
        if issubclass(RelayProxyConfig, dict):
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
        if not isinstance(other, RelayProxyConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
