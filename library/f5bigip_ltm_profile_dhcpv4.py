#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2016-2018, Eric Jacob <erjac77@gmail.com>
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
        suboptions:
            enabled:
                description:
                    - To enable or disable subscriber authentication.
                default: false
                choices: ['true', 'false']
            user_name:
                description:
                    - Manages the authentication user name's attributes.
                suboptions:
                    format:
                        description:
                            - Specifies the user-name format.
                        choices: ['mac-address', 'mac-and-relay-id', 'tcl-snippet']
                    suboption_id1:
                        description:
                            - The relay-agent option (option 82) first suboption ID.
                        default: 1
                    suboption_id2:
                        description:
                            - The relay-agent option (option 82) second suboption ID.
                        default: 2
                    separator1:
                        description:
                            - A string that is used to concatenate the MAC address and the relay-agent info option
                              (option 82) to create the authentication user-name.
                        default: '@'
                    separator2:
                        description:
                            - A string that is used to concatenate the relay-agent info option (option 82) suboptions 1
                              and 2 to create the authentication user-name.
                        default: '@'
                    tcl_snippet:
                        description:
                            - A tcl snippet to format the user name.
            virtual:
                description:
                    - Specifies the authentication virtual server name.
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
        suboptions:
            add:
                description:
                    - Specifies if the user wants the DHCP relay agent to insert option 82 or not.
                default: false
                choices: ['true', 'false']
            remove:
                description:
                    - Specifies if the user wants the DHCP relay agent to remove option 82 from the server-to-client
                      traffic or not.
                default: false
                choices: ['true', 'false']
            suboption:
                description:
                    - Manages the inserted relay agent information option (option 82) suboptions.
                suboptions:
                    id1:
                        description:
                            - An integer to represent the first suboption ID.
                        default: 1
                    id2:
                        description:
                            - An integer to represent the second suboption ID.
                        default: 2
                    value1:
                        description:
                            - A string to represent the first suboption value.
                    value2:
                        description:
                            - A string to represent the second suboption value.
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    subscriber_discovery:
        description:
            - Manages the subscriber discovery attributes.
        suboptions:
            enabled:
                description:
                    - To enable or disable subscriber discovery.
                default: false
                choices: ['true', 'false']
            subscriber_id:
                description:
                    - Manages the subscriber-id attributes.
                suboptions:
                    format:
                        description:
                            - Specifies the user-name format.
                        choices: ['mac-address', 'mac-and-relay-id', 'tcl-snippet']
                    suboption_id1:
                        description:
                            - The relay-agent option (option 82) first suboption ID.
                        default: 1
                    suboption_id2:
                        description:
                            - The relay-agent option (option 82) second suboption ID.
                        default: 2
                    separator1:
                        description:
                            - A string that is used to concatenate the MAC address and the relay-agent info option
                              (option 82) to create the authentication user-name.
                        default: '@'
                    separator2:
                        description:
                            - A string that is used to concatenate the relay-agent info option (option 82) suboptions 1
                              and 2 to create the authentication user-name.
                        default: '@'
                    tcl_snippet:
                        description:
                            - A tcl snippet to format the user name.
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
requirements:
    - BIG-IP >= 12.0
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

RETURN = ''' # '''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.base import F5_NAMED_OBJ_ARGS
from ansible_common_f5.base import F5_PROVIDER_ARGS
from ansible_common_f5.bigip import F5BigIpNamedObject


class ModuleParams(object):
    @property
    def argument_spec(self):
        argument_spec = dict(
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
        argument_spec.update(F5_PROVIDER_ARGS)
        argument_spec.update(F5_NAMED_OBJ_ARGS)
        return argument_spec

    @property
    def supports_check_mode(self):
        return True


class F5BigIpLtmProfileDhcpv4(F5BigIpNamedObject):
    def _set_crud_methods(self):
        self._methods = {
            'create': self._api.tm.ltm.profile.dhcpv4s.dhcpv4.create,
            'read': self._api.tm.ltm.profile.dhcpv4s.dhcpv4.load,
            'update': self._api.tm.ltm.profile.dhcpv4s.dhcpv4.update,
            'delete': self._api.tm.ltm.profile.dhcpv4s.dhcpv4.delete,
            'exists': self._api.tm.ltm.profile.dhcpv4s.dhcpv4.exists
        }


def main():
    params = ModuleParams()
    module = AnsibleModule(argument_spec=params.argument_spec, supports_check_mode=params.supports_check_mode)

    try:
        obj = F5BigIpLtmProfileDhcpv4(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
