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

DOCUMENTATION = '''
---
module: f5bigip_gtm_global_settings_metrics
short_description: BIG-IP gtm global-settings metrics module
description:
    - Configures the metrics settings for the Global Traffic Manager.
version_added: 2.3
author:
    - "Gabriel Fortin"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    default_probe_limit:
        description:
            - Specifies the number of probe attempts that the system performs before removing the path from the metrics.
        required: false
        default: 12
        choices: []
        aliases: []
        version_added: 2.3
    hops_ttl:
        description:
            - Specifies the number of seconds that the system considers traceroute utility data to be valid for name resolution and load balancing.
        required: false
        default: 604800
        choices: range(hops_timeout, infinity)
        aliases: []
        version_added: 2.3
    hops_packet_length:
        description:
            - Specifies the length of packets, in bytes, that the system sends to a local DNS server to determine the path information between the two systems.
        required: false
        default: 64
        choices: []
        aliases: []
        version_added: 2.3
    hops_sample_count:
        description:
            - Specifies the number of packets that the system sends to a local DNS server to determine the path information between those two systems.
        required: false
        default: 3
        choices: []
        aliases: []
        version_added: 2.3
    hops_timeout:
        description:
            - Specifies the number of seconds that the big3d daemon waits for a probe.
        required: false
        default: 3
        choices: []
        aliases: []
        version_added: 2.3
    inactive_ldns_ttl:
        description:
            - Specifies the number of seconds that an inactive LDNS remains in the cache.
        required: false
        default: 2419200
        choices: range(60, 4294967296)
        aliases: []
        version_added: 2.3
    ldns_update_interval:
        description:
            - Specifies the number of seconds that a tmm will wait before sending an update for a LDNS which has been accessed.
        required: false
        default: 20
        choices: []
        aliases: []
        version_added: 2.3
    inactive_paths_ttl:
        description:
            - Specifies the number of seconds that a path remains in the cache after its last access.
        required: false
        default: 604800
        choices: range(60, 4294967296)
        aliases: []
        version_added: 2.3
    max_synchronous_monitor_requests:
        description:
            - Specifies how many monitors can attempt to verify the availability of a given resource at the same time.
        required: false
        default: 20
        choices: []
        aliases: []
        version_added: 2.3
    metrics_caching:
        description:
            - Specifies the interval (in seconds) at which the system dumps path and other metrics data.
        required: false
        default: 3600
        choices: range(0, 604801)
        aliases: []
        version_added: 2.3
    metrics_collection_protocols:
        description:
            - Specifies the protocols that the system uses to collect metrics information relevant to LDNS servers.
        required: false
        default: null
        choices: ['dns_dot', 'dns_rev', 'icmp', 'tcp', 'udp']
        aliases: []
        version_added: 2.3
   path_ttl:
        description:
            - Specifies the number of seconds that the system considers path data to be valid for name resolution and load balancing purposes.
        required: false
        default: 2400
        choices: range(paths_retry, infinity)
        aliases: []
        version_added: 2.3
    paths_retry:
        description:
            - Specifies the interval (in seconds) at which the system retries the path data.
        required: false
        default: 120
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
'''

EXAMPLES = '''
- name: Create GTM Global Settings Metrics
  f5bigip_gtm_global_settings_metrics:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    default_probe_limit: 10
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_GTM_GLOBAL_SETTINGS_METRICS_ARGS = dict(
    default_probe_limit                 =   dict(type='int'),
    hops_ttl                            =   dict(type='int'),
    hops_packet_length                  =   dict(type='int'),
    hops_sample_count                   =   dict(type='int'),
    hops_timeout                        =   dict(type='int'),
    inactive_ldns_ttl                   =   dict(type='int'),
    ldns_update_interval                =   dict(type='int'),
    inactive_paths_ttl                  =   dict(type='int'),
    max_synchronous_monitor_requests    =   dict(type='int'),
    metrics_caching                     =   dict(type='int', choices=range(0, 604801)),
    metrics_collection_protocols        =   dict(type='str', choices=['dns_dot', 'dns_rev', 'icmp', 'tcp', 'udp']),
    path_ttl                            =   dict(type='int'),
    paths_retry                         =   dict(type='int')
)

class F5BigIpGtmGlobalSettingsMetrics(F5BigIpUnnamedObject):
    def set_crud_methods(self):
        self.methods = {
            'read':     self.mgmt_root.tm.gtm.global_settings.metrics.load,
            'update':   self.mgmt_root.tm.gtm.global_settings.metrics.update,
        }

def main():
    # Translation list for conflictual params
    tr = {}
    
    module = AnsibleModuleF5BigIpUnnamedObject(argument_spec=BIGIP_GTM_GLOBAL_SETTINGS_METRICS_ARGS, supports_check_mode=False)
    
    try:
        obj = F5BigIpGtmGlobalSettingsMetrics(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()