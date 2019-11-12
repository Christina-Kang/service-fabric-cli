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

from .service_update_description_py3 import ServiceUpdateDescription


class StatelessServiceUpdateDescription(ServiceUpdateDescription):
    """Describes an update for a stateless service.

    All required parameters must be populated in order to send to Azure.

    :param flags: Flags indicating whether other properties are set. Each of
     the associated properties corresponds to a flag, specified below, which,
     if set, indicate that the property is specified.
     This property can be a combination of those flags obtained using bitwise
     'OR' operator.
     For example, if the provided value is 6 then the flags for
     ReplicaRestartWaitDuration (2) and QuorumLossWaitDuration (4) are set.
     - None - Does not indicate any other properties are set. The value is
     zero.
     - TargetReplicaSetSize/InstanceCount - Indicates whether the
     TargetReplicaSetSize property (for Stateful services) or the InstanceCount
     property (for Stateless services) is set. The value is 1.
     - ReplicaRestartWaitDuration - Indicates the ReplicaRestartWaitDuration
     property is set. The value is  2.
     - QuorumLossWaitDuration - Indicates the QuorumLossWaitDuration property
     is set. The value is 4.
     - StandByReplicaKeepDuration - Indicates the StandByReplicaKeepDuration
     property is set. The value is 8.
     - MinReplicaSetSize - Indicates the MinReplicaSetSize property is set. The
     value is 16.
     - PlacementConstraints - Indicates the PlacementConstraints property is
     set. The value is 32.
     - PlacementPolicyList - Indicates the ServicePlacementPolicies property is
     set. The value is 64.
     - Correlation - Indicates the CorrelationScheme property is set. The value
     is 128.
     - Metrics - Indicates the ServiceLoadMetrics property is set. The value is
     256.
     - DefaultMoveCost - Indicates the DefaultMoveCost property is set. The
     value is 512.
     - ScalingPolicy - Indicates the ScalingPolicies property is set. The value
     is 1024.
     - ServicePlacementTimeLimit - Indicates the ServicePlacementTimeLimit
     property is set. The value is 2048.
     - MinInstanceCount - Indicates the MinInstanceCount property is set. The
     value is 4096.
     - MinInstancePercentage - Indicates the MinInstancePercentage property is
     set. The value is 8192.
    :type flags: str
    :param placement_constraints: The placement constraints as a string.
     Placement constraints are boolean expressions on node properties and allow
     for restricting a service to particular nodes based on the service
     requirements. For example, to place a service on nodes where NodeType is
     blue specify the following: "NodeColor == blue)".
    :type placement_constraints: str
    :param correlation_scheme: The correlation scheme.
    :type correlation_scheme:
     list[~azure.servicefabric.models.ServiceCorrelationDescription]
    :param load_metrics: The service load metrics.
    :type load_metrics:
     list[~azure.servicefabric.models.ServiceLoadMetricDescription]
    :param service_placement_policies: The service placement policies.
    :type service_placement_policies:
     list[~azure.servicefabric.models.ServicePlacementPolicyDescription]
    :param default_move_cost: The move cost for the service. Possible values
     include: 'Zero', 'Low', 'Medium', 'High', 'VeryHigh'
    :type default_move_cost: str or ~azure.servicefabric.models.MoveCost
    :param scaling_policies: Scaling policies for this service.
    :type scaling_policies:
     list[~azure.servicefabric.models.ScalingPolicyDescription]
    :param service_kind: Required. Constant filled by server.
    :type service_kind: str
    :param instance_count: The instance count.
    :type instance_count: int
    :param min_instance_count: MinInstanceCount is the minimum number of
     instances that must be up to meet the EnsureAvailability safety check
     during operations like upgrade or deactivate node.
     The actual number that is used is max( MinInstanceCount, ceil(
     MinInstancePercentage/100.0 * InstanceCount) ).
     Note, if InstanceCount is set to -1, during MinInstanceCount computation
     -1 is first converted into the number of nodes on which the instances are
     allowed to be placed according to the placement constraints on the
     service.
    :type min_instance_count: int
    :param min_instance_percentage: MinInstancePercentage is the minimum
     percentage of InstanceCount that must be up to meet the EnsureAvailability
     safety check during operations like upgrade or deactivate node.
     The actual number that is used is max( MinInstanceCount, ceil(
     MinInstancePercentage/100.0 * InstanceCount) ).
     Note, if InstanceCount is set to -1, during MinInstancePercentage
     computation, -1 is first converted into the number of nodes on which the
     instances are allowed to be placed according to the placement constraints
     on the service.
    :type min_instance_percentage: int
    """

    _validation = {
        'service_kind': {'required': True},
        'instance_count': {'minimum': -1},
    }

    _attribute_map = {
        'flags': {'key': 'Flags', 'type': 'str'},
        'placement_constraints': {'key': 'PlacementConstraints', 'type': 'str'},
        'correlation_scheme': {'key': 'CorrelationScheme', 'type': '[ServiceCorrelationDescription]'},
        'load_metrics': {'key': 'LoadMetrics', 'type': '[ServiceLoadMetricDescription]'},
        'service_placement_policies': {'key': 'ServicePlacementPolicies', 'type': '[ServicePlacementPolicyDescription]'},
        'default_move_cost': {'key': 'DefaultMoveCost', 'type': 'str'},
        'scaling_policies': {'key': 'ScalingPolicies', 'type': '[ScalingPolicyDescription]'},
        'service_kind': {'key': 'ServiceKind', 'type': 'str'},
        'instance_count': {'key': 'InstanceCount', 'type': 'int'},
        'min_instance_count': {'key': 'MinInstanceCount', 'type': 'int'},
        'min_instance_percentage': {'key': 'MinInstancePercentage', 'type': 'int'},
    }

    def __init__(self, *, flags: str=None, placement_constraints: str=None, correlation_scheme=None, load_metrics=None, service_placement_policies=None, default_move_cost=None, scaling_policies=None, instance_count: int=None, min_instance_count: int=None, min_instance_percentage: int=None, **kwargs) -> None:
        super(StatelessServiceUpdateDescription, self).__init__(flags=flags, placement_constraints=placement_constraints, correlation_scheme=correlation_scheme, load_metrics=load_metrics, service_placement_policies=service_placement_policies, default_move_cost=default_move_cost, scaling_policies=scaling_policies, **kwargs)
        self.instance_count = instance_count
        self.min_instance_count = min_instance_count
        self.min_instance_percentage = min_instance_percentage
        self.service_kind = 'Stateless'
