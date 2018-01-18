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
module: f5bigip_util_clientssl_ciphers
short_description: BIG-IP util client ssl ciphers module
description:
    - Runs a client ssl ciphers command.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    arguments:
        description:
            - Specifies the arguments for the command.
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Run Client SSL Ciphers command
  f5bigip_util_clientssl_ciphers:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    arguments: 'DEFAULT'
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_UTIL_CLIENT_SSL_CIPHERS_ARGS = dict(
    arguments=dict(type='str')
)


class F5BigIpUtilClientSslCiphers(F5BigIpUnnamedObject):
    def set_crud_methods(self):
        self.methods = {
            'command': self.mgmt_root.tm.util.clientssl_ciphers.exec_cmd
        }

    def command(self):
        has_changed = False

        try:
            obj = self.methods['command']('run', utilCmdArgs=self.params['arguments'])
            has_changed = True
        except Exception:
            raise AnsibleF5Error("Couldn't run command.")

        return {'result': obj.commandResult, 'changed': has_changed}


def main():
    module = AnsibleModuleF5BigIpUnnamedObject(argument_spec=BIGIP_UTIL_CLIENT_SSL_CIPHERS_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpUtilClientSslCiphers(check_mode=module.supports_check_mode, **module.params)
        result = obj.command()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
