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
module: f5bigip_ltm_monitor_snmp_dca_base
short_description: BIG-IP ltm monitor snmp dca base module
description:
    - Configures a base Simple Network Management Protocol (SNMP) Data Center Audit monitor.
version_added: 2.3
author:
    - "Gabriel Fortin"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    app_service:
        description:
            - Specifies the name of the application service to which the monitor belongs.
        required: false
        default: none
        choices: []
        aliases: []
    community:
        description:
            - Specifies the community name that the BIG-IP system must use to authenticate with the host server through SNMP.
        required: false
        default: public
        choices: []
        aliases: []
    cpu_coefficient:
        description:
            - Specifies the coefficient that the system uses to calculate the weight of the CPU threshold in the dynamic ratio load balancing algorithm.
        required: false
        default: 1.5
        choices: []
        aliases: []
    defaults_from:
        description:
            - Specifies the name of the monitor from which you want your custom monitor to inherit settings.
        required: false
        default: snmp_dca_base
        choices: []
        aliases: []
    description:
        description:
            - User defined description.
        required: false
        default: null
        choices: []
        aliases: []
    interval:
        description:
            - Specifies the frequency at which the system issues the monitor check.
        required: false
        default: 10
        choices: []
        aliases: []
    name:
        description:
            - Specifies a unique name for the component.
        required: true
        default: null
        choices: []
        aliases: []
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        required: false
        default: Common
        choices: []
        aliases: []
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        required: false
        default: present
        choices: ['absent', 'present']
        aliases: []
    time_until_up:
        description:
            - Specifies the amount of time, in seconds, after the first successful response before a node is marked up.
        required: false
        default: 0
        choices: []
        aliases: []
    timeout:
        description:
            - Specifies the number of seconds the target has in which to respond to the monitor request.
        required: false
        default: 30
        choices: []
        aliases: []
    user_defined:
        description:
            - Specifies any user-defined command-line arguments and variables that the external program requires.
        required: false
        default: null
        choices: []
        aliases: []
    version:
        description:
            - Specifies the version of SNMP that the host server uses.
        required: false
        default: none
        choices: []
        aliases: []
'''

EXAMPLES = '''
- name: Create LTM Monitor SNMP DCA Base
  f5bigip_ltm_monitor_snmp_dca_base:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_snmp_dca_base_monitor
    partition: Common
    description: My snmp dca base monitor
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_LTM_MONITOR_SNMP_DCA_BASE_ARGS = dict(
    app_service        =    dict(type='str'),
    community          =    dict(type='str'),
    cpu_coefficient    =    dict(type='int'),
    defaults_from      =    dict(type='str'),
    description        =    dict(type='str'),
    interval           =    dict(type='int'),
    time_until_up      =    dict(type='int'),
    timeout            =    dict(type='int'),
    user_defined       =    dict(type='str'),
    version            =    dict(type='int')
)

class F5BigIpLtmMonitorSnmpDcaBase(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.monitor.snmp_dca_bases.snmp_dca_base.create,
            'read':     self.mgmt_root.tm.ltm.monitor.snmp_dca_bases.snmp_dca_base.load,
            'update':   self.mgmt_root.tm.ltm.monitor.snmp_dca_bases.snmp_dca_base.update,
            'delete':   self.mgmt_root.tm.ltm.monitor.snmp_dca_bases.snmp_dca_base.delete,
            'exists':   self.mgmt_root.tm.ltm.monitor.snmp_dca_bases.snmp_dca_base.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}

    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_MONITOR_SNMP_DCA_BASE_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpLtmMonitorSnmpDcaBase(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()