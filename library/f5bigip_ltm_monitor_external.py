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
module: f5bigip_ltm_monitor_external
short_description: BIG-IP ltm monitor external module
description:
    - Configures an external monitor.
version_added: 2.3
author:
    - "Gabriel Fortin"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    args:
        description:
            - Specifies any command-line arguments that the external program requires.
        required: false
        default: none
        choices: []
        aliases: []
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
        default: external
        choices: []
        aliases: []
    description:
        description:
            - Specifies descriptive text that identifies the component.
        required: false
        default: null
        choices: []
        aliases: []
    destination:
        description:
            - Specifies the IP address and service port of the resource that is the destination of this monitor.
        required: false
        default: null
        choices: []
        aliases: []
    interval:
        description:
            - Specifies, in seconds, the frequency at which the system issues the monitor check when either the resource is down or the status of the resource is unknown.
        required: false
        default: 5
        choices: []
        aliases: []
    manual_resume:
        description:
            - Specifies whether the system automatically changes the status of a resource to up at the next successful monitor check.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
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
    run:
        description:
            - Specifies the path and file name of a program to run as the external monitor, for example /config/monitors/myMonitor.
        required: false
        default: none
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
    up_interval:
        description:
            - Specifies, in seconds, the frequency at which the system issues the monitor check when the resource is up.
        required: false
        default: 0
        choices: []
        aliases: []
'''

EXAMPLES = '''
- name: Create LTM Monitor External
  f5bigip_ltm_monitor_external:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_external_monitor
    partition: Common
    description: My external monitor
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_LTM_MONITOR_EXTERNAL_ARGS = dict(
    args            =   dict(type='str'),
    app_service     =   dict(type='str'),
    defaults_from   =   dict(type='str'),
    description     =   dict(type='str'),
    destination     =   dict(type='str'),
    interval        =   dict(type='int'),
    manual_resume   =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    run             =   dict(type='str'),
    time_until_up   =   dict(type='int'),
    timeout         =   dict(type='int'),
    user_defined    =   dict(type='str'),
    up_interval     =   dict(type='int')
)

class F5BigIpLtmMonitorExternal(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.monitor.externals.external.create,
            'read':     self.mgmt_root.tm.ltm.monitor.externals.external.load,
            'update':   self.mgmt_root.tm.ltm.monitor.externals.external.update,
            'delete':   self.mgmt_root.tm.ltm.monitor.externals.external.delete,
            'exists':   self.mgmt_root.tm.ltm.monitor.externals.external.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}

    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_MONITOR_EXTERNAL_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpLtmMonitorExternal(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()