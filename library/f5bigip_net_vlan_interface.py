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
module: f5bigip_net_vlan_interface
short_description: BIG-IP net vlan interface module
description:
    - Configures a tagged or untagged interface and trunk for a VLAN.
version_added: "2.4"
author:
    - "Eric Jacob (@erjac77)"
options:
    app_service:
        description:
            - Specifies the application service that the object belongs to.
    description:
        description:
            - Specifies descriptive text that identifies the component.
    name:
        description:
            - Specifies unique name for the component.
        required: true
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        default: Common
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    tag_mode:
        description:
            - Specifies the tag mode of the interface or trunk associated with.
        choices: ['customer', 'service', 'double', 'none']
    tagged:
        description:
            - Specifies the type of the interface.
        choices: ['true', 'false']
    untagged:
        description:
            - Specifies the type of the interface.
        choices: ['true', 'false']
    vlan:
        description:
            - Specifies the vlan in which the interface belongs.
        required: true
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Add NET VLAN Interface
  f5bigip_net_vlan_interface:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: 1.1
    partition: Common
    vlan: internal
    untagged: true
    state: present
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_NET_VLAN_INTERFACE_ARGS = dict(
    app_service =   dict(type='str'),
    description =   dict(type='str'),
    tag_mode    =   dict(type='str', choices=['customer', 'service', 'double', 'none']),
    tagged      =   dict(type='bool'),
    untagged    =   dict(type='bool'),
    vlan        =   dict(type='str', required=True)
)

class F5BigIpNetVlanInterface(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.vlan = self.mgmt_root.tm.net.vlans.vlan.load(
            name=self.params['vlan'],
            partition=self.params['partition']
        )
        self.methods = {
            'create':   self.vlan.interfaces_s.interfaces.create,
            'read':     self.vlan.interfaces_s.interfaces.load,
            'update':   self.vlan.interfaces_s.interfaces.update,
            'delete':   self.vlan.interfaces_s.interfaces.delete,
            'exists':   self.vlan.interfaces_s.interfaces.exists
        }
        del self.params['vlan']
        del self.params['partition']

    def _exists(self):
        interfaces = self.vlan.interfaces_s.get_collection()
        for interface in interfaces:
            name = self.params['name']
            if interface.name == name:
                return True

        return False

    def _read(self):
        return self.methods['read'](
            name=self.params['name']
        )

def main():
    module = AnsibleModuleF5BigIpNamedObject(
        argument_spec=BIGIP_NET_VLAN_INTERFACE_ARGS,
        supports_check_mode=False,
        mutually_exclusive=[
            ['tagged', 'untagged']
        ]
    )

    try:
        obj = F5BigIpNetVlanInterface(check_mode=module.supports_check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

if __name__ == '__main__':
    main()