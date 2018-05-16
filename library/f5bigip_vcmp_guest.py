#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2016-2018, Eric Jacob <erjac77@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: f5bigip_vcmp_guest
short_description: BIG-IP vcmp guest module
description:
    - Configures a cluster of virtual machines (VMs) that run on one or all slots.
version_added: "2.4"
author:
    - "Eric Jacob (@erjac77)"
options:
    allowed_slots:
        description:
            - Specifies the list of slots that the guest is allowed to be assigned to.
    app_service:
        description:
            - Specifies the name of the application service to which the guest belongs.
    capabilities:
        description:
            - This list contains the various capability flags and an optional value associated with the guest.
    cores_per_slot:
        description:
            - Specifies the number of cores that should be allocated to this guest on each slot that the guest has been
              assigned to.
    hostname:
        description:
            - The FQDN to assign to the guest.
    initial_hotfix:
        description:
            - Specifies which hotfix image to install on newly created virtual disks for this guest.
    initial_image:
        description:
            - Specifies which software image to install on newly created virtual disks for this guest.
    management_gw:
        description:
            - Specifies the IP address of the default gateway for the management network.
    management_ip:
        description:
            - Specifies the management IP address and netmask to assign to the guest.
    management_network:
        description:
            - Specifies the management network mode for this guest.
        default: bridged
        choices: ['bridged', 'isolated']
    min_slots:
        description:
            - Specifies the minimum number of slots that the guest must be assigned to.
        default: 1
    name:
        description:
            - Specifies unique name for the component.
        required: true
    slots:
        description:
            - Specifies the number of slots to which this guest should be assigned.
        default: 1
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    state_guest:
        description:
            - Specifies the state of the guest.
        default: configured
        choices: ['configured', 'provisioned', 'deployed']
    traffic_profile:
        description:
            - Specifies a traffic-profile to be used in defining characteristics of traffic which transits the guest's
              data-plane.
    virtual_disk:
        description:
            - Specifies the filename of the virtual disk to use for this guest's VMs.
    vlans:
        description:
            - The VLANs that should be passed to the host. The guest will be able to use these VLANs to pass traffic.
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Create vCMP Guest
  f5bigip_vcmp_guest:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_guest
    hostname: my_guest.localhost
    slots: 2
    min_slots: 2
    cores_per_slot: 2
    management_ip: 10.0.2.15/24
    management_gw: 10.0.2.1
    initial_image: BIGIP-12.1.2.0.0.249.iso
    state_guest: deployed
    state: present
  delegate_to: localhost
'''

RETURN = ''' # '''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.base import F5_NAMED_OBJ_ARGS
from ansible_common_f5.base import F5_PROVIDER_ARGS
from ansible_common_f5.bigip import F5BigIpNamedObject


class ModuleParams(object):
    @property
    def argument_spec(self):
        argument_spec = dict(
            allowed_slots=dict(type='list'),
            app_service=dict(type='str'),
            capabilities=dict(type='list'),
            cores_per_slot=dict(type='int'),
            hostname=dict(type='str'),
            initial_hotfix=dict(type='str'),
            initial_image=dict(type='str'),
            management_gw=dict(type='str'),
            management_ip=dict(type='str'),
            management_network=dict(type='str', choices=['bridged', 'isolated']),
            min_slots=dict(type='int'),
            slots=dict(type='int'),
            state_guest=dict(type='str', choices=['configured', 'provisioned', 'deployed']),
            traffic_profile=dict(type='str'),
            virtual_disk=dict(type='str'),
            vlans=dict(type='list')
        )
        argument_spec.update(F5_PROVIDER_ARGS)
        argument_spec.update(F5_NAMED_OBJ_ARGS)
        del argument_spec['partition']
        return argument_spec

    @property
    def supports_check_mode(self):
        return True

    @property
    def tr(self):
        # Translation dict for conflictual params
        return {'state_guest': 'state'}


class F5BigIpVcmpGuest(F5BigIpNamedObject):
    def _set_crud_methods(self):
        self._methods = {
            'create': self._api.tm.vcmp.guests.guest.create,
            'read': self._api.tm.vcmp.guests.guest.load,
            'update': self._api.tm.vcmp.guests.guest.update,
            'delete': self._api.tm.vcmp.guests.guest.delete,
            'exists': self._api.tm.vcmp.guests.guest.exists
        }


def main():
    params = ModuleParams()
    module = AnsibleModule(argument_spec=params.argument_spec, supports_check_mode=params.supports_check_mode)

    try:
        obj = F5BigIpVcmpGuest(check_mode=module.check_mode, tr=params.tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
