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

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: f5bigip_ltm_virtual_persist
short_description: BIG-IP ltm virtual persist module
description:
    - Configures profiles on the specified virtual server to manage connection persistence.
version_added: 2.3
author:
    - "Eric Jacob, @erjac77"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    default:
        description:
            - Specifies which profile you want the virtual server to use if an iRule does not specify a persistence method.
        required: false
        default: no
        choices: ['no', 'yes']
        aliases: []
        version_added: 2.3
    name:
        description:
            - Specifies unique name for the component.
        required: true
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        required: false
        default: Common
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
    virtual:
        description:
            - Specifies the virtual to which the profile belongs.
        required: true
        default: Common
        choices: []
        aliases: []
        version_added: 2.3
'''

EXAMPLES = '''
- name: Add LTM Persist Profile to VS
  f5bigip_ltm_virtual_persist:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: source_addr
    partition: Common
    virtual: my_http_vs
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_LTM_VIRTUAL_PERSIST_ARGS = dict(
    default     =   dict(type='str', choices=F5_POLAR_CHOICES),
    virtual     =   dict(type='str')
)

class F5BigIpLtmVirtualPersist(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.virtual = self.mgmt_root.tm.ltm.virtuals.virtual.load(
            name=self.params['virtual'],
            partition=self.params['partition']
        )
        self.methods = {
            'create':   self.virtual.profiles_s.profiles.create,
            'read':     self.virtual.profiles_s.profiles.load,
            'update':   self.virtual.profiles_s.profiles.update,
            'delete':   self.virtual.profiles_s.profiles.delete,
            'exists':   self.virtual.profiles_s.profiles.exists
        }
        self.params.pop('virtual', None)

    def _exists(self):
        keys = self.virtual.profiles_s.get_collection()
        for key in keys:
            name = self.params['name']
            if key.name == name:
                return True

        return False

def main():
    # Translation list for conflictual params
    tr = {}
    
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_VIRTUAL_PERSIST_ARGS, supports_check_mode=False)
    
    try:
        obj = F5BigIpLtmVirtualPersist(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()