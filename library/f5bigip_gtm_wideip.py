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
module: f5bigip_gtm_wideip
short_description: BIG-IP gtm wideip module
description:
    - Configures a wide IP.
version_added: 2.3
author:
    - "Eric Jacob, @erjac77"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    aliases:
        description:
            - Specifies alternate domain names for the web site content you are load balancing.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    app_service:
        description:
            - Specifies the application service that the object belongs to.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    description:
        description:
            - Specifies a user-defined description.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    disabled:
        description:
            - Specifies whether the wide IP and its resources are available for load balancing.
        required: false
        default: false
        choices: []
        aliases: []
        version_added: 2.3
    enabled:
        description:
            - Specifies whether the wide IP and its resources are available for load balancing.
        required: false
        default: true
        choices: []
        aliases: []
        version_added: 2.3
    ipv6_no_error_neg_ttl:
        description:
            - Specifies the negative caching TTL of the SOA for the IPv6 NoError response.
        required: false
        default: 0
        choices: []
        aliases: []
        version_added: 2.3
    ipv6_no_error_response:
        description:
            - Specifies the negative caching TTL of the SOA for the IPv6 NoError response.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
        aliases: []
        version_added: 2.3
    last_resort_pool:
        description:
            - Specifies which pool for the system to use as the last resort pool when load balancing requests for this wide IP.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    load_balancing_decision_log_verbosity:
        description:
            - Specifies the amount of detail logged when making load balancing decisions.
        required: false
        default: null
        choices: ['pool-selection', 'pool-traversal', 'pool-member-selection', 'pool-member-traversal']
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
    persistence:
        description:
            - When enabled, specifies that when a local DNS server makes repetitive requests on behalf of a client, the system reconnects the client to the same resource as previous requests.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
        aliases: []
        version_added: 2.3
    persist_cidr_ipv4:
        description:
            - Specifies a mask used to group IPv4 LDNS addresses.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    persist_cidr_ipv6:
        description:
            - Specifies a mask used to group IPv6 LDNS addresses.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    pool_lb_mode:
        description:
            - Specifies the load balancing method used to select a pool in this wide IP.
        required: false
        default: round-robin
        choices: ['global-availability', 'random', 'ratio', 'round-robin', 'topology']
        aliases: []
        version_added: 2.3
    pools:
        description:
            - Configures the pools the system uses when load balancing requests for this wide IP.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    rules:
        description:
            - Specifies the iRules that this wide IP uses for load balancing decisions.
        required: false
        default: null
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
    ttl_persistence:
        description:
            - Specifies, in seconds, the length of time for which a persistence entry is valid.
        required: false
        default: 3600
        choices: []
        aliases: []
        version_added: 2.3
'''

EXAMPLES = '''
- name: Create GTM WideIP
  f5bigip_gtm_server:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: mywideip.localhost
    partition: Common
    description: My wideip
    pool_lb_mode: global-availability
    pools:
      - my_pool1
      - my_pool2
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_GTM_WIDEIP_ARGS = dict(
    aliases                                 =   dict(type='list'),
    app_service                             =   dict(type='str'),
    description                             =   dict(type='str'),
    disabled                                =   dict(type='bool'),
    enabled                                 =   dict(type='bool'),
    ipv6_no_error_neg_ttl                   =   dict(type='int'),
    ipv6_no_error_response                  =   dict(type='str', choices=[F5_ACTIVATION_CHOICES]),
    last_resort_pool                        =   dict(type='str'),
    load_balancing_decision_log_verbosity   =   dict(type='str', choices=['pool-selection', 'pool-traversal', 'pool-member-selection', 'pool-member-traversal']),
    #metadata                                =   dict(type='list'),
    persistence                             =   dict(type='str', choices=[F5_ACTIVATION_CHOICES]),
    persist_cidr_ipv4                       =   dict(type='int'),
    persist_cidr_ipv6                       =   dict(type='int'),
    pool_lb_mode                            =   dict(type='str', choices=['global-availability', 'random', 'ratio', 'round-robin', 'topology']),
    pools                                   =   dict(type='list'),
    rules                                   =   dict(type='list'),
    ttl_persistence                         =   dict(type='int')
)

class F5BigIpGtmWideip(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.gtm.wideips.wideip.create,
            'read':     self.mgmt_root.tm.gtm.wideips.wideip.load,
            'update':   self.mgmt_root.tm.gtm.wideips.wideip.update,
            'delete':   self.mgmt_root.tm.gtm.wideips.wideip.delete,
            'exists':   self.mgmt_root.tm.gtm.wideips.wideip.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}
    
    module = AnsibleModuleF5BigIpNamedObject(
        argument_spec=BIGIP_GTM_WIDEIP_ARGS,
        supports_check_mode=False,
        mutually_exclusive=[
            ['disabled', 'enabled']
        ]
    )
    
    try:
        obj = F5BigIpGtmWideip(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()