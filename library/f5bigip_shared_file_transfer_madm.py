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
module: f5bigip_shared_file_transfer_madm
short_description: BIG-IP shared file transfer madm module
description:
    - Downloads files.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    file_name:
        description:
            - Specifies the name of the file to download.
        required: true
    download_path:
        description:
            - Specifies the path where the file will be downloaded.
        required: true
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Download file
  f5bigip_shared_file_transfer_madm:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    file_name: test.txt
    download_path: /var/test.txt
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_SHARED_FILE_TRANSFER_MADM_ARGS = dict(
    file_name=dict(type='str', required=True),
    download_path=dict(type='str', required=True)
)


class F5BigIpSharedFileTransferMadm(F5BigIpUnnamedObject):
    def set_crud_methods(self):
        self.methods = {
            'download_file': self.mgmt_root.shared.file_transfer.madm.download_file
        }

    def download(self):
        has_changed = False

        try:
            self.methods['download_file'](self.params['fileName'], self.params['downloadPath'])
            has_changed = True
        except Exception:
            raise AnsibleF5Error("Can't download the file")

        return {'changed': has_changed}


def main():
    module = AnsibleModuleF5BigIpUnnamedObject(argument_spec=BIGIP_SHARED_FILE_TRANSFER_MADM_ARGS,
                                               supports_check_mode=False)

    try:
        obj = F5BigIpSharedFileTransferMadm(check_mode=module.supports_check_mode, **module.params)
        result = obj.download()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
