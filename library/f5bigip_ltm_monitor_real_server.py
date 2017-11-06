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
module: f5bigip_ltm_monitor_real_server
short_description: BIG-IP ltm monitor real server module
description:
    - Configures a RealServer monitor.
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
        default: real-server
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
        default: 5
        choices: []
        aliases: []
    metrics:
        description:
            - Specifies the performance metrics that the commands collect from the target.
        required: false
        default: ServerBandwidth:1.5, CPUPercentUsage, MemoryUsage, TotalClientCount
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
        default: 16
        choices: []
        aliases: []
'''

EXAMPLES = '''
- name: Create LTM Monitor RealServer
  f5bigip_ltm_monitor_real_server:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_real_server_monitor
    partition: Common
    description: My real server monitor
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_LTM_MONITOR_REAL_SERVER_ARGS = dict(
    app_service      =    dict(type='str'),
    defaults_from    =    dict(type='str'),
    description      =    dict(type='str'),
    interval         =    dict(type='int'),
    metrics          =    dict(type='str'),
    time_until_up    =    dict(type='int'),
    timeout          =    dict(type='int')
)

class F5BigIpLtmMonitorRealServer(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.monitor.real_servers.real_server.create,
            'read':     self.mgmt_root.tm.ltm.monitor.real_servers.real_server.load,
            'update':   self.mgmt_root.tm.ltm.monitor.real_servers.real_server.update,
            'delete':   self.mgmt_root.tm.ltm.monitor.real_servers.real_server.delete,
            'exists':   self.mgmt_root.tm.ltm.monitor.real_servers.real_server.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}

    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_MONITOR_REAL_SERVER_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpLtmMonitorRealServer(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()