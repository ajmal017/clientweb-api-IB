# coding: utf-8

"""
    Client Portal Web API

    Production version of the Client Portal Web API  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Body7(object):
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
        'devicename': 'str',
        'device_id': 'str',
        'ui_name': 'str',
        'enabled': 'bool'
    }

    attribute_map = {
        'devicename': 'devicename',
        'device_id': 'deviceId',
        'ui_name': 'uiName',
        'enabled': 'enabled'
    }

    def __init__(self, devicename=None, device_id=None, ui_name=None, enabled=None):  # noqa: E501
        """Body7 - a model defined in Swagger"""  # noqa: E501

        self._devicename = None
        self._device_id = None
        self._ui_name = None
        self._enabled = None
        self.discriminator = None

        if devicename is not None:
            self.devicename = devicename
        if device_id is not None:
            self.device_id = device_id
        if ui_name is not None:
            self.ui_name = ui_name
        if enabled is not None:
            self.enabled = enabled

    @property
    def devicename(self):
        """Gets the devicename of this Body7.  # noqa: E501


        :return: The devicename of this Body7.  # noqa: E501
        :rtype: str
        """
        return self._devicename

    @devicename.setter
    def devicename(self, devicename):
        """Sets the devicename of this Body7.


        :param devicename: The devicename of this Body7.  # noqa: E501
        :type: str
        """

        self._devicename = devicename

    @property
    def device_id(self):
        """Gets the device_id of this Body7.  # noqa: E501


        :return: The device_id of this Body7.  # noqa: E501
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this Body7.


        :param device_id: The device_id of this Body7.  # noqa: E501
        :type: str
        """

        self._device_id = device_id

    @property
    def ui_name(self):
        """Gets the ui_name of this Body7.  # noqa: E501


        :return: The ui_name of this Body7.  # noqa: E501
        :rtype: str
        """
        return self._ui_name

    @ui_name.setter
    def ui_name(self, ui_name):
        """Sets the ui_name of this Body7.


        :param ui_name: The ui_name of this Body7.  # noqa: E501
        :type: str
        """

        self._ui_name = ui_name

    @property
    def enabled(self):
        """Gets the enabled of this Body7.  # noqa: E501


        :return: The enabled of this Body7.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this Body7.


        :param enabled: The enabled of this Body7.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

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
        if issubclass(Body7, dict):
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
        if not isinstance(other, Body7):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
