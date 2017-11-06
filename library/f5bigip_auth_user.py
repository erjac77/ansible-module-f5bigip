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
module: f5bigip_auth_user
short_description: BIG-IP auth user module
description:
    - Configures user accounts for the BIG-IP system.
version_added: 2.3
author:
    - "Gabriel Fortin"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    description:
        description:
            - Describes the user account in free form text.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    name:
        description:
            - Specifies unique name for the component.
        required: true
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    partition:
        description:
            - Displays the name of the administrative partition in which the user account resides.
        required: false
        default: Common
        choices: []
        aliases: []
        version_added: 2.3
    partition_access:
        description:
            - Specifies the administrative partitions to which the user currently has access.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    role:
        description:
            - Specifies the user role that pertains to the partition specified by the partition-access property.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    password:
        description:
            - Sets the user password during creation or modification of a user account without prompting or confirmation.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    prompt_for_password:
        description:
            - Indicates that when the account is created or modified, the BIG-IP system prompts the administrator or user manager for both a password and a password confirmation for the account.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    shell:
        description:
            - Specifies the shell to which the user has access.
        required: false
        default: null
        choices: ['bash', 'none', 'tmsh']
        aliases: []
        version_added: 2.3
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        required: false
        default: present
        choices: ['absent', 'present']
        aliases: []
        version_added: 2.3
'''

EXAMPLES = '''
- name: Create Auth User
  f5bigip_auth_user:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: user1
    partition: Common
    description: user 1
    partitionAccess:
      - name: Common
        role: Guest
      - name: Test
        role: Guest
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_AUTH_USER_ARGS = dict(
    description             =   dict(type='str'),
    partition_access        =   dict(type='list'),
    password                =   dict(type='str'),
    prompt_for_password     =   dict(type='str'),
    shell                   =   dict(type='str', choices=['bash', 'none', 'tmsh'])
)

class F5BigIpAuthUser(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.auth.users.user.create,
            'read':     self.mgmt_root.tm.auth.users.user.load,
            'update':   self.mgmt_root.tm.auth.users.user.update,
            'delete':   self.mgmt_root.tm.auth.users.user.delete,
            'exists':   self.mgmt_root.tm.auth.users.user.exists
        }
        self.params.pop('partition', None)
        self.params.pop('sub_path', None)

def main():
    # Translation list for conflictual params
    tr = {}

    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_AUTH_USER_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpAuthUser(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()