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
module: f5bigip_net_route
short_description: BIG-IP net route module
description:
    - Configures a route for traffic management.
version_added: "2.4"
author:
    - "Eric Jacob (@erjac77)"
options:
    blackhole:
        description:
            - Specifies that the system drops traffic that is addressed to the specified destination.
    description:
        description:
            - Specifies descriptive text that identifies the component.
    gw:
        description:
            - Specifies a gateway address for the system.
    interface:
        description:
            - Specifies the tunnel, VLAN or VLAN group to which the system sends traffic.
    mtu:
        description:
            - Sets a specific maximum transition unit (MTU).
    name:
        description:
            - Specifies unique name for the component.
        required: true
    network:
        description:
            - Specifies the destination subnet and mask using CIDR notation.
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        default: Common
    pool:
        description:
            - Specifies a pool to which the system sends traffic.
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
- name: Create NET Route
  f5bigip_net_route:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_route
    partition: Common
    network: 10.0.0.0/8
    gw: 10.10.20.1
    state: present
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_NET_ROUTE_ARGS = dict(
    blackhole   =   dict(type='bool'),
    description =   dict(type='str'),
    gw          =   dict(type='str'),
    interface   =   dict(type='str'),
    mtu         =   dict(type='int'),
    network     =   dict(type='str'),
    pool        =   dict(type='str')
)

class F5BigIpNetRoute(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.net.routes.route.create,
            'read':     self.mgmt_root.tm.net.routes.route.load,
            'update':   self.mgmt_root.tm.net.routes.route.update,
            'delete':   self.mgmt_root.tm.net.routes.route.delete,
            'exists':   self.mgmt_root.tm.net.routes.route.exists
        }

def main():
    module = AnsibleModuleF5BigIpNamedObject(
        argument_spec=BIGIP_NET_ROUTE_ARGS,
        supports_check_mode=False,
        mutually_exclusive=[
            ['blackhole', 'gw', 'interface', 'pool']
        ]
    )

    try:
        obj = F5BigIpNetRoute(check_mode=module.supports_check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

if __name__ == '__main__':
    main()