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


class ModelMetricsInnerCurve(object):
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
        'csv': 'str'
    }

    attribute_map = {
        'csv': 'csv'
    }

    def __init__(self, csv=None):  # noqa: E501
        """ModelMetricsInnerCurve - a model defined in Swagger"""  # noqa: E501

        self._csv = None
        self.discriminator = None

        if csv is not None:
            self.csv = csv

    @property
    def csv(self):
        """Gets the csv of this ModelMetricsInnerCurve.  # noqa: E501


        :return: The csv of this ModelMetricsInnerCurve.  # noqa: E501
        :rtype: str
        """
        return self._csv

    @csv.setter
    def csv(self, csv):
        """Sets the csv of this ModelMetricsInnerCurve.


        :param csv: The csv of this ModelMetricsInnerCurve.  # noqa: E501
        :type: str
        """

        self._csv = csv

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
        if issubclass(ModelMetricsInnerCurve, dict):
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
        if not isinstance(other, ModelMetricsInnerCurve):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
