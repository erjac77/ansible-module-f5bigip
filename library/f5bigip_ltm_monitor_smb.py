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
module: f5bigip_ltm_monitor_smb
short_description: BIG-IP ltm monitor smb module
description:
    - Configures a Server Message Bloc (SMB)/Common Internet File System (CIFS) monitor.
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
    debug:
        description:
            - Specifies whether the monitor sends error messages and additional information to a log file created and labeled specifically for this monitor.
        required: false
        default: no
        choices: ['no', 'yes']
        aliases: []
    defaults_from:
        description:
            - Specifies the name of the monitor from which you want your custom monitor to inherit settings.
        required: false
        default: smb
        choices: []
        aliases: []
    description:
        description:
            - User defined description.
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
    get:
        description:
            - Specifies a file associated with a service.
        required: false
        default: none
        choices: []
        aliases: []
    interval:
        description:
            - Specifies, in seconds, the frequency at which the system issues the monitor check when either the resource is down or the status of the resource is unknown.
        required: false
        default: 10
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
    password:
        description:
            - Specifies the password if the monitored target requires authentication.
        required: false
        default: none
        choices: []
        aliases: []
    server:
        description:
            - Specifies the NetBIOS name of the SMB/CIFS server for which this monitor checks for availability.
        required: false
        default: none
        choices: []
        aliases: []
    service:
        description:
            - Specifies a specific service on the SMB/CIFS for which you want to verify availability.
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
        default: 31
        choices: []
        aliases: []
    up_interval:
        description:
            - Specifies, in seconds, the frequency at which the system issues the monitor check when the resource is up.
        required: false
        default: 0
        choices: []
        aliases: []
    username:
        description:
            - Specifies the user name if the monitored target requires authentication.
        required: false
        default: none
        choices: []
        aliases: []
'''

EXAMPLES = '''
- name: Create LTM Monitor SMB
  f5bigip_ltm_monitor_smb:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_smb_monitor
    partition: Common
    description: My smb monitor
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_LTM_MONITOR_SMB_ARGS = dict(
    app_service      =    dict(type='str'),
    debug            =    dict(type='str', choices=F5_POLAR_CHOICES),
    defaults_from    =    dict(type='str'),
    description      =    dict(type='str'),
    destination      =    dict(type='str'),
    get              =    dict(type='str'),
    interval         =    dict(type='int'),
    manual_resume    =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    password         =    dict(type='str'),
    server           =    dict(type='str'),
    service          =    dict(type='str'),
    time_until_up    =    dict(type='int'),
    timeout          =    dict(type='int'),
    up_interval      =    dict(type='int'),
    username         =    dict(type='str')
)

class F5BigIpLtmMonitorSmb(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.monitor.smbs.smb.create,
            'read':     self.mgmt_root.tm.ltm.monitor.smbs.smb.load,
            'update':   self.mgmt_root.tm.ltm.monitor.smbs.smb.update,
            'delete':   self.mgmt_root.tm.ltm.monitor.smbs.smb.delete,
            'exists':   self.mgmt_root.tm.ltm.monitor.smbs.smb.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}

    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_MONITOR_SMB_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpLtmMonitorSmb(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()