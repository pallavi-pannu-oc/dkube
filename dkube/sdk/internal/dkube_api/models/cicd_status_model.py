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


class CICDStatusModel(object):
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
        'state': 'str',
        'reason': 'str',
        'program_path': 'str',
        'repo': 'str',
        'commit_id': 'str'
    }

    attribute_map = {
        'state': 'state',
        'reason': 'reason',
        'program_path': 'programPath',
        'repo': 'repo',
        'commit_id': 'commitID'
    }

    def __init__(self, state=None, reason=None, program_path=None, repo=None, commit_id=None):  # noqa: E501
        """CICDStatusModel - a model defined in Swagger"""  # noqa: E501

        self._state = None
        self._reason = None
        self._program_path = None
        self._repo = None
        self._commit_id = None
        self.discriminator = None

        if state is not None:
            self.state = state
        if reason is not None:
            self.reason = reason
        if program_path is not None:
            self.program_path = program_path
        if repo is not None:
            self.repo = repo
        if commit_id is not None:
            self.commit_id = commit_id

    @property
    def state(self):
        """Gets the state of this CICDStatusModel.  # noqa: E501


        :return: The state of this CICDStatusModel.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this CICDStatusModel.


        :param state: The state of this CICDStatusModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["GITCLONE", "CICDBUILD", "WAITINGIMAGE", "CICDBUILDCOMPLETE"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def reason(self):
        """Gets the reason of this CICDStatusModel.  # noqa: E501


        :return: The reason of this CICDStatusModel.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this CICDStatusModel.


        :param reason: The reason of this CICDStatusModel.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def program_path(self):
        """Gets the program_path of this CICDStatusModel.  # noqa: E501


        :return: The program_path of this CICDStatusModel.  # noqa: E501
        :rtype: str
        """
        return self._program_path

    @program_path.setter
    def program_path(self, program_path):
        """Sets the program_path of this CICDStatusModel.


        :param program_path: The program_path of this CICDStatusModel.  # noqa: E501
        :type: str
        """

        self._program_path = program_path

    @property
    def repo(self):
        """Gets the repo of this CICDStatusModel.  # noqa: E501


        :return: The repo of this CICDStatusModel.  # noqa: E501
        :rtype: str
        """
        return self._repo

    @repo.setter
    def repo(self, repo):
        """Sets the repo of this CICDStatusModel.


        :param repo: The repo of this CICDStatusModel.  # noqa: E501
        :type: str
        """

        self._repo = repo

    @property
    def commit_id(self):
        """Gets the commit_id of this CICDStatusModel.  # noqa: E501


        :return: The commit_id of this CICDStatusModel.  # noqa: E501
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        """Sets the commit_id of this CICDStatusModel.


        :param commit_id: The commit_id of this CICDStatusModel.  # noqa: E501
        :type: str
        """

        self._commit_id = commit_id

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
        if issubclass(CICDStatusModel, dict):
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
        if not isinstance(other, CICDStatusModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
