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
module: f5bigip_sys_software_update
short_description: BIG-IP sys software update module
description:
    - Configures the BIG-IP update check schedule settings.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    auto_check:
        description:
            - Set this to enabled in order to turn on the auto update check feature.
        choices: ['disabled', 'enabled']
    frequency:
        description:
            - Specifies the frequency to look for software updates.
        default: weekly
        choices: ['daily', 'monthly', 'weekly']
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Change SYS Software Update frequency
  f5bigip_sys_software_update:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    frequency: daily
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_SYS_SOFTWARE_UPDATE_ARGS = dict(
    auto_check          =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    frequency           =   dict(type='str', choices=['daily', 'monthly', 'weekly'])
)

class F5BigIpSysSoftwareUpdate(F5BigIpUnnamedObject):
    def set_crud_methods(self):
        self.methods = {
            'read':     self.mgmt_root.tm.sys.software.update.load,
            'update':   self.mgmt_root.tm.sys.software.update.update,
        }

def main():
    module = AnsibleModuleF5BigIpUnnamedObject(argument_spec=BIGIP_SYS_SOFTWARE_UPDATE_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpSysSoftwareUpdate(check_mode=module.supports_check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

if __name__ == '__main__':
    main()