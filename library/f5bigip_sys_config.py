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
module: f5bigip_sys_config
short_description: BIG-IP sys config module
description:
    - Manages the BIG-IP system configuration.
version_added: "2.4"
author:
    - "Eric Jacob (@erjac77)"
options:
    args:
        description:
            - Specifies arguments of the config command.
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Save SYS Config
  f5bigip_sys_config:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    command: 'save'
  delegate_to: localhost

- name: Load/Merge SYS Config
  f5bigip_sys_config:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    command: 'load'
    merge: True
    file: my_file
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_SYS_CONFIG_ARGS = dict(
    command=dict(type='str', choices=['save', 'load']),
    base=dict(type='str', choices=['binary', 'default', 'gtm-only', 'user-only']),
    binary=dict(type='bool'),
    current_partition=dict(type='bool'),
    default=dict(type='bool'),
    exclude_gtm=dict(type='bool'),
    file=dict(type='str'),
    files_folder=dict(type='str'),
    gtm_only=dict(type='bool'),
    merge=dict(type='bool'),
    partitions=dict(type='list'),
    passphrase=dict(type='str', no_log=True),
    user_only=dict(type='bool'),
    tar_file=dict(type='str'),
    time_stamp=dict(type='bool'),
    verify=dict(type='bool'),
    wait=dict(type='bool')
)


class F5BigIpSysConfig(F5BigIpUnnamedObject):
    def set_crud_methods(self):
        self.methods = {
            'exec_cmd': self.mgmt_root.tm.sys.config.exec_cmd
        }

    def exec_cmd(self):
        has_changed = False
        command = self.params.pop('command', None)

        # Remove empty params
        params = dict((k, v) for k, v in self.params.iteritems() if v is not None)

        try:
            self.methods['exec_cmd'](command, **params)
            has_changed = True
        except Exception as e:
            raise AnsibleF5Error("Could not execute '" + command + "' command: " + e.message)

        return {'changed': has_changed}


def main():
    module = AnsibleModuleF5BigIpUnnamedObject(argument_spec=BIGIP_SYS_CONFIG_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpSysConfig(check_mode=module.supports_check_mode, **module.params)
        result = obj.exec_cmd()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()
