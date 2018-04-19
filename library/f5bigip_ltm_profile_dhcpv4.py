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
module: f5bigip_ltm_profile_dhcpv4
short_description: BIG-IP ltm profile dhcpv4 module
description:
    - Configures a Dynamic Host Configuration Protocol (DHCP) profile.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    app_service:
        description:
            - Specifies the name of the application service to which the profile belongs.
    authentication:
        description:
            - Manages the subscriber authentication attributes.
    default_lease_time:
        description:
            - Provides the default value in seconds of DHCPv4 lease time in case it was missing in the client-server
              exchange.
        default: 86400
    defaults_from:
        description:
            - Specifies the profile that you want to use as the parent profile.
        default: dhcpv4
    description:
        description:
            - User defined description.
    idle_timeout:
        description:
            - Specifies the number of seconds that a connection is idle before the connection is eligible for deletion.
        default: 60
    mode:
        description:
            - Specifies the operation mode of the DHCP virtual. If the virtual to run in relay mode, then it means that
              it is acting as a standard DHCPv4 relay agent.
        default: relay
        choices: ['relay', 'forwarding']
    name:
        description:
            - Specifies a unique name for the component.
        required: true
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        default: Common
    relay_agent_id:
        description:
            - Manages the relay agent information option (option 82) attributes.
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    subscriber_discovery:
        description:
            - Manages the subscriber discovery attributes.
    transaction_timeout:
        description:
            - Specifies DHCPv4 transaction timeout, in seconds.
        default: 45
    ttl_dec_value:
        description:
            - Specifies the amount that the DHCP virtual will use to decrement the ttl for each outgoing DHCP packet.
        default: by-1
        choices: ['by-0', 'by-1', 'by-2', 'by-3', 'by-4']
    ttl_value:
        description:
            - Specifies the ttl absolute value that the user may want to set for each outgoing DHCP packet.
        default: 0
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Create LTM Profile DHCPv4
  f5bigip_ltm_profile_dhcpv4:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_dhcpv4_profile
    partition: Common
    description: My dhcpv4 profile
    state: present
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_LTM_PROFILE_DHCPV4_ARGS = dict(
    app_service=dict(type='str'),
    authentication=dict(type='dict'),
    default_lease_time=dict(type='int'),
    defaults_from=dict(type='str'),
    description=dict(type='str'),
    idle_timeout=dict(type='int'),
    mode=dict(type='str', choices=['relay', 'forwarding']),
    relay_agent_id=dict(type='dict'),
    subscriber_discovery=dict(type='dict'),
    transaction_timeout=dict(type='int'),
    ttl_dec_value=dict(type='str', choices=['by-0', 'by-1', 'by-2', 'by-3', 'by-4']),
    ttl_value=dict(type='int')
)


class F5BigIpLtmProfileDhcpv4(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create': self.mgmt_root.tm.ltm.profile.dhcpv4s.dhcpv4.create,
            'read': self.mgmt_root.tm.ltm.profile.dhcpv4s.dhcpv4.load,
            'update': self.mgmt_root.tm.ltm.profile.dhcpv4s.dhcpv4.update,
            'delete': self.mgmt_root.tm.ltm.profile.dhcpv4s.dhcpv4.delete,
            'exists': self.mgmt_root.tm.ltm.profile.dhcpv4s.dhcpv4.exists
        }


def main():
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_PROFILE_DHCPV4_ARGS, supports_check_mode=True)

    try:
        obj = F5BigIpLtmProfileDhcpv4(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
