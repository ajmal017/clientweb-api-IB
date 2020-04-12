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


class InlineResponse2009(object):
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
        'scan_type_list': 'list[InlineResponse2009ScanTypeList]',
        'instrument_list': 'list[InlineResponse2009InstrumentList]',
        'filter_list': 'list[InlineResponse2009FilterList]',
        'location_tree': 'list[InlineResponse2009LocationTree]'
    }

    attribute_map = {
        'scan_type_list': 'scan_type_list',
        'instrument_list': 'instrument_list',
        'filter_list': 'filter_list',
        'location_tree': 'location_tree'
    }

    def __init__(self, scan_type_list=None, instrument_list=None, filter_list=None, location_tree=None):  # noqa: E501
        """InlineResponse2009 - a model defined in Swagger"""  # noqa: E501

        self._scan_type_list = None
        self._instrument_list = None
        self._filter_list = None
        self._location_tree = None
        self.discriminator = None

        if scan_type_list is not None:
            self.scan_type_list = scan_type_list
        if instrument_list is not None:
            self.instrument_list = instrument_list
        if filter_list is not None:
            self.filter_list = filter_list
        if location_tree is not None:
            self.location_tree = location_tree

    @property
    def scan_type_list(self):
        """Gets the scan_type_list of this InlineResponse2009.  # noqa: E501


        :return: The scan_type_list of this InlineResponse2009.  # noqa: E501
        :rtype: list[InlineResponse2009ScanTypeList]
        """
        return self._scan_type_list

    @scan_type_list.setter
    def scan_type_list(self, scan_type_list):
        """Sets the scan_type_list of this InlineResponse2009.


        :param scan_type_list: The scan_type_list of this InlineResponse2009.  # noqa: E501
        :type: list[InlineResponse2009ScanTypeList]
        """

        self._scan_type_list = scan_type_list

    @property
    def instrument_list(self):
        """Gets the instrument_list of this InlineResponse2009.  # noqa: E501


        :return: The instrument_list of this InlineResponse2009.  # noqa: E501
        :rtype: list[InlineResponse2009InstrumentList]
        """
        return self._instrument_list

    @instrument_list.setter
    def instrument_list(self, instrument_list):
        """Sets the instrument_list of this InlineResponse2009.


        :param instrument_list: The instrument_list of this InlineResponse2009.  # noqa: E501
        :type: list[InlineResponse2009InstrumentList]
        """

        self._instrument_list = instrument_list

    @property
    def filter_list(self):
        """Gets the filter_list of this InlineResponse2009.  # noqa: E501


        :return: The filter_list of this InlineResponse2009.  # noqa: E501
        :rtype: list[InlineResponse2009FilterList]
        """
        return self._filter_list

    @filter_list.setter
    def filter_list(self, filter_list):
        """Sets the filter_list of this InlineResponse2009.


        :param filter_list: The filter_list of this InlineResponse2009.  # noqa: E501
        :type: list[InlineResponse2009FilterList]
        """

        self._filter_list = filter_list

    @property
    def location_tree(self):
        """Gets the location_tree of this InlineResponse2009.  # noqa: E501


        :return: The location_tree of this InlineResponse2009.  # noqa: E501
        :rtype: list[InlineResponse2009LocationTree]
        """
        return self._location_tree

    @location_tree.setter
    def location_tree(self, location_tree):
        """Sets the location_tree of this InlineResponse2009.


        :param location_tree: The location_tree of this InlineResponse2009.  # noqa: E501
        :type: list[InlineResponse2009LocationTree]
        """

        self._location_tree = location_tree

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
        if issubclass(InlineResponse2009, dict):
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
        if not isinstance(other, InlineResponse2009):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
