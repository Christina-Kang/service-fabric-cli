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

from .node_event import NodeEvent


class NodeHealthReportCreatedEvent(NodeEvent):
    """Node Health Report Created event.

    :param event_instance_id: The identifier for the FabricEvent instance.
    :type event_instance_id: str
    :param category: The category of event.
    :type category: str
    :param time_stamp: The time event was logged.
    :type time_stamp: datetime
    :param has_correlated_events: Shows there is existing related events
     available.
    :type has_correlated_events: bool
    :param kind: Constant filled by server.
    :type kind: str
    :param node_name: The name of a Service Fabric node.
    :type node_name: str
    :param node_instance_id: Id of Node instance.
    :type node_instance_id: long
    :param source_id: Id of report source.
    :type source_id: str
    :param property: Describes the property.
    :type property: str
    :param health_state: Describes the property health state.
    :type health_state: str
    :param time_to_live_ms: Time to live in milli-seconds.
    :type time_to_live_ms: long
    :param sequence_number: Sequence number of report.
    :type sequence_number: long
    :param description: Description of report.
    :type description: str
    :param remove_when_expired: Indicates the removal when it expires.
    :type remove_when_expired: bool
    :param source_utc_timestamp: Source time.
    :type source_utc_timestamp: datetime
    """

    _validation = {
        'event_instance_id': {'required': True},
        'time_stamp': {'required': True},
        'kind': {'required': True},
        'node_name': {'required': True},
        'node_instance_id': {'required': True},
        'source_id': {'required': True},
        'property': {'required': True},
        'health_state': {'required': True},
        'time_to_live_ms': {'required': True},
        'sequence_number': {'required': True},
        'description': {'required': True},
        'remove_when_expired': {'required': True},
        'source_utc_timestamp': {'required': True},
    }

    _attribute_map = {
        'event_instance_id': {'key': 'EventInstanceId', 'type': 'str'},
        'category': {'key': 'Category', 'type': 'str'},
        'time_stamp': {'key': 'TimeStamp', 'type': 'iso-8601'},
        'has_correlated_events': {'key': 'HasCorrelatedEvents', 'type': 'bool'},
        'kind': {'key': 'Kind', 'type': 'str'},
        'node_name': {'key': 'NodeName', 'type': 'str'},
        'node_instance_id': {'key': 'NodeInstanceId', 'type': 'long'},
        'source_id': {'key': 'SourceId', 'type': 'str'},
        'property': {'key': 'Property', 'type': 'str'},
        'health_state': {'key': 'HealthState', 'type': 'str'},
        'time_to_live_ms': {'key': 'TimeToLiveMs', 'type': 'long'},
        'sequence_number': {'key': 'SequenceNumber', 'type': 'long'},
        'description': {'key': 'Description', 'type': 'str'},
        'remove_when_expired': {'key': 'RemoveWhenExpired', 'type': 'bool'},
        'source_utc_timestamp': {'key': 'SourceUtcTimestamp', 'type': 'iso-8601'},
    }

    def __init__(self, event_instance_id, time_stamp, node_name, node_instance_id, source_id, property, health_state, time_to_live_ms, sequence_number, description, remove_when_expired, source_utc_timestamp, category=None, has_correlated_events=None):
        super(NodeHealthReportCreatedEvent, self).__init__(event_instance_id=event_instance_id, category=category, time_stamp=time_stamp, has_correlated_events=has_correlated_events, node_name=node_name)
        self.node_instance_id = node_instance_id
        self.source_id = source_id
        self.property = property
        self.health_state = health_state
        self.time_to_live_ms = time_to_live_ms
        self.sequence_number = sequence_number
        self.description = description
        self.remove_when_expired = remove_when_expired
        self.source_utc_timestamp = source_utc_timestamp
        self.kind = 'NodeNewHealthReport'
