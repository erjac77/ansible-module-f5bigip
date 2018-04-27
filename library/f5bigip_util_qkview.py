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
module: f5bigip_util_qkview
short_description: BIG-IP util qkview module
description:
    - Gathers diagnostic information from a BIG-IP system.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
    - "Eric Jacob (@erjac77)"
options:
    complete:
        description:
            - Collects complete system information, possibly including sensitive user information.
        type: bool
        default: false
    exclude:
        description:
            - Excludes specified log files from output.
        choices: ['audit', 'secure', 'bash_history', 'all']
    filename:
        description:
            - Provides an alternate file name.
        default: <hostname of BIG-IP>.qkview
    max_file_size:
        description:
            - Sets maximum file size to capture, in bytes.
            - Setting this value to 0 is equivalent to 75 MB.
        default: 0
    timeout:
        description:
            - Sets maximum time (in seconds) for any one module to complete.
            - To set the value to the utility's maximum value, type 0.
        default: 360
    verbose:
        description:
            - Displays verbose output.
        type: bool
        default: false
notes:
    - Requires BIG-IP software version >= 12.0
    - See U(https://support.f5.com/csp/article/K23928121) for an overview of qkview command-line options.
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Generates a Qkview file
  f5bigip_util_qkview:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    filename: "{{ inventory_hostname }}.qkview"
    max_file_size: 0
    timeout: 420
    exclude: [audit, secure]
    verbose: yes
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

BIGIP_UTIL_QKVIEW_ARGS = dict(
    complete=dict(type='bool'),
    exclude=dict(type='list'),
    filename=dict(type='str'),
    max_file_size=dict(type='int'),
    timeout=dict(type='int'),
    verbose=dict(type='bool')
)


class F5BigIpUtilQkview(F5BigIpUnnamedObject):

    def set_crud_methods(self):
        self.methods = {
            'run': self.mgmt_root.tm.util.qkview.exec_cmd
        }

    @property
    def complete(self):
        if self.params['complete']:
            return '-c'
        return None

    @property
    def exclude(self):
        if self.params['exclude'] is None:
            return None
        exclude = ','.join(self.params['exclude'])
        return '--exclude {0}'.format(exclude)

    @property
    def filename(self):
        if self.params['filename'] is None:
            return None
        return '-f {0}'.format(self.params['filename'])

    @property
    def max_file_size(self):
        if self.params['maxFileSize'] is None:
            return None
        return '-s {0}'.format(self.params['maxFileSize'])

    @property
    def timeout(self):
        if self.params['timeout'] is None:
            return None
        return '-t {0}'.format(self.params['timeout'])

    @property
    def verbose(self):
        if self.params['verbose']:
            return '-v'
        return None

    def run(self):
        result = dict(changed=False, stdout=list())

        args = dict()
        for key in BIGIP_UTIL_QKVIEW_ARGS:
            if getattr(self, key) is not None:
                args[key] = getattr(self, key)

        if self.check_mode:
            result['changed'] = True
            return result

        try:
            output = self.methods['run']('run', utilCmdArgs='{0}'.format(' '.join(str(a) for a in args.values())))
            result['changed'] = True
        except Exception as exc:
            err_msg = 'Cannot generate the Qkview file.'
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

    module = AnsibleModuleF5BigIpUnnamedObject(argument_spec=BIGIP_UTIL_QKVIEW_ARGS, supports_check_mode=True)

    try:
        obj = F5BigIpUtilQkview(check_mode=module.check_mode, **module.params)
        result = obj.run()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
