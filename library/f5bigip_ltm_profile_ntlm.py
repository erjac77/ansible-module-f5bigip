#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2016-2018, Eric Jacob <erjac77@gmail.com>
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
module: f5bigip_ltm_profile_ntlm
short_description: BIG-IP ltm profile ntlm module
description:
    - Configures a Microsoft Windows NT Local Area Network (LAN) manager profile.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    app_service:
        description:
            - Specifies the name of the application service to which the profile belongs.
    defaults_from:
        description:
            - Specifies the profile that you want to use as the parent profile.
        default: ntlm
    description:
        description:
            - User defined description.
    insert_cookie_domain:
        description:
            - Specifies an optional domain for the inserted cookie.
    insert_cookie_name:
        description:
            - Specifies a cookie name that the system inserts in the cookie.
        required: true
        default: NTLMconnpool
    insert_cookie_passphrase:
        description:
            - Specifies a cookie passphrase that the system inserts in the cookie.
        default: mypassphrase
    key_by_cookie:
        description:
            - Specifies whether the system uses the value of the insert-cookie-name option as the key.
        default: disabled
        choices: ['disabled', 'enabled']
    key_by_cookie_name:
        description:
            - Specifies whether the system uses the value of the insert-cookie-name option as the key.
        default: mycookie
    key_by_domain:
        description:
            - Specifies whether the system uses the NTLM domain as the key.
        default: disabled
        choices: ['disabled', 'enabled']
    key_by_ip_address:
        description:
            - Specifies whether the system uses the client IP address as the key.
        default: disabled
        choices: ['disabled', 'enabled']
    key_by_target:
        description:
            - Specifies whether the system uses the NTLM target as the key.
        default: disabled
        choices: ['disabled', 'enabled']
    key_by_user:
        description:
            - Specifies whether the system uses the NTLM user as the key.
        default: enabled
        choices: ['disabled', 'enabled']
    key_by_workstation:
        description:
            - Specifies whether the system uses the NTLM workstation as the key.
        default: disabled
        choices: ['disabled', 'enabled']
    name:
        description:
            - Specifies a unique name for the component.
        required: true
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
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

RETURN = ''' # '''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.base import F5_ACTIVATION_CHOICES
from ansible_common_f5.base import F5_NAMED_OBJ_ARGS
from ansible_common_f5.base import F5_PROVIDER_ARGS
from ansible_common_f5.bigip import F5BigIpNamedObject


class ModuleParams(object):
    @property
    def argument_spec(self):
        argument_spec = dict(
            app_service=dict(type='str'),
            defaults_from=dict(type='str'),
            description=dict(type='str'),
            insert_cookie_domain=dict(type='str'),
            insert_cookie_name=dict(type='str'),
            insert_cookie_passphrase=dict(type='str', no_log=True),
            key_by_cookie=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            key_by_cookie_name=dict(type='str'),
            key_by_domain=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            key_by_ip_address=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            key_by_target=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            key_by_user=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            key_by_workstation=dict(type='str', choices=F5_ACTIVATION_CHOICES)
        )
        argument_spec.update(F5_PROVIDER_ARGS)
        argument_spec.update(F5_NAMED_OBJ_ARGS)
        return argument_spec

    @property
    def supports_check_mode(self):
        return True


class F5BigIpLtmProfileNtlm(F5BigIpNamedObject):
    def _set_crud_methods(self):
        self._methods = {
            'create': self._api.tm.ltm.profile.ntlms.ntlm.create,
            'read': self._api.tm.ltm.profile.ntlms.ntlm.load,
            'update': self._api.tm.ltm.profile.ntlms.ntlm.update,
            'delete': self._api.tm.ltm.profile.ntlms.ntlm.delete,
            'exists': self._api.tm.ltm.profile.ntlms.ntlm.exists
        }


def main():
    params = ModuleParams()
    module = AnsibleModule(argument_spec=params.argument_spec, supports_check_mode=params.supports_check_mode)

    try:
        obj = F5BigIpLtmProfileNtlm(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
