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

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: f5bigip_ltm_virtual_address
short_description: BIG-IP ltm virtual address module
description:
    - Configures virtual addresses.
version_added: 2.3
author:
    - "Eric Jacob, @erjac77"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    address:
        description:
            - The virtual IP address.
        required: true
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    app_service:
        description:
            - Specifies the application service that the object belongs to.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    arp:
        description:
            - Enables or disables ARP for the specified virtual address.
        required: false
        default: enabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    auto_delete:
        description:
            - Indicates if the virtual address will be deleted automatically on deletion of the last associated virtual server or not.
        required: false
        default: true
        choices: [true, false]
        aliases: []
        version_added: 2.3
    connection_limit:
        description:
            - Sets a concurrent connection limit for one or more virtual servers.
        required: false
        default: 0 (meaning "no limit")
        choices: []
        aliases: []
        version_added: 2.3
    description:
        description:
            - Specifies descriptive text that identifies the component.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    enabled:
        description:
            - Specifies whether the specified virtual address is enabled.
        required: false
        default: yes
        choices: ['yes', 'no']
        aliases: []
        version_added: 2.3
    icmp_echo:
        description:
            - Enables or disables ICMP echo replies for the specified virtual address.
        required: false
        default: enabled
        choices: ['enabled', 'disabled', 'selective']
        aliases: []
        version_added: 2.3
    mask:
        description:
            - Sets the netmask for one or more network virtual servers only.
        required: false
        default: 255.255.255.255
        choices: []
        aliases: []
        version_added: 2.3
    name:
        description:
            - Specifies unique name for the component.
        required: true
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        required: false
        default: Common
        choices: []
        aliases: []
        version_added: 2.3
    route_advertisement:
        description:
            - Enables or disables route advertisement for the specified virtual address.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    server_scope:
        description:
            - Specifies the server that uses the specified virtual address.
        required: false
        default: any
        choices: ['all', 'any', 'none']
        aliases: []
        version_added: 2.3
    traffic_group:
        description:
            - Specifies the traffic group on which the virtual address is active.
        required: false
        default: Inherited from the containing folder
        choices: []
        aliases: []
        version_added: 2.3
'''

EXAMPLES = '''
- name: Modify LTM Virtual Address icmp-echo
  f5bigip_ltm_virtual_address:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: 10.10.20.201
    partition: Common
    icmp_echo: selective
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_LTM_VIRTUAL_ADDRESS_ARGS = dict(
    address             =   dict(type='str'),
    app_service         =   dict(type='str'),
    arp                 =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    auto_delete         =   dict(type='bool'),
    connection_limit    =   dict(type='int'),
    description         =   dict(type='str'),
    enable              =   dict(type='bool'),
    icmp_echo           =   dict(type='str', choices=['enabled', 'disabled', 'selective']),
    mask                =   dict(type='str'),
    #metadata            =   dict(type='list'),
    route_advertisement =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    server_scope        =   dict(type='str', choices=['all', 'any', 'none']),
    traffic_group       =   dict(type='str')
)

class F5BigIpLtmVirtualAddress(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.virtual_address_s.virtual_address.create,
            'read':     self.mgmt_root.tm.ltm.virtual_address_s.virtual_address.load,
            'update':   self.mgmt_root.tm.ltm.virtual_address_s.virtual_address.update,
            'delete':   self.mgmt_root.tm.ltm.virtual_address_s.virtual_address.delete,
            'exists':   self.mgmt_root.tm.ltm.virtual_address_s.virtual_address.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}
    
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_VIRTUAL_ADDRESS_ARGS, supports_check_mode=False)
    
    try:
        obj = F5BigIpLtmVirtualAddress(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()