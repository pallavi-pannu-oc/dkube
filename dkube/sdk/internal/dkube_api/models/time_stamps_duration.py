# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.2.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class TimeStampsDuration(object):
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
        'days': 'str',
        'hours': 'str',
        'minutes': 'str',
        'seconds': 'str'
    }

    attribute_map = {
        'days': 'days',
        'hours': 'hours',
        'minutes': 'minutes',
        'seconds': 'seconds'
    }

    def __init__(self, days=None, hours=None, minutes=None, seconds=None):  # noqa: E501
        """TimeStampsDuration - a model defined in Swagger"""  # noqa: E501

        self._days = None
        self._hours = None
        self._minutes = None
        self._seconds = None
        self.discriminator = None

        if days is not None:
            self.days = days
        if hours is not None:
            self.hours = hours
        if minutes is not None:
            self.minutes = minutes
        if seconds is not None:
            self.seconds = seconds

    @property
    def days(self):
        """Gets the days of this TimeStampsDuration.  # noqa: E501


        :return: The days of this TimeStampsDuration.  # noqa: E501
        :rtype: str
        """
        return self._days

    @days.setter
    def days(self, days):
        """Sets the days of this TimeStampsDuration.


        :param days: The days of this TimeStampsDuration.  # noqa: E501
        :type: str
        """

        self._days = days

    @property
    def hours(self):
        """Gets the hours of this TimeStampsDuration.  # noqa: E501


        :return: The hours of this TimeStampsDuration.  # noqa: E501
        :rtype: str
        """
        return self._hours

    @hours.setter
    def hours(self, hours):
        """Sets the hours of this TimeStampsDuration.


        :param hours: The hours of this TimeStampsDuration.  # noqa: E501
        :type: str
        """

        self._hours = hours

    @property
    def minutes(self):
        """Gets the minutes of this TimeStampsDuration.  # noqa: E501


        :return: The minutes of this TimeStampsDuration.  # noqa: E501
        :rtype: str
        """
        return self._minutes

    @minutes.setter
    def minutes(self, minutes):
        """Sets the minutes of this TimeStampsDuration.


        :param minutes: The minutes of this TimeStampsDuration.  # noqa: E501
        :type: str
        """

        self._minutes = minutes

    @property
    def seconds(self):
        """Gets the seconds of this TimeStampsDuration.  # noqa: E501


        :return: The seconds of this TimeStampsDuration.  # noqa: E501
        :rtype: str
        """
        return self._seconds

    @seconds.setter
    def seconds(self, seconds):
        """Sets the seconds of this TimeStampsDuration.


        :param seconds: The seconds of this TimeStampsDuration.  # noqa: E501
        :type: str
        """

        self._seconds = seconds

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
        if issubclass(TimeStampsDuration, dict):
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
        if not isinstance(other, TimeStampsDuration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
