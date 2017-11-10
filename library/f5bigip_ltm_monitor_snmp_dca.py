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
module: f5bigip_ltm_monitor_snmp_dca
short_description: BIG-IP ltm monitor snmp dca module
description:
    - Configures a Simple Network Management Protocol (SNMP) Data Center Audit monitor.
version_added: 2.3
author:
    - "Gabriel Fortin"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    agent_type:
        description:
            - Specifies the type of agent.
        required: false
        default: ucd
        choices: []
        aliases: []
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
    cpu_threshold:
        description:
            - Specifies the maximum acceptable CPU usage on the target server.
        required: false
        default: 80
        choices: []
        aliases: []
    defaults_from:
        description:
            - Specifies the name of the monitor from which you want your custom monitor to inherit settings.
        required: false
        default: snmp_dca
        choices: []
        aliases: []
    description:
        description:
            - User defined description.
        required: false
        default: null
        choices: []
        aliases: []
    disk_coefficient:
        description:
            - Specifies the coefficient that the system uses to calculate the weight of the disk threshold in the dynamic ratio load balancing algorithm.
        required: false
        default: 2.0
        choices: []
        aliases: []
    disk_threshold:
        description:
            - Specifies the maximum acceptable disk usage on the target server.
        required: false
        default: 90
        choices: []
        aliases: []
    interval:
        description:
            - Specifies the frequency at which the system issues the monitor check.
        required: false
        default: 10
        choices: []
        aliases: []
    memory_coefficient:
        description:
            - Specifies the coefficient that the system uses to calculate the weight of the memory threshold in the dynamic ratio load balancing algorithm.
        required: false
        default: 1.0
        choices: []
        aliases: []
    memory_threshold:
        description:
            - Specifies the maximum acceptable memory usage on the target server.
        required: false
        default: 70
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
            - Specifies attributes for a monitor that you define.
        required: false
        default: none
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
- name: Create LTM Monitor SNMP DCA
  f5bigip_ltm_monitor_snmp_dca:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_snmp_dca_monitor
    partition: Common
    description: My snmp dca monitor
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_LTM_MONITOR_SNMP_DCA_ARGS = dict(
    agent_type            =    dict(type='str', choices=['generic', 'other', 'win2000', 'ucd']),
    app_service           =    dict(type='str'),
    community             =    dict(type='str'),
    cpu_coefficient       =    dict(type='int'),
    cpu_threshold         =    dict(type='int'),
    defaults_from         =    dict(type='str'),
    description           =    dict(type='str'),
    disk_coefficient      =    dict(type='int'),
    disk_threshold        =    dict(type='int'),
    interval              =    dict(type='int'),
    memory_coefficient    =    dict(type='int'),
    memory_threshold      =    dict(type='int'),
    time_until_up         =    dict(type='int'),
    timeout               =    dict(type='int'),
    user_defined          =    dict(type='str'),
    version               =    dict(type='int')
)

class F5BigIpLtmMonitorSnmpDca(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.monitor.snmp_dcas.snmp_dca.create,
            'read':     self.mgmt_root.tm.ltm.monitor.snmp_dcas.snmp_dca.load,
            'update':   self.mgmt_root.tm.ltm.monitor.snmp_dcas.snmp_dca.update,
            'delete':   self.mgmt_root.tm.ltm.monitor.snmp_dcas.snmp_dca.delete,
            'exists':   self.mgmt_root.tm.ltm.monitor.snmp_dcas.snmp_dca.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}

    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_MONITOR_SNMP_DCA_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpLtmMonitorSnmpDca(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()