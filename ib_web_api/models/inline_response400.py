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


class InlineResponse400(object):
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
        'error': 'str',
        'status_code': 'int'
    }

    attribute_map = {
        'error': 'error',
        'status_code': 'statusCode'
    }

    def __init__(self, error=None, status_code=None):  # noqa: E501
        """InlineResponse400 - a model defined in Swagger"""  # noqa: E501

        self._error = None
        self._status_code = None
        self.discriminator = None

        if error is not None:
            self.error = error
        if status_code is not None:
            self.status_code = status_code

    @property
    def error(self):
        """Gets the error of this InlineResponse400.  # noqa: E501

        for example-order not confirmed  # noqa: E501

        :return: The error of this InlineResponse400.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this InlineResponse400.

        for example-order not confirmed  # noqa: E501

        :param error: The error of this InlineResponse400.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def status_code(self):
        """Gets the status_code of this InlineResponse400.  # noqa: E501


        :return: The status_code of this InlineResponse400.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this InlineResponse400.


        :param status_code: The status_code of this InlineResponse400.  # noqa: E501
        :type: int
        """

        self._status_code = status_code

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
        if issubclass(InlineResponse400, dict):
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
        if not isinstance(other, InlineResponse400):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
