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


class AllocationInnerGroupLong(object):
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
        'computers': 'float',
        'semiconductors': 'float',
        'others': 'float',
        'chemicals': 'float',
        'apparel': 'float',
        'communications': 'float'
    }

    attribute_map = {
        'computers': 'Computers',
        'semiconductors': 'Semiconductors',
        'others': 'Others',
        'chemicals': 'Chemicals',
        'apparel': 'Apparel',
        'communications': 'Communications'
    }

    def __init__(self, computers=None, semiconductors=None, others=None, chemicals=None, apparel=None, communications=None):  # noqa: E501
        """AllocationInnerGroupLong - a model defined in Swagger"""  # noqa: E501

        self._computers = None
        self._semiconductors = None
        self._others = None
        self._chemicals = None
        self._apparel = None
        self._communications = None
        self.discriminator = None

        if computers is not None:
            self.computers = computers
        if semiconductors is not None:
            self.semiconductors = semiconductors
        if others is not None:
            self.others = others
        if chemicals is not None:
            self.chemicals = chemicals
        if apparel is not None:
            self.apparel = apparel
        if communications is not None:
            self.communications = communications

    @property
    def computers(self):
        """Gets the computers of this AllocationInnerGroupLong.  # noqa: E501


        :return: The computers of this AllocationInnerGroupLong.  # noqa: E501
        :rtype: float
        """
        return self._computers

    @computers.setter
    def computers(self, computers):
        """Sets the computers of this AllocationInnerGroupLong.


        :param computers: The computers of this AllocationInnerGroupLong.  # noqa: E501
        :type: float
        """

        self._computers = computers

    @property
    def semiconductors(self):
        """Gets the semiconductors of this AllocationInnerGroupLong.  # noqa: E501


        :return: The semiconductors of this AllocationInnerGroupLong.  # noqa: E501
        :rtype: float
        """
        return self._semiconductors

    @semiconductors.setter
    def semiconductors(self, semiconductors):
        """Sets the semiconductors of this AllocationInnerGroupLong.


        :param semiconductors: The semiconductors of this AllocationInnerGroupLong.  # noqa: E501
        :type: float
        """

        self._semiconductors = semiconductors

    @property
    def others(self):
        """Gets the others of this AllocationInnerGroupLong.  # noqa: E501


        :return: The others of this AllocationInnerGroupLong.  # noqa: E501
        :rtype: float
        """
        return self._others

    @others.setter
    def others(self, others):
        """Sets the others of this AllocationInnerGroupLong.


        :param others: The others of this AllocationInnerGroupLong.  # noqa: E501
        :type: float
        """

        self._others = others

    @property
    def chemicals(self):
        """Gets the chemicals of this AllocationInnerGroupLong.  # noqa: E501


        :return: The chemicals of this AllocationInnerGroupLong.  # noqa: E501
        :rtype: float
        """
        return self._chemicals

    @chemicals.setter
    def chemicals(self, chemicals):
        """Sets the chemicals of this AllocationInnerGroupLong.


        :param chemicals: The chemicals of this AllocationInnerGroupLong.  # noqa: E501
        :type: float
        """

        self._chemicals = chemicals

    @property
    def apparel(self):
        """Gets the apparel of this AllocationInnerGroupLong.  # noqa: E501


        :return: The apparel of this AllocationInnerGroupLong.  # noqa: E501
        :rtype: float
        """
        return self._apparel

    @apparel.setter
    def apparel(self, apparel):
        """Sets the apparel of this AllocationInnerGroupLong.


        :param apparel: The apparel of this AllocationInnerGroupLong.  # noqa: E501
        :type: float
        """

        self._apparel = apparel

    @property
    def communications(self):
        """Gets the communications of this AllocationInnerGroupLong.  # noqa: E501


        :return: The communications of this AllocationInnerGroupLong.  # noqa: E501
        :rtype: float
        """
        return self._communications

    @communications.setter
    def communications(self, communications):
        """Sets the communications of this AllocationInnerGroupLong.


        :param communications: The communications of this AllocationInnerGroupLong.  # noqa: E501
        :type: float
        """

        self._communications = communications

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
        if issubclass(AllocationInnerGroupLong, dict):
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
        if not isinstance(other, AllocationInnerGroupLong):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
