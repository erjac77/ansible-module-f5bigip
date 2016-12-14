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
module: f5bigip_ltm_pool
short_description: BIG-IP LTM pool module
description:
    - Configures load balancing pools.
version_added: "1.0"
author:
    - "Eric Jacob, @erjac77"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    all:
        description:
            - Specifies that you want to modify all of the existing components of the specified type.
        required: false
        default: null
        choices: [true, false]
        aliases: []
        version_added: 1.0
    allow_nat:
        description:
            - Specifies whether the pool can load balance network address translation (NAT) connections.
        required: false
        default: yes
        choices: ['yes', 'no']
        aliases: []
        version_added: 1.0
    allow_snat:
        description:
            - Specifies whether the pool can load balance secure network address translation (SNAT) connections.
        required: false
        default: yes
        choices: ['yes', 'no']
        aliases: []
        version_added: 1.0
    description:
        description:
            - Specifies a user-defined description.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 1.0
    gateway_failsafe_device:
        description:
            - Specifies that the pool is a gateway failsafe pool in a redundant configuration.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 1.0
    ignore_persisted_weight:
        description:
            - Discounts the weight of connections made to pool members selected through persistence, rather than as a result of the algorithm configured on the pool.
        required: false
        default: no
        choices: ['yes', 'no']
        aliases: []
        version_added: 1.0
    ip_tos_to_client:
        description:
            - Specifies the Type of Service (ToS) level to use when sending packets to a client.
        required: false
        default: pass-through (or 65535)
        choices: []
        aliases: []
        version_added: 1.0
    ip_tos_to_server:
        description:
            - Specifies the ToS level to use when sending packets to a server.
        required: false
        default: pass-through (or 65535)
        choices: []
        aliases: []
        version_added: 1.0
    link_qos_to_client:
        description:
            - Specifies the Link Quality of Service (QoS) level to use when sending packets to a client.
        required: false
        default: pass-through (or 65535)
        choices: []
        aliases: []
        version_added: 1.0
    link_qos_to_server:
        description:
            - Specifies the Link QoS level to use when sending packets to a server.
        required: false
        default: pass-through (or 65535)
        choices: []
        aliases: []
        version_added: 1.0
    load_balancing_mode:
        description:
            - Specifies the modes that the system uses to load balance name resolution requests among the members of this pool.
        required: false
        default: round-robin
        choices: [
            'dynamic-ratio-member', 'dynamic-ratio-node', 'fastest-app-response', 'fastest-node',
            'least-connections-members', 'least-connections-node', 'least-sessions', 'observed-member',
            'observed-node', 'predictive-member', 'predictive-node', 'ratio-least-connections-member',
            'ratio-least-connections-node', 'ratio-member', 'ratio-node', 'ratio-session', 'round-robin',
            'weighted-least-connections-member', 'weighted-least-connections-node'
        ]
        aliases: []
        version_added: 1.0
    min_active_members:
        description:
            - Specifies the minimum number of members that must be up for traffic to be confined to a priority group when using priority-based activation.
        required: false
        default: 0
        choices: []
        aliases: []
        version_added: 1.0
    min_up_members:
        description:
            - Specifies the minimum number of pool members that must be up; otherwise, the system takes the action specified in the min-up-members-action option.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 1.0
    min_up_members_action:
        description:
            - Specifies the action to take if min-up-members-checking is enabled, and the number of active pool members falls below the number specified in the min-up-members option.
        required: false
        default: failover
        choices: ['failover', 'reboot', 'restart-all']
        aliases: []
        version_added: 1.0
    min_up_members_checking:
        description:
            - Enables or disables the min-up-members feature.
        required: false
        default: null
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 1.0
    monitor:
        description:
            - Specifies the health monitors that the system uses to determine whether it can use this pool for load balancing.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 1.0
    name:
        description:
            - Specifies unique name for the component.
        required: true
        default: null
        choices: []
        aliases: []
        version_added: 1.0
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        required: false
        default: Common
        choices: []
        aliases: []
        version_added: 1.0
    profiles:
        description:
            - Specifies the profile to use for encapsulation.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 1.0
    reselect_tries:
        description:
            - Specifies the number of reselection tries.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 1.0
    service_down_action:
        description:
            - Specifies the action to take if the service specified in the pool is marked down.
        required: false
        default: none
        choices: ['drop', 'none', 'reselect', 'reset']
        aliases: []
        version_added: 1.0
    slow_ramp_time:
        description:
            - Specifies, in seconds, the ramp time for the pool.
        required: false
        default: 10
        choices: []
        aliases: []
        version_added: 1.0
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        required: false
        default: present
        choices: ['absent', 'present']
        aliases: []
        version_added: 1.0
'''

EXAMPLES = '''
- name: Create LTM Pool
  f5bigip_ltm_pool:
    f5bigip_hostname: "172.16.227.35"
    f5bigip_username: "admin"
    f5bigip_password: "admin"
    f5bigip_port: "443"
    name: "my_pool"
    partition: "Common"
    description: "my ltm pool"
    load_balancing_mode: "least-connections-members"
    state: "present"
  delegate_to: localhost

- name: Modify LTM Pool
  f5bigip_ltm_node:
    f5bigip_hostname: "172.16.227.35"
    f5bigip_username: "admin"
    f5bigip_password: "admin"
    f5bigip_port: "443"
    name: "my_pool"
    partition: "Common"
    connection_limit: 10
    description: "new pool"
    dynamic_ratio: 2
    logging: "enabled"
    rate_limit: 5
    ratio: 2
  delegate_to: localhost

- name: Delete LTM Pool
  f5bigip_ltm_pool:
    f5bigip_hostname: "172.16.227.35"
    f5bigip_username: "admin"
    f5bigip_password: "admin"
    f5bigip_port: "443"
    name: "my_pool"
    partition: "Common"
    state: "absent"
  delegate_to: localhost
  register: result
'''

from ansible_common_f5bigip.f5bigip import *

BIGIP_LTM_POOL_LB_CHOICES = [
    'dynamic-ratio-member', 'dynamic-ratio-node', 'fastest-app-response', 'fastest-node',
    'least-connections-member', 'least-connections-node', 'least-sessions', 'observed-member',
    'observed-node', 'predictive-member', 'predictive-node', 'ratio-least-connections-member',
    'ratio-least-connections-node', 'ratio-member', 'ratio-node', 'ratio-session', 'round-robin',
    'weighted-least-connections-member', 'weighted-least-connections-node'
]

BIGIP_LTM_POOL_ARGS = dict(
    all                         =   dict(type='bool'),
    allow_nat                   =   dict(type='str', choices=F5BIGIP_POLAR_CHOICES),
    allow_snat                  =   dict(type='str', choices=F5BIGIP_POLAR_CHOICES),
    #app_service                 =   dict(type='str'),
    description                 =   dict(type='str'),
    gateway_failsafe_device     =   dict(type='str'),
    ignore_persisted_weight     =   dict(type='str', choices=F5BIGIP_POLAR_CHOICES),
    ip_tos_to_client            =   dict(type='str'),
    ip_tos_to_server            =   dict(type='str'),
    link_qos_to_client          =   dict(type='str'),
    link_qos_to_server          =   dict(type='str'),
    load_balancing_mode         =   dict(type='str', choices=BIGIP_LTM_POOL_LB_CHOICES),
    #members                     =   dict(type='list'),
    #metadata                    =   dict(type='list'),
    min_active_members          =   dict(type='int'),
    min_up_members              =   dict(type='int'),
    min_up_members_action       =   dict(type='str', choices=['failover', 'reboot', 'restart-all']),
    min_up_members_checking     =   dict(type='str', choices=F5BIGIP_ACTIVATION_CHOICES),
    monitor                     =   dict(type='str'),
    profiles                    =   dict(type='str'),
    queue_depth_limit           =   dict(type='int'),
    queue_on_connection_limit   =   dict(type='str', choices=F5BIGIP_ACTIVATION_CHOICES),
    queue_time_limit            =   dict(type='int'),
    reselect_tries              =   dict(type='int'),
    service_down_action         =   dict(type='str', choices=['drop', 'none', 'reselect', 'reset']),
    slow_ramp_time              =   dict(type='int')
)

class F5BigIpLtmPool(F5BigIpObject):
    def _set_crud_methods(self):
        self.methods = {
            'create':self.mgmt.tm.ltm.pools.pool.create,
            'read':self.mgmt.tm.ltm.pools.pool.load,
            'update':self.mgmt.tm.ltm.pools.pool.update,
            'delete':self.mgmt.tm.ltm.pools.pool.delete,
            'exists':self.mgmt.tm.ltm.pools.pool.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}
    
    module = AnsibleModuleF5BigIpObject(argument_spec=BIGIP_LTM_POOL_ARGS, supports_check_mode=False)
    
    try:
        obj = F5BigIpLtmPool(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()