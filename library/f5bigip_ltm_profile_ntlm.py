#!/usr/bin/python
#
# Copyright 2016, Eric Jacob <erjac77@gmail.com>
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
module: f5bigip_ltm_profile_ntlm
short_description: BIG-IP ltm profile ntlm module
description:
    - Configures a Microsoft Windows NT Local Area Network (LAN) manager profile.
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
        default: ntlm
        choices: []
        aliases: []
    description:
        description:
            - User defined description.
        required: false
        default: null
        choices: []
        aliases: []
    insert_cookie_domain:
        description:
            - Specifies an optional domain for the inserted cookie.
        required: false
        default: null
        choices: []
        aliases: []
    insert_cookie_name:
        description:
            - Specifies a cookie name that the system inserts in the cookie.
        required: true
        default: NTLMconnpool
        choices: []
        aliases: []
    insert_cookie_passphrase:
        description:
            - Specifies a cookie passphrase that the system inserts in the cookie.
        required: false
        default: mypassphrase
        choices: []
        aliases: []
    key_by_cookie:
        description:
            - Specifies whether the system uses the value of the insert-cookie-name option as the key.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
        aliases: []
    key_by_cookie_name:
        description:
            - Specifies whether the system uses the value of the insert-cookie-name option as the key.
        required: false
        default: mycookie
        choices: []
        aliases: []
    key_by_domain:
        description:
            - Specifies whether the system uses the NTLM domain as the key.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
        aliases: []
    key_by_ip_address:
        description:
            - Specifies whether the system uses the client IP address as the key.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
        aliases: []
    key_by_target:
        description:
            - Specifies whether the system uses the NTLM target as the key.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
        aliases: []
    key_by_user:
        description:
            - Specifies whether the system uses the NTLM user as the key.
        required: false
        default: enabled
        choices: ['disabled', 'enabled']
        aliases: []
    key_by_workstation:
        description:
            - Specifies whether the system uses the NTLM workstation as the key.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
        aliases: []
    name:
        description:
            - Specifies a unique name for the component.
        required: true
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
- name: Create LTM Profile NTLM
  f5bigip_ltm_profile_ntlm:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_ntlm_profile
    partition: Common
    description: My ntlm profile
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_LTM_PROFILE_NTLM_ARGS = dict(
    app_service                 =    dict(type='str'),
    defaults_from               =    dict(type='str'),
    description                 =    dict(type='str'),
    insert_cookie_domain        =    dict(type='str'),
    insert_cookie_name          =    dict(type='str'),
    insert_cookie_passphrase    =    dict(type='str'),
    key_by_cookie               =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    key_by_cookie_name          =    dict(type='str'),
    key_by_domain               =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    key_by_ip_address           =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    key_by_target               =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    key_by_user                 =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    key_by_workstation          =    dict(type='str', choices=F5_ACTIVATION_CHOICES)
)

class F5BigIpLtmProfileNtlm(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.profile.ntlms.ntlm.create,
            'read':     self.mgmt_root.tm.ltm.profile.ntlms.ntlm.load,
            'update':   self.mgmt_root.tm.ltm.profile.ntlms.ntlm.update,
            'delete':   self.mgmt_root.tm.ltm.profile.ntlms.ntlm.delete,
            'exists':   self.mgmt_root.tm.ltm.profile.ntlms.ntlm.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}

    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_PROFILE_NTLM_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpLtmProfileNtlm(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()