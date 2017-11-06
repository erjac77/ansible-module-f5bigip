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

DOCUMENTATION = '''
---
module: f5bigip_ltm_monitor_sasp
short_description: BIG-IP ltm monitor sasp module
description:
    - Configures a Server Application State Protocol (SASP) monitor.
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
    defaults_from:
        description:
            - Specifies the name of the monitor from which you want your custom monitor to inherit settings.
        required: false
        default: sasp
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
        default: auto
        choices: []
        aliases: []
    mode:
        description:
            - Specifies whether the load balancer should send Get Weight Request messages (pull) or receive Send Weights messages (push) from the GWM.
        required: false
        default: pull
        choices: ['pull', 'push']
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
    primary_address:
        description:
            - Specifies the IP address of the primary Group Workload Manager.
        required: false
        default: null
        choices: []
        aliases: []
    protocol:
        description:
            - Specifies the protocol that the monitor uses to communicate with the target.
        required: false
        default: tcp
        choices: ['tcp', 'udp']
        aliases: []
    secondary_address:
        description:
            - Specifies the IP address of the secondary Group Workload Manager.
        required: false
        default: null
        choices: []
        aliases: []
    service:
        description:
            - Specifies the port through which the SASP monitor communicates with the Group Workload Manager.
        required: false
        default: 3860
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
        default: 100
        choices: []
        aliases: []
'''

EXAMPLES = '''
- name: Create LTM Monitor SASP
  f5bigip_ltm_monitor_sasp:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_sasp_monitor
    partition: Common
    description: My sasp monitor
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_LTM_MONITOR_SASP_ARGS = dict(
    app_service          =    dict(type='str'),
    defaults_from        =    dict(type='str'),
    description          =    dict(type='str'),
    interval             =    dict(type='int'),
    mode                 =    dict(type='str', choices=['pull', 'push']),
    primary_address      =    dict(type='str'),
    protocol             =    dict(type='str', choices=['tcp', 'udp']),
    secondary_address    =    dict(type='str'),
    service              =    dict(type='int'),
    time_until_up        =    dict(type='int'),
    timeout              =    dict(type='int')
)

class F5BigIpLtmMonitorSasp(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.monitor.sasps.sasp.create,
            'read':     self.mgmt_root.tm.ltm.monitor.sasps.sasp.load,
            'update':   self.mgmt_root.tm.ltm.monitor.sasps.sasp.update,
            'delete':   self.mgmt_root.tm.ltm.monitor.sasps.sasp.delete,
            'exists':   self.mgmt_root.tm.ltm.monitor.sasps.sasp.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}

    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_MONITOR_SASP_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpLtmMonitorSasp(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()