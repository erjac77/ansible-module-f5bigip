#!/usr/bin/python
#
# Copyright 2016-2017, Eric Jacob <erjac77@gmail.com>
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
      *** IMPORTANT: THIS COMPONENT HAS NOT BEEN TESTED!! HELP WANTED! ***
version_added: "2.4"
author:
    - "Eric Jacob (@erjac77)"
options:
    allowed_slots:
        description:
            - Specifies the list of slots that the guest is allowed to be assigned to.
    app_service:
        description:
            - The application service that the object belongs to.
    cores_per_slot:
        description:
            - Specifies the number of cores that should be allocated to this guest on each slot that the guest has been assigned to.
    hostname:
        description:
            - The FQDN to assign to the guest.
    initial_hotfix:
        description:
            - The hotfix image to install onto any of this guest's newly created virtual disks.
    initial_image:
        description:
            - The software image to install onto any of this guest's newly created virtual disks.
    management_gw:
        description:
            - Management gateway IP address for the guest.
    management_ip:
        description:
            - Management IP address configuration for the guest.
    management_network:
        description:
            - Accessibility of this vCMP guest's management network.
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
            - Specifies the number of slots the guest should be assigned to.
        default: 1
    state:
        description:
            - Specifies the state of the guest.
        default: present
        choices: ['absent', 'present']
    state_guest:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: configured
        choices: ['configured', 'provisioned', 'deployed']
    virtual_disk:
        description:
            - The filename of the virtual disk to use for this guest.
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

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_VCMP_GUEST_ARGS = dict(
    allowed_slots       =   dict(type='list'),
    app_service         =   dict(type='str'),
    cores_per_slot      =   dict(type='int'),
    hostname            =   dict(type='str'),
    initial_hotfix      =   dict(type='str'),
    initial_image       =   dict(type='str'),
    management_ip       =   dict(type='str'),
    management_gw       =   dict(type='str'),
    management_network  =   dict(type='str', choices=['bridged', 'isolated']),
    min_slots           =   dict(type='int'),
    state_guest         =   dict(type='str', choices=['configured', 'provisioned', 'deployed']),
    slots               =   dict(type='int'),
    virtual_disk        =   dict(type='list'),
    vlans               =   dict(type='str')
)

class F5BigIpVcmpGuest(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.vcmp.guests.guest.create,
            'read':     self.mgmt_root.tm.vcmp.guests.guest.load,
            'update':   self.mgmt_root.tm.vcmp.guests.guest.update,
            'delete':   self.mgmt_root.tm.vcmp.guests.guest.delete,
            'exists':   self.mgmt_root.tm.vcmp.guests.guest.exists
        }
        del self.params['partition']

def main():
    # Translation list for conflictual params
    tr = { 'state_guest':'state' }

    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_VCMP_GUEST_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpVcmpGuest(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

if __name__ == '__main__':
    main()