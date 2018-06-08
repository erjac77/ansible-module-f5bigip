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
module: f5bigip_ltm_virtual_address
short_description: BIG-IP ltm virtual address module
description:
    - Configures virtual addresses.
version_added: "2.4"
author:
    - "Eric Jacob (@erjac77)"
options:
    address:
        description:
            - The virtual IP address.
        required: true
    app_service:
        description:
            - Specifies the application service that the object belongs to.
    arp:
        description:
            - Enables or disables ARP for the specified virtual address.
        default: enabled
        choices: ['enabled', 'disabled']
    auto_delete:
        description:
            - Indicates if the virtual address will be deleted automatically on deletion of the last associated virtual
              server or not.
        default: true
        type: bool
    connection_limit:
        description:
            - Sets a concurrent connection limit for one or more virtual servers.
        default: 0 (meaning "no limit")
    description:
        description:
            - Specifies descriptive text that identifies the component.
    enabled:
        description:
            - Specifies whether the specified virtual address is enabled.
        default: yes
        choices: ['yes', 'no']
    icmp_echo:
        description:
            - Enables or disables ICMP echo replies for the specified virtual address.
        default: enabled
        choices: ['enabled', 'disabled', 'selective']
    mask:
        description:
            - Sets the netmask for one or more network virtual servers only.
        default: 255.255.255.255
    name:
        description:
            - Specifies unique name for the component.
        required: true
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        default: Common
    route_advertisement:
        description:
            - Enables or disables route advertisement for the specified virtual address.
        default: disabled
        choices: ['enabled', 'disabled']
    server_scope:
        description:
            - Specifies the server that uses the specified virtual address.
        default: any
        choices: ['all', 'any', 'none']
    traffic_group:
        description:
            - Specifies the traffic group on which the virtual address is active.
        default: Inherited from the containing folder
requirements:
    - BIG-IP >= 12.0
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Modify LTM Virtual Address icmp-echo
  f5bigip_ltm_virtual_address:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: 10.10.20.201
    partition: Common
    icmp_echo: selective
    state: present
  delegate_to: localhost
'''

RETURN = ''' # '''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.base import F5_ACTIVATION_CHOICES
from ansible_common_f5.base import F5_NAMED_OBJ_ARGS
from ansible_common_f5.base import F5_PROVIDER_ARGS
from ansible_common_f5.bigip import F5BigIpNamedObject


class ModuleParams(object):
    @property
    def argument_spec(self):
        argument_spec = dict(
            address=dict(type='str'),
            app_service=dict(type='str'),
            arp=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            auto_delete=dict(type='bool'),
            connection_limit=dict(type='int'),
            description=dict(type='str'),
            enable=dict(type='bool'),
            icmp_echo=dict(type='str', choices=['enabled', 'disabled', 'selective']),
            mask=dict(type='str'),
            # metadata=dict(type='list'),
            route_advertisement=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            server_scope=dict(type='str', choices=['all', 'any', 'none']),
            traffic_group=dict(type='str')
        )
        argument_spec.update(F5_PROVIDER_ARGS)
        argument_spec.update(F5_NAMED_OBJ_ARGS)
        return argument_spec

    @property
    def supports_check_mode(self):
        return True


class F5BigIpLtmVirtualAddress(F5BigIpNamedObject):
    def _set_crud_methods(self):
        self._methods = {
            'create': self._api.tm.ltm.virtual_address_s.virtual_address.create,
            'read': self._api.tm.ltm.virtual_address_s.virtual_address.load,
            'update': self._api.tm.ltm.virtual_address_s.virtual_address.update,
            'delete': self._api.tm.ltm.virtual_address_s.virtual_address.delete,
            'exists': self._api.tm.ltm.virtual_address_s.virtual_address.exists
        }


def main():
    params = ModuleParams()
    module = AnsibleModule(argument_spec=params.argument_spec, supports_check_mode=params.supports_check_mode)

    try:
        obj = F5BigIpLtmVirtualAddress(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
