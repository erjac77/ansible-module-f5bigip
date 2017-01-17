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
module: f5bigip_ltm_virtual_profile
short_description: BIG-IP ltm virtual profile module
description:
    - Configures profiles on the specified virtual server to direct and manage traffic.
version_added: 2.3
author:
    - "Eric Jacob, @erjac77"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    context:
        description:
            - Specifies that the profile is either a clientside or serverside (or both) profile.
        required: false
        default: all
        choices: ['all', 'clientside', 'serverside']
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
- name: Add LTM HTTP Profile to VS
  f5bigip_ltm_virtual_profile:
    f5bigip_hostname: 172.16.227.35
    f5bigip_username: admin
    f5bigip_password: admin
    f5bigip_port: 443
    name: http
    partition: Common
    virtual: my_http_vs
    state: present
  delegate_to: localhost
'''

from ansible_common_f5bigip.f5bigip import *

BIGIP_LTM_VIRTUAL_PROFILE_ARGS = dict(
    context     =   dict(type='str', choices=['all', 'clientside', 'serverside']),
    virtual     =   dict(type='str')
)

class F5BigIpLtmVirtualProfile(F5BigIpObject):
    def _set_crud_methods(self):
        self.virtual = self.mgmt.tm.ltm.virtuals.virtual.load(
            name=self.params['virtual'],
            partition=self.params['partition']
        )
        self.methods = {
            'create':self.virtual.profiles_s.profiles.create,
            'read':self.virtual.profiles_s.profiles.load,
            'update':self.virtual.profiles_s.profiles.update,
            'delete':self.virtual.profiles_s.profiles.delete,
            'exists':self.virtual.profiles_s.profiles.exists
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
    
    module = AnsibleModuleF5BigIpObject(argument_spec=BIGIP_LTM_VIRTUAL_PROFILE_ARGS, supports_check_mode=False)
    
    try:
        obj = F5BigIpLtmVirtualProfile(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':  
    main()