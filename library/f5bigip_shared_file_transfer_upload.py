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
module: f5bigip_shared_file_transfer_upload
short_description: BIG-IP shared file transfer upload module
description:
    - Manages uploads.
version_added: 2.3
author:
    - "Eric Jacob, @erjac77"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    bytestring:
        description:
            - Specifies the byte string.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    filepathname:
        description:
            - Specifies the file path name.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    stringio:
        description:
            - Specifies the string io.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        required: false
        default: present
        choices: ['absent', 'present']
        aliases: []
        version_added: 2.3
    target:
        description:
            - Specifies the target.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
'''

EXAMPLES = '''
- name: Upload a file
  f5bigip_shared_file_transfer_upload:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    filepathname: "{{ playbook_dir }}/files/test.txt"
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_SHARED_FILE_TRANSFER_UPLOAD_ARGS = dict(
    bytestring      =   dict(type='str'),
    filepathname    =   dict(type='str'),
    stringio        =   dict(type='str'),
    target          =   dict(type='str')
)

class F5BigIpSharedFileTransferUpload(F5BigIpUnnamedObject):
    def set_crud_methods(self):
        self.methods = {
            'upload_file':      self.mgmt_root.shared.file_transfer.uploads.upload_file,
            'upload_stringio':  self.mgmt_root.shared.file_transfer.uploads.upload_stringio,
            'upload_bytes':     self.mgmt_root.shared.file_transfer.uploads.upload_bytes
        }

    def _upload(self):
        if self.params['filepathname']:
            self.methods['upload_file'](self.params['filepathname'])
        elif self.params['stringio']:
            self.methods['upload_stringio'](self.params['stringio'])
        elif self.params['bytestring']:
            self.methods['upload_bytes'](self.params['bytestring'])

    def _present(self):
        has_changed = False

        try:
            self._upload()
            has_changed = True
        except Exception as exc:
            AnsibleF5Error("Cannot upload the file")

        return has_changed

def main():
    # Translation list for conflictual params
    tr = {}
    
    module = AnsibleModuleF5BigIpUnnamedObject(
        argument_spec=BIGIP_SHARED_FILE_TRANSFER_UPLOAD_ARGS,
        supports_check_mode=False,
        mutually_exclusive=[
            ['bytestring', 'filepathname', 'stringio']
        ]
    )

    try:
        obj = F5BigIpSharedFileTransferUpload(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':  
    main()