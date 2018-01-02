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
module: f5bigip_util_unix_mv
short_description: BIG-IP util unix mv module
description:
    - Moves files.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    dest_path:
        description:
            - Specifies the path where the file will be moved.
        required: true
    file_name:
        description:
            - Specifies the name of the file to be moved.
        required: true
    source_path:
        description:
            - Specifies the path where the file will be taken.
        required: true
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Move file
  f5bigip_util_unix_mv:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    file_name: test.txt
    source_path: /var/
    dest_path: /home/
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_UTIL_UNIX_MV_ARGS = dict(
    dest_path=dict(type='str', required=True),
    file_name=dict(type='str', required=True),
    source_path=dict(type='str', required=True)
)


class F5BigIpUtilUnixMv(F5BigIpUnnamedObject):
    def set_crud_methods(self):
        self.methods = {
            'move': self.mgmt_root.tm.util.unix_mv.exec_cmd,
        }

    def move(self):
        has_changed = False

        try:
            self.methods['move']('run', utilCmdArgs='{0}/{2} {1}/{2}'.format(self.params['sourcePath'],
                                                                             self.params['destPath'],
                                                                             self.params['fileName']))
            has_changed = True
        except Exception:
            raise AnsibleF5Error("Can't move the file.")

        return {'changed': has_changed}


def main():
    module = AnsibleModuleF5BigIpUnnamedObject(argument_spec=BIGIP_UTIL_UNIX_MV_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpUtilUnixMv(check_mode=module.supports_check_mode, **module.params)
        result = obj.move()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
