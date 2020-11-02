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


class GitAccessCredentials(object):
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
        'username': 'str',
        'password': 'str',
        'apikey': 'str',
        'sshkey': 'str',
        'private': 'bool'
    }

    attribute_map = {
        'username': 'username',
        'password': 'password',
        'apikey': 'apikey',
        'sshkey': 'sshkey',
        'private': 'private'
    }

    def __init__(self, username=None, password=None, apikey=None, sshkey=None, private=False):  # noqa: E501
        """GitAccessCredentials - a model defined in Swagger"""  # noqa: E501

        self._username = None
        self._password = None
        self._apikey = None
        self._sshkey = None
        self._private = None
        self.discriminator = None

        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if apikey is not None:
            self.apikey = apikey
        if sshkey is not None:
            self.sshkey = sshkey
        if private is not None:
            self.private = private

    @property
    def username(self):
        """Gets the username of this GitAccessCredentials.  # noqa: E501


        :return: The username of this GitAccessCredentials.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this GitAccessCredentials.


        :param username: The username of this GitAccessCredentials.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this GitAccessCredentials.  # noqa: E501


        :return: The password of this GitAccessCredentials.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this GitAccessCredentials.


        :param password: The password of this GitAccessCredentials.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def apikey(self):
        """Gets the apikey of this GitAccessCredentials.  # noqa: E501


        :return: The apikey of this GitAccessCredentials.  # noqa: E501
        :rtype: str
        """
        return self._apikey

    @apikey.setter
    def apikey(self, apikey):
        """Sets the apikey of this GitAccessCredentials.


        :param apikey: The apikey of this GitAccessCredentials.  # noqa: E501
        :type: str
        """

        self._apikey = apikey

    @property
    def sshkey(self):
        """Gets the sshkey of this GitAccessCredentials.  # noqa: E501


        :return: The sshkey of this GitAccessCredentials.  # noqa: E501
        :rtype: str
        """
        return self._sshkey

    @sshkey.setter
    def sshkey(self, sshkey):
        """Sets the sshkey of this GitAccessCredentials.


        :param sshkey: The sshkey of this GitAccessCredentials.  # noqa: E501
        :type: str
        """

        self._sshkey = sshkey

    @property
    def private(self):
        """Gets the private of this GitAccessCredentials.  # noqa: E501


        :return: The private of this GitAccessCredentials.  # noqa: E501
        :rtype: bool
        """
        return self._private

    @private.setter
    def private(self, private):
        """Sets the private of this GitAccessCredentials.


        :param private: The private of this GitAccessCredentials.  # noqa: E501
        :type: bool
        """

        self._private = private

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
        if issubclass(GitAccessCredentials, dict):
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
        if not isinstance(other, GitAccessCredentials):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other