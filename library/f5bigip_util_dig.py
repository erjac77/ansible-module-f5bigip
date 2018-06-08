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
requirements:
    - BIG-IP >= 12.0
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
from ansible_common_f5.base import AnsibleF5Error
from ansible_common_f5.base import F5_PROVIDER_ARGS
from ansible_common_f5.bigip import F5BigIpUnnamedObject
from ansible_common_f5.utils import to_lines


class ModuleParams(object):
    @property
    def argument_spec(self):
        argument_spec = dict(
            args=dict(type='str', required=True)
        )
        argument_spec.update(F5_PROVIDER_ARGS)
        return argument_spec

    @property
    def supports_check_mode(self):
        return True


class F5BigIpUtilDig(F5BigIpUnnamedObject):
    def _set_crud_methods(self):
        self._methods = {
            'run': self._api.tm.util.dig.exec_cmd
        }

    def flush(self):
        result = dict(changed=False, stdout=list())

        try:
            output = self._methods['run']('run', utilCmdArgs=self._params['args'])
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
    params = ModuleParams()
    module = AnsibleModule(argument_spec=params.argument_spec, supports_check_mode=params.supports_check_mode)

    try:
        obj = F5BigIpUtilDig(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
