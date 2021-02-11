# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.2.1.11
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class NodeModelNetwork(object):
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
        'hostname': 'str',
        'hostip': 'str',
        'hostmac': 'str'
    }

    attribute_map = {
        'hostname': 'hostname',
        'hostip': 'hostip',
        'hostmac': 'hostmac'
    }

    def __init__(self, hostname=None, hostip=None, hostmac=None):  # noqa: E501
        """NodeModelNetwork - a model defined in Swagger"""  # noqa: E501

        self._hostname = None
        self._hostip = None
        self._hostmac = None
        self.discriminator = None

        if hostname is not None:
            self.hostname = hostname
        if hostip is not None:
            self.hostip = hostip
        if hostmac is not None:
            self.hostmac = hostmac

    @property
    def hostname(self):
        """Gets the hostname of this NodeModelNetwork.  # noqa: E501


        :return: The hostname of this NodeModelNetwork.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this NodeModelNetwork.


        :param hostname: The hostname of this NodeModelNetwork.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def hostip(self):
        """Gets the hostip of this NodeModelNetwork.  # noqa: E501


        :return: The hostip of this NodeModelNetwork.  # noqa: E501
        :rtype: str
        """
        return self._hostip

    @hostip.setter
    def hostip(self, hostip):
        """Sets the hostip of this NodeModelNetwork.


        :param hostip: The hostip of this NodeModelNetwork.  # noqa: E501
        :type: str
        """

        self._hostip = hostip

    @property
    def hostmac(self):
        """Gets the hostmac of this NodeModelNetwork.  # noqa: E501


        :return: The hostmac of this NodeModelNetwork.  # noqa: E501
        :rtype: str
        """
        return self._hostmac

    @hostmac.setter
    def hostmac(self, hostmac):
        """Sets the hostmac of this NodeModelNetwork.


        :param hostmac: The hostmac of this NodeModelNetwork.  # noqa: E501
        :type: str
        """

        self._hostmac = hostmac

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
        if issubclass(NodeModelNetwork, dict):
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
        if not isinstance(other, NodeModelNetwork):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
