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
module: f5bigip_sys_snmp
short_description: BIG-IP sys snmp module
description:
    - Configures the simple network management protocol (SNMP) daemon.
version_added: "2.4"
author:
    - "Eric Jacob (@erjac77)"
options:
    agent_addresses:
        description:
            - Indicates that the SNMP agent is to listen on the specified address.
    agent_trap:
        description:
            - Specifies, when enabled, that the snmpd daemon sends traps, for example, start and stop traps.
        default: enabled
        choices: ['enabled', 'disabled']
    allowed_addresses:
        description:
            - Configures the IP addresses of the SNMP clients from which the snmpd daemon accepts requests.
        default: 127
    auth_trap:
        description:
            - Specifies, when enabled, that the snmpd daemon generates authentication failure traps.
        default: disabled
        choices: ['enabled', 'disabled']
    bigip_traps:
        description:
            - Specifies, when enabled, that the BIG-IP system sends device warning traps to the trap destinations.
        default: enabled
        choices: ['enabled', 'disabled']
    description:
        description:
            - Specifies descriptive text that identifies the component.
    l2forward_vlan:
        description:
            - Specifies the VLANs for which you want the snmpd daemon to expose Layer 2 forwarding information.
    load_max1:
        description:
            - Specifies the maximum 1-minute load average of the machine.
    load_max5:
        description:
            - Specifies the maximum 5-minute load average of the machine.
    load_max15:
        description:
            - Specifies the maximum 15-minute load average of the machine.
    sys_contact:
        description:
            - Specifies the name of the person who administers the snmpd daemon for this system.
        default: Customer Name <admin@customer.com>
    sys_location:
        description:
            - Describes this system's physical location.
        default: Network Closet 1
    sys_services:
        description:
            - Specifies the value of the system.sysServices.0 object.
        default: 78
    trap_community:
        description:
            - Specifies the community name for the trap destination.
        default: public
    trap_source:
        description:
            - Specifies the source of the SNMP trap.
requirements:
    - BIG-IP >= 12.0
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Set SYS SNMP contact, location and allowed addresses
  f5bigip_sys_snmp:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    allowed_addresses:
      - 172.16.227.0/24
      - 10.0.0./8
    sys_contact: 'admin@company.com'
    sys_location: Central Office
  delegate_to: localhost

- name: Clear SYS SNMP allowed addresses
  f5bigip_sys_snmp:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    allowed_addresses:
      - ALL
      - '127'
  delegate_to: localhost
'''

RETURN = ''' # '''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.base import F5_ACTIVATION_CHOICES
from ansible_common_f5.base import F5_PROVIDER_ARGS
from ansible_common_f5.bigip import F5BigIpUnnamedObject


class ModuleParams(object):
    @property
    def argument_spec(self):
        argument_spec = dict(
            agent_addresses=dict(type='list'),
            agent_trap=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            allowed_addresses=dict(type='list'),
            auth_trap=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            bigip_traps=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            description=dict(type='str'),
            # disk_monitors       =   dict(type='list'),
            l2forward_vlan=dict(type='list'),
            load_max1=dict(type='int'),
            load_max5=dict(type='int'),
            load_max15=dict(type='int'),
            # process_monitors    =   dict(type='list'),
            sys_contact=dict(type='str'),
            sys_location=dict(type='str'),
            sys_services=dict(type='int'),
            trap_community=dict(type='str'),
            trap_source=dict(type='str')  # ,
            # users               =   dict(type='list'),
            # v1_traps            =   dict(type='list'),
            # v2_traps            =   dict(type='list')
        )
        argument_spec.update(F5_PROVIDER_ARGS)
        return argument_spec

    @property
    def supports_check_mode(self):
        return True


class F5BigIpSysSnmp(F5BigIpUnnamedObject):
    def _set_crud_methods(self):
        self._methods = {
            'read': self._api.tm.sys.snmp.load,
            'update': self._api.tm.sys.snmp.update
        }


def main():
    params = ModuleParams()
    module = AnsibleModule(argument_spec=params.argument_spec, supports_check_mode=params.supports_check_mode)

    try:
        obj = F5BigIpSysSnmp(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
