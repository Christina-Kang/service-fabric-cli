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

from .entity_health_state_py3 import EntityHealthState


class ServiceHealthState(EntityHealthState):
    """Represents the health state of a service, which contains the service
    identifier and its aggregated health state.

    :param aggregated_health_state: The health state of a Service Fabric
     entity such as Cluster, Node, Application, Service, Partition, Replica
     etc. Possible values include: 'Invalid', 'Ok', 'Warning', 'Error',
     'Unknown'
    :type aggregated_health_state: str or
     ~azure.servicefabric.models.HealthState
    :param service_name: Name of the service whose health state is represented
     by this object.
    :type service_name: str
    """

    _attribute_map = {
        'aggregated_health_state': {'key': 'AggregatedHealthState', 'type': 'str'},
        'service_name': {'key': 'ServiceName', 'type': 'str'},
    }

    def __init__(self, *, aggregated_health_state=None, service_name: str=None, **kwargs) -> None:
        super(ServiceHealthState, self).__init__(aggregated_health_state=aggregated_health_state, **kwargs)
        self.service_name = service_name