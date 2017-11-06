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
module: f5bigip_ltm_profile_dns
short_description: BIG-IP ltm profile dns module
description:
    - Configures a Domain Name System (DNS) profile.
version_added: 2.3
author:
    - "Gabriel Fortin"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    app_service:
        description:
            - Specifies the name of the application service to which the profile belongs.
        required: false
        default: none
        choices: []
        aliases: []
    avr_dnsstat_sample_rate:
        description:
            - Sets AVR DNS statistics rate.
        required: false
        default: 0
        choices: []
        aliases: []
    defaults_from:
        description:
            - Specifies the profile that you want to use as the parent profile.
        required: false
        default: dns
        choices: []
        aliases: []
    description:
        description:
            - User defined description.
        required: false
        default: null
        choices: []
        aliases: []
    dns64:
        description:
            - Specifies DNS64 mapping IPv6 prefix.
        required: false
        default: disabled
        choices: ['disabled', 'secondary', 'immediate', 'v4-only']
        aliases: []
    dns64_additional_section_rewrite:
        description:
            - Sets DNS64 additional section rewriting.
        required: false
        default: disabled
        choices: ['disabled', 'v6-only', 'v4-only', 'any']
        aliases: []
    dns64_prefix:
        description:
            - Specifies DNS64 mapping IPv6 prefix.
        required: false
        default: null
        choices: []
        aliases: []
    enable_dns_express:
        description:
            - Indicates whether the dns-express service is enabled.
        required: false
        default: null
        choices: ['no', 'yes']
        aliases: []
    enable_dnssec:
        description:
            - Indicates whether to perform DNS Security Extension (DNSSEC) operations on the DNS packet, for example, respond to DNSKEY queries; add RRSIGs to response.
        required: false
        default: null
        choices: ['no', 'yes']
        aliases: []
    enable_gtm:
        description:
            - Indicates whether the Global Traffic Manager handles DNS resolution for DNS queries and responses that contain Wide IP names.
        required: false
        default: yes
        choices: ['no', 'yes']
        aliases: []
    enable_logging:
        description:
            - Indicates whether to enable high speed logging for DNS queries and responses or not.
        required: false
        default: no
        choices: ['no', 'yes']
        aliases: []
    enable_rapid_response:
        description:
            - Indicates whether to allow queries to be answered by Rapid Response.
        required: false
        default: no
        choices: ['no', 'yes']
        aliases: []
    log_profile:
        description:
            - Specifies the DNS logging profile used to configure what events get logged and their message format.
        required: false
        default: null
        choices: []
        aliases: []
    name:
        description:
            - Specifies a unique name for the component.
        required: true
        default: null
        choices: []
        aliases: []
    partition:
        description:
            - Displays the administrative partition within which the profile resides.
        required: false
        default: null
        choices: []
        aliases: []
    process_rd:
        description:
            - Indicates whether to process clientside DNS packets with Recursion Desired set in the header.
        required: false
        default: null
        choices: ['no', 'yes']
        aliases: []
    rapid_response_last_action:
        description:
            - Specifies what action to take when Rapid Response is enabled and the incoming query has not matched a DNS-Express Zone.
        required: false
        default: null
        choices: ['allow', 'drop', 'noerror', 'nxdomain', 'refuse', 'truncate']
        aliases: []
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        required: false
        default: present
        choices: ['absent', 'present']
        aliases: []
        version_added: 2.3
    unhandled_query_action:
        description:
            - Specifies the action to take when a query does not match a Wide IP or a DNS Express Zone.
        required: false
        default: null
        choices: ['allow', 'drop', 'hint', 'noerror', 'reject']
        aliases: []
    use_local_bind:
        description:
            - Indicates whether non-GTM and non-dns-express requests should be forwarded to the local BIND.
        required: false
        default: null
        choices: ['no', 'yes']
        aliases: []
'''

EXAMPLES = '''
- name: Create LTM Profile DNS
  f5bigip_ltm_profile_dns:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_dns_profile
    partition: Common
    description: My dns profile
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_LTM_PROFILE_DNS_ARGS = dict(
    app_service                         =    dict(type='str'),
    avr_dnsstat_sample_rate             =    dict(type='int'),
    defaults_from                       =    dict(type='str'),
    description                         =    dict(type='str'),
    dns64                               =    dict(type='str', choices=['disabled', 'secondary', 'immediate', 'v4-only']),
    dns64_additional_section_rewrite    =    dict(type='str', choices=['disabled', 'v6-only', 'v4-only', 'any']),
    dns64_prefix                        =    dict(type='str'),
    enable_dns_express                  =    dict(type='str', choices=F5_POLAR_CHOICES),
    enable_dnssec                       =    dict(type='str', choices=F5_POLAR_CHOICES),
    enable_gtm                          =    dict(type='str', choices=F5_POLAR_CHOICES),
    enable_logging                      =    dict(type='str', choices=F5_POLAR_CHOICES),
    enable_rapid_response               =    dict(type='str', choices=F5_POLAR_CHOICES),
    log_profile                         =    dict(type='str'),
    process_rd                          =    dict(type='str', choices=F5_POLAR_CHOICES),
    rapid_response_last_action          =    dict(type='str', choices=['allow', 'drop', 'noerror', 'nxdomain', 'refuse', 'truncate']),
    unhandled_query_action              =    dict(type='str', choices=['allow', 'drop', 'hint', 'noerror', 'reject']),
    use_local_bind                      =    dict(type='str', choices=F5_POLAR_CHOICES)
)

class F5BigIpLtmProfileDns(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.profile.dns_s.dns.create,
            'read':     self.mgmt_root.tm.ltm.profile.dns_s.dns.load,
            'update':   self.mgmt_root.tm.ltm.profile.dns_s.dns.update,
            'delete':   self.mgmt_root.tm.ltm.profile.dns_s.dns.delete,
            'exists':   self.mgmt_root.tm.ltm.profile.dns_s.dns.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}

    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_PROFILE_DNS_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpLtmProfileDns(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()