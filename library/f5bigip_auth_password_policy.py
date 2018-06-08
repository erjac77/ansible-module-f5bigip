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
module: f5bigip_auth_password_policy
short_description: BIG-IP auth password policy module
description:
    - Configures a Password Policy.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    expiration_warning:
        description:
            - Specifies the number of days before a password expires.
        default: 7
    max_duration:
        description:
            - Specifies the maximum number of days a password is valid.
        default: 99999
    max_login_failures:
        description:
            - Specifies the number of consecutive unsuccessful login attempts that the system allows before locking out
              the user.
        default: 0
    min_duration:
        description:
            - Specifies the minimum number of days a password is valid.
        default: 0
    minimum_length:
        description:
            - Specifies the minimum number of characters in a valid password.
        default: 6
    password_memory:
        description:
            - Specifies whether the user has configured the BIG-IP system to remember a password on a specific computer.
        default: 0
    policy_enforcement:
        description:
            - Enables or disables the password policy on the BIG-IP system.
        default: disabled
        choices: ['disabled', 'enabled']
    required_lowercase:
        description:
            - Specifies the number of lowercase alpha characters that must be present in a password for the password to
              be valid.
        default: 0
    required_numeric:
        description:
            - Specifies the number of numeric characters that must be present in a password for the password to be
              valid.
        default: 0
    required_special:
        description:
            - Specifies the number of special characters that must be present in a password for the password to be
              valid.
        default: 0
    required_uppercase:
        description:
            - Specifies the number of uppercase alpha characters that must be present in a password for the password to
              be valid.
        default: 0
requirements:
    - BIG-IP >= 12.0
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Change Password Policy
  f5bigip_auth_password_policy:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    max_duration: 90
    min_duration: 30
    minimum_length: 8
    required_lowercase: 2
    required_uppercase: 2
    required_special: 1
    required_numeric: 1
    expiration_warning: 5
  delegate_to: localhost
  register: result
'''

RETURN = ''' # '''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.base import F5_ACTIVATION_CHOICES
from ansible_common_f5.base import F5_PROVIDER_ARGS
from ansible_common_f5.bigip import F5BigIpUnnamedObject


class ModuleParams(object):
    @property
    def argument_spec(self):
        argument_spec = dict(
            expiration_warning=dict(type='int'),
            max_duration=dict(type='int'),
            max_login_failures=dict(type='int'),
            min_duration=dict(type='int'),
            minimum_length=dict(type='int'),
            password_memory=dict(type='int'),
            policy_enforcement=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            required_lowercase=dict(type='int'),
            required_numeric=dict(type='int'),
            required_special=dict(type='int'),
            required_uppercase=dict(type='int')
        )
        argument_spec.update(F5_PROVIDER_ARGS)
        return argument_spec

    @property
    def supports_check_mode(self):
        return True


class F5BigIpAuthPasswordPolicy(F5BigIpUnnamedObject):
    def _set_crud_methods(self):
        self._methods = {
            'read': self._api.tm.auth.password_policy.load,
            'update': self._api.tm.auth.password_policy.update,
        }


def main():
    params = ModuleParams()
    module = AnsibleModule(argument_spec=params.argument_spec, supports_check_mode=params.supports_check_mode)

    try:
        obj = F5BigIpAuthPasswordPolicy(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
