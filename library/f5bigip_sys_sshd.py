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
module: f5bigip_sys_sshd
short_description: BIG-IP sys sshd module
description:
    - Configures the Secure Shell (SSH) daemon for the BIG-IP system.
version_added: "1.0"
author:
    - "Eric Jacob, @erjac77"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    allow:
        description:
            - Configures servers in the /etc/hosts.allow file.
        required: false
        default: all
        choices: []
        aliases: []
        version_added: 1.0
    banner:
        description:
            - Enables or disables the display of the banner text field when a user logs in to the system using SSH.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 1.0
    banner_text:
        description:
            - When the banner option is enabled, specifies the text to include in the banner that displays when a user attempts to log on to the system.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 1.0
    inactivity_timeout:
        description:
            - Specifies the number of seconds before inactivity causes an SSH session to log out.
        required: false
        default: 0
        choices: []
        aliases: []
        version_added: 1.0
    login:
        description:
            - Enables or disables SSH logins to the system.
        required: false
        default: enabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 1.0
    log_level:
        description:
            - Specifies the minimum sshd message level to include in the system log.
        required: false
        default: null
        choices: ['debug', 'debug1', 'debug2', 'debug3', 'error', 'fatal', 'info', 'quiet', 'verbose']
        aliases: []
        version_added: 1.0
'''

EXAMPLES = '''
- name: Add SYS HTTPD allow clients
  f5bigip_sys_sshd:
    f5bigip_hostname: "172.16.227.35"
    f5bigip_username: "admin"
    f5bigip_password: "admin"
    f5bigip_port: "443"
    allow:
      - 172.16.227.11
      - 172.16.227.12
    state: "present"
  delegate_to: localhost
'''

from ansible_common_f5bigip.f5bigip import *

BIGIP_SYS_SSHD_ARGS = dict(
    allow               =   dict(type='list'),
    banner              =   dict(type='str', choices=F5BIGIP_ACTIVATION_CHOICES),
    banner_text         =   dict(type='str'),
    inactivity_timeout  =   dict(type='int'),
    login               =   dict(type='str', choices=F5BIGIP_ACTIVATION_CHOICES),
    log_level           =   dict(type='str', choices=['debug', 'debug1', 'debug2', 'debug3', 'error', 'fatal', 'info', 'quiet', 'verbose']),
)

class F5BigIpSysSshd(F5BigIpUnnamedObject):
    def _set_crud_methods(self):
        self.methods = {
            'read':self.mgmt.tm.sys.sshd.load
        }
    
    def _absent(self):
        if not (self.params['allow']):
            raise AnsibleModuleF5BigIpError("Absent can only be used when removing allow hostnames or IP addresses")
        
        return super(F5BigIpSysSshd, self)._absent()

def main():
    # Translation list for conflictual params
    tr = {}
    
    module = AnsibleModuleF5BigIpUnnamedObject(argument_spec=BIGIP_SYS_SSHD_ARGS, supports_check_mode=False)
    
    try:
        obj = F5BigIpSysSshd(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':  
    main()