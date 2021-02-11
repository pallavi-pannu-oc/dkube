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


class NotificationData(object):
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
        'job_uuid': 'str',
        '_class': 'str',
        'subclass': 'str',
        'status': 'str',
        'reason': 'str',
        'notebook_url': 'str',
        'serving_url': 'str',
        'tensorboard_url': 'str',
        'is_tensorboard': 'bool',
        'study': 'NotificationDataStudy',
        'worker': 'WorkerModel',
        'datum': 'DatumModel',
        'version': 'VersionModel'
    }

    attribute_map = {
        'username': 'Username',
        'job_uuid': 'JobUUID',
        '_class': 'Class',
        'subclass': 'Subclass',
        'status': 'Status',
        'reason': 'Reason',
        'notebook_url': 'NotebookUrl',
        'serving_url': 'ServingUrl',
        'tensorboard_url': 'TensorboardUrl',
        'is_tensorboard': 'IsTensorboard',
        'study': 'Study',
        'worker': 'Worker',
        'datum': 'Datum',
        'version': 'Version'
    }

    def __init__(self, username=None, job_uuid=None, _class=None, subclass=None, status=None, reason=None, notebook_url=None, serving_url=None, tensorboard_url=None, is_tensorboard=None, study=None, worker=None, datum=None, version=None):  # noqa: E501
        """NotificationData - a model defined in Swagger"""  # noqa: E501

        self._username = None
        self._job_uuid = None
        self.__class = None
        self._subclass = None
        self._status = None
        self._reason = None
        self._notebook_url = None
        self._serving_url = None
        self._tensorboard_url = None
        self._is_tensorboard = None
        self._study = None
        self._worker = None
        self._datum = None
        self._version = None
        self.discriminator = None

        if username is not None:
            self.username = username
        if job_uuid is not None:
            self.job_uuid = job_uuid
        if _class is not None:
            self._class = _class
        if subclass is not None:
            self.subclass = subclass
        if status is not None:
            self.status = status
        if reason is not None:
            self.reason = reason
        if notebook_url is not None:
            self.notebook_url = notebook_url
        if serving_url is not None:
            self.serving_url = serving_url
        if tensorboard_url is not None:
            self.tensorboard_url = tensorboard_url
        if is_tensorboard is not None:
            self.is_tensorboard = is_tensorboard
        if study is not None:
            self.study = study
        if worker is not None:
            self.worker = worker
        if datum is not None:
            self.datum = datum
        if version is not None:
            self.version = version

    @property
    def username(self):
        """Gets the username of this NotificationData.  # noqa: E501


        :return: The username of this NotificationData.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this NotificationData.


        :param username: The username of this NotificationData.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def job_uuid(self):
        """Gets the job_uuid of this NotificationData.  # noqa: E501


        :return: The job_uuid of this NotificationData.  # noqa: E501
        :rtype: str
        """
        return self._job_uuid

    @job_uuid.setter
    def job_uuid(self, job_uuid):
        """Sets the job_uuid of this NotificationData.


        :param job_uuid: The job_uuid of this NotificationData.  # noqa: E501
        :type: str
        """

        self._job_uuid = job_uuid

    @property
    def _class(self):
        """Gets the _class of this NotificationData.  # noqa: E501


        :return: The _class of this NotificationData.  # noqa: E501
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this NotificationData.


        :param _class: The _class of this NotificationData.  # noqa: E501
        :type: str
        """

        self.__class = _class

    @property
    def subclass(self):
        """Gets the subclass of this NotificationData.  # noqa: E501


        :return: The subclass of this NotificationData.  # noqa: E501
        :rtype: str
        """
        return self._subclass

    @subclass.setter
    def subclass(self, subclass):
        """Sets the subclass of this NotificationData.


        :param subclass: The subclass of this NotificationData.  # noqa: E501
        :type: str
        """

        self._subclass = subclass

    @property
    def status(self):
        """Gets the status of this NotificationData.  # noqa: E501


        :return: The status of this NotificationData.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NotificationData.


        :param status: The status of this NotificationData.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def reason(self):
        """Gets the reason of this NotificationData.  # noqa: E501


        :return: The reason of this NotificationData.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this NotificationData.


        :param reason: The reason of this NotificationData.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def notebook_url(self):
        """Gets the notebook_url of this NotificationData.  # noqa: E501


        :return: The notebook_url of this NotificationData.  # noqa: E501
        :rtype: str
        """
        return self._notebook_url

    @notebook_url.setter
    def notebook_url(self, notebook_url):
        """Sets the notebook_url of this NotificationData.


        :param notebook_url: The notebook_url of this NotificationData.  # noqa: E501
        :type: str
        """

        self._notebook_url = notebook_url

    @property
    def serving_url(self):
        """Gets the serving_url of this NotificationData.  # noqa: E501


        :return: The serving_url of this NotificationData.  # noqa: E501
        :rtype: str
        """
        return self._serving_url

    @serving_url.setter
    def serving_url(self, serving_url):
        """Sets the serving_url of this NotificationData.


        :param serving_url: The serving_url of this NotificationData.  # noqa: E501
        :type: str
        """

        self._serving_url = serving_url

    @property
    def tensorboard_url(self):
        """Gets the tensorboard_url of this NotificationData.  # noqa: E501


        :return: The tensorboard_url of this NotificationData.  # noqa: E501
        :rtype: str
        """
        return self._tensorboard_url

    @tensorboard_url.setter
    def tensorboard_url(self, tensorboard_url):
        """Sets the tensorboard_url of this NotificationData.


        :param tensorboard_url: The tensorboard_url of this NotificationData.  # noqa: E501
        :type: str
        """

        self._tensorboard_url = tensorboard_url

    @property
    def is_tensorboard(self):
        """Gets the is_tensorboard of this NotificationData.  # noqa: E501


        :return: The is_tensorboard of this NotificationData.  # noqa: E501
        :rtype: bool
        """
        return self._is_tensorboard

    @is_tensorboard.setter
    def is_tensorboard(self, is_tensorboard):
        """Sets the is_tensorboard of this NotificationData.


        :param is_tensorboard: The is_tensorboard of this NotificationData.  # noqa: E501
        :type: bool
        """

        self._is_tensorboard = is_tensorboard

    @property
    def study(self):
        """Gets the study of this NotificationData.  # noqa: E501


        :return: The study of this NotificationData.  # noqa: E501
        :rtype: NotificationDataStudy
        """
        return self._study

    @study.setter
    def study(self, study):
        """Sets the study of this NotificationData.


        :param study: The study of this NotificationData.  # noqa: E501
        :type: NotificationDataStudy
        """

        self._study = study

    @property
    def worker(self):
        """Gets the worker of this NotificationData.  # noqa: E501


        :return: The worker of this NotificationData.  # noqa: E501
        :rtype: WorkerModel
        """
        return self._worker

    @worker.setter
    def worker(self, worker):
        """Sets the worker of this NotificationData.


        :param worker: The worker of this NotificationData.  # noqa: E501
        :type: WorkerModel
        """

        self._worker = worker

    @property
    def datum(self):
        """Gets the datum of this NotificationData.  # noqa: E501


        :return: The datum of this NotificationData.  # noqa: E501
        :rtype: DatumModel
        """
        return self._datum

    @datum.setter
    def datum(self, datum):
        """Sets the datum of this NotificationData.


        :param datum: The datum of this NotificationData.  # noqa: E501
        :type: DatumModel
        """

        self._datum = datum

    @property
    def version(self):
        """Gets the version of this NotificationData.  # noqa: E501


        :return: The version of this NotificationData.  # noqa: E501
        :rtype: VersionModel
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this NotificationData.


        :param version: The version of this NotificationData.  # noqa: E501
        :type: VersionModel
        """

        self._version = version

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
        if issubclass(NotificationData, dict):
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
        if not isinstance(other, NotificationData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
