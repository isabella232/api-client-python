# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 2.0.19
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class WebhookBody(object):
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
        'url': 'str',
        'secret': 'str',
        'sign': 'bool',
        'on': 'bool',
        'name': 'str'
    }

    attribute_map = {
        'url': 'url',
        'secret': 'secret',
        'sign': 'sign',
        'on': 'on',
        'name': 'name'
    }

    def __init__(self, url=None, secret=None, sign=None, on=None, name=None):  # noqa: E501
        """WebhookBody - a model defined in Swagger"""  # noqa: E501

        self._url = None
        self._secret = None
        self._sign = None
        self._on = None
        self._name = None
        self.discriminator = None

        self.url = url
        if secret is not None:
            self.secret = secret
        self.sign = sign
        self.on = on
        if name is not None:
            self.name = name

    @property
    def url(self):
        """Gets the url of this WebhookBody.  # noqa: E501

        The URL of the remote webhook.  # noqa: E501

        :return: The url of this WebhookBody.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this WebhookBody.

        The URL of the remote webhook.  # noqa: E501

        :param url: The url of this WebhookBody.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def secret(self):
        """Gets the secret of this WebhookBody.  # noqa: E501

        If sign is true, and the secret attribute is omitted, LaunchDarkly will automatically generate a secret for you.  # noqa: E501

        :return: The secret of this WebhookBody.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this WebhookBody.

        If sign is true, and the secret attribute is omitted, LaunchDarkly will automatically generate a secret for you.  # noqa: E501

        :param secret: The secret of this WebhookBody.  # noqa: E501
        :type: str
        """

        self._secret = secret

    @property
    def sign(self):
        """Gets the sign of this WebhookBody.  # noqa: E501

        If sign is false, the webhook will not include a signature header, and the secret can be omitted.  # noqa: E501

        :return: The sign of this WebhookBody.  # noqa: E501
        :rtype: bool
        """
        return self._sign

    @sign.setter
    def sign(self, sign):
        """Sets the sign of this WebhookBody.

        If sign is false, the webhook will not include a signature header, and the secret can be omitted.  # noqa: E501

        :param sign: The sign of this WebhookBody.  # noqa: E501
        :type: bool
        """
        if sign is None:
            raise ValueError("Invalid value for `sign`, must not be `None`")  # noqa: E501

        self._sign = sign

    @property
    def on(self):
        """Gets the on of this WebhookBody.  # noqa: E501

        Whether this webhook is enabled or not.  # noqa: E501

        :return: The on of this WebhookBody.  # noqa: E501
        :rtype: bool
        """
        return self._on

    @on.setter
    def on(self, on):
        """Sets the on of this WebhookBody.

        Whether this webhook is enabled or not.  # noqa: E501

        :param on: The on of this WebhookBody.  # noqa: E501
        :type: bool
        """
        if on is None:
            raise ValueError("Invalid value for `on`, must not be `None`")  # noqa: E501

        self._on = on

    @property
    def name(self):
        """Gets the name of this WebhookBody.  # noqa: E501

        The name of the webhook.  # noqa: E501

        :return: The name of this WebhookBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WebhookBody.

        The name of the webhook.  # noqa: E501

        :param name: The name of this WebhookBody.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(WebhookBody, dict):
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
        if not isinstance(other, WebhookBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
