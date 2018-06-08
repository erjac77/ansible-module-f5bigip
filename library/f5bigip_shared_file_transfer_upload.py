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
module: f5bigip_shared_file_transfer_upload
short_description: BIG-IP shared file transfer upload module
description:
    - Manages uploads.
version_added: "2.4"
author:
    - "Eric Jacob (@erjac77)"
options:
    bytestring:
        description:
            - Specifies the byte string.
    filepathname:
        description:
            - Specifies the file path name.
    stringio:
        description:
            - Specifies the string io.
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    target:
        description:
            - Specifies the target.
requirements:
    - BIG-IP >= 12.0
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Upload a file
  f5bigip_shared_file_transfer_upload:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    filepathname: "{{ playbook_dir }}/files/test.txt"
  delegate_to: localhost
'''

RETURN = ''' # '''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.base import AnsibleF5Error
from ansible_common_f5.base import F5_PROVIDER_ARGS
from ansible_common_f5.bigip import F5BigIpUnnamedObject


class ModuleParams(object):
    @property
    def argument_spec(self):
        argument_spec = dict(
            bytestring=dict(type='str'),
            filepathname=dict(type='str'),
            stringio=dict(type='str'),
            target=dict(type='str')
        )
        argument_spec.update(F5_PROVIDER_ARGS)
        return argument_spec

    @property
    def supports_check_mode(self):
        return True

    @property
    def mutually_exclusive(self):
        return [
            ['bytestring', 'filepathname', 'stringio']
        ]


class F5BigIpSharedFileTransferUpload(F5BigIpUnnamedObject):
    def _set_crud_methods(self):
        self._methods = {
            'upload_file': self._api.shared.file_transfer.uploads.upload_file,
            'upload_stringio': self._api.shared.file_transfer.uploads.upload_stringio,
            'upload_bytes': self._api.shared.file_transfer.uploads.upload_bytes
        }

    def flush(self):
        result = dict(changed=False)

        if self._check_mode:
            result['changed'] = True
            return result

        try:
            if self._params['filepathname']:
                self._methods['upload_file'](self._params['filepathname'])
            elif self._params['stringio']:
                self._methods['upload_stringio'](self._params['stringio'])
            elif self._params['bytestring']:
                self._methods['upload_bytes'](self._params['bytestring'])
            result['changed'] = True
        except Exception:
            AnsibleF5Error("Cannot upload the file.")

        return result


def main():
    params = ModuleParams()
    module = AnsibleModule(argument_spec=params.argument_spec, supports_check_mode=params.supports_check_mode,
                           mutually_exclusive=params.mutually_exclusive)

    try:
        obj = F5BigIpSharedFileTransferUpload(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
