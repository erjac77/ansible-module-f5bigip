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
module: f5bigip_ltm_monitor_dns
short_description: BIG-IP ltm monitor dns module
description:
    - Configures a Domain Name System (DNS) monitor.
version_added: 2.3
author:
    - "Gabriel Fortin"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    accept_rcode:
        description:
            - Specifies the RCODE required in the response for an 'up' status.
        required: false
        default: no-error
        choices: ['no-error', 'anything']
        aliases: []
    adaptive:
        description:
            - Specifies whether the adaptive feature is enabled for this monitor.
        required: false
        default: null
        choices: []
        aliases: []
    adaptive_divergence_type:
        description:
            - Specifies whether the adaptive-divergence-value is relative or absolute.
        required: false
        default: null
        choices: ['relative', 'absolute']
        aliases: []
    adaptive_divergence_value:
        description:
            - Specifies how far from mean latency each monitor probe is allowed to be.
        required: false
        default: null
        choices: []
        aliases: []
    adaptive_limit:
        description:
            - Specifies the hard limit, in milliseconds, which the probe is not allowed to exceed, regardless of the divergence value.
        required: false
        default: null
        choices: []
        aliases: []
    adaptive_sampling_timespan:
        description:
            - Specifies the size of the sliding window, in seconds, which records probe history.
        required: false
        default: null
        choices: []
        aliases: []
    answer_contains:
        description:
            - Specifies the record types required in the answer section of the response in order to mark the status of a node up.
        required: false
        default: query-type
        choices: ['query-type', 'any-type', 'anything']
        aliases: []
    app_service:
        description:
            - Specifies the name of the application service to which the monitor belongs.
        required: false
        default: none
        choices: []
        aliases: []
    defaults_from:
        description:
            - Specifies the name of the monitor from which you want your custom monitor to inherit settings.
        required: false
        default: dns
        choices: []
        aliases: []
    description:
        description:
            - Specifies descriptive text that identifies the component.
        required: false
        default: null
        choices: []
        aliases: []
    destination:
        description:
            - Specifies the IP address and service port of the resource that is the destination of this monitor.
        required: false
        default: null
        choices: []
        aliases: []
    interval:
        description:
            - Specifies, in seconds, the frequency at which the system issues the monitor check when either the resource is down or the status of the resource is unknown.
        required: false
        default: 5
        choices: []
        aliases: []
    manual_resume:
        description:
            - Specifies whether the system automatically changes the status of a resource to up at the next successful monitor check.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
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
            - Specifies the administrative partition in which the component object resides.
        required: false
        default: Common
        choices: []
        aliases: []
    qname:
        description:
            - Specifies the query name that the monitor send a DNS query for.
        required: False
        default: Enter a query name
        choices: []
        aliases: []
    qtype:
        description:
            - Specifies the query type of that the monitor sends a query.
        required: false
        default: null
        choices: ['a', 'aaa']
        aliases: []
    recv:
        description:
            - Specifies the ip address that the monitor looks for in the dns response's resource record sections.
        required: false
        default: null
        choices: []
        aliases: []
    reverse:
        description:
            - Specifies whether the monitor operates in reverse mode.
        required: false
        default: null
        choices: []
        aliases: []
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        required: false
        default: present
        choices: ['absent', 'present']
        aliases: []
    time_until_up:
        description:
            - Specifies the amount of time, in seconds, after the first successful response before a node is marked up.
        required: false
        default: 0
        choices: []
        aliases: []
    timeout:
        description:
            - Specifies the number of seconds the target has in which to respond to the monitor request.
        required: false
        default: 16
        choices: []
        aliases: []
    transparent:
        description:
            - Specifies whether the monitor operates in transparent mode.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
    up_interval:
        description:
            - Specifies, in seconds, the frequency at which the system issues the monitor check when the resource is up.
        required: false
        default: 0
        choices: []
        aliases: []
'''

EXAMPLES = '''
- name: Create LTM Monitor DNS
  f5bigip_ltm_monitor_dns:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_dns_monitor
    partition: Common
    description: My dns monitor
    qname: www.test.com
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_LTM_MONITOR_DNS_ARGS = dict(
    accept_rcode                =   dict(type='str', choices=['no-error', 'anything']),
    adaptive                    =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    adaptive_divergence_type    =   dict(type='str', choices=['absolute', 'relative']),
    adaptive_divergence_value   =   dict(type='int'),
    adaptive_limit              =   dict(type='int'),
    adaptive_sampling_timespan  =   dict(type='int'),
    answer_contains             =   dict(type='str', choices=['query-type', 'any-type', 'anything']),
    app_service                 =   dict(type='str'),
    defaults_from               =   dict(type='str'),
    description                 =   dict(type='str'),
    destination                 =   dict(type='str'),
    interval                    =   dict(type='int'),
    manual_resume               =   dict(type='int', choices=F5_ACTIVATION_CHOICES),
    qname                       =   dict(type='str'),
    qtype                       =   dict(type='str', choices=['a', 'aaa']),
    recv                        =   dict(type='str'),
    reverse                     =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    time_until_up               =   dict(type='int'),
    timeout                     =   dict(type='int'),
    transparent                 =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    up_interval                 =   dict(type='int')
)

class F5BigIpLtmMonitorDns(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.monitor.dns_s.dns.create,
            'read':     self.mgmt_root.tm.ltm.monitor.dns_s.dns.load,
            'update':   self.mgmt_root.tm.ltm.monitor.dns_s.dns.update,
            'delete':   self.mgmt_root.tm.ltm.monitor.dns_s.dns.delete,
            'exists':   self.mgmt_root.tm.ltm.monitor.dns_s.dns.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}

    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_MONITOR_DNS_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpLtmMonitorDns(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()