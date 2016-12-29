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
module: f5bigip_gtm_pool
short_description: BIG-IP GTM pool module
description:
    - Configures load balancing pools for the Global Traffic Manager.
version_added: "1.0"
author:
    - "Eric Jacob, @erjac77"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    alternate_mode:
        description:
            - Specifies the load balancing mode that the system uses to load balance name resolution requests among the members of this pool, if the preferred method is unsuccessful in picking a pool.
        required: false
        default: round-robin
        choices: ['drop-packet', 'fallback-ip', 'global-availability', 'none', 'packet-rate', 'ratio', 'return-to-dns', 'round-robin', 'static-persistence', 'topology', 'virtual-server-capacity', 'virtual-server-score']
        aliases: []
        version_added: 1.0
    canonical_name:
        description:
            - Specifies the canonical name of the zone.
        required: false
        default: null
        choices: []
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
    disabled:
        description:
            - Specifies whether the data center and its resources are available for load balancing.
        required: false
        default: false
        choices: []
        aliases: []
        version_added: 1.0
    dynamic_ratio:
        description:
            - Enables or disables a dynamic ratio load balancing algorithm for this pool.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
        aliases: []
        version_added: 1.0
    enabled:
        description:
            - Specifies whether the data center and its resources are available for load balancing.
        required: false
        default: true
        choices: []
        aliases: []
        version_added: 1.0
    fallback_ipv4:
        description:
            - Specifies the IPv4 address of the server to which the system directs requests in the event that the load balancing methods configured for this pool fail to return a valid virtual server.
        required: false
        default: ::
        choices: []
        aliases: []
        version_added: 1.0
    fallback_ipv6:
        description:
            - Specifies the IPv6 address of the server to which the system directs requests in the event that the load balancing methods configured for this pool fail to return a valid virtual server.
        required: false
        default: ::
        choices: []
        aliases: []
        version_added: 1.0
    fallback_mode:
        description:
            - Specifies the load balancing mode that the system uses to load balance name resolution requests among the members of this pool, if the preferred and alternate modes are unsuccessful in picking a pool.
        required: false
        default: return-to-dns
        choices: ['completion-rate', 'cpu', 'drop-packet', 'fallback-ip', 'fewest-hops', 'global-availability', 'kilobytes-per-second', 'least-connections', 'lowest-round-trip-time', 'none', 'packet-rate', 'quality-of-service', 'ratio', 'return-to-dns', 'round-robin', 'static-persistence', 'topology', 'virtual-server-capacity', 'virtual-server-score']
        aliases: []
        version_added: 1.0
    load_balancing_mode:
        description:
            - Specifies the preferred load balancing mode that the system uses to load balance name resolution requests among the members of this pool.
        required: false
        default: round-robin
        choices: ['completion-rate', 'cpu', 'drop-packet', 'fallback-ip', 'fewest-hops', 'global-availability', 'kilobytes-per-second', 'least-connections', 'lowest-round-trip-time', 'packet-rate', 'quality-of-service', 'ratio', 'return-to-dns', 'round-robin', 'static-persistence', 'topology', 'virtual-server-capacity', 'virtual-server-score']
        aliases: []
        version_added: 1.0
    manual_resume:
        description:
            - Enables or disables the manual resume function for this pool.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
        aliases: []
        version_added: 1.0
    max_addresses_returned:
        description:
            - Specifies the maximum number of available virtual servers that the system lists in an A record response.
        required: false
        default: 1
        choices: []
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
    qos_hit_ratio:
        description:
            - Assigns a weight to the Hit Ratio performance factor for the Quality of Service dynamic load balancing mode.
        required: false
        default: 5
        choices: []
        aliases: []
        version_added: 1.0
    qos_hops:
        description:
            - Assigns a weight to the Hops performance factor when the value of the either the load-balancing-mode or fallback-mode options is quality-of-service.
        required: false
        default: 0
        choices: []
        aliases: []
        version_added: 1.0
    qos_kilobytes_second:
        description:
            - Assigns a weight to the Kilobytes per Second performance factor when the value of the either the load-balancing-mode or fallback-mode options is quality-of-service.
        required: false
        default: 3
        choices: []
        aliases: []
        version_added: 1.0
    qos_lcs:
        description:
            - Assigns a weight to the Link Capacity performance factor when the value of the either the load-balancing-mode or fallback-mode options is quality-of-service.
        required: false
        default: 30
        choices: []
        aliases: []
        version_added: 1.0
    qos_packet_rate:
        description:
            - Assigns a weight to the Packet Rate performance factor when the value of the either the load-balancing-mode or fallback-mode options is quality-of-service.
        required: false
        default: 1
        choices: []
        aliases: []
        version_added: 1.0
    qos_rtt:
        description:
            - Assigns a weight to the Round Trip Time performance factor when the value of the either the load-balancing-mode or fallback-mode options is quality-of-service.
        required: false
        default: 50
        choices: []
        aliases: []
        version_added: 1.0
    qos_topology:
        description:
            - Assigns a weight to the Topology performance factor when the value of the either the load-balancing-mode or fallback-mode options is quality-of-service.
        required: false
        default: 0
        choices: []
        aliases: []
        version_added: 1.0
    qos_vs_capacity:
        description:
            - Assigns a weight to the Virtual Server performance factor when the value of the either the load-balancing-mode or fallback-mode options is quality-of-service.
        required: false
        default: 0
        choices: []
        aliases: []
        version_added: 1.0
    qos_vs_score:
        description:
            - Assigns a weight to the Virtual Server Score performance factor when the value of the either the load-balancing-mode or fallback-mode options is quality-of-service.
        required: false
        default: 0
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
    ttl:
        description:
            - Specifies the number of seconds that the IP address, once found, is valid.
        required: false
        default: 30
        choices: []
        aliases: []
        version_added: 1.0
    verify_member_availability:
        description:
            - Specifies that the system verifies the availability of the members before sending a connection to those resources.
        required: false
        default: enabled
        choices: ['disabled', 'enabled']
        aliases: []
        version_added: 1.0
'''

EXAMPLES = '''
- name: Create GTM Pool
  f5bigip_gtm_pool:
    f5bigip_hostname: 172.16.227.35
    f5bigip_username: admin
    f5bigip_password: admin
    f5bigip_port: 443
    name: my_pool
    partition: Common
    description: My pool
    load_balancing_mode: global-availability
    state: present
  delegate_to: localhost

- name: Delete GTM Pool
  f5bigip_gtm_pool:
    f5bigip_hostname: 172.16.227.35
    f5bigip_username: admin
    f5bigip_password: admin
    f5bigip_port: 443
    name: my_pool
    partition: Common
    state: absent
  delegate_to: localhost
'''

from ansible_common_f5bigip.f5bigip import *

BIGIP_GTM_POOL_ARGS = dict(
    alternate_mode                  =   dict(type='str', choices=['drop-packet', 'fallback-ip', 'global-availability', 'none', 'packet-rate', 'ratio', 'return-to-dns', 'round-robin', 'static-persistence', 'topology', 'virtual-server-capacity', 'virtual-server-score']),
    #app_service                     =   dict(type='str'),
    canonical_name                  =   dict(type='str'),
    description                     =   dict(type='str'),
    disabled                        =   dict(type='bool'),
    enabled                         =   dict(type='bool'),
    dynamic_ratio                   =   dict(type='str', choices=[F5BIGIP_ACTIVATION_CHOICES]),
    fallback_ipv4                   =   dict(type='str'),
    fallback_ipv6                   =   dict(type='str'),
    fallback_mode                   =   dict(type='str', choices=['completion-rate', 'cpu', 'drop-packet', 'fallback-ip', 'fewest-hops', 'global-availability', 'kilobytes-per-second', 'least-connections', 'lowest-round-trip-time', 'none', 'packet-rate', 'quality-of-service', 'ratio', 'return-to-dns', 'round-robin', 'static-persistence', 'topology', 'virtual-server-capacity', 'virtual-server-score']),
    #limit_max_bps                   =   dict(type='int'),
    #limit_max_bps_status            =   dict(type='str', choices=[F5BIGIP_ACTIVATION_CHOICES]),
    #limit_max_connections           =   dict(type='int'),
    #limit_max_connections_status    =   dict(type='str', choices=[F5BIGIP_ACTIVATION_CHOICES]),
    #limit_max_pps                   =   dict(type='int'),
    #limit_max_pps_status            =   dict(type='str', choices=[F5BIGIP_ACTIVATION_CHOICES]),
    load_balancing_mode             =   dict(type='str', choices=['completion-rate', 'cpu', 'drop-packet', 'fallback-ip', 'fewest-hops', 'global-availability', 'kilobytes-per-second', 'least-connections', 'lowest-round-trip-time', 'packet-rate', 'quality-of-service', 'ratio', 'return-to-dns', 'round-robin', 'static-persistence', 'topology', 'virtual-server-capacity', 'virtual-server-score']),
    manual_resume                   =   dict(type='str', choices=[F5BIGIP_ACTIVATION_CHOICES]),
    max_addresses_returned          =   dict(type='int'),
    #members                         =   dict(type='list'),
    #metadata                        =   dict(type='list'),
    monitor                         =   dict(type='str'),
    qos_hit_ratio                   =   dict(type='int'),
    qos_hops                        =   dict(type='int'),
    qos_kilobytes_second            =   dict(type='int'),
    qos_lcs                         =   dict(type='int'),
    qos_packet_rate                 =   dict(type='int'),
    qos_rtt                         =   dict(type='int'),
    qos_topology                    =   dict(type='int'),
    qos_vs_capacity                 =   dict(type='int'),
    qos_vs_score                    =   dict(type='int'),
    ttl                             =   dict(type='int'),
    verify_member_availability      =   dict(type='str', choices=[F5BIGIP_ACTIVATION_CHOICES])
)

class F5BigIpGtmPool(F5BigIpObject):
    def _set_crud_methods(self):
        self.methods = {
            'create':self.mgmt.tm.gtm.pools.pool.create,
            'read':self.mgmt.tm.gtm.pools.pool.load,
            'update':self.mgmt.tm.gtm.pools.pool.update,
            'delete':self.mgmt.tm.gtm.pools.pool.delete,
            'exists':self.mgmt.tm.gtm.pools.pool.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}
    
    module = AnsibleModuleF5BigIpObject(
        argument_spec=BIGIP_GTM_POOL_ARGS,
        supports_check_mode=False,
        mutually_exclusive=[
            ['disabled', 'enabled']
        ]
    )
    
    try:
        obj = F5BigIpGtmPool(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()