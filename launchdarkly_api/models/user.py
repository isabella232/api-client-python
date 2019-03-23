# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 2.0.15
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class User(object):
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
        'secondary': 'str',
        'ip': 'str',
        'country': 'str',
        'email': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'avatar': 'str',
        'name': 'str',
        'anonymous': 'bool',
        'custom': 'object'
    }

    attribute_map = {
        'key': 'key',
        'secondary': 'secondary',
        'ip': 'ip',
        'country': 'country',
        'email': 'email',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'avatar': 'avatar',
        'name': 'name',
        'anonymous': 'anonymous',
        'custom': 'custom'
    }

    def __init__(self, key=None, secondary=None, ip=None, country=None, email=None, first_name=None, last_name=None, avatar=None, name=None, anonymous=None, custom=None):  # noqa: E501
        """User - a model defined in Swagger"""  # noqa: E501

        self._key = None
        self._secondary = None
        self._ip = None
        self._country = None
        self._email = None
        self._first_name = None
        self._last_name = None
        self._avatar = None
        self._name = None
        self._anonymous = None
        self._custom = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if secondary is not None:
            self.secondary = secondary
        if ip is not None:
            self.ip = ip
        if country is not None:
            self.country = country
        if email is not None:
            self.email = email
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if avatar is not None:
            self.avatar = avatar
        if name is not None:
            self.name = name
        if anonymous is not None:
            self.anonymous = anonymous
        if custom is not None:
            self.custom = custom

    @property
    def key(self):
        """Gets the key of this User.  # noqa: E501


        :return: The key of this User.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this User.


        :param key: The key of this User.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def secondary(self):
        """Gets the secondary of this User.  # noqa: E501


        :return: The secondary of this User.  # noqa: E501
        :rtype: str
        """
        return self._secondary

    @secondary.setter
    def secondary(self, secondary):
        """Sets the secondary of this User.


        :param secondary: The secondary of this User.  # noqa: E501
        :type: str
        """

        self._secondary = secondary

    @property
    def ip(self):
        """Gets the ip of this User.  # noqa: E501


        :return: The ip of this User.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this User.


        :param ip: The ip of this User.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def country(self):
        """Gets the country of this User.  # noqa: E501


        :return: The country of this User.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this User.


        :param country: The country of this User.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def email(self):
        """Gets the email of this User.  # noqa: E501


        :return: The email of this User.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this User.


        :param email: The email of this User.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this User.  # noqa: E501


        :return: The first_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this User.


        :param first_name: The first_name of this User.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this User.  # noqa: E501


        :return: The last_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this User.


        :param last_name: The last_name of this User.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def avatar(self):
        """Gets the avatar of this User.  # noqa: E501


        :return: The avatar of this User.  # noqa: E501
        :rtype: str
        """
        return self._avatar

    @avatar.setter
    def avatar(self, avatar):
        """Sets the avatar of this User.


        :param avatar: The avatar of this User.  # noqa: E501
        :type: str
        """

        self._avatar = avatar

    @property
    def name(self):
        """Gets the name of this User.  # noqa: E501


        :return: The name of this User.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this User.


        :param name: The name of this User.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def anonymous(self):
        """Gets the anonymous of this User.  # noqa: E501


        :return: The anonymous of this User.  # noqa: E501
        :rtype: bool
        """
        return self._anonymous

    @anonymous.setter
    def anonymous(self, anonymous):
        """Sets the anonymous of this User.


        :param anonymous: The anonymous of this User.  # noqa: E501
        :type: bool
        """

        self._anonymous = anonymous

    @property
    def custom(self):
        """Gets the custom of this User.  # noqa: E501


        :return: The custom of this User.  # noqa: E501
        :rtype: object
        """
        return self._custom

    @custom.setter
    def custom(self, custom):
        """Sets the custom of this User.


        :param custom: The custom of this User.  # noqa: E501
        :type: object
        """

        self._custom = custom

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
        if issubclass(User, dict):
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
        if not isinstance(other, User):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
