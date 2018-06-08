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
module: f5bigip_sys_config
short_description: BIG-IP sys config module
description:
    - Manages the BIG-IP system configuration.
version_added: "2.4"
author:
    - "Eric Jacob (@erjac77)"
options:
    base:
        description:
            - Indicates the base configuration.
        choices: ['yes', 'no']
    binary:
        description:
            - Indicates binary configuration.
        choices: ['yes', 'no']
    default:
        description:
            - Indicates factory default configuration.
        choices: ['yes', 'no']
    exclude_gtm:
        description:
            - Indicates the BIG-IP configuration, excluding GTMs.
        choices: ['yes', 'no']
    file:
        description:
            - Loads or saves a configuration from the specified file.
    files_folder:
        description:
            - Loads disk files referred to by the configuration from the folder tree under the specified folder.
    gtm_only:
        description:
            - Indicates the Global Traffic Manage (GTM) configuration.
        choices: ['yes', 'no']
    merge:
        description:
            - Loads the configuration from the specified file, which modifies the running configuration.
        choices: ['yes', 'no']
    options:
        description:
            - Specifies the options for the specified command.
    partitions:
        description:
            - Indicates the partitions in which configuration components reside.
    passphrase:
        description:
            - Specifies a password to save or load an encrypted configuration file.
    user_only:
        description:
            - Indicates the configuration including user account information only.
        choices: ['yes', 'no']
    tar_file:
        description:
            - Loads or saves disk files referred to by the configuration from the specified tar file.
    time_stamp:
        description:
            - Inserts a time-stamp in a file name.
        choices: ['yes', 'no']
    verify:
        description:
            - Validates the specified configuration from file(s) without changing the running configuration.
        choices: ['yes', 'no']
    wait:
        description:
            - Specifies that tmsh should wait for another instance of tmsh to finish saving the configuration before
              proceeding.
        choices: ['yes', 'no']
requirements:
    - BIG-IP >= 12.0
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Save the configuration
  f5bigip_sys_config:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    command: save
  delegate_to: localhost

- name: Save the configuration to a SCF file
  f5bigip_sys_config:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    command: save
    options:
      - { "file": "{{ scf_filename }}" }
      - { "no-passphrase": true }
  delegate_to: localhost

- name: Load and merge the specified configuration
  f5bigip_sys_config:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    command: load
    merge: yes
    file: my_file
  delegate_to: localhost
'''

RETURN = ''' # '''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.six import iteritems
from ansible_common_f5.base import AnsibleF5Error
from ansible_common_f5.base import F5_PROVIDER_ARGS
from ansible_common_f5.bigip import F5BigIpUnnamedObject


class ModuleParams(object):
    @property
    def argument_spec(self):
        argument_spec = dict(
            # Command
            command=dict(type='str', choices=['save', 'load'], required=True),
            options=dict(type='list'),
            # Common arguments
            base=dict(type='bool'),
            current_partition=dict(type='bool'),
            exclude_gtm=dict(type='bool'),
            file=dict(type='str'),
            gtm_only=dict(type='bool'),
            partitions=dict(type='list'),
            passphrase=dict(type='str', no_log=True),
            user_only=dict(type='bool'),
            tar_file=dict(type='str'),
            # Save specific arguments
            binary=dict(type='bool'),
            time_stamp=dict(type='bool'),
            wait=dict(type='bool'),
            # Load specific arguments
            default=dict(type='bool'),
            files_folder=dict(type='str'),
            merge=dict(type='bool'),
            verify=dict(type='bool')
        )
        argument_spec.update(F5_PROVIDER_ARGS)
        return argument_spec

    @property
    def supports_check_mode(self):
        return True

    @property
    def mutually_exclusive(self):
        return [
            ['base', 'binary', 'default', 'exclude_gtm', 'gtm_only', 'user_only']
        ]


class F5BigIpSysConfig(F5BigIpUnnamedObject):
    def _set_crud_methods(self):
        self._methods = {
            'exec_cmd': self._api.tm.sys.config.exec_cmd
        }

    def flush(self):
        result = dict(changed=False)
        command = self._params.pop('command', None)

        # Remove empty params
        params = dict((k, v) for k, v in iteritems(self._params) if v is not None)

        if self._check_mode:
            result['changed'] = True
            return result

        try:
            self._methods['exec_cmd'](command, **params)
            result['changed'] = True
        except Exception as exc:
            raise AnsibleF5Error("Could not execute '" + command + "' command: " + exc.message)

        return result


def main():
    params = ModuleParams()
    module = AnsibleModule(argument_spec=params.argument_spec, supports_check_mode=params.supports_check_mode,
                           mutually_exclusive=params.mutually_exclusive)

    try:
        obj = F5BigIpSysConfig(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
