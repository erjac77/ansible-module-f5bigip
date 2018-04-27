#!/usr/bin/python
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
module: f5bigip_util_dig
short_description: BIG-IP util dig module
description:
    - Interrogates DNS name servers.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
    - "Eric Jacob (@erjac77)"
options:
    args:
        description:
            - Specifies the arguments of the dig command.
        required: true
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Runs a Dig command
  f5bigip_util_dig:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    args: 'f5.com NS'
  delegate_to: localhost
'''

RETURN = '''
stdout:
    description: The output of the command.
    returned: success
    type: list
    sample:
        - ['...', '...']
stdout_lines:
    description: A list of strings, each containing one item per line from the original output.
    returned: success
    type: list
    sample:
        - [['...', '...'], ['...'], ['...']]
'''

from ansible.module_utils.basic import AnsibleModule

try:
    from ansible_common_f5.f5_bigip import AnsibleF5Error
    from ansible_common_f5.f5_bigip import AnsibleModuleF5BigIpUnnamedObject
    from ansible_common_f5.f5_bigip import F5BigIpUnnamedObject
    from ansible_common_f5.f5_bigip import to_lines

    HAS_F5COMMON = True
except ImportError:
    HAS_F5COMMON = False

BIGIP_UTIL_DIG_ARGS = dict(
    args=dict(type='str', required=True)
)


class F5BigIpUtilDig(F5BigIpUnnamedObject):
    def set_crud_methods(self):
        self.methods = {
            'run': self.mgmt_root.tm.util.dig.exec_cmd
        }

    def dig(self):
        result = dict(changed=False, stdout=list())

        try:
            output = self.methods['run']('run', utilCmdArgs=self.params['args'])
            # result['changed'] = True
        except Exception as exc:
            err_msg = 'Could not execute the Dig command.'
            err_msg += ' The error message was "{0}".'.format(str(exc))
            raise AnsibleF5Error(err_msg)

        if hasattr(output, 'commandResult'):
            result['stdout'].append(str(output.commandResult))
        result['stdout_lines'] = list(to_lines(result['stdout']))

        return result


def main():
    if not HAS_F5COMMON:
        module = AnsibleModule(argument_spec={})
        module.fail_json(msg="The python ansible-common-f5 module is required.")

    module = AnsibleModuleF5BigIpUnnamedObject(argument_spec=BIGIP_UTIL_DIG_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpUtilDig(check_mode=module.check_mode, **module.params)
        result = obj.dig()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
