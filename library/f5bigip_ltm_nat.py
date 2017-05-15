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
module: f5bigip_ltm_nat
short_description: BIG-IP LTM NAT module
description:
    - A network address translation (NAT) defines a mapping between an originating IP address and an IP address that you specify.
version_added: 2.3
author:
    - "Gabriel Fortin"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    app_service:
        description:
            - Specifies the name of the application service to which the NAT belongs.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    arp:
        description:
            - Enables or disables Address Resolution Protocol (ARP).
        required: false
        default: null
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    auto_lasthop:
        description:
            - When enabled, allows the system to send return traffic to the MAC address that transmitted the request, even if the routing table points to a different network or interface.
        required: false
        default: null
        choices: ['default, 'enabled', 'disabled']
        aliases: []
        version_added: 2.3
    description:
        description:
            - Specifies a user-defined description.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    disabled:
        description:
            - Enables or disables the specified interface.
        required: false
        default: disabled
        choices: null
        aliases: []
        version_added: 2.3
    enabled:
        description:
            - Enables or disables the specified interface.
        required: false
        default: enabled
        choices: null
        aliases: []
        version_added: 2.
    name:
        description:
            - Specifies unique name for the component.
        required: true
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    originating_address:
        description:
            - Specifies the IP address from which traffic is being initiated.
        required: false
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
            - Specifies the traffic group of the failover device group on which the NAT is active.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    translation_address:
        description:
            - Specifies the IP address that is translated or mapped, and the IP address to which it is translated or mapped.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    vlans:
        description:
            - Specifies a list of existing VLANs on which access to the NAT is enabled or disabled.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    vlans_disabled:
        description:
            - Indicates the NAT is disabled on the list of VLANs.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    vlans_enabled:
        description:
            - Indicates the NAT is enabled on the list of VLANs.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
'''

EXAMPLES = '''
- name: Create LTM NAT
  f5bigip_ltm_nat:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_nat
    partition: Common
    description: My nat
    originating_address : 10,0.1.43
    translation_address: 10.10.10.253
    vlans_enabled: true
    vlans: net1
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_LTM_NAT_ARGS = dict(
    app_service             =   dict(type='str'),
    arp                     =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    auto_lasthop            =   dict(type='str', choices=['default', 'enabled', 'disabled']),
    description             =   dict(type='str'),
    disabled                =   dict(type='bool'),
    enabled                 =   dict(type='bool'),
    originating_address     =   dict(type='str'),
    traffic_group           =   dict(type='str'),
    translation_address     =   dict(type='str'),
    vlans                   =   dict(type='list'),
    vlans_disabled          =   dict(type='bool'),
    vlans_enabled           =   dict(type='bool')
)

class F5BigIpLtmNat(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.nats.nat.create,
            'read':     self.mgmt_root.tm.ltm.nats.nat.load,
            'update':   self.mgmt_root.tm.ltm.nats.nat.update,
            'delete':   self.mgmt_root.tm.ltm.nats.nat.delete,
            'exists':   self.mgmt_root.tm.ltm.nats.nat.exists
        }

def main():
    # Translation list for conflictual params
    tr = { }
    
    module = AnsibleModuleF5BigIpNamedObject(
        argument_spec=BIGIP_LTM_NAT_ARGS, 
        supports_check_mode=False,
        mutually_exclusive=[
            ['enabled', 'disabled'], ['vlans_disabled', 'vlans_enabled']
        ]
    )
    
    try:
        obj = F5BigIpLtmNat(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()