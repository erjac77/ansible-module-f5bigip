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
module: f5bigip_ltm_virtual_source_address_translation
short_description: BIG-IP LTM virtual source address translation module
description:
    - Configures the type of source address translation enabled for the virtual server as well as the pool that the source address translation will use.
version_added: "1.0"
author:
    - "Eric Jacob, @erjac77"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        required: false
        default: Common
        choices: []
        aliases: []
        version_added: 1.0
    pool:
        description:
            - Specifies the name of a LSN or SNAT pool used by the specified virtual server.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 1.0
    type:
        description:
            - Specifies the type of source address translation associated with the specified virtual server.
        required: false
        default: null
        choices: ['automap', 'lsn', 'snat', 'none']
        aliases: []
        version_added: 1.0
    virtual:
        description:
            - Specifies the virtual to which the profile belongs.
        required: true
        default: Common
        choices: []
        aliases: []
        version_added: 1.0
'''

EXAMPLES = '''
- name: Add LTM VS HTTP Profile
  f5bigip_ltm_virtual_source_address_translation:
    f5bigip_hostname: "172.16.227.35"
    f5bigip_username: "admin"
    f5bigip_password: "admin"
    f5bigip_port: "443"
    name: "http"
    partition: "Common"
    virtual: "my_http_vs"
    state: "present"
  delegate_to: localhost
'''

from ansible_common_f5bigip.f5bigip import *

BIGIP_LTM_VIRTUAL_SOURCE_ADDRESS_TRANSLATION_ARGS = dict(
    partition   =   dict(type='str'),
    pool        =   dict(type='str'),
    type        =   dict(type='str', choices=['automap', 'lsn', 'snat', 'none']),
    virtual     =   dict(type='str')
)

class F5BigIpLtmVirtualSourceAddressTranslation(F5BigIpUnnamedObject):
    def _set_crud_methods(self):
        self.virtual = self.mgmt.tm.ltm.virtuals.virtual.load(
            name=self.params['virtual'],
            partition=self.params['partition']
        )
        self.methods = {
            #'read':self.virtual.profiles_s.profiles.load,
            #'update':self.virtual.profiles_s.profiles.update,
            #'exists':self.virtual.profiles_s.profiles.exists
        }
        self.params.pop('virtual', None)

def main():
    # Translation list for conflictual params
    tr = {}
    
    module = AnsibleModuleF5BigIpObject(argument_spec=BIGIP_LTM_VIRTUAL_SOURCE_ADDRESS_TRANSLATION_ARGS, supports_check_mode=False)
    
    try:
        obj = F5BigIpLtmVirtualSourceAddressTranslation(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()