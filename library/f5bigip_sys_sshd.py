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

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: f5bigip_sys_sshd
short_description: BIG-IP sys sshd module
description:
    - Configures the Secure Shell (SSH) daemon for the BIG-IP system.
version_added: "2.4"
author:
    - "Eric Jacob (@erjac77)"
options:
    allow:
        description:
            - Configures servers in the /etc/hosts.allow file.
        default: all
    banner:
        description:
            - Enables or disables the display of the banner text field when a user logs in to the system using SSH.
        default: disabled
        choices: ['enabled', 'disabled']
    banner_text:
        description:
            - When the banner option is enabled, specifies the text to include in the banner that displays when a user
              attempts to log on to the system.
    inactivity_timeout:
        description:
            - Specifies the number of seconds before inactivity causes an SSH session to log out.
        default: 0
    login:
        description:
            - Enables or disables SSH logins to the system.
        default: enabled
        choices: ['enabled', 'disabled']
    log_level:
        description:
            - Specifies the minimum sshd message level to include in the system log.
        choices: ['debug', 'debug1', 'debug2', 'debug3', 'error', 'fatal', 'info', 'quiet', 'verbose']
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Set SYS SSHD allow clients and banner
  f5bigip_sys_sshd:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    allow:
      - 172.16.227.0/24
      - 10.0.0./8
    banner: enabled
    banner_text: "NOTICE: Improper use of this computer may result in prosecution!"
  delegate_to: localhost

- name: Reset SYS SSHD allow clients
  f5bigip_sys_sshd:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    allow:
      - ALL
      - 127.
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_SYS_SSHD_ARGS = dict(
    allow=dict(type='list'),
    banner=dict(type='str', choices=F5_ACTIVATION_CHOICES),
    banner_text=dict(type='str'),
    inactivity_timeout=dict(type='int'),
    login=dict(type='str', choices=F5_ACTIVATION_CHOICES),
    log_level=dict(type='str',
                   choices=['debug', 'debug1', 'debug2', 'debug3', 'error', 'fatal', 'info', 'quiet', 'verbose']),
)


class F5BigIpSysSshd(F5BigIpUnnamedObject):
    def set_crud_methods(self):
        self.methods = {
            'read': self.mgmt_root.tm.sys.sshd.load,
            'update': self.mgmt_root.tm.sys.sshd.update
        }


def main():
    module = AnsibleModuleF5BigIpUnnamedObject(argument_spec=BIGIP_SYS_SSHD_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpSysSshd(check_mode=module.supports_check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
