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
module: f5bigip_net_dns_resolver
short_description: BIG-IP net dns_resolver module
description:
    - Configures a DNS resolver on the BIG-IP system.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    answer_default_zones:
        description:
            - Specifies whether the resolver answers queries for default zones: localhost, reverse 127.0.0.1 and ::1,
              and AS112 zones.
        default: no
        choices: ['yes', 'no']
    cache_size:
        description:
            - Specifies the maximum cache size in bytes of the DNS Resolver object.
        default: 5767168
    forward-zones:
        description:
            - Adds, deletes, modifies, or replaces a set of forward zones on a DNS Resolver, by specifying zone name(s).
    name:
        description:
            - Specifies unique name for the component.
        required: true
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        default: Common
    randomize_query_name_case:
        description:
            - Specifies whether the resolver randomizes the case of query names.
        default: yes
        choices: ['yes', 'no']
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    route_domain:
        description:
            - Specifies the route domain the resolver uses for outbound traffic.
    use_ipv4:
        description:
            - Specifies whether the resolver sends DNS queries to IPv4 addresses.
        default: yes
        choices: ['yes', 'no']
    use_ipv6:
        description:
            - Specifies whether the resolver sends DNS queries to IPv6 addresses.
        default: yes
        choices: ['yes', 'no']
    use_tcp:
        description:
            - Specifies whether the resolver can send queries over the TCP protocol.
        default: yes
        choices: ['yes', 'no']
    use_udp:
        description:
            - Specifies whether the resolver can send queries over the UDP protocol.
        default: yes
        choices: ['yes', 'no']
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Create NET DNS Resolver
  f5bigip_net_dns_resolver:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_dns_resolver
    partition: Common
    use_ipv6: no
    state: present
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_NET_DNS_RESOLVER_ARGS = dict(
    answer_default_zones=dict(type='str', choices=F5_POLAR_CHOICES),
    cache_size=dict(type='int'),
    # forward_zones=dict(type='list'),
    randomize_query_name_case=dict(type='str', choices=F5_POLAR_CHOICES),
    route_domain=dict(type='str'),
    use_ipv4=dict(type='str', choices=F5_POLAR_CHOICES),
    use_ipv6=dict(type='str', choices=F5_POLAR_CHOICES),
    use_tcp=dict(type='str', choices=F5_POLAR_CHOICES),
    use_udp=dict(type='str', choices=F5_POLAR_CHOICES)
)


class F5BigIpNetDnsResolver(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create': self.mgmt_root.tm.net.dns_resolvers.dns_resolver.create,
            'read': self.mgmt_root.tm.net.dns_resolvers.dns_resolver.load,
            'update': self.mgmt_root.tm.net.dns_resolvers.dns_resolver.update,
            'delete': self.mgmt_root.tm.net.dns_resolvers.dns_resolver.delete,
            'exists': self.mgmt_root.tm.net.dns_resolvers.dns_resolver.exists
        }


def main():
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_NET_DNS_RESOLVER_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpNetDnsResolver(check_mode=module.supports_check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
