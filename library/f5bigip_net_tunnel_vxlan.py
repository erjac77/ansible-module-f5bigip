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
module: f5bigip_net_tunnel_vxlan
short_description: BIG-IP net tunnel vxlan module
description:
    - Configures a VXLAN profile.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    app_service:
        description:
            - Specifies the name of the application service to which the object belongs.
    defaults_from:
        description:
            - Specifies the existing profile from which the system imports settings for the new profile.
        default: vxlan
    description:
        description:
            - User defined description.
    flooding_type:
        description:
            - Specifies the flooding type to use to transmit multicast, broadcast and unknown destination frames.
        default: multicast
        choices: ['none', 'multicast', 'multipoint']
    name:
        description:
            - Specifies a unique name for the component.
        required: true
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        default: Common
    port:
        description:
            - Specifies the local port for receiving VXLAN packets.
        default: 4789
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Create NET Tunnel Vxlan
  f5bigip_net_tunnel_vxlan:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_vxlan_tunnel
    partition: Common
    description: My vxlan tunnel
    state: present
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_NET_TUNNEL_VXLAN_ARGS = dict(
    app_service      =    dict(type='str'),
    defaults_from    =    dict(type='str'),
    description      =    dict(type='str'),
    flooding_type    =    dict(type='str', choices=['none', 'multicast', 'multipoint']),
    port             =    dict(type='int')
)

class F5BigIpNetTunnelVxlan(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.net.tunnels.vxlans.vxlan.create,
            'read':     self.mgmt_root.tm.net.tunnels.vxlans.vxlan.load,
            'update':   self.mgmt_root.tm.net.tunnels.vxlans.vxlan.update,
            'delete':   self.mgmt_root.tm.net.tunnels.vxlans.vxlan.delete,
            'exists':   self.mgmt_root.tm.net.tunnels.vxlans.vxlan.exists
        }

def main():
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_NET_TUNNEL_VXLAN_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpNetTunnelVxlan(check_mode=module.supports_check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

if __name__ == '__main__':
    main()