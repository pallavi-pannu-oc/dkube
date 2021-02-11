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


class ModelTrainingInfoTrainingCode(object):
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
        'repo': 'str',
        'commit': 'str',
        'project': 'str'
    }

    attribute_map = {
        'repo': 'repo',
        'commit': 'commit',
        'project': 'project'
    }

    def __init__(self, repo=None, commit=None, project=None):  # noqa: E501
        """ModelTrainingInfoTrainingCode - a model defined in Swagger"""  # noqa: E501

        self._repo = None
        self._commit = None
        self._project = None
        self.discriminator = None

        if repo is not None:
            self.repo = repo
        if commit is not None:
            self.commit = commit
        if project is not None:
            self.project = project

    @property
    def repo(self):
        """Gets the repo of this ModelTrainingInfoTrainingCode.  # noqa: E501


        :return: The repo of this ModelTrainingInfoTrainingCode.  # noqa: E501
        :rtype: str
        """
        return self._repo

    @repo.setter
    def repo(self, repo):
        """Sets the repo of this ModelTrainingInfoTrainingCode.


        :param repo: The repo of this ModelTrainingInfoTrainingCode.  # noqa: E501
        :type: str
        """

        self._repo = repo

    @property
    def commit(self):
        """Gets the commit of this ModelTrainingInfoTrainingCode.  # noqa: E501


        :return: The commit of this ModelTrainingInfoTrainingCode.  # noqa: E501
        :rtype: str
        """
        return self._commit

    @commit.setter
    def commit(self, commit):
        """Sets the commit of this ModelTrainingInfoTrainingCode.


        :param commit: The commit of this ModelTrainingInfoTrainingCode.  # noqa: E501
        :type: str
        """

        self._commit = commit

    @property
    def project(self):
        """Gets the project of this ModelTrainingInfoTrainingCode.  # noqa: E501


        :return: The project of this ModelTrainingInfoTrainingCode.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this ModelTrainingInfoTrainingCode.


        :param project: The project of this ModelTrainingInfoTrainingCode.  # noqa: E501
        :type: str
        """

        self._project = project

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
        if issubclass(ModelTrainingInfoTrainingCode, dict):
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
        if not isinstance(other, ModelTrainingInfoTrainingCode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
