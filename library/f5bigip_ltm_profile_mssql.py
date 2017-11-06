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
module: f5bigip_ltm_profile_mssql
short_description: BIG-IP ltm profile mssql module
description:
    - Configures a profile to manage mssql(tds) database traffic.
version_added: 2.3
author:
    - "Gabriel Fortin"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    partition:
        description:
            - Displays the administrative partition within which the profile resides.
        required: false
        default: null
        choices: []
        aliases: []
    read_pool:
        description:
            - Specifies the pool of MS SQL database servers to which the system sends ready-only requests.
        required: false
        default: null
        choices: []
        aliases: []
    read_write_split_by_command:
        description:
            - When enabled, the system decides which pool to send the client requests the by the content in the message.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
        aliases: []
    read_write_split_by_user:
        description:
            - When enabled, the system decides which pool to send the client requests the by user name.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
        aliases: []
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        required: false
        default: present
        choices: ['absent', 'present']
        aliases: []
    user_can_write_by_default:
        description:
            - Specifies whether users have write access by default.
        required: false
        default: true
        choices: ['false', 'true']
        aliases: []
    user_list:
        description:
            - Specifies the users who have read-only access to the MS SQL if user-can-write-by-default is true, or the users who have write access to the MS SQL database if user-can-write-by-default is false.
        required: false
        default: null
        choices: []
        aliases: []
    write_persist_timer:
        description:
            - Specify how many minimum time in milliseconds the connection will be persisted to write-pool after connection switch to write pool.
        required: false
        default: null
        choices: []
        aliases: []
    write_pool:
        description:
            - Specifies the pool of MS SQL database servers to which the system sends requests that are not read-only.
        required: false
        default: null
        choices: []
        aliases: []
'''

EXAMPLES = '''
- name: Create LTM Profile MSSQL
  f5bigip_ltm_profile_mssql:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_mssql_profile
    partition: Common
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_LTM_PROFILE_MSSQL_ARGS = dict(
    read_pool                      =    dict(type='str'),
    read_write_split_by_command    =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    read_write_split_by_user       =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    user_can_write_by_default      =    dict(type='str', choices=['false', 'true']),
    user_list                      =    dict(type='list'),
    write_persist_timer            =    dict(type='int'),
    write_pool                     =    dict(type='str')
)

class F5BigIpLtmProfileMssql(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.profile.mssqls.mssql.create,
            'read':     self.mgmt_root.tm.ltm.profile.mssqls.mssql.load,
            'update':   self.mgmt_root.tm.ltm.profile.mssqls.mssql.update,
            'delete':   self.mgmt_root.tm.ltm.profile.mssqls.mssql.delete,
            'exists':   self.mgmt_root.tm.ltm.profile.mssqls.mssql.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}

    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_PROFILE_MSSQL_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpLtmProfileMssql(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()