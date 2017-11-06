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

DOCUMENTATION = '''
---
module: f5bigip_ltm_profile_statistics
short_description: BIG-IP ltm profile statistics module
description:
    - Configures a Statistics profile.
version_added: 2.3
author:
    - "Gabriel Fortin"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    app_service:
        description:
            - Specifies the name of the application service to which the profile belongs.
        required: false
        default: none
        choices: []
        aliases: []
    defaults_from:
        description:
            - Specifies the profile that you want to use as the parent profile.
        required: false
        default: stats
        choices: []
        aliases: []
    description:
        description:
            - User defined description.
        required: false
        default: null
        choices: []
        aliases: []
    field1:
        description:
            - Specifies the name of a counter.
        required: false
        default: none
        choices: []
        aliases: []
    name:
        description:
            - Specifies a unique name for the component.
        required: true
        default: none
        choices: []
        aliases: []
    partition:
        description:
            - Displays the administrative partition within which the component resides.
        required: false
        default: null
        choices: []
        aliases: []
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        required: false
        default: present
        choices: ['absent', 'present']
        aliases: []
'''

EXAMPLES = '''
- name: Create LTM Profile statistics
  f5bigip_ltm_profile_statistics:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_statistics_profile
    partition: Common
    description: My statistics profile
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_LTM_PROFILE_STATISTICS_ARGS = dict(
    app_service      =    dict(type='str'),
    defaults_from    =    dict(type='str'),
    description      =    dict(type='str'),
    field1           =    dict(type='str'),
    field2           =    dict(type='str'),
    field3           =    dict(type='str'),
    field4           =    dict(type='str'),
    field5           =    dict(type='str'),
    field6           =    dict(type='str'),
    field7           =    dict(type='str'),
    field8           =    dict(type='str'),
    field9           =    dict(type='str'),
    field10          =    dict(type='str'),
    field11          =    dict(type='str'),
    field12          =    dict(type='str'),
    field13          =    dict(type='str'),
    field14          =    dict(type='str'),
    field15          =    dict(type='str'),
    field16          =    dict(type='str'),
    field17          =    dict(type='str'),
    field18          =    dict(type='str'),
    field19          =    dict(type='str'),
    field20          =    dict(type='str'),
    field21          =    dict(type='str'),
    field22          =    dict(type='str'),
    field23          =    dict(type='str'),
    field24          =    dict(type='str'),
    field25          =    dict(type='str'),
    field26          =    dict(type='str'),
    field27          =    dict(type='str'),
    field28          =    dict(type='str'),
    field29          =    dict(type='str'),
    field30          =    dict(type='str'),
    field31          =    dict(type='str'),
    field32          =    dict(type='str')
)

class F5BigIpLtmProfileStatistics(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.profile.statistics_s.statistics.create,
            'read':     self.mgmt_root.tm.ltm.profile.statistics_s.statistics.load,
            'update':   self.mgmt_root.tm.ltm.profile.statistics_s.statistics.update,
            'delete':   self.mgmt_root.tm.ltm.profile.statistics_s.statistics.delete,
            'exists':   self.mgmt_root.tm.ltm.profile.statistics_s.statistics.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}

    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_PROFILE_STATISTICS_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpLtmProfileStatistics(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()