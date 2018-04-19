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
module: f5bigip_util_qkview
short_description: BIG-IP util qkview module
description:
    - Gathers diagnostic information from a BIG-IP system.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    args:
        description:
            - Specifies the qkview arguments.
        default: ''
notes:
    - Requires BIG-IP software version >= 12.0
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Generates a Qkview file
  f5bigip_util_qkview:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_UTIL_QKVIEW_ARGS = dict(
    args=dict(type='str', default='')
)


class F5BigIpUtilQkview(F5BigIpUnnamedObject):
    def set_crud_methods(self):
        self.methods = {
            'run': self.mgmt_root.tm.util.qkview.exec_cmd
        }

    def run(self):
        result = dict(changed=False)

        if self.check_mode:
            result['changed'] = True
            return result

        try:
            self.methods['run']('run', utilCmdArgs=self.params['args'])
            result['changed'] = True
        except Exception:
            raise AnsibleF5Error("Cannot generate the Qkview file.")

        return result


def main():
    module = AnsibleModuleF5BigIpUnnamedObject(argument_spec=BIGIP_UTIL_QKVIEW_ARGS, supports_check_mode=True)

    try:
        obj = F5BigIpUtilQkview(check_mode=module.check_mode, **module.params)
        result = obj.run()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
