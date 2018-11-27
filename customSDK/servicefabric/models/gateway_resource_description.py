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


class GatewayResourceDescription(Model):
    """This type describes a gateway resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param name: Name of the Gateway resource.
    :type name: str
    :param description: User readable description of the gateway.
    :type description: str
    :param source_network: Network the gateway should listen on for requests.
    :type source_network: ~azure.servicefabric.models.NetworkRef
    :param destination_network: Network that the Application is using.
    :type destination_network: ~azure.servicefabric.models.NetworkRef
    :param tcp: Configuration for tcp connectivity for this gateway.
    :type tcp: list[~azure.servicefabric.models.TcpConfig]
    :param http: Configuration for http connectivity for this gateway.
    :type http: list[~azure.servicefabric.models.HttpConfig]
    :ivar status: Status of the resource. Possible values include: 'Unknown',
     'Ready', 'Upgrading', 'Creating', 'Deleting', 'Failed'
    :vartype status: str or ~azure.servicefabric.models.ResourceStatus
    :ivar status_details: Gives additional information about the current
     status of the gateway.
    :vartype status_details: str
    :ivar ip_address: IP address of the gateway. This is populated in the
     response and is ignored for incoming requests.
    :vartype ip_address: str
    """

    _validation = {
        'name': {'required': True},
        'source_network': {'required': True},
        'destination_network': {'required': True},
        'status': {'readonly': True},
        'status_details': {'readonly': True},
        'ip_address': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'source_network': {'key': 'properties.sourceNetwork', 'type': 'NetworkRef'},
        'destination_network': {'key': 'properties.destinationNetwork', 'type': 'NetworkRef'},
        'tcp': {'key': 'properties.tcp', 'type': '[TcpConfig]'},
        'http': {'key': 'properties.http', 'type': '[HttpConfig]'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'status_details': {'key': 'properties.statusDetails', 'type': 'str'},
        'ip_address': {'key': 'properties.ipAddress', 'type': 'str'},
    }

    def __init__(self, name, source_network, destination_network, description=None, tcp=None, http=None):
        super(GatewayResourceDescription, self).__init__()
        self.name = name
        self.description = description
        self.source_network = source_network
        self.destination_network = destination_network
        self.tcp = tcp
        self.http = http
        self.status = None
        self.status_details = None
        self.ip_address = None
