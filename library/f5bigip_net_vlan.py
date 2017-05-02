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
module: f5bigip_net_vlan
short_description: BIG-IP net vlan module
description:
    - Configures a virtual local area network (VLAN).
version_added: 2.3
author:
    - "Eric Jacob, @erjac77"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    app_service:
        description:
            - Specifies the application service that the object belongs to.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    auto_lasthop:
        description:
            - Specifies whether auto lasthop is enabled or not.
        default: default
        choices: ['default', 'enabled', 'disabled']
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
    failsafe:
        description:
            - Enables a fail-safe mechanism that causes the active cluster to fail over to a redundant cluster when loss of traffic is detected on a VLAN.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    failsafe_action:
        description:
            - Specifies the action for the system to take when the fail-safe mechanism is triggered.
        required: false
        default: failover-restart-tm
        choices: ['failover', 'failover-restart-tm', 'reboot', 'restart-all']
        aliases: []
        version_added: 2.3
    failsafe_timeout:
        description:
            - Specifies the number of seconds that an active unit can run without detecting network traffic on this VLAN before it starts a failover.
        required: false
        default: 90
        choices: []
        aliases: []
        version_added: 2.3
    learning:
        description:
            - Specifies whether switch ports placed in the VLAN are configured for switch learning, forwarding only, or dropped.
        required: false
        default: enable-forward
        choices: ['disable-drop', 'disable-forward', 'enable-forward']
        aliases: []
        version_added: 2.3
    mtu:
        description:
            - Sets a specific maximum transition unit (MTU) for the VLAN.
        required: false
        default: 1500
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
    source-checking:
        description:
            - Specifies that only connections that have a return route in the routing table are accepted.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
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
    tag:
        description:
            - Specifies a number that the system adds into the header of any frame passing through the VLAN.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    customer_tag:
        description:
            - Specifies a number that the system adds into the header of any double tagged frame passing through the VLAN.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    cmp_hash:
        description:
            - Specifies how the traffic on the VLAN will be disaggregated.
        required: false
        default: default
        choices: ['default', 'dst-ip', 'src-ip']
        aliases: []
        version_added: 2.3
    dag_tunnel:
        description:
            - Specifies whether the ip tunnel traffic on the VLAN should be disaggregated based on the inner ip header or outer ip header.
        required: false
        default: null
        choices: ['outer', 'inner']
        aliases: []
        version_added: 2.3
    dag_round_robin:
        description:
            - Specifies whether some of the stateless traffic on the VLAN should be disaggregated in a round-robin order instead of using static hash.
        required: false
        default: null
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
'''

EXAMPLES = '''
- name: Create NET VLAN
  f5bigip_net_vlan:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: internal
    partition: Common
    tag: 10
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_NET_VLAN_ARGS = dict(
    app_service         =   dict(type='str'),
    auto_lasthop        =   dict(type='str', choices=['default', 'enabled', 'disabled']),
    description         =   dict(type='str'),
    failsafe            =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    failsafe_action     =   dict(type='str', choices=['failover', 'failover-restart-tm', 'reboot', 'restart-all']),
    failsafe_timeout    =   dict(type='int'),
    learning            =   dict(type='str', choices=['disable-drop', 'disable-forward', 'enable-forward']),
    mtu                 =   dict(type='int'),
    #sflow               =   dict(type='list'),
    source_checking     =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    tag                 =   dict(type='int'),
    customer_tag        =   dict(type='str'),
    cmp_hash            =   dict(type='str', choices=['default', 'dst-ip', 'src-ip']),
    dag_tunnel          =   dict(type='str', choices=['outer', 'inner']),
    dag_round_robin     =   dict(type='str', choices=F5_ACTIVATION_CHOICES)
)

class F5BigIpNetVlan(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.net.vlans.vlan.create,
            'read':     self.mgmt_root.tm.net.vlans.vlan.load,
            'update':   self.mgmt_root.tm.net.vlans.vlan.update,
            'delete':   self.mgmt_root.tm.net.vlans.vlan.delete,
            'exists':   self.mgmt_root.tm.net.vlans.vlan.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}
    
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_NET_VLAN_ARGS, supports_check_mode=False)
    
    try:
        obj = F5BigIpNetVlan(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':  
    main()