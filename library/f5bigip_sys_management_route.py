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
module: f5bigip_sys_management_route
short_description: BIG-IP SYS provision module
description:
    - Configures route settings for the management interface (MGMT).
version_added: "2.4"
author:
    - "Eric Jacob (@erjac77)"
options:
    description:
        description:
            - User defined description.
    gateway:
        description:
            - Specifies that the system forwards packets to the destination through the gateway with the specified IP address.
    mtu:
        description:
            - Specifies the maximum transmission unit (MTU) for the management interface.
    name:
        description:
            - Specifies a unique name for the component.
        required: true
    network:
        description:
            - The subnet and netmask to be used for the route.
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Sets the management interface default gateway IP address
  f5bigip_sys_management_route:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: default
    gateway: 10.10.10.254
    state: present
  delegate_to: localhost

- name: Creates a management route
  f5bigip_sys_management_route:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_mgmt_route
    network: 10.10.20.0/24
    gateway: 10.10.10.254
    state: present
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_SYS_MANAGEMENT_ROUTE_ARGS = dict(
    description     =   dict(type='str'),
    gateway         =   dict(type='str'),
    mtu             =   dict(type='int'),
    network         =   dict(type='str')
)

class F5BigIpSysManagementRoute(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.sys.management_routes.management_route.create,
            'read':     self.mgmt_root.tm.sys.management_routes.management_route.load,
            'update':   self.mgmt_root.tm.sys.management_routes.management_route.update,
            'delete':   self.mgmt_root.tm.sys.management_routes.management_route.delete,
            'exists':   self.mgmt_root.tm.sys.management_routes.management_route.exists
        }
        del self.params['partition']
        del self.params['sub_path']

def main():
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_SYS_MANAGEMENT_ROUTE_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpSysManagementRoute(check_mode=module.supports_check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

if __name__ == '__main__':
    main()