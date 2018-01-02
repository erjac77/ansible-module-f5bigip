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
module: f5bigip_ltm_monitor_dns
short_description: BIG-IP ltm monitor dns module
description:
    - Configures a Domain Name System (DNS) monitor.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    accept_rcode:
        description:
            - Specifies the RCODE required in the response for an 'up' status.
        default: no-error
        choices: ['no-error', 'anything']
    adaptive:
        description:
            - Specifies whether the adaptive feature is enabled for this monitor.
    adaptive_divergence_type:
        description:
            - Specifies whether the adaptive-divergence-value is relative or absolute.
        choices: ['relative', 'absolute']
    adaptive_divergence_value:
        description:
            - Specifies how far from mean latency each monitor probe is allowed to be.
    adaptive_limit:
        description:
            - Specifies the hard limit, in milliseconds, which the probe is not allowed to exceed, regardless of the
              divergence value.
    adaptive_sampling_timespan:
        description:
            - Specifies the size of the sliding window, in seconds, which records probe history.
    answer_contains:
        description:
            - Specifies the record types required in the answer section of the response in order to mark the status of a
              node up.
        default: query-type
        choices: ['query-type', 'any-type', 'anything']
    app_service:
        description:
            - Specifies the name of the application service to which the monitor belongs.
    defaults_from:
        description:
            - Specifies the name of the monitor from which you want your custom monitor to inherit settings.
        default: dns
    description:
        description:
            - Specifies descriptive text that identifies the component.
    destination:
        description:
            - Specifies the IP address and service port of the resource that is the destination of this monitor.
    interval:
        description:
            - Specifies, in seconds, the frequency at which the system issues the monitor check when either the resource
              is down or the status of the resource is unknown.
        default: 5
    manual_resume:
        description:
            - Specifies whether the system automatically changes the status of a resource to up at the next successful
              monitor check.
        default: disabled
        choices: ['enabled', 'disabled']
    name:
        description:
            - Specifies a unique name for the component.
        required: true
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        default: Common
    qname:
        description:
            - Specifies the query name that the monitor send a DNS query for.
        required: False
        default: Enter a query name
    qtype:
        description:
            - Specifies the query type of that the monitor sends a query.
        choices: ['a', 'aaa']
    recv:
        description:
            - Specifies the ip address that the monitor looks for in the dns response's resource record sections.
    reverse:
        description:
            - Specifies whether the monitor operates in reverse mode.
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    time_until_up:
        description:
            - Specifies the amount of time, in seconds, after the first successful response before a node is marked up.
        default: 0
    timeout:
        description:
            - Specifies the number of seconds the target has in which to respond to the monitor request.
        default: 16
    transparent:
        description:
            - Specifies whether the monitor operates in transparent mode.
        default: disabled
        choices: ['enabled', 'disabled']
    up_interval:
        description:
            - Specifies, in seconds, the frequency at which the system issues the monitor check when the resource is up.
        default: 0
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
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

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_LTM_MONITOR_DNS_ARGS = dict(
    accept_rcode=dict(type='str', choices=['no-error', 'anything']),
    adaptive=dict(type='str', choices=F5_ACTIVATION_CHOICES),
    adaptive_divergence_type=dict(type='str', choices=['absolute', 'relative']),
    adaptive_divergence_value=dict(type='int'),
    adaptive_limit=dict(type='int'),
    adaptive_sampling_timespan=dict(type='int'),
    answer_contains=dict(type='str', choices=['query-type', 'any-type', 'anything']),
    app_service=dict(type='str'),
    defaults_from=dict(type='str'),
    description=dict(type='str'),
    destination=dict(type='str'),
    interval=dict(type='int'),
    manual_resume=dict(type='int', choices=F5_ACTIVATION_CHOICES),
    qname=dict(type='str'),
    qtype=dict(type='str', choices=['a', 'aaa']),
    recv=dict(type='str'),
    reverse=dict(type='str', choices=F5_ACTIVATION_CHOICES),
    time_until_up=dict(type='int'),
    timeout=dict(type='int'),
    transparent=dict(type='str', choices=F5_ACTIVATION_CHOICES),
    up_interval=dict(type='int')
)


class F5BigIpLtmMonitorDns(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create': self.mgmt_root.tm.ltm.monitor.dns_s.dns.create,
            'read': self.mgmt_root.tm.ltm.monitor.dns_s.dns.load,
            'update': self.mgmt_root.tm.ltm.monitor.dns_s.dns.update,
            'delete': self.mgmt_root.tm.ltm.monitor.dns_s.dns.delete,
            'exists': self.mgmt_root.tm.ltm.monitor.dns_s.dns.exists
        }


def main():
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_MONITOR_DNS_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpLtmMonitorDns(check_mode=module.supports_check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
