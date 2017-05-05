#!/usr/bin/python
#
# Copyright 2016, Eric Jacob <erjac77@gmail.com>
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
module: f5bigip_sys_snmp
short_description: BIG-IP sys snmp module
description:
    - Configures the simple network management protocol (SNMP) daemon.
version_added: 2.3
author:
    - "Eric Jacob, @erjac77"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    agent_addresses:
        description:
            - Indicates that the SNMP agent is to listen on the specified address.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    agent_trap:
        description:
            - Specifies, when enabled, that the snmpd daemon sends traps, for example, start and stop traps.
        required: false
        default: enabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    allowed_addresses:
        description:
            - Configures the IP addresses of the SNMP clients from which the snmpd daemon accepts requests.
        required: false
        default: 127
        choices: []
        aliases: []
        version_added: 2.3
    auth_trap:
        description:
            - Specifies, when enabled, that the snmpd daemon generates authentication failure traps.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    bigip_traps:
        description:
            - Specifies, when enabled, that the BIG-IP system sends device warning traps to the trap destinations.
        required: false
        default: enabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    description:
        description:
            - Specifies descriptive text that identifies the component.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    l2forward_vlan:
        description:
            - Specifies the VLANs for which you want the snmpd daemon to expose Layer 2 forwarding information.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    load_max1:
        description:
            - Specifies the maximum 1-minute load average of the machine.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    load_max5:
        description:
            - Specifies the maximum 5-minute load average of the machine.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    load_max15:
        description:
            - Specifies the maximum 15-minute load average of the machine.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    sys_contact:
        description:
            - Specifies the name of the person who administers the snmpd daemon for this system.
        required: false
        default: Customer Name <admin@customer.com>
        choices: []
        aliases: []
        version_added: 2.3
    sys_location:
        description:
            - Describes this system's physical location.
        required: false
        default: Network Closet 1
        choices: []
        aliases: []
        version_added: 2.3
    sys_services:
        description:
            - Specifies the value of the system.sysServices.0 object.
        required: false
        default: 78
        choices: []
        aliases: []
        version_added: 2.3
    trap_community:
        description:
            - Specifies the community name for the trap destination.
        required: false
        default: public
        choices: []
        aliases: []
        version_added: 2.3
    trap_source:
        description:
            - Specifies the source of the SNMP trap.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
'''

EXAMPLES = '''
- name: Add SYS SNMP contact, location and allowed addresses
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
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_SYS_SNMP_ARGS = dict(
    agent_addresses     =   dict(type='list'),
    agent_trap          =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    allowed_addresses   =   dict(type='list'),
    auth_trap           =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    bigip_traps         =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    description         =   dict(type='str'),
    #disk_monitors       =   dict(type='list'),
    l2forward_vlan      =   dict(type='list'),
    load_max1           =   dict(type='int'),
    load_max5           =   dict(type='int'),
    load_max15          =   dict(type='int'),
    #process_monitors    =   dict(type='list'),
    sys_contact         =   dict(type='str'),
    sys_location        =   dict(type='str'),
    sys_services        =   dict(type='int'),
    trap_community      =   dict(type='str'),
    trap_source         =   dict(type='str')#,
    #users               =   dict(type='list'),
    #v1_traps            =   dict(type='list'),
    #v2_traps            =   dict(type='list')
)

class F5BigIpSysSnmp(F5BigIpUnnamedObject):
    def set_crud_methods(self):
        self.methods = {
            'read':     self.mgmt_root.tm.sys.snmp.load,
            'update':   self.mgmt_root.tm.sys.snmp.update
        }
    
    def _absent(self):
        if not (self.params['agentAddresses'] or self.params['allowedAddresses']):
            raise AnsibleModuleF5BigIpError("Absent can only be used when removing Agent Addresses or Allowed Addresses")
        
        return super(F5BigIpSysSnmp, self)._absent()

def main():
    # Translation list for conflictual params
    tr = {}
    
    module = AnsibleModuleF5BigIpUnnamedObject(argument_spec=BIGIP_SYS_SNMP_ARGS, supports_check_mode=False)
    
    try:
        obj = F5BigIpSysSnmp(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()