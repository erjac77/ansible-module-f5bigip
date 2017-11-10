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

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: f5bigip_gtm_global_settings_general
short_description: BIG-IP gtm global-settings general module
description:
    - Configures the general settings for the Global Traffic Manager.
version_added: 2.3
author:
    - "Gabriel Fortin"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    automatic_configuration_save_timeout:
        description:
            - Sets the timeout, in seconds, indicating how long to wait after a GTM configuration change before automatically saving the GTM configuration to the bigip_gtm.conf.
        required: false
        default: 15
        choices: []
        aliases: []
        version_added: 2.3
    auto_discovery:
        description:
            - Specifies whether the auto-discovery process is activated for this system.
        required: false
        default: no
        choices: ['yes', 'no']
        aliases: []
        version_added: 2.3
    auto_discovery_interval:
        description:
            - Specifies the frequency, in seconds, between system attempts to discover network components.
        required: false
        default: 30
        choices: []
        aliases: []
        version_added: 2.3
    cache_ldns_servers:
        description:
            - Specifies whether the system retains, in cache, all local DNS servers that make requests.
        required: false
        default: yes
        choices: ['yes', 'no']
        aliases: []
        version_added: 2.3
    domain_name_check:
        description:
            - Specifies the parameters for the Global Traffic Manager to use when performing domain name checking.
        required: false
        default: strict
        choices: ['allow_underscore', 'idn_compatible', 'none', 'strict']
        aliases: []
        version_added: 2.3
    drain_persistent_requests:
        description:
            - Specifies, when set to yes, that when you disable a pool, load-balanced, persistent connections remain connected until the TTL expires.
        required: false
        default: yes
        choices: ['yes', 'no']
        aliases: []
        version_added: 2.3
    forward_status:
        description:
            - Specifies, when set to enabled, that the availibility status change for GTM objects will be shared with subscribers.
        required: false
        default: null
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    gtm_sets_recursion:
        description:
            - Specifies, when set to yes, that the system enables recursive DNS queries, regardless of whether the requesting local DNS enabled recursive queries.
        required: false
        default: no
        choices: ['yes', 'no']
        aliases: []
        version_added: 2.3
    heartbeat_interval:
        description:
            - Specifies the frequency at which the Global Traffic Manager queries other BIG-IP systems for updated data.
        required: false
        default: 10
        choices: range(0, 11)
        aliases: []
        version_added: 2.3
    monitor_disabled_objects:
        description:
            - Specifies, when set to yes, that the system will continue to monitor objects even if the objects are disabled.
        required: false
        default: no
        choices: ['yes', 'no']
        aliases: []
        version_added: 2.3
    nethsm_timeout:
        description:
            - Time to wait on a NetHSM key creation operation for DNSSEC before retry.
        required: false
        default: 20
        choices: []
        aliases: []
        version_added: 2.3
    peer_leader:
        description:
            - Specifies the name of a GTM server to be used for executing certain features, such as creating DNSSEC keys.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    port:
        description:
            - Specifies the port on which the listener listens for connections.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
   send-wildcard-rrs:
        description:
            - Specifies, when set to enable, that WideIPs or WideIP aliases that contain wildcards will autogenerate Resource Records in the BIND database.
        default: disable
        choices: ['enable', 'disable']
        aliases: []
        version_added: 2.3
    static_persist_cidr_ipv4:
        description:
            - Specifies the number of bits of the IPv4 address that the system considers when using the Static Persist load balancing mode.
        required: false
        default: 32
        choices: []
        aliases: []
        version_added: 2.3
    static_persist_cidr_ipv6:
        description:
            - Specifies the number of bits of the IPv6 address that the system considers when using the Static Persist load balancing mode.
        required: false
        default: 128
        choices: []
        aliases: []
        version_added: 2.3
    synchronization
        description:
            - Specifies whether this system is a member of a synchronization group.
        required: false
        default: no
        choices: ['yes', 'no]
        aliases: []
        version_added: 2.3
    synchronization_group_name:
        description:
            - Specifies the name of the synchronization group to which the system belongs.
        required: false
        default: default
        choices: []
        aliases: []
        version_added: 2.3
    synchronization_time_tolerance:
        description:
            - Specifies the number of seconds that one system clock can be out of sync with another system clock, in the synchronization group.
        required: false
        default: 10
        choices: [0, range(5, 601)]
        aliases: []
        version_added: 2.3
    synchronization_timeout:
        description:
            - Specifies the number of seconds that the system attempts to synchronize the Global Traffic Manager configuration with a synchronization group member.
        required: false
        default: 180
        choices: []
        aliases: []
        version_added: 2.3
    synchronize_zone_files:
        description:
            - Specifies whether the system synchronizes zone files among the synchronization group members.
        required: false
        default: no
        choices: ['yes', 'no']
        aliases: []
        version_added: 2.3
    synchronize_zone_files_timeout:
        description:
            - Specifies the number of seconds that a synchronization group member attempts to synchronize its zone files with a synchronization group member.
        required: false
        default: 300
        choices: []
        aliases: []
        version_added: 2.3
    topology_allow_zero_scores:
        description:
            - Specifies if topology load-balancing or QoS load-balancing with topology enabled will return pool members with zero topology scores.
        required: false
        default: yes
        choices: ['yes', 'no']
        aliases: []
        version_added: 2.3
    virtuals_depend_on_server_state:
        description:
            - Specifies whether the system marks a virtual server down when the server on which the virtual server is configured can no longer be reached via iQuery.
        required: false
        default: yes
        choices: ['yes', 'no']
        aliases: []
        version_added: 2.3
'''

EXAMPLES = '''
- name: Change GTM Global General Settings heartbeat interval
  f5bigip_gtm_global_settings_general:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    heartbeat_interval: 8
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_GTM_GLOBAL_SETTINGS_GENERAL_ARGS = dict(
    automatic_configuration_save_timeout    =   dict(type='int'),
    auto_discovery                          =   dict(type='str', choices=F5_POLAR_CHOICES),
    auto_discovery_interval                 =   dict(type='int'),
    cache_ldns_servers                      =   dict(type='str', choices=F5_POLAR_CHOICES),
    domain_name_check                       =   dict(type='str', choices=['allow_underscore', 'idn_compatible', 'none', 'strict']),
    drain_persistent_requests               =   dict(type='str', choices=F5_POLAR_CHOICES),
    forward_status                          =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    gtm_sets_recursion                      =   dict(type='str', choices=F5_POLAR_CHOICES),
    heartbeat_interval                      =   dict(type='int', choices=range(0, 11)),
    monitor_disabled_objects                =   dict(type='str', choices=F5_POLAR_CHOICES),
    nethsm_timeout                          =   dict(type='int'),
    peer_leader                             =   dict(type='str'),
    send_wildcards_rrs                      =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    static_persist_cidr_ipv4                =   dict(type='int'),
    static_persist_cidr_ipv6                =   dict(type='int'),
    synchronization                         =   dict(type='str', choices=F5_POLAR_CHOICES),
    synchronization_group_name              =   dict(type='str'),
    synchronization_time_tolerance          =   dict(type='int', choices=[0, range(5, 601)]),
    synchronization_timeout                 =   dict(type='int'),
    synchronize_zone_files                  =   dict(type='str', choices=F5_POLAR_CHOICES),
    synchronize_zone_files_timeout          =   dict(type='int'),
    topology_allow_zero_scores              =   dict(type='str', choices=F5_POLAR_CHOICES),
    virtuals_depend_on_server_state         =   dict(type='str', choices=F5_POLAR_CHOICES)
)

class F5BigIpGtmGlobalSettingsGeneral(F5BigIpUnnamedObject):
    def set_crud_methods(self):
        self.methods = {
            'read':     self.mgmt_root.tm.gtm.global_settings.general.load,
            'update':   self.mgmt_root.tm.gtm.global_settings.general.update
        }

def main():
    # Translation list for conflictual params
    tr = {}
    
    module = AnsibleModuleF5BigIpUnnamedObject(argument_spec=BIGIP_GTM_GLOBAL_SETTINGS_GENERAL_ARGS, supports_check_mode=False)
    
    try:
        obj = F5BigIpGtmGlobalSettingsGeneral(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()