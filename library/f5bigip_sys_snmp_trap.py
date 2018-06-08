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
module: f5bigip_sys_snmp_trap
short_description: BIG-IP sys snmp trap module
description:
    - Configures the simple network management protocol (SNMP) traps.
version_added: "2.4"
author:
    - "Eric Jacob (@erjac77)"
options:
    auth_password:
        description:
            - Specifies the authentication password, which must be at least eight characters long.
    auth_protocol:
        description:
            - Specifies the authentication method to use to deliver the trap message.
        choices: ['md5', 'sha', 'none']
    community:
        description:
            - Specifies a community that has access to the trap message.
    description:
        description:
            - Specifies descriptive text that identifies the component.
    engine_id:
        description:
            - Specifies the unique authoritative security engine ID.
    host:
        description:
            - Specifies the trap destination that you are configuring, the IP address, FQDN, or either of these with an
              embedded protocol.
        required: true
    port:
        description:
            - Specifies the port for the trap destination that you are configuring.
        default: 162
    privacy_password:
        description:
            - Specifies the privacy password, which must be at least eight characters long.
    privacy_protocol:
        description:
            - Specifies the encryption/privacy method to use to deliver the trap message.
        choices: ['aes', 'des', 'none']
    security_level:
        description:
            - Specifies the security level to use to deliver the trap message.
        default: no-auth-no-privacy
        choices: ['auth-no-privacy', 'auth-privacy', 'no-auth-no-privacy']
    security_name:
        description:
            - Specifies the security name the system uses to handle SNMP version 3 trap message.
    version:
        description:
            - Specifies the security model to use.
        default: 2c
        choices: ['1', '2c', '3']
requirements:
    - BIG-IP >= 12.0
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Add SYS SNMP trap
  f5bigip_sys_snmp_trap:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: i172_16_227_140_1
    community: mycommunity1
    host: 10.20.20.21
    port: 162
    version: 2c
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
            auth_password=dict(type='str', no_log=True),
            auth_protocol=dict(type='str', choices=['md5', 'sha', 'none']),
            community=dict(type='str'),
            description=dict(type='str'),
            engine_id=dict(type='str'),
            host=dict(type='str'),
            port=dict(type='int'),
            privacy_password=dict(type='str', no_log=True),
            privacy_protocol=dict(type='str', choices=['aes', 'des', 'none']),
            security_level=dict(type='str', choices=['auth-no-privacy', 'auth-privacy', 'no-auth-no-privacy']),
            security_name=dict(type='str'),
            version=dict(type='str', choices=['1', '2c', '3'])
        )
        argument_spec.update(F5_PROVIDER_ARGS)
        argument_spec.update(F5_NAMED_OBJ_ARGS)
        del argument_spec['partition']
        return argument_spec

    @property
    def supports_check_mode(self):
        return True


class F5BigIpSysSnmpTrap(F5BigIpNamedObject):
    def _set_crud_methods(self):
        snmp = self._api.tm.sys.snmp.load()
        self._methods = {
            'create': snmp.traps_s.trap.create,
            'read': snmp.traps_s.trap.load,
            'modify': snmp.traps_s.trap.modify,
            'delete': snmp.traps_s.trap.delete,
            'exists': snmp.traps_s.trap.exists
        }


def main():
    params = ModuleParams()
    module = AnsibleModule(argument_spec=params.argument_spec, supports_check_mode=params.supports_check_mode)

    try:
        obj = F5BigIpSysSnmpTrap(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
