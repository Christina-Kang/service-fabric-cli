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


class ServiceTypeManifest(Model):
    """Contains the manifest describing a service type registered as part of an
    application in a Service Fabric cluster.

    :param manifest: The XML manifest as a string.
    :type manifest: str
    """

    _attribute_map = {
        'manifest': {'key': 'Manifest', 'type': 'str'},
    }

    def __init__(self, *, manifest: str=None, **kwargs) -> None:
        super(ServiceTypeManifest, self).__init__(**kwargs)
        self.manifest = manifest
