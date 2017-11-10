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

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: f5bigip_sys_snmp_community
short_description: BIG-IP sys snmp community module
description:
    - Configures the simple network management protocol (SNMP) communities.
version_added: 2.3
author:
    - "Eric Jacob, @erjac77"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    access:
        description:
            - Specifies the community access level to the MIB.
        required: false
        default: ro
        choices: ['ro', 'rw']
        aliases: []
        version_added: 2.3
    community_name:
        description:
            - Specifies the name of the community that you are configuring for the snmpd daemon.
        required: false
        default: public
        choices: []
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
    ipv6:
        description:
            - Specifies to enable or disable IPv6 addresses for the community that you are configuring.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    oid_subset:
        description:
            - Specifies to restrict access by the community to every object below the specified object identifier (OID).
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    source:
        description:
            - Specifies the source addresses with the specified community name that can access the management information base (MIB).
        required: false
        default: default
        choices: []
        aliases: []
        version_added: 2.3
'''

EXAMPLES = '''
- name: Add SYS SNMP community
  f5bigip_sys_snmp_community:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: community1
    access: ro
    community_name: mycommunity1
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_SYS_SNMP_COMMUNITY_ARGS = dict(
    access          =   dict(type='str', choices=['ro', 'rw']),
    community_name  =   dict(type='str'),
    description     =   dict(type='str'),
    ipv6            =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    oid_subset      =   dict(type='str'),
    source          =   dict(type='str')
)

class F5BigIpSysSnmpCommunity(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.snmp = self.mgmt_root.tm.sys.snmp.load()
        self.methods = {
            'create':   self.snmp.communities_s.community.create,
            'read':     self.snmp.communities_s.community.load,
            'update':   self.snmp.communities_s.community.update,
            'delete':   self.snmp.communities_s.community.delete,
            'exists':   self.snmp.communities_s.community.exists
        }
    
    def _exists(self):
        keys = self.snmp.communities_s.get_collection()
        for key in keys:
            name = self.params['name']
            if key.name == name:
                return True

        return False

def main():
    # Translation list for conflictual params
    tr = {}
    
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_SYS_SNMP_COMMUNITY_ARGS, supports_check_mode=False)
    
    try:
        obj = F5BigIpSysSnmpCommunity(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()