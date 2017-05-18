#!/usr/bin/python
#
# Copyright 2016, Eric Jacob <erjac77@gmail.com>
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

DOCUMENTATION = '''
---
module: f5bigip_net_arp
short_description: BIG-IP net arp module
description:
    - You can use the arp component to add entries to or delete entries from the ARP table.
version_added: 2.3
author:
    - "Gabriel Fortin"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    description:
        description:
            - Specifies descriptive text that identifies the component.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    ip_address:
        description:
            - Specifies the IP address.
        required: true
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    mac_address:
        description:
            - Specifies a 6-byte ethernet address in not case-sensitive hexadecimal colon notation.
        required: true
        default: null
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
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        required: false
        default: present
        choices: ['absent', 'present']
        aliases: []
        version_added: 2.3
'''

EXAMPLES = '''
- name: Create NET ARP
  f5bigip_net_arp:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_net_arp
    partition: Common
    ip_address: 10.10.10.20
    mac_address: 00:0b:09:88:00:9a
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_NET_ARP_ARGS = dict(
    description     =   dict(type='str'),
    ip_address      =   dict(type='str'),
    mac_address     =   dict(type='str')
)

class F5BigIpNetArp(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.net.arps.arp.create,
            'read':     self.mgmt_root.tm.net.arps.arp.load,
            'update':   self.mgmt_root.tm.net.arps.arp.update,
            'delete':   self.mgmt_root.tm.net.arps.arp.delete,
            'exists':   self.mgmt_root.tm.net.arps.arp.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}
    
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_NET_ARP_ARGS, supports_check_mode=False)
    
    try:
        obj = F5BigIpNetArp(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()