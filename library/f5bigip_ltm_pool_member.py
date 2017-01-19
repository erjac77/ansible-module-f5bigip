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
module: f5bigip_ltm_pool_member
short_description: BIG-IP ltm pool member module
description:
    - Configures a set of pool members.
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
            - Specifies the IP address of a pool member if a node by the name specified does not already exist.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    connection_limit:
        description:
            - Specifies the maximum number of concurrent connections allowed for a pool member.
        required: false
        default: 0
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
    dynamic_ratio:
        description:
            - Specifies a range of numbers that you want the system to use in conjunction with the ratio load balancing method.
        required: false
        default: 1
        choices: []
        aliases: []
        version_added: 2.3
    inherit-profile
        description:
            - Specifies whether the pool member inherits the encapsulation profile from the parent pool.
        required: false
        default: enabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    logging:
        description:
            - Specifies whether the monitor applied should log its actions.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    monitor:
        description:
            - Specifies the health monitors that are configured to monitor the pool member.
        required: false
        default: default
        choices: []
        aliases: []
        version_added: 2.3
    monitor_state:
        description:
            - Specifies the current state of the node.
        required: false
        default: user-up
        choices: ['user-down', 'user-up']
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
    pool:
        description:
            - Specifies the pool in which the member belongs.
        required: false
        default: Common
        choices: []
        aliases: []
        version_added: 2.3
    priority-group
        description:
            - Specifies the priority group within the pool for this pool member.
        required: false
        default: 0
        choices: []
        aliases: []
        version_added: 2.3
    rate_limit:
        description:
            - Specifies the maximum number of connections per second allowed for a pool member.
        required: false
        default: disabled or 0
        choices: []
        aliases: []
        version_added: 2.3
    ratio:
        description:
            - Specifies the weight of the pool member for load balancing purposes.
        required: false
        default: 1
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
    session:
        description:
            - Specifies the ability of the client to persist to the pool member when making new connections.
        required: false
        default: user-enabled
        choices: ['user-enabled', 'user-disabled']
        aliases: []
        version_added: 2.3
'''

EXAMPLES = '''
- name: Add LTM Pool Member
  f5bigip_ltm_pool_member:
    f5bigip_hostname: 172.16.227.35
    f5bigip_username: admin
    f5bigip_password: admin
    f5bigip_port: 443
    name: my_member1:80
    partition: Common
    address: 10.10.10.101
    pool: my_pool
    state: present
  delegate_to: localhost
'''

from ansible_common_f5bigip.f5bigip import *

BIGIP_LTM_POOL_MEMBER_ARGS = dict(
    address             =   dict(type='str'),
    #app_service         =   dict(type='str'),
    connection_limit    =   dict(type='int'),
    description         =   dict(type='str'),
    dynamic_ratio       =   dict(type='int'),
    #fqdn                =   dict(type='list'),
    inherit_profile     =   dict(type='str', choices=F5BIGIP_ACTIVATION_CHOICES),
    logging             =   dict(type='str', choices=F5BIGIP_ACTIVATION_CHOICES),
    monitor             =   dict(type='str'),
    monitor_state       =   dict(type='str', choices=['user-down', 'user-up']),
    pool                =   dict(type='str'),
    priority_group      =   dict(type='int'),
    profiles            =   dict(type='str'),
    rate_limit          =   dict(type='int'),
    ratio               =   dict(type='int'),
    session             =   dict(type='str', choices=['user-enabled', 'user-disabled'])
)

class F5BigIpLtmPoolMember(F5BigIpObject):
    def _set_crud_methods(self):
        self.pool = self.mgmt.tm.ltm.pools.pool.load(
            name=self.params['pool'],
            partition=self.params['partition']
        )
        self.methods = {
            'create':self.pool.members_s.members.create,
            'read':self.pool.members_s.members.load,
            'update':self.pool.members_s.members.update,
            'delete':self.pool.members_s.members.delete,
            'exists':self.pool.members_s.members.exists
        }
        self.params.pop('pool', None)

    def _check_update_params(self):
        key = 'state'
        cur_val = None
        if hasattr(self.big, key):
            attr = getattr(self.big, key)
            cur_val = format_value(attr)
            if self.params[key] is None and 'user' not in cur_val:
                self.params[key] = 'user-up'

        key = 'session'
        cur_val = None
        if hasattr(self.big, key):
            attr = getattr(self.big, key)
            cur_val = format_value(attr)
            if self.params[key] is None and 'user' not in cur_val:
                self.params[key] = 'user-enabled'

        key = 'rateLimit'
        cur_val = None
        if hasattr(self.big, key):
            attr = getattr(self.big, key)
            cur_val = format_value(attr)
            if (self.params[key] is None and self.params[key] == 0) and cur_val == 'disabled':
                self.params[key] = cur_val

        super(F5BigIpLtmPoolMember, self)._check_update_params()

def main():
    # Translation list for conflictual params
    tr = { 'monitor_state':'state' }
    
    module = AnsibleModuleF5BigIpObject(argument_spec=BIGIP_LTM_POOL_MEMBER_ARGS, supports_check_mode=False)
    
    try:
        obj = F5BigIpLtmPoolMember(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':  
    main()