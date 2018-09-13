# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class HttpRouteMatchHeader(Model):
    """Describes header information for http route matching.

    :param name: Name of header to match in request.
    :type name: str
    :param value: Value of header to match in request.
    :type value: str
    :param type: how to match header value. Possible values include: 'exact'
    :type type: str or ~azure.servicefabric.models.HeaderMatchType
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, name, value=None, type=None):
        super(HttpRouteMatchHeader, self).__init__()
        self.name = name
        self.value = value
        self.type = type
