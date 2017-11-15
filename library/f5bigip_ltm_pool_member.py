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
module: f5bigip_ltm_pool_member
short_description: BIG-IP ltm pool member module
description:
    - Configures a set of pool members.
version_added: "2.4"
author:
    - "Eric Jacob (@erjac77)"
options:
    address:
        description:
            - Specifies the IP address of a pool member if a node by the name specified does not already exist.
    app_service:
        description:
            - Specifies the application service to which the object belongs.
    connection_limit:
        description:
            - Specifies the maximum number of concurrent connections allowed for a pool member.
        default: 0
    description:
        description:
            - Specifies descriptive text that identifies the component.
    dynamic_ratio:
        description:
            - Specifies a range of numbers that you want the system to use in conjunction with the ratio load balancing method.
        default: 1
    inherit-profile
        description:
            - Specifies whether the pool member inherits the encapsulation profile from the parent pool.
        default: enabled
        choices: ['enabled', 'disabled']
    logging:
        description:
            - Specifies whether the monitor applied should log its actions.
        default: disabled
        choices: ['enabled', 'disabled']
    monitor:
        description:
            - Specifies the health monitors that are configured to monitor the pool member.
        default: default
    name:
        description:
            - Specifies unique name for the component.
        required: true
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        default: Common
    pool:
        description:
            - Specifies the pool in which the member belongs.
        default: Common
    priority-group
        description:
            - Specifies the priority group within the pool for this pool member.
        default: 0
    rate_limit:
        description:
            - Specifies the maximum number of connections per second allowed for a pool member.
        default: disabled or 0
    ratio:
        description:
            - Specifies the weight of the pool member for load balancing purposes.
        default: 1
    session:
        description:
            - Specifies the ability of the client to persist to the pool member when making new connections.
        default: user-enabled
        choices: ['user-enabled', 'user-disabled']
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    state_user:
        description:
            - Specifies the current state of the node.
        default: user-up
        choices: ['user-down', 'user-up']
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Add LTM Pool Member
  f5bigip_ltm_pool_member:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_member1:80
    partition: Common
    address: 10.10.10.101
    pool: my_pool
    state: present
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_LTM_POOL_MEMBER_ARGS = dict(
    address             =   dict(type='str'),
    app_service         =   dict(type='str'),
    connection_limit    =   dict(type='int'),
    description         =   dict(type='str'),
    dynamic_ratio       =   dict(type='int'),
    fqdn                =   dict(type='dict'),
    inherit_profile     =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    logging             =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    monitor             =   dict(type='str'),
    pool                =   dict(type='str'),
    priority_group      =   dict(type='int'),
    profiles            =   dict(type='str'),
    rate_limit          =   dict(type='int'),
    ratio               =   dict(type='int'),
    session             =   dict(type='str', choices=['user-enabled', 'user-disabled']),
    state_user          =   dict(type='str', choices=['user-down', 'user-up'])
)

class F5BigIpLtmPoolMember(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.pool = self.mgmt_root.tm.ltm.pools.pool.load(**self._get_resource_id_from_path(self.params['pool']))
        self.methods = {
            'create':   self.pool.members_s.members.create,
            'read':     self.pool.members_s.members.load,
            'update':   self.pool.members_s.members.update,
            'delete':   self.pool.members_s.members.delete,
            'exists':   self.pool.members_s.members.exists
        }
        del self.params['pool']

def main():
    # Translation list for conflictual params
    tr = { 'state_user':'state' }

    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_POOL_MEMBER_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpLtmPoolMember(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

if __name__ == '__main__':
    main()