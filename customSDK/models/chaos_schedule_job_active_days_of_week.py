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


class ChaosScheduleJobActiveDaysOfWeek(Model):
    """Defines the days of the week that a Chaos Schedule Job will run for.

    :param sunday: Indicates if the Chaos Schedule Job will run on Sunday.
     Default value: False .
    :type sunday: bool
    :param monday: Indicates if the Chaos Schedule Job will run on Monday.
     Default value: False .
    :type monday: bool
    :param tuesday: Indicates if the Chaos Schedule Job will run on Tuesday.
     Default value: False .
    :type tuesday: bool
    :param wednesday: Indicates if the Chaos Schedule Job will run on
     Wednesday. Default value: False .
    :type wednesday: bool
    :param thursday: Indicates if the Chaos Schedule Job will run on Thursday.
     Default value: False .
    :type thursday: bool
    :param friday: Indicates if the Chaos Schedule Job will run on Friday.
     Default value: False .
    :type friday: bool
    :param saturday: Indicates if the Chaos Schedule Job will run on Saturday.
     Default value: False .
    :type saturday: bool
    """

    _attribute_map = {
        'sunday': {'key': 'Sunday', 'type': 'bool'},
        'monday': {'key': 'Monday', 'type': 'bool'},
        'tuesday': {'key': 'Tuesday', 'type': 'bool'},
        'wednesday': {'key': 'Wednesday', 'type': 'bool'},
        'thursday': {'key': 'Thursday', 'type': 'bool'},
        'friday': {'key': 'Friday', 'type': 'bool'},
        'saturday': {'key': 'Saturday', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(ChaosScheduleJobActiveDaysOfWeek, self).__init__(**kwargs)
        self.sunday = kwargs.get('sunday', False)
        self.monday = kwargs.get('monday', False)
        self.tuesday = kwargs.get('tuesday', False)
        self.wednesday = kwargs.get('wednesday', False)
        self.thursday = kwargs.get('thursday', False)
        self.friday = kwargs.get('friday', False)
        self.saturday = kwargs.get('saturday', False)
