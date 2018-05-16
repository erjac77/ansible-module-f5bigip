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
module: f5bigip_ltm_profile_dhcpv6
short_description: BIG-IP ltm profile dhcpv6 module
description:
    - Configures a Dynamic Host Configuration Protocol for IPv6 (DHCPv6) profile.
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
            - Provides the default value in seconds of DHCPv6 lease time in case it was missing in the client-server
              exchange.
        default: 86400
    defaults_from:
        description:
            - Specifies the profile that you want to use as the parent profile.
        default: dhcpv6
    description:
        description:
            - User defined description.
    idle_timeout:
        description:
            - Specifies the number of seconds that a connection is idle before the connection is eligible for deletion.
        default: 60
    mode:
        description:
            - Specifies the operation mode of the DHCP virtual.
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
    remote_id_option:
        description:
            - Manages the DHCPv6 relay agent remote-id option (option 37) attributes.
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    subscriber_discovery:
        description:
            - Manages the subscriber discovery attributes.
    subscriber_id_option:
        description:
            - Manages the DHCPv6 relay agent subscriber-id option (option 38) attributes.
    transaction_timeout:
        description:
            - Specifies DHCPv6 transaction timeout, in seconds.
        default: 45
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Create LTM Profile DHCPv6
  f5bigip_ltm_profile_dhcpv6:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_dhcpv6_profile
    partition: Common
    description: My dhcpv6 profile
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
            remote_id_option=dict(type='dict'),
            subscriber_discovery=dict(type='dict'),
            subscriber_id_option=dict(type='dict'),
            transaction_timeout=dict(type='int')
        )
        argument_spec.update(F5_PROVIDER_ARGS)
        argument_spec.update(F5_NAMED_OBJ_ARGS)
        return argument_spec

    @property
    def supports_check_mode(self):
        return True


class F5BigIpLtmProfileDhcpv6(F5BigIpNamedObject):
    def _set_crud_methods(self):
        self._methods = {
            'create': self._api.tm.ltm.profile.dhcpv6s.dhcpv6.create,
            'read': self._api.tm.ltm.profile.dhcpv6s.dhcpv6.load,
            'update': self._api.tm.ltm.profile.dhcpv6s.dhcpv6.update,
            'delete': self._api.tm.ltm.profile.dhcpv6s.dhcpv6.delete,
            'exists': self._api.tm.ltm.profile.dhcpv6s.dhcpv6.exists
        }


def main():
    params = ModuleParams()
    module = AnsibleModule(argument_spec=params.argument_spec, supports_check_mode=params.supports_check_mode)

    try:
        obj = F5BigIpLtmProfileDhcpv6(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
