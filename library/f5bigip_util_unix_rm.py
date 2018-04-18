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
module: f5bigip_util_unix_rm
short_description: BIG-IP util unix rm module
description:
    - Removes files or directories.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    path:
        description:
            - Specifies the path of the file that is to be removed.
        required: true
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Removes a file
  f5bigip_util_unix_rm:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    path: /var/config/rest/downloads/data.dat
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_UTIL_UNIX_RM_ARGS = dict(
    path=dict(type='str', required=True)
)


class F5BigIpUtilUnixRm(F5BigIpUnnamedObject):
    def set_crud_methods(self):
        self.methods = {
            'run': self.mgmt_root.tm.util.unix_rm.exec_cmd,
        }

    def remove(self):
        result = dict(changed=False)

        try:
            self.methods['run']('run', utilCmdArgs=self.params['path'])
            result['changed'] = True
        except Exception:
            raise AnsibleF5Error("Cannot remove the file.")

        return result


def main():
    module = AnsibleModuleF5BigIpUnnamedObject(argument_spec=BIGIP_UTIL_UNIX_RM_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpUtilUnixRm(check_mode=module.supports_check_mode, **module.params)
        result = obj.remove()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
