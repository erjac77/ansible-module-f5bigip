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
module: f5bigip_sys_file_ifile
short_description: BIG-IP sys file ifile module
description:
    - Manages an iFile file.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    app_service:
        description:
            - Specifies the application service that the object belongs to.
    name:
        description:
            - Specifies unique name for the component.
        required: true
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        default: Common
    source_path:
        description:
            - This optional attribute takes a URL.
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Create SYS iFile
  f5bigip_sys_file_ifile:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_file
    partition: Common
    source_path: file:/var/config/rest/downloads/my_file.txt
    state: present
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_SYS_FILE_IFILE_ARGS = dict(
    app_service     =   dict(type='str'),
    source_path     =   dict(type='str'),
)

class F5BigIpSysFileIfile(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.sys.file.ifiles.ifile.create,
            'read':     self.mgmt_root.tm.sys.file.ifiles.ifile.load,
            'update':   self.mgmt_root.tm.sys.file.ifiles.ifile.update,
            'delete':   self.mgmt_root.tm.sys.file.ifiles.ifile.delete,
            'exists':   self.mgmt_root.tm.sys.file.ifiles.ifile.exists
        }

def main():
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_SYS_FILE_IFILE_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpSysFileIfile(check_mode=module.supports_check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

if __name__ == '__main__':
    main()