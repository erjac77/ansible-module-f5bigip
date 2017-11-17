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
module: f5bigip_gtm_wideip
short_description: BIG-IP gtm wideip module
description:
    - Configures a wide IP.
version_added: "2.4"
author:
    - "Eric Jacob (@erjac77)"
options:
    aliases:
        description:
            - Specifies alternate domain names for the web site content you are load balancing.
    app_service:
        description:
            - Specifies the application service that the object belongs to.
    description:
        description:
            - Specifies a user-defined description.
    disabled:
        description:
            - Specifies whether the wide IP and its resources are available for load balancing.
        default: false
    enabled:
        description:
            - Specifies whether the wide IP and its resources are available for load balancing.
        default: true
    ipv6_no_error_neg_ttl:
        description:
            - Specifies the negative caching TTL of the SOA for the IPv6 NoError response.
        default: 0
    ipv6_no_error_response:
        description:
            - Specifies the negative caching TTL of the SOA for the IPv6 NoError response.
        default: disabled
        choices: ['disabled', 'enabled']
    last_resort_pool:
        description:
            - Specifies which pool for the system to use as the last resort pool when load balancing requests for this wide IP.
    load_balancing_decision_log_verbosity:
        description:
            - Specifies the amount of detail logged when making load balancing decisions.
        choices: ['pool-selection', 'pool-traversal', 'pool-member-selection', 'pool-member-traversal']
    name:
        description:
            - Specifies unique name for the component.
        required: true
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        default: Common
    persistence:
        description:
            - When enabled, specifies that when a local DNS server makes repetitive requests on behalf of a client, the system reconnects the client to the same resource as previous requests.
        default: disabled
        choices: ['disabled', 'enabled']
    persist_cidr_ipv4:
        description:
            - Specifies a mask used to group IPv4 LDNS addresses.
    persist_cidr_ipv6:
        description:
            - Specifies a mask used to group IPv6 LDNS addresses.
    pool_lb_mode:
        description:
            - Specifies the load balancing method used to select a pool in this wide IP.
        default: round-robin
        choices: ['global-availability', 'random', 'ratio', 'round-robin', 'topology']
    pools:
        description:
            - Configures the pools the system uses when load balancing requests for this wide IP.
    rules:
        description:
            - Specifies the iRules that this wide IP uses for load balancing decisions.
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    ttl_persistence:
        description:
            - Specifies, in seconds, the length of time for which a persistence entry is valid.
        default: 3600
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
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

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *
from f5.bigip.resource import OrganizingCollection

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
    metadata                                =   dict(type='list'),
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
        if isinstance(self.mgmt_root.tm.gtm.wideips, OrganizingCollection):
            self.methods = {
                'create':   self.mgmt_root.tm.gtm.wideips.a_s.a.create,
                'read':     self.mgmt_root.tm.gtm.wideips.a_s.a.load,
                'update':   self.mgmt_root.tm.gtm.wideips.a_s.a.update,
                'delete':   self.mgmt_root.tm.gtm.wideips.a_s.a.delete,
                'exists':   self.mgmt_root.tm.gtm.wideips.a_s.a.exists
            }
        else:
            self.methods = {
                'create':   self.mgmt_root.tm.gtm.wideips.wideip.create,
                'read':     self.mgmt_root.tm.gtm.wideips.wideip.load,
                'update':   self.mgmt_root.tm.gtm.wideips.wideip.update,
                'delete':   self.mgmt_root.tm.gtm.wideips.wideip.delete,
                'exists':   self.mgmt_root.tm.gtm.wideips.wideip.exists
            }

def main():
    module = AnsibleModuleF5BigIpNamedObject(
        argument_spec=BIGIP_GTM_WIDEIP_ARGS,
        supports_check_mode=False,
        mutually_exclusive=[
            ['disabled', 'enabled']
        ]
    )

    try:
        obj = F5BigIpGtmWideip(check_mode=module.supports_check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

if __name__ == '__main__':
    main()