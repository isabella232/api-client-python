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

from launchdarkly_api.models.id import Id  # noqa: F401,E501
from launchdarkly_api.models.links import Links  # noqa: F401,E501


class Environment(object):
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
        'id': 'Id',
        'key': 'str',
        'name': 'str',
        'api_key': 'str',
        'mobile_key': 'str',
        'color': 'str',
        'default_ttl': 'float',
        'secure_mode': 'bool',
        'default_track_events': 'bool',
        'tags': 'list[str]',
        'require_comments': 'bool',
        'confirm_changes': 'bool'
    }

    attribute_map = {
        'links': '_links',
        'id': '_id',
        'key': 'key',
        'name': 'name',
        'api_key': 'apiKey',
        'mobile_key': 'mobileKey',
        'color': 'color',
        'default_ttl': 'defaultTtl',
        'secure_mode': 'secureMode',
        'default_track_events': 'defaultTrackEvents',
        'tags': 'tags',
        'require_comments': 'requireComments',
        'confirm_changes': 'confirmChanges'
    }

    def __init__(self, links=None, id=None, key=None, name=None, api_key=None, mobile_key=None, color=None, default_ttl=None, secure_mode=None, default_track_events=None, tags=None, require_comments=None, confirm_changes=None):  # noqa: E501
        """Environment - a model defined in Swagger"""  # noqa: E501

        self._links = None
        self._id = None
        self._key = None
        self._name = None
        self._api_key = None
        self._mobile_key = None
        self._color = None
        self._default_ttl = None
        self._secure_mode = None
        self._default_track_events = None
        self._tags = None
        self._require_comments = None
        self._confirm_changes = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if id is not None:
            self.id = id
        if key is not None:
            self.key = key
        if name is not None:
            self.name = name
        if api_key is not None:
            self.api_key = api_key
        if mobile_key is not None:
            self.mobile_key = mobile_key
        if color is not None:
            self.color = color
        if default_ttl is not None:
            self.default_ttl = default_ttl
        if secure_mode is not None:
            self.secure_mode = secure_mode
        if default_track_events is not None:
            self.default_track_events = default_track_events
        if tags is not None:
            self.tags = tags
        if require_comments is not None:
            self.require_comments = require_comments
        if confirm_changes is not None:
            self.confirm_changes = confirm_changes

    @property
    def links(self):
        """Gets the links of this Environment.  # noqa: E501


        :return: The links of this Environment.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Environment.


        :param links: The links of this Environment.  # noqa: E501
        :type: Links
        """

        self._links = links

    @property
    def id(self):
        """Gets the id of this Environment.  # noqa: E501


        :return: The id of this Environment.  # noqa: E501
        :rtype: Id
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Environment.


        :param id: The id of this Environment.  # noqa: E501
        :type: Id
        """

        self._id = id

    @property
    def key(self):
        """Gets the key of this Environment.  # noqa: E501

        The key for the environment.  # noqa: E501

        :return: The key of this Environment.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this Environment.

        The key for the environment.  # noqa: E501

        :param key: The key of this Environment.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def name(self):
        """Gets the name of this Environment.  # noqa: E501

        The name of the environment.  # noqa: E501

        :return: The name of this Environment.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Environment.

        The name of the environment.  # noqa: E501

        :param name: The name of this Environment.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def api_key(self):
        """Gets the api_key of this Environment.  # noqa: E501

        The SDK key for backend LaunchDarkly SDKs.  # noqa: E501

        :return: The api_key of this Environment.  # noqa: E501
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this Environment.

        The SDK key for backend LaunchDarkly SDKs.  # noqa: E501

        :param api_key: The api_key of this Environment.  # noqa: E501
        :type: str
        """

        self._api_key = api_key

    @property
    def mobile_key(self):
        """Gets the mobile_key of this Environment.  # noqa: E501

        The SDK key for mobile LaunchDarkly SDKs.  # noqa: E501

        :return: The mobile_key of this Environment.  # noqa: E501
        :rtype: str
        """
        return self._mobile_key

    @mobile_key.setter
    def mobile_key(self, mobile_key):
        """Sets the mobile_key of this Environment.

        The SDK key for mobile LaunchDarkly SDKs.  # noqa: E501

        :param mobile_key: The mobile_key of this Environment.  # noqa: E501
        :type: str
        """

        self._mobile_key = mobile_key

    @property
    def color(self):
        """Gets the color of this Environment.  # noqa: E501

        The swatch color for the environment.  # noqa: E501

        :return: The color of this Environment.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this Environment.

        The swatch color for the environment.  # noqa: E501

        :param color: The color of this Environment.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def default_ttl(self):
        """Gets the default_ttl of this Environment.  # noqa: E501

        The default TTL.  # noqa: E501

        :return: The default_ttl of this Environment.  # noqa: E501
        :rtype: float
        """
        return self._default_ttl

    @default_ttl.setter
    def default_ttl(self, default_ttl):
        """Sets the default_ttl of this Environment.

        The default TTL.  # noqa: E501

        :param default_ttl: The default_ttl of this Environment.  # noqa: E501
        :type: float
        """

        self._default_ttl = default_ttl

    @property
    def secure_mode(self):
        """Gets the secure_mode of this Environment.  # noqa: E501

        Determines if this environment is in safe mode.  # noqa: E501

        :return: The secure_mode of this Environment.  # noqa: E501
        :rtype: bool
        """
        return self._secure_mode

    @secure_mode.setter
    def secure_mode(self, secure_mode):
        """Sets the secure_mode of this Environment.

        Determines if this environment is in safe mode.  # noqa: E501

        :param secure_mode: The secure_mode of this Environment.  # noqa: E501
        :type: bool
        """

        self._secure_mode = secure_mode

    @property
    def default_track_events(self):
        """Gets the default_track_events of this Environment.  # noqa: E501

        Set to true to send detailed event information for new flags.  # noqa: E501

        :return: The default_track_events of this Environment.  # noqa: E501
        :rtype: bool
        """
        return self._default_track_events

    @default_track_events.setter
    def default_track_events(self, default_track_events):
        """Sets the default_track_events of this Environment.

        Set to true to send detailed event information for new flags.  # noqa: E501

        :param default_track_events: The default_track_events of this Environment.  # noqa: E501
        :type: bool
        """

        self._default_track_events = default_track_events

    @property
    def tags(self):
        """Gets the tags of this Environment.  # noqa: E501

        An array of tags for this environment.  # noqa: E501

        :return: The tags of this Environment.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Environment.

        An array of tags for this environment.  # noqa: E501

        :param tags: The tags of this Environment.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def require_comments(self):
        """Gets the require_comments of this Environment.  # noqa: E501

        Determines if this environment requires comments for flag and segment changes.  # noqa: E501

        :return: The require_comments of this Environment.  # noqa: E501
        :rtype: bool
        """
        return self._require_comments

    @require_comments.setter
    def require_comments(self, require_comments):
        """Sets the require_comments of this Environment.

        Determines if this environment requires comments for flag and segment changes.  # noqa: E501

        :param require_comments: The require_comments of this Environment.  # noqa: E501
        :type: bool
        """

        self._require_comments = require_comments

    @property
    def confirm_changes(self):
        """Gets the confirm_changes of this Environment.  # noqa: E501

        Determines if this environment requires confirmation for flag and segment changes.  # noqa: E501

        :return: The confirm_changes of this Environment.  # noqa: E501
        :rtype: bool
        """
        return self._confirm_changes

    @confirm_changes.setter
    def confirm_changes(self, confirm_changes):
        """Sets the confirm_changes of this Environment.

        Determines if this environment requires confirmation for flag and segment changes.  # noqa: E501

        :param confirm_changes: The confirm_changes of this Environment.  # noqa: E501
        :type: bool
        """

        self._confirm_changes = confirm_changes

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
        if issubclass(Environment, dict):
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
        if not isinstance(other, Environment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
