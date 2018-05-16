#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2016-2018, Eric Jacob <erjac77@gmail.com>
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

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: f5bigip_sys_syslog
short_description: BIG-IP sys syslog module
description:
    - Configures the BIG-IP system log.
version_added: "2.4"
author:
    - "Eric Jacob (@erjac77)"
options:
    auth_priv_from:
        description:
            - Specifies the lowest level of messages about user authentication to include in the system log.
        default: notice
        choices: ['alert', 'crit', 'debug', 'emerg', 'err', 'info', 'notice', 'warning']
    auth_priv_to:
        description:
            - Specifies the highest level of messages about user authentication to include in the system log.
        default: emerg
        choices: ['alert', 'crit', 'debug', 'emerg', 'err', 'info', 'notice', 'warning']
    console_log:
        description:
            - Enables or disables logging emergency syslog messages to the console.
        default: enabled
        choices: ['enabled', 'disabled']
    cron_from:
        description:
            - Specifies the lowest level of messages about time-based scheduling to include in the system log.
        default: warning
        choices: ['alert', 'crit', 'debug', 'emerg', 'err', 'info', 'notice', 'warning']
    cron_to:
        description:
            - Specifies the highest level of messages about time-based scheduling to include in the system log.
        default: emerg
        choices: ['alert', 'crit', 'debug', 'emerg', 'err', 'info', 'notice', 'warning']
    daemon_from:
        description:
            - Specifies the lowest level of messages about daemon performance to include in the system log.
        default: notice
        choices: ['alert', 'crit', 'debug', 'emerg', 'err', 'info', 'notice', 'warning']
    daemon_to:
        description:
            - Specifies the highest level of messages about daemon performance to include in the system log.
        default: emerg
        choices: ['alert', 'crit', 'debug', 'emerg', 'err', 'info', 'notice', 'warning']
    description:
        description:
            - Specifies descriptive text that identifies the component.
    iso_date:
        description:
            - Enables or disables the ISO date format for messages in the log files.
        default: disabled
        choices: ['enabled', 'disabled']
    kern_from:
        description:
            - Specifies the lowest level of kernel messages to include in the system log.
        default: notice
        choices: ['alert', 'crit', 'debug', 'emerg', 'err', 'info', 'notice', 'warning']
    kern_to:
        description:
            - Specifies the highest level of kernel messages to include in the system log.
        default: emerg
        choices: ['alert', 'crit', 'debug', 'emerg', 'err', 'info', 'notice', 'warning']
    local6_from:
        description:
            - Specifies the lowest error level for messages from the local6 facility to include in the log.
        default: notice
        choices: ['alert', 'crit', 'debug', 'emerg', 'err', 'info', 'notice', 'warning']
    local6_to:
        description:
            - Specifies the highest error level for messages from the local6 facility to include in the log.
        default: emerg
        choices: ['alert', 'crit', 'debug', 'emerg', 'err', 'info', 'notice', 'warning']
    mail_from:
        description:
            - Specifies the lowest level of mail log messages to include in the system log.
        default: notice
        choices: ['alert', 'crit', 'debug', 'emerg', 'err', 'info', 'notice', 'warning']
    mail_to:
        description:
            - Specifies the highest level of mail log messages to include in the system log.
        default: emerg
        choices: ['alert', 'crit', 'debug', 'emerg', 'err', 'info', 'notice', 'warning']
    messages_from:
        description:
            - Specifies the lowest level of messages about user authentication to include in the system log.
        default: notice
        choices: ['alert', 'crit', 'debug', 'emerg', 'err', 'info', 'notice', 'warning']
    messages_to:
        description:
            - Specifies the highest level of system messages to include in the system log.
        default: emerg
        choices: ['alert', 'crit', 'debug', 'emerg', 'err', 'info', 'notice', 'warning']
    remote_servers:
        description:
            - Configures the remote servers, identified by IP address, to which syslog sends messages.
    user_log_from:
        description:
            - Specifies the lowest level of user account messages to include in the system log.
        default: notice
        choices: ['alert', 'crit', 'debug', 'emerg', 'err', 'info', 'notice', 'warning']
    user_log_to:
        description:
            - Specifies the highest level of user account messages to include in the system log.
        default: emerg
        choices: ['alert', 'crit', 'debug', 'emerg', 'err', 'info', 'notice', 'warning']
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Change SYS Syslog User Log
  f5bigip_sys_syslog:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    remote_servers:
      - { name: /Common/remotesyslog1, host: 10.20.20.21, localIp: none, remotePort: 514 }
      - { name: /Common/remotesyslog2, host: 10.20.20.22, localIp: none, remotePort: 514 }
    user_log_from: alert
    user_log_to: alert
  delegate_to: localhost
'''

RETURN = ''' # '''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.base import F5_ACTIVATION_CHOICES
from ansible_common_f5.base import F5_PROVIDER_ARGS
from ansible_common_f5.base import F5_SEVERITY_CHOICES
from ansible_common_f5.bigip import F5BigIpUnnamedObject


class ModuleParams(object):
    @property
    def argument_spec(self):
        argument_spec = dict(
            auth_priv_from=dict(type='str', choices=F5_SEVERITY_CHOICES),
            auth_priv_to=dict(type='str', choices=F5_SEVERITY_CHOICES),
            cron_from=dict(type='str', choices=F5_SEVERITY_CHOICES),
            cron_to=dict(type='str', choices=F5_SEVERITY_CHOICES),
            daemon_from=dict(type='str', choices=F5_SEVERITY_CHOICES),
            daemon_to=dict(type='str', choices=F5_SEVERITY_CHOICES),
            description=dict(type='str'),
            iso_date=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            console_log=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            kern_from=dict(type='str', choices=F5_SEVERITY_CHOICES),
            kern_to=dict(type='str', choices=F5_SEVERITY_CHOICES),
            local6_from=dict(type='str', choices=F5_SEVERITY_CHOICES),
            local6_to=dict(type='str', choices=F5_SEVERITY_CHOICES),
            mail_from=dict(type='str', choices=F5_SEVERITY_CHOICES),
            mail_to=dict(type='str', choices=F5_SEVERITY_CHOICES),
            messages_from=dict(type='str', choices=F5_SEVERITY_CHOICES),
            messages_to=dict(type='str', choices=F5_SEVERITY_CHOICES),
            remote_servers=dict(type='list'),
            user_log_from=dict(type='str', choices=F5_SEVERITY_CHOICES),
            user_log_to=dict(type='str', choices=F5_SEVERITY_CHOICES)
        )
        argument_spec.update(F5_PROVIDER_ARGS)
        return argument_spec

    @property
    def supports_check_mode(self):
        return True


class F5BigIpSysSyslog(F5BigIpUnnamedObject):
    def _set_crud_methods(self):
        self._methods = {
            'read': self._api.tm.sys.syslog.load,
            'update': self._api.tm.sys.syslog.update
        }


def main():
    params = ModuleParams()
    module = AnsibleModule(argument_spec=params.argument_spec, supports_check_mode=params.supports_check_mode)

    try:
        obj = F5BigIpSysSyslog(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
