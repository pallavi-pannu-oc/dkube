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


class JobModelParametersGeneratedPipeline(object):
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
        'runid': 'str',
        'name': 'str'
    }

    attribute_map = {
        'runid': 'runid',
        'name': 'name'
    }

    def __init__(self, runid=None, name=None):  # noqa: E501
        """JobModelParametersGeneratedPipeline - a model defined in Swagger"""  # noqa: E501

        self._runid = None
        self._name = None
        self.discriminator = None

        if runid is not None:
            self.runid = runid
        if name is not None:
            self.name = name

    @property
    def runid(self):
        """Gets the runid of this JobModelParametersGeneratedPipeline.  # noqa: E501


        :return: The runid of this JobModelParametersGeneratedPipeline.  # noqa: E501
        :rtype: str
        """
        return self._runid

    @runid.setter
    def runid(self, runid):
        """Sets the runid of this JobModelParametersGeneratedPipeline.


        :param runid: The runid of this JobModelParametersGeneratedPipeline.  # noqa: E501
        :type: str
        """

        self._runid = runid

    @property
    def name(self):
        """Gets the name of this JobModelParametersGeneratedPipeline.  # noqa: E501


        :return: The name of this JobModelParametersGeneratedPipeline.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JobModelParametersGeneratedPipeline.


        :param name: The name of this JobModelParametersGeneratedPipeline.  # noqa: E501
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
        if issubclass(JobModelParametersGeneratedPipeline, dict):
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
        if not isinstance(other, JobModelParametersGeneratedPipeline):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
