# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.2.7.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ModelDetailsTensorpbSignatures(object):
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
        'name': 'str',
        'method': 'str',
        'inputs': 'list[Tensor]',
        'outputs': 'list[Tensor]'
    }

    attribute_map = {
        'name': 'name',
        'method': 'method',
        'inputs': 'inputs',
        'outputs': 'outputs'
    }

    def __init__(self, name=None, method=None, inputs=None, outputs=None):  # noqa: E501
        """ModelDetailsTensorpbSignatures - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._method = None
        self._inputs = None
        self._outputs = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if method is not None:
            self.method = method
        if inputs is not None:
            self.inputs = inputs
        if outputs is not None:
            self.outputs = outputs

    @property
    def name(self):
        """Gets the name of this ModelDetailsTensorpbSignatures.  # noqa: E501


        :return: The name of this ModelDetailsTensorpbSignatures.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModelDetailsTensorpbSignatures.


        :param name: The name of this ModelDetailsTensorpbSignatures.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def method(self):
        """Gets the method of this ModelDetailsTensorpbSignatures.  # noqa: E501


        :return: The method of this ModelDetailsTensorpbSignatures.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this ModelDetailsTensorpbSignatures.


        :param method: The method of this ModelDetailsTensorpbSignatures.  # noqa: E501
        :type: str
        """

        self._method = method

    @property
    def inputs(self):
        """Gets the inputs of this ModelDetailsTensorpbSignatures.  # noqa: E501


        :return: The inputs of this ModelDetailsTensorpbSignatures.  # noqa: E501
        :rtype: list[Tensor]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this ModelDetailsTensorpbSignatures.


        :param inputs: The inputs of this ModelDetailsTensorpbSignatures.  # noqa: E501
        :type: list[Tensor]
        """

        self._inputs = inputs

    @property
    def outputs(self):
        """Gets the outputs of this ModelDetailsTensorpbSignatures.  # noqa: E501


        :return: The outputs of this ModelDetailsTensorpbSignatures.  # noqa: E501
        :rtype: list[Tensor]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this ModelDetailsTensorpbSignatures.


        :param outputs: The outputs of this ModelDetailsTensorpbSignatures.  # noqa: E501
        :type: list[Tensor]
        """

        self._outputs = outputs

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
        if issubclass(ModelDetailsTensorpbSignatures, dict):
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
        if not isinstance(other, ModelDetailsTensorpbSignatures):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
