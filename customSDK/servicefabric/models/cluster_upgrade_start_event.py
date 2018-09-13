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

from .cluster_event import ClusterEvent


class ClusterUpgradeStartEvent(ClusterEvent):
    """Cluster Upgrade Start event.

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
    :param current_cluster_version: Current Cluster version.
    :type current_cluster_version: str
    :param target_cluster_version: Target Cluster version.
    :type target_cluster_version: str
    :param upgrade_type: Type of upgrade.
    :type upgrade_type: str
    :param rolling_upgrade_mode: Mode of upgrade.
    :type rolling_upgrade_mode: str
    :param failure_action: Action if failed.
    :type failure_action: str
    """

    _validation = {
        'event_instance_id': {'required': True},
        'time_stamp': {'required': True},
        'kind': {'required': True},
        'current_cluster_version': {'required': True},
        'target_cluster_version': {'required': True},
        'upgrade_type': {'required': True},
        'rolling_upgrade_mode': {'required': True},
        'failure_action': {'required': True},
    }

    _attribute_map = {
        'event_instance_id': {'key': 'EventInstanceId', 'type': 'str'},
        'category': {'key': 'Category', 'type': 'str'},
        'time_stamp': {'key': 'TimeStamp', 'type': 'iso-8601'},
        'has_correlated_events': {'key': 'HasCorrelatedEvents', 'type': 'bool'},
        'kind': {'key': 'Kind', 'type': 'str'},
        'current_cluster_version': {'key': 'CurrentClusterVersion', 'type': 'str'},
        'target_cluster_version': {'key': 'TargetClusterVersion', 'type': 'str'},
        'upgrade_type': {'key': 'UpgradeType', 'type': 'str'},
        'rolling_upgrade_mode': {'key': 'RollingUpgradeMode', 'type': 'str'},
        'failure_action': {'key': 'FailureAction', 'type': 'str'},
    }

    def __init__(self, event_instance_id, time_stamp, current_cluster_version, target_cluster_version, upgrade_type, rolling_upgrade_mode, failure_action, category=None, has_correlated_events=None):
        super(ClusterUpgradeStartEvent, self).__init__(event_instance_id=event_instance_id, category=category, time_stamp=time_stamp, has_correlated_events=has_correlated_events)
        self.current_cluster_version = current_cluster_version
        self.target_cluster_version = target_cluster_version
        self.upgrade_type = upgrade_type
        self.rolling_upgrade_mode = rolling_upgrade_mode
        self.failure_action = failure_action
        self.kind = 'ClusterUpgradeStarted'