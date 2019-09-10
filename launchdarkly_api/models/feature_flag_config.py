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

from launchdarkly_api.models.fallthrough import Fallthrough  # noqa: F401,E501
from launchdarkly_api.models.prerequisite import Prerequisite  # noqa: F401,E501
from launchdarkly_api.models.rule import Rule  # noqa: F401,E501
from launchdarkly_api.models.target import Target  # noqa: F401,E501


class FeatureFlagConfig(object):
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
        'on': 'bool',
        'archived': 'bool',
        'salt': 'str',
        'sel': 'str',
        'last_modified': 'int',
        'version': 'int',
        'targets': 'list[Target]',
        'rules': 'list[Rule]',
        'fallthrough': 'Fallthrough',
        'off_variation': 'int',
        'prerequisites': 'list[Prerequisite]',
        'track_events': 'bool'
    }

    attribute_map = {
        'on': 'on',
        'archived': 'archived',
        'salt': 'salt',
        'sel': 'sel',
        'last_modified': 'lastModified',
        'version': 'version',
        'targets': 'targets',
        'rules': 'rules',
        'fallthrough': 'fallthrough',
        'off_variation': 'offVariation',
        'prerequisites': 'prerequisites',
        'track_events': 'trackEvents'
    }

    def __init__(self, on=None, archived=None, salt=None, sel=None, last_modified=None, version=None, targets=None, rules=None, fallthrough=None, off_variation=None, prerequisites=None, track_events=None):  # noqa: E501
        """FeatureFlagConfig - a model defined in Swagger"""  # noqa: E501

        self._on = None
        self._archived = None
        self._salt = None
        self._sel = None
        self._last_modified = None
        self._version = None
        self._targets = None
        self._rules = None
        self._fallthrough = None
        self._off_variation = None
        self._prerequisites = None
        self._track_events = None
        self.discriminator = None

        if on is not None:
            self.on = on
        if archived is not None:
            self.archived = archived
        if salt is not None:
            self.salt = salt
        if sel is not None:
            self.sel = sel
        if last_modified is not None:
            self.last_modified = last_modified
        if version is not None:
            self.version = version
        if targets is not None:
            self.targets = targets
        if rules is not None:
            self.rules = rules
        if fallthrough is not None:
            self.fallthrough = fallthrough
        if off_variation is not None:
            self.off_variation = off_variation
        if prerequisites is not None:
            self.prerequisites = prerequisites
        if track_events is not None:
            self.track_events = track_events

    @property
    def on(self):
        """Gets the on of this FeatureFlagConfig.  # noqa: E501


        :return: The on of this FeatureFlagConfig.  # noqa: E501
        :rtype: bool
        """
        return self._on

    @on.setter
    def on(self, on):
        """Sets the on of this FeatureFlagConfig.


        :param on: The on of this FeatureFlagConfig.  # noqa: E501
        :type: bool
        """

        self._on = on

    @property
    def archived(self):
        """Gets the archived of this FeatureFlagConfig.  # noqa: E501


        :return: The archived of this FeatureFlagConfig.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this FeatureFlagConfig.


        :param archived: The archived of this FeatureFlagConfig.  # noqa: E501
        :type: bool
        """

        self._archived = archived

    @property
    def salt(self):
        """Gets the salt of this FeatureFlagConfig.  # noqa: E501


        :return: The salt of this FeatureFlagConfig.  # noqa: E501
        :rtype: str
        """
        return self._salt

    @salt.setter
    def salt(self, salt):
        """Sets the salt of this FeatureFlagConfig.


        :param salt: The salt of this FeatureFlagConfig.  # noqa: E501
        :type: str
        """

        self._salt = salt

    @property
    def sel(self):
        """Gets the sel of this FeatureFlagConfig.  # noqa: E501


        :return: The sel of this FeatureFlagConfig.  # noqa: E501
        :rtype: str
        """
        return self._sel

    @sel.setter
    def sel(self, sel):
        """Sets the sel of this FeatureFlagConfig.


        :param sel: The sel of this FeatureFlagConfig.  # noqa: E501
        :type: str
        """

        self._sel = sel

    @property
    def last_modified(self):
        """Gets the last_modified of this FeatureFlagConfig.  # noqa: E501


        :return: The last_modified of this FeatureFlagConfig.  # noqa: E501
        :rtype: int
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this FeatureFlagConfig.


        :param last_modified: The last_modified of this FeatureFlagConfig.  # noqa: E501
        :type: int
        """

        self._last_modified = last_modified

    @property
    def version(self):
        """Gets the version of this FeatureFlagConfig.  # noqa: E501


        :return: The version of this FeatureFlagConfig.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this FeatureFlagConfig.


        :param version: The version of this FeatureFlagConfig.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def targets(self):
        """Gets the targets of this FeatureFlagConfig.  # noqa: E501


        :return: The targets of this FeatureFlagConfig.  # noqa: E501
        :rtype: list[Target]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """Sets the targets of this FeatureFlagConfig.


        :param targets: The targets of this FeatureFlagConfig.  # noqa: E501
        :type: list[Target]
        """

        self._targets = targets

    @property
    def rules(self):
        """Gets the rules of this FeatureFlagConfig.  # noqa: E501


        :return: The rules of this FeatureFlagConfig.  # noqa: E501
        :rtype: list[Rule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this FeatureFlagConfig.


        :param rules: The rules of this FeatureFlagConfig.  # noqa: E501
        :type: list[Rule]
        """

        self._rules = rules

    @property
    def fallthrough(self):
        """Gets the fallthrough of this FeatureFlagConfig.  # noqa: E501


        :return: The fallthrough of this FeatureFlagConfig.  # noqa: E501
        :rtype: Fallthrough
        """
        return self._fallthrough

    @fallthrough.setter
    def fallthrough(self, fallthrough):
        """Sets the fallthrough of this FeatureFlagConfig.


        :param fallthrough: The fallthrough of this FeatureFlagConfig.  # noqa: E501
        :type: Fallthrough
        """

        self._fallthrough = fallthrough

    @property
    def off_variation(self):
        """Gets the off_variation of this FeatureFlagConfig.  # noqa: E501


        :return: The off_variation of this FeatureFlagConfig.  # noqa: E501
        :rtype: int
        """
        return self._off_variation

    @off_variation.setter
    def off_variation(self, off_variation):
        """Sets the off_variation of this FeatureFlagConfig.


        :param off_variation: The off_variation of this FeatureFlagConfig.  # noqa: E501
        :type: int
        """

        self._off_variation = off_variation

    @property
    def prerequisites(self):
        """Gets the prerequisites of this FeatureFlagConfig.  # noqa: E501


        :return: The prerequisites of this FeatureFlagConfig.  # noqa: E501
        :rtype: list[Prerequisite]
        """
        return self._prerequisites

    @prerequisites.setter
    def prerequisites(self, prerequisites):
        """Sets the prerequisites of this FeatureFlagConfig.


        :param prerequisites: The prerequisites of this FeatureFlagConfig.  # noqa: E501
        :type: list[Prerequisite]
        """

        self._prerequisites = prerequisites

    @property
    def track_events(self):
        """Gets the track_events of this FeatureFlagConfig.  # noqa: E501

        Set to true to send detailed event information for this flag.  # noqa: E501

        :return: The track_events of this FeatureFlagConfig.  # noqa: E501
        :rtype: bool
        """
        return self._track_events

    @track_events.setter
    def track_events(self, track_events):
        """Sets the track_events of this FeatureFlagConfig.

        Set to true to send detailed event information for this flag.  # noqa: E501

        :param track_events: The track_events of this FeatureFlagConfig.  # noqa: E501
        :type: bool
        """

        self._track_events = track_events

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
        if issubclass(FeatureFlagConfig, dict):
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
        if not isinstance(other, FeatureFlagConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
