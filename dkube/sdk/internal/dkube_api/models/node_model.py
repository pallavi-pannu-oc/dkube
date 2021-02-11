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


class NodeModel(object):
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
        'version': 'str',
        'name': 'str',
        'network': 'NodeModelNetwork',
        'software': 'NodeModelSoftware',
        'capacity': 'NodeModelCapacity',
        'accelerator': 'NodeModelAccelerator',
        'dkube': 'NodeModelDkube',
        'uptime': 'str',
        'generated': 'ModelCatalogItemGenerated',
        'cluster_name': 'str',
        'blob': 'str'
    }

    attribute_map = {
        'version': 'version',
        'name': 'name',
        'network': 'network',
        'software': 'software',
        'capacity': 'capacity',
        'accelerator': 'accelerator',
        'dkube': 'dkube',
        'uptime': 'uptime',
        'generated': 'generated',
        'cluster_name': 'cluster_name',
        'blob': 'blob'
    }

    def __init__(self, version=None, name=None, network=None, software=None, capacity=None, accelerator=None, dkube=None, uptime=None, generated=None, cluster_name=None, blob=None):  # noqa: E501
        """NodeModel - a model defined in Swagger"""  # noqa: E501

        self._version = None
        self._name = None
        self._network = None
        self._software = None
        self._capacity = None
        self._accelerator = None
        self._dkube = None
        self._uptime = None
        self._generated = None
        self._cluster_name = None
        self._blob = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if name is not None:
            self.name = name
        if network is not None:
            self.network = network
        if software is not None:
            self.software = software
        if capacity is not None:
            self.capacity = capacity
        if accelerator is not None:
            self.accelerator = accelerator
        if dkube is not None:
            self.dkube = dkube
        if uptime is not None:
            self.uptime = uptime
        if generated is not None:
            self.generated = generated
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if blob is not None:
            self.blob = blob

    @property
    def version(self):
        """Gets the version of this NodeModel.  # noqa: E501


        :return: The version of this NodeModel.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this NodeModel.


        :param version: The version of this NodeModel.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def name(self):
        """Gets the name of this NodeModel.  # noqa: E501


        :return: The name of this NodeModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NodeModel.


        :param name: The name of this NodeModel.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def network(self):
        """Gets the network of this NodeModel.  # noqa: E501


        :return: The network of this NodeModel.  # noqa: E501
        :rtype: NodeModelNetwork
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this NodeModel.


        :param network: The network of this NodeModel.  # noqa: E501
        :type: NodeModelNetwork
        """

        self._network = network

    @property
    def software(self):
        """Gets the software of this NodeModel.  # noqa: E501


        :return: The software of this NodeModel.  # noqa: E501
        :rtype: NodeModelSoftware
        """
        return self._software

    @software.setter
    def software(self, software):
        """Sets the software of this NodeModel.


        :param software: The software of this NodeModel.  # noqa: E501
        :type: NodeModelSoftware
        """

        self._software = software

    @property
    def capacity(self):
        """Gets the capacity of this NodeModel.  # noqa: E501


        :return: The capacity of this NodeModel.  # noqa: E501
        :rtype: NodeModelCapacity
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this NodeModel.


        :param capacity: The capacity of this NodeModel.  # noqa: E501
        :type: NodeModelCapacity
        """

        self._capacity = capacity

    @property
    def accelerator(self):
        """Gets the accelerator of this NodeModel.  # noqa: E501


        :return: The accelerator of this NodeModel.  # noqa: E501
        :rtype: NodeModelAccelerator
        """
        return self._accelerator

    @accelerator.setter
    def accelerator(self, accelerator):
        """Sets the accelerator of this NodeModel.


        :param accelerator: The accelerator of this NodeModel.  # noqa: E501
        :type: NodeModelAccelerator
        """

        self._accelerator = accelerator

    @property
    def dkube(self):
        """Gets the dkube of this NodeModel.  # noqa: E501


        :return: The dkube of this NodeModel.  # noqa: E501
        :rtype: NodeModelDkube
        """
        return self._dkube

    @dkube.setter
    def dkube(self, dkube):
        """Sets the dkube of this NodeModel.


        :param dkube: The dkube of this NodeModel.  # noqa: E501
        :type: NodeModelDkube
        """

        self._dkube = dkube

    @property
    def uptime(self):
        """Gets the uptime of this NodeModel.  # noqa: E501


        :return: The uptime of this NodeModel.  # noqa: E501
        :rtype: str
        """
        return self._uptime

    @uptime.setter
    def uptime(self, uptime):
        """Sets the uptime of this NodeModel.


        :param uptime: The uptime of this NodeModel.  # noqa: E501
        :type: str
        """

        self._uptime = uptime

    @property
    def generated(self):
        """Gets the generated of this NodeModel.  # noqa: E501


        :return: The generated of this NodeModel.  # noqa: E501
        :rtype: ModelCatalogItemGenerated
        """
        return self._generated

    @generated.setter
    def generated(self, generated):
        """Sets the generated of this NodeModel.


        :param generated: The generated of this NodeModel.  # noqa: E501
        :type: ModelCatalogItemGenerated
        """

        self._generated = generated

    @property
    def cluster_name(self):
        """Gets the cluster_name of this NodeModel.  # noqa: E501


        :return: The cluster_name of this NodeModel.  # noqa: E501
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this NodeModel.


        :param cluster_name: The cluster_name of this NodeModel.  # noqa: E501
        :type: str
        """

        self._cluster_name = cluster_name

    @property
    def blob(self):
        """Gets the blob of this NodeModel.  # noqa: E501


        :return: The blob of this NodeModel.  # noqa: E501
        :rtype: str
        """
        return self._blob

    @blob.setter
    def blob(self, blob):
        """Sets the blob of this NodeModel.


        :param blob: The blob of this NodeModel.  # noqa: E501
        :type: str
        """

        self._blob = blob

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
        if issubclass(NodeModel, dict):
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
        if not isinstance(other, NodeModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
