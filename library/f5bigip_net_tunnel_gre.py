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
module: f5bigip_net_tunnel_gre
short_description: BIG-IP net tunnel gre module
description:
    - Configures a Generic Router Encapsulation (GRE) profile.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    app_service:
        description:
            - Specifies the name of the application service to which the object belongs.
    defaults_from:
        description:
            - Specifies the existing profile from which the system imports settings for the new profile.
        default: gre
    description:
        description:
            - User defined description.
    encapsulation:
        description:
            - Specifies the flavor of GRE header to use for encapsulation.
        default: standard
        choices: ['standard', 'nvgre']
    flooding_type:
        description:
            - Specifies the flooding type to use to transmit broadcast and unknown destination frames.
        choices: ['none', 'multipoint']
    name:
        description:
            - Specifies a unique name for the component.
        required: true
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        default: Common
    rx_csum:
        description:
            - Specifies whether the system verifies the checksum on received packets.
        default: disabled
        choices: ['disabled', 'enabled']
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    tx_csum:
        description:
            - Specifies whether the system includes a checksum on transmitted packets.
        default: disabled
        choices: ['disabled', 'enabled']
requirements:
    - BIG-IP >= 12.0
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Create NET Tunnel GRE
  f5bigip_net_tunnel_gre:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_gre_tunnel
    partition: Common
    description: My gre tunnel
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
            app_service=dict(type='str'),
            defaults_from=dict(type='str'),
            description=dict(type='str'),
            encapsulation=dict(type='str', choices=['standard', 'nvgre']),
            flooding_type=dict(type='str', choices=['none', 'multipoint']),
            rx_csum=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            tx_csum=dict(type='str', choices=F5_ACTIVATION_CHOICES)
        )
        argument_spec.update(F5_PROVIDER_ARGS)
        argument_spec.update(F5_NAMED_OBJ_ARGS)
        return argument_spec

    @property
    def supports_check_mode(self):
        return True


class F5BigIpNetTunnelGre(F5BigIpNamedObject):
    def _set_crud_methods(self):
        self._methods = {
            'create': self._api.tm.net.tunnels.gres.gre.create,
            'read': self._api.tm.net.tunnels.gres.gre.load,
            'update': self._api.tm.net.tunnels.gres.gre.update,
            'delete': self._api.tm.net.tunnels.gres.gre.delete,
            'exists': self._api.tm.net.tunnels.gres.gre.exists
        }


def main():
    params = ModuleParams()
    module = AnsibleModule(argument_spec=params.argument_spec, supports_check_mode=params.supports_check_mode)

    try:
        obj = F5BigIpNetTunnelGre(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
