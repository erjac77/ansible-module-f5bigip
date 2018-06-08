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
module: f5bigip_util_get_dossier
short_description: BIG-IP util get dossier module
description:
    - Displays info about system dossier.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
    - "Eric Jacob (@erjac77)"
options:
    addon_key:
        description:
            - Specifies the add-on registration key.
            - To apply to multiple keys, you can separate the keys using comma (,) characters.
    base_key:
        description:
            - Specifies the base registration key.
            - To apply to multiple keys, you can separate the keys using comma (,) characters.
        required: true
    clear_text:
        description:
            - Displays clear-text dossier.
        type: bool
        default: false
    inactive_key:
        description:
            - Specifies the expired evaluation license key.
            - To apply to multiple keys, you can separate the keys using comma (,) characters.
    kernel_version:
        description:
            - Specifies the kernel version.
    version:
        description:
            - Specifies the system version.
            - Required format is "<product> <version> <build>".
requirements:
    - BIG-IP >= 12.0
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Gets a Dossier
  f5bigip_util_get_dossier:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    base_key: 'registration-key'
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
            addon_key=dict(type='str'),
            clear_text=dict(type='bool'),
            base_key=dict(type='str', required=True),
            inactive_key=dict(type='str'),
            kernel_version=dict(type='str'),
            version=dict(type='str')
        )
        argument_spec.update(F5_PROVIDER_ARGS)
        return argument_spec

    @property
    def supports_check_mode(self):
        return True


class F5BigIpUtilGetDossier(F5BigIpUnnamedObject):
    def _set_crud_methods(self):
        self._methods = {
            'run': self._api.tm.util.get_dossier.exec_cmd
        }

    @property
    def addon_key(self):
        if self._params['addonKey'] is None:
            return None
        return '-a {0}'.format(self._params['addonKey'])

    @property
    def base_key(self):
        if self._params['baseKey'] is None:
            return None
        return '-b {0}'.format(self._params['baseKey'])

    @property
    def clear_text(self):
        if self._params['clearText']:
            return '-c'
        return None

    @property
    def inactive_key(self):
        if self._params['inactiveKey'] is None:
            return None
        return '-i {0}'.format(self._params['inactiveKey'])

    @property
    def kernel_version(self):
        if self._params['kernelVersion'] is None:
            return None
        return '-k {0}'.format(self._params['kernelVersion'])

    @property
    def version(self):
        if self._params['version'] is None:
            return None
        return '-v "{0}"'.format(self._params['version'])

    def flush(self):
        result = dict(changed=False, stdout=list())

        if self._check_mode:
            result['changed'] = True
            return result

        try:
            output = self._methods['run']('run',
                                          utilCmdArgs='{0}'.format(' '.join(str(a) for a in self._params.values())))
            result['changed'] = True
        except Exception as exc:
            err_msg = 'Could not execute the Get Dossier command.'
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
        obj = F5BigIpUtilGetDossier(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
