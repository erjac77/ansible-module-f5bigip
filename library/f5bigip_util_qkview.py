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
module: f5bigip_util_qkview
short_description: BIG-IP util qkview module
description:
    - Generates a Qkview.
version_added: 2.3
author:
    - "Gabriel Fortin"
notes:
    - Requires BIG-IP software version >= 12.0
requirements:
    - f5-sdk
'''

EXAMPLES = '''
- name: Generate qkview
  f5bigip_util_qkview:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_UTIL_QKVIEW_ARGS = dict(
)

class F5BigIpUtilQkview(F5BigIpUnnamedObject):
    def set_crud_methods(self):
        self.methods = {
            'run':   self.mgmt_root.tm.util.qkview.exec_cmd
        }

    def generate_qkview(self):
        has_changed = True

        try:
            self.methods['run']('run', utilCmdArgs='')  
        except Exception:
            has_changed = False

        return { 'changed': has_changed}

def main():
    module = AnsibleModuleF5BigIpUnnamedObject(argument_spec=BIGIP_UTIL_QKVIEW_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpUtilQkview(check_mode=module.supports_check_mode, **module.params)
        result = obj.generate_qkview()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()
