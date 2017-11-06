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
module: f5bigip_sys_syslog
short_description: BIG-IP sys syslog module
description:
    - Configures the BIG-IP system log.
version_added: 2.3
author:
    - "Eric Jacob, @erjac77"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    auth_priv_from:
        description:
            - Specifies the lowest level of messages about user authentication to include in the system log.
        required: false
        default: notice
        choices: ['alert', 'crit', 'debug', 'emerg', 'err', 'info', 'notice', 'warning']
        aliases: []
        version_added: 2.3
    auth_priv_to:
        description:
            - Specifies the highest level of messages about user authentication to include in the system log.
        required: false
        default: emerg
        choices: ['alert', 'crit', 'debug', 'emerg', 'err', 'info', 'notice', 'warning']
        aliases: []
        version_added: 2.3
    cron_from:
        description:
            - Specifies the lowest level of messages about time-based scheduling to include in the system log.
        required: false
        default: warning
        choices: ['alert', 'crit', 'debug', 'emerg', 'err', 'info', 'notice', 'warning']
        aliases: []
        version_added: 2.3
    cron_to:
        description:
            - Specifies the highest level of messages about time-based scheduling to include in the system log.
        required: false
        default: emerg
        choices: ['alert', 'crit', 'debug', 'emerg', 'err', 'info', 'notice', 'warning']
        aliases: []
        version_added: 2.3
    daemon_from:
        description:
            - Specifies the lowest level of messages about daemon performance to include in the system log.
        required: false
        default: notice
        choices: ['alert', 'crit', 'debug', 'emerg', 'err', 'info', 'notice', 'warning']
        aliases: []
        version_added: 2.3
    daemon_to:
        description:
            - Specifies the highest level of messages about daemon performance to include in the system log.
        required: false
        default: emerg
        choices: ['alert', 'crit', 'debug', 'emerg', 'err', 'info', 'notice', 'warning']
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
    iso_date:
        description:
            - Enables or disables the ISO date format for messages in the log files.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    console_log:
        description:
            - Enables or disables logging emergency syslog messages to the console.
        required: false
        default: enabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    kern_from:
        description:
            - Specifies the lowest level of kernel messages to include in the system log.
        required: false
        default: notice
        choices: ['alert', 'crit', 'debug', 'emerg', 'err', 'info', 'notice', 'warning']
        aliases: []
        version_added: 2.3
    kern_to:
        description:
            - Specifies the highest level of kernel messages to include in the system log.
        required: false
        default: emerg
        choices: ['alert', 'crit', 'debug', 'emerg', 'err', 'info', 'notice', 'warning']
        aliases: []
        version_added: 2.3
    local6_from:
        description:
            - Specifies the lowest error level for messages from the local6 facility to include in the log.
        required: false
        default: notice
        choices: ['alert', 'crit', 'debug', 'emerg', 'err', 'info', 'notice', 'warning']
        aliases: []
        version_added: 2.3
    local6_to:
        description:
            - Specifies the highest error level for messages from the local6 facility to include in the log.
        required: false
        default: emerg
        choices: ['alert', 'crit', 'debug', 'emerg', 'err', 'info', 'notice', 'warning']
        aliases: []
        version_added: 2.3
    mail_from:
        description:
            - Specifies the lowest level of mail log messages to include in the system log.
        required: false
        default: notice
        choices: ['alert', 'crit', 'debug', 'emerg', 'err', 'info', 'notice', 'warning']
        aliases: []
        version_added: 2.3
    mail_to:
        description:
            - Specifies the highest level of mail log messages to include in the system log.
        required: false
        default: emerg
        choices: ['alert', 'crit', 'debug', 'emerg', 'err', 'info', 'notice', 'warning']
        aliases: []
        version_added: 2.3
    messages_from:
        description:
            - Specifies the lowest level of messages about user authentication to include in the system log.
        required: false
        default: notice
        choices: ['alert', 'crit', 'debug', 'emerg', 'err', 'info', 'notice', 'warning']
        aliases: []
        version_added: 2.3
    messages_to:
        description:
            - Specifies the highest level of system messages to include in the system log.
        required: false
        default: emerg
        choices: ['alert', 'crit', 'debug', 'emerg', 'err', 'info', 'notice', 'warning']
        aliases: []
        version_added: 2.3
    user_log_from:
        description:
            - Specifies the lowest level of user account messages to include in the system log.
        required: false
        default: notice
        choices: ['alert', 'crit', 'debug', 'emerg', 'err', 'info', 'notice', 'warning']
        aliases: []
        version_added: 2.3
    user_log_to:
        description:
            - Specifies the highest level of user account messages to include in the system log.
        required: false
        default: emerg
        choices: ['alert', 'crit', 'debug', 'emerg', 'err', 'info', 'notice', 'warning']
        aliases: []
        version_added: 2.3
'''

EXAMPLES = '''
- name: Change SYS Syslog User Log
  f5bigip_sys_syslog:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    user_log_from: alert
    user_log_to: alert
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_SYS_SYSLOG_ARGS = dict(
    auth_priv_from  =   dict(type='str', choices=F5_SEVERITY_CHOICES),
    auth_priv_to    =   dict(type='str', choices=F5_SEVERITY_CHOICES),
    cron_from       =   dict(type='str', choices=F5_SEVERITY_CHOICES),
    cron_to         =   dict(type='str', choices=F5_SEVERITY_CHOICES),
    daemon_from     =   dict(type='str', choices=F5_SEVERITY_CHOICES),
    daemon_to       =   dict(type='str', choices=F5_SEVERITY_CHOICES),
    description     =   dict(type='str'),
    iso_date        =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    console_log     =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    kern_from       =   dict(type='str', choices=F5_SEVERITY_CHOICES),
    kern_to         =   dict(type='str', choices=F5_SEVERITY_CHOICES),
    local6_from     =   dict(type='str', choices=F5_SEVERITY_CHOICES),
    local6_to       =   dict(type='str', choices=F5_SEVERITY_CHOICES),
    mail_from       =   dict(type='str', choices=F5_SEVERITY_CHOICES),
    mail_to         =   dict(type='str', choices=F5_SEVERITY_CHOICES),
    messages_from   =   dict(type='str', choices=F5_SEVERITY_CHOICES),
    messages_to     =   dict(type='str', choices=F5_SEVERITY_CHOICES),
    user_log_from   =   dict(type='str', choices=F5_SEVERITY_CHOICES),
    user_log_to     =   dict(type='str', choices=F5_SEVERITY_CHOICES)
)

class F5BigIpSysSyslog(F5BigIpUnnamedObject):
    def set_crud_methods(self):
        self.methods = {
            'read':     self.mgmt_root.tm.sys.syslog.load,
            'update':   self.mgmt_root.tm.sys.syslog.update
        }

def main():
    # Translation list for conflictual params
    tr = {}
    
    module = AnsibleModuleF5BigIpUnnamedObject(argument_spec=BIGIP_SYS_SYSLOG_ARGS, supports_check_mode=False)
    
    try:
        obj = F5BigIpSysSyslog(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()