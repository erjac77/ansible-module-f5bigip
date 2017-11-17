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
module: f5bigip_sys_ucs
short_description: BIG-IP sys ucs module
description:
    - Saves a ucs file.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
notes:
    - Requires BIG-IP software version >= 12.0
requirements:
    - ansible-common-f5
    - f5-sdk
options:
    name:
        description:
            - Specifies a unique name for the component.
        required: true
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Save SYS UCS
  f5bigip_sys_ucs:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_ucs.ucs
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_SYS_UCS_ARGS = dict(
)

class F5BigIpSysUcs(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'save':   self.mgmt_root.tm.sys.ucs.exec_cmd
        }

    def save(self):
        has_changed = False

        try:
            self.methods['save']('save', name=self.params['name'])
            has_changed = True 
        except Exception:
            raise AnsibleF5Error('Cannot save ucs.')

        return { 'changed': has_changed }

def main():
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_SYS_UCS_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpSysUcs(check_mode=module.supports_check_mode, **module.params)
        result = obj.save()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

if __name__ == '__main__':
    main()