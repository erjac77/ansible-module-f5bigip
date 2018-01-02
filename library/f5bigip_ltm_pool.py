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
module: f5bigip_ltm_pool
short_description: BIG-IP ltm pool module
description:
    - Configures load balancing pools.
version_added: "2.4"
author:
    - "Eric Jacob (@erjac77)"
options:
    all:
        description:
            - Specifies that you want to modify all of the existing components of the specified type.
        choices: [true, false]
    allow_nat:
        description:
            - Specifies whether the pool can load balance network address translation (NAT) connections.
        default: yes
        choices: ['yes', 'no']
    allow_snat:
        description:
            - Specifies whether the pool can load balance secure network address translation (SNAT) connections.
        default: yes
        choices: ['yes', 'no']
    app_service:
        description:
            - Specifies the application service to which the object belongs.
    description:
        description:
            - Specifies a user-defined description.
    gateway_failsafe_device:
        description:
            - Specifies that the pool is a gateway failsafe pool in a redundant configuration.
    ignore_persisted_weight:
        description:
            - Discounts the weight of connections made to pool members selected through persistence, rather than as a
              result of the algorithm configured on the pool.
        default: no
        choices: ['yes', 'no']
    ip_tos_to_client:
        description:
            - Specifies the Type of Service (ToS) level to use when sending packets to a client.
        default: pass-through (or 65535)
    ip_tos_to_server:
        description:
            - Specifies the ToS level to use when sending packets to a server.
        default: pass-through (or 65535)
    link_qos_to_client:
        description:
            - Specifies the Link Quality of Service (QoS) level to use when sending packets to a client.
        default: pass-through (or 65535)
    link_qos_to_server:
        description:
            - Specifies the Link QoS level to use when sending packets to a server.
        default: pass-through (or 65535)
    load_balancing_mode:
        description:
            - Specifies the modes that the system uses to load balance name resolution requests among the members of
              this pool.
        default: round-robin
        choices: [
            'dynamic-ratio-member', 'dynamic-ratio-node', 'fastest-app-response', 'fastest-node',
            'least-connections-members', 'least-connections-node', 'least-sessions', 'observed-member',
            'observed-node', 'predictive-member', 'predictive-node', 'ratio-least-connections-member',
            'ratio-least-connections-node', 'ratio-member', 'ratio-node', 'ratio-session', 'round-robin',
            'weighted-least-connections-member', 'weighted-least-connections-node'
        ]
    min_active_members:
        description:
            - Specifies the minimum number of members that must be up for traffic to be confined to a priority group
              when using priority-based activation.
        default: 0
    min_up_members:
        description:
            - Specifies the minimum number of pool members that must be up; otherwise, the system takes the action
              specified in the min-up-members-action option.
    min_up_members_action:
        description:
            - Specifies the action to take if min-up-members-checking is enabled, and the number of active pool members
              falls below the number specified in the min-up-members option.
        default: failover
        choices: ['failover', 'reboot', 'restart-all']
    min_up_members_checking:
        description:
            - Enables or disables the min-up-members feature.
        choices: ['enabled', 'disabled']
    monitor:
        description:
            - Specifies the health monitors that the system uses to determine whether it can use this pool for load
              balancing.
    name:
        description:
            - Specifies unique name for the component.
        required: true
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        default: Common
    profiles:
        description:
            - Specifies the profile to use for encapsulation.
    reselect_tries:
        description:
            - Specifies the number of reselection tries.
    service_down_action:
        description:
            - Specifies the action to take if the service specified in the pool is marked down.
        choices: ['drop', 'none', 'reselect', 'reset']
    slow_ramp_time:
        description:
            - Specifies, in seconds, the ramp time for the pool.
        default: 10
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
- name: Create LTM Pool
  f5bigip_ltm_pool:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_pool
    partition: Common
    description: My ltm pool
    load_balancing_mode: least-connections-members
    state: present
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_LTM_POOL_LB_MODE_CHOICES = [
    'dynamic-ratio-member', 'dynamic-ratio-node', 'fastest-app-response', 'fastest-node',
    'least-connections-member', 'least-connections-node', 'least-sessions', 'observed-member',
    'observed-node', 'predictive-member', 'predictive-node', 'ratio-least-connections-member',
    'ratio-least-connections-node', 'ratio-member', 'ratio-node', 'ratio-session', 'round-robin',
    'weighted-least-connections-member', 'weighted-least-connections-node'
]

BIGIP_LTM_POOL_ARGS = dict(
    all=dict(type='bool'),
    allow_nat=dict(type='str', choices=F5_POLAR_CHOICES),
    allow_snat=dict(type='str', choices=F5_POLAR_CHOICES),
    app_service=dict(type='str'),
    description=dict(type='str'),
    gateway_failsafe_device=dict(type='str'),
    ignore_persisted_weight=dict(type='str', choices=F5_POLAR_CHOICES),
    ip_tos_to_client=dict(type='str'),
    ip_tos_to_server=dict(type='str'),
    link_qos_to_client=dict(type='str'),
    link_qos_to_server=dict(type='str'),
    load_balancing_mode=dict(type='str', choices=BIGIP_LTM_POOL_LB_MODE_CHOICES),
    metadata=dict(type='list'),
    min_active_members=dict(type='int'),
    min_up_members=dict(type='int'),
    min_up_members_action=dict(type='str', choices=['failover', 'reboot', 'restart-all']),
    min_up_members_checking=dict(type='str', choices=F5_ACTIVATION_CHOICES),
    monitor=dict(type='str'),
    profiles=dict(type='list'),
    queue_depth_limit=dict(type='int'),
    queue_on_connection_limit=dict(type='str', choices=F5_ACTIVATION_CHOICES),
    queue_time_limit=dict(type='int'),
    reselect_tries=dict(type='int'),
    service_down_action=dict(type='str', choices=['drop', 'none', 'reselect', 'reset']),
    slow_ramp_time=dict(type='int')
)


class F5BigIpLtmPool(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create': self.mgmt_root.tm.ltm.pools.pool.create,
            'read': self.mgmt_root.tm.ltm.pools.pool.load,
            'update': self.mgmt_root.tm.ltm.pools.pool.update,
            'delete': self.mgmt_root.tm.ltm.pools.pool.delete,
            'exists': self.mgmt_root.tm.ltm.pools.pool.exists
        }


def main():
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_POOL_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpLtmPool(check_mode=module.supports_check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
