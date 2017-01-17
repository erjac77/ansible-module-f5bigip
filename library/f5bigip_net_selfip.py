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
module: f5bigip_net_selfip
short_description: BIG-IP net selfip module
description:
    - Configures a self IP address for a VLAN.
version_added: 2.3
author:
    - "Eric Jacob, @erjac77"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    address [ip address/netmask]:
        description:
            - Specifies the IP address and netmask to be assigned to the system. Must appear in the format [ip address/mask].
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    allow_service:
        description:
            - Specifies the type of protocol/service that the VLAN handles.
        required: false
        default: none
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
    traffic_group:
        description:
            - Specifies the traffic group of the self IP address.
        required: false
        default: traffic-group-local-only
        choices: []
        aliases: []
        version_added: 2.3
    vlan:
        description:
            - Specifies the VLAN for which you are setting a self IP address.
        required: false
        default: traffic-group-local-only
        choices: []
        aliases: []
        version_added: 2.3
'''

EXAMPLES = '''
- name: Create NET Self IP
  f5bigip_net_selfip:
    f5bigip_hostname: 172.16.227.35
    f5bigip_username: admin
    f5bigip_password: admin
    f5bigip_port: 443
    name: my_self_ip
    address: 10.10.10.11/24
    vlan: internal
    state: present
  delegate_to: localhost
'''

from ansible_common_f5bigip.f5bigip import *

BIGIP_NET_SELFIP_ARGS = dict(
    address             =   dict(type='str'),
    allow_service       =   dict(type='list'),
    #app_service         =   dict(type='str'),
    description         =   dict(type='str'),
    #fw_enforced_policy  =   dict(type='str'),
    #fw_rules
    #fw_staged_policy    =   dict(type='str'),
    traffic_group       =   dict(type='str'),
    vlan                =   dict(type='str')
)

class F5BigIpNetSelfip(F5BigIpObject):
    def _set_crud_methods(self):
        self.methods = {
            'create':self.mgmt.tm.net.selfips.selfip.create,
            'read':self.mgmt.tm.net.selfips.selfip.load,
            'update':self.mgmt.tm.net.selfips.selfip.update,
            'delete':self.mgmt.tm.net.selfips.selfip.delete,
            'exists':self.mgmt.tm.net.selfips.selfip.exists
        }
    
    def _read(self):
        selfip = self.methods['read'](
            name=self.params['name'],
            partition=self.params['partition']
        )
        selfip.vlan = self._strip_partition(selfip.vlan)
        return selfip

def main():
    # Translation list for conflictual params
    tr = {}
    
    module = AnsibleModuleF5BigIpObject(argument_spec=BIGIP_NET_SELFIP_ARGS, supports_check_mode=False)
    
    try:
        obj = F5BigIpNetSelfip(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':  
    main()