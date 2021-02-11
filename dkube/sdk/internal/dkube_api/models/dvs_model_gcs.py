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


class DVSModelGcs(object):
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
        'bucket': 'str',
        'secret': 'str'
    }

    attribute_map = {
        'bucket': 'bucket',
        'secret': 'secret'
    }

    def __init__(self, bucket=None, secret=None):  # noqa: E501
        """DVSModelGcs - a model defined in Swagger"""  # noqa: E501

        self._bucket = None
        self._secret = None
        self.discriminator = None

        if bucket is not None:
            self.bucket = bucket
        if secret is not None:
            self.secret = secret

    @property
    def bucket(self):
        """Gets the bucket of this DVSModelGcs.  # noqa: E501


        :return: The bucket of this DVSModelGcs.  # noqa: E501
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this DVSModelGcs.


        :param bucket: The bucket of this DVSModelGcs.  # noqa: E501
        :type: str
        """

        self._bucket = bucket

    @property
    def secret(self):
        """Gets the secret of this DVSModelGcs.  # noqa: E501

        JSON string of google service account  # noqa: E501

        :return: The secret of this DVSModelGcs.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this DVSModelGcs.

        JSON string of google service account  # noqa: E501

        :param secret: The secret of this DVSModelGcs.  # noqa: E501
        :type: str
        """

        self._secret = secret

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
        if issubclass(DVSModelGcs, dict):
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
        if not isinstance(other, DVSModelGcs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
