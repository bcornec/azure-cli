# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
#pylint: skip-file
from msrest.serialization import Model


class LifetimeAction(Model):
    """Action and its trigger that will be performed by Key Vault over the
    lifetime of a certificate.

    :param trigger: The condition that will execute the action.
    :type trigger: :class:`Trigger <KeyVault.models.Trigger>`
    :param action: The action that will be executed.
    :type action: :class:`Action <KeyVault.models.Action>`
    """ 

    _attribute_map = {
        'trigger': {'key': 'trigger', 'type': 'Trigger'},
        'action': {'key': 'action', 'type': 'Action'},
    }

    def __init__(self, trigger=None, action=None):
        self.trigger = trigger
        self.action = action
