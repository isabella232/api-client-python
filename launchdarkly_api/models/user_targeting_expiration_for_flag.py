# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 3.2.0
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from launchdarkly_api.models.links import Links  # noqa: F401,E501
from launchdarkly_api.models.user_targeting_expiration_resource_id_for_flag import UserTargetingExpirationResourceIdForFlag  # noqa: F401,E501


class UserTargetingExpirationForFlag(object):
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
        'expiration_date': 'int',
        'variation_id': 'str',
        'user_key': 'str',
        'id': 'str',
        'resource_id': 'UserTargetingExpirationResourceIdForFlag',
        'links': 'Links',
        'version': 'int'
    }

    attribute_map = {
        'expiration_date': 'expirationDate',
        'variation_id': 'variationId',
        'user_key': 'userKey',
        'id': '_id',
        'resource_id': '_resourceId',
        'links': '_links',
        'version': '_version'
    }

    def __init__(self, expiration_date=None, variation_id=None, user_key=None, id=None, resource_id=None, links=None, version=None):  # noqa: E501
        """UserTargetingExpirationForFlag - a model defined in Swagger"""  # noqa: E501

        self._expiration_date = None
        self._variation_id = None
        self._user_key = None
        self._id = None
        self._resource_id = None
        self._links = None
        self._version = None
        self.discriminator = None

        if expiration_date is not None:
            self.expiration_date = expiration_date
        if variation_id is not None:
            self.variation_id = variation_id
        if user_key is not None:
            self.user_key = user_key
        if id is not None:
            self.id = id
        if resource_id is not None:
            self.resource_id = resource_id
        if links is not None:
            self.links = links
        if version is not None:
            self.version = version

    @property
    def expiration_date(self):
        """Gets the expiration_date of this UserTargetingExpirationForFlag.  # noqa: E501

        Date scheduled for expiration  # noqa: E501

        :return: The expiration_date of this UserTargetingExpirationForFlag.  # noqa: E501
        :rtype: int
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """Sets the expiration_date of this UserTargetingExpirationForFlag.

        Date scheduled for expiration  # noqa: E501

        :param expiration_date: The expiration_date of this UserTargetingExpirationForFlag.  # noqa: E501
        :type: int
        """

        self._expiration_date = expiration_date

    @property
    def variation_id(self):
        """Gets the variation_id of this UserTargetingExpirationForFlag.  # noqa: E501

        the ID of the variation that the user is targeted on a flag  # noqa: E501

        :return: The variation_id of this UserTargetingExpirationForFlag.  # noqa: E501
        :rtype: str
        """
        return self._variation_id

    @variation_id.setter
    def variation_id(self, variation_id):
        """Sets the variation_id of this UserTargetingExpirationForFlag.

        the ID of the variation that the user is targeted on a flag  # noqa: E501

        :param variation_id: The variation_id of this UserTargetingExpirationForFlag.  # noqa: E501
        :type: str
        """

        self._variation_id = variation_id

    @property
    def user_key(self):
        """Gets the user_key of this UserTargetingExpirationForFlag.  # noqa: E501

        Unique identifier for the user  # noqa: E501

        :return: The user_key of this UserTargetingExpirationForFlag.  # noqa: E501
        :rtype: str
        """
        return self._user_key

    @user_key.setter
    def user_key(self, user_key):
        """Sets the user_key of this UserTargetingExpirationForFlag.

        Unique identifier for the user  # noqa: E501

        :param user_key: The user_key of this UserTargetingExpirationForFlag.  # noqa: E501
        :type: str
        """

        self._user_key = user_key

    @property
    def id(self):
        """Gets the id of this UserTargetingExpirationForFlag.  # noqa: E501


        :return: The id of this UserTargetingExpirationForFlag.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserTargetingExpirationForFlag.


        :param id: The id of this UserTargetingExpirationForFlag.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def resource_id(self):
        """Gets the resource_id of this UserTargetingExpirationForFlag.  # noqa: E501


        :return: The resource_id of this UserTargetingExpirationForFlag.  # noqa: E501
        :rtype: UserTargetingExpirationResourceIdForFlag
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this UserTargetingExpirationForFlag.


        :param resource_id: The resource_id of this UserTargetingExpirationForFlag.  # noqa: E501
        :type: UserTargetingExpirationResourceIdForFlag
        """

        self._resource_id = resource_id

    @property
    def links(self):
        """Gets the links of this UserTargetingExpirationForFlag.  # noqa: E501


        :return: The links of this UserTargetingExpirationForFlag.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this UserTargetingExpirationForFlag.


        :param links: The links of this UserTargetingExpirationForFlag.  # noqa: E501
        :type: Links
        """

        self._links = links

    @property
    def version(self):
        """Gets the version of this UserTargetingExpirationForFlag.  # noqa: E501


        :return: The version of this UserTargetingExpirationForFlag.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this UserTargetingExpirationForFlag.


        :param version: The version of this UserTargetingExpirationForFlag.  # noqa: E501
        :type: int
        """

        self._version = version

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
        if issubclass(UserTargetingExpirationForFlag, dict):
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
        if not isinstance(other, UserTargetingExpirationForFlag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
