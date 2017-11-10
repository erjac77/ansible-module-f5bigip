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
module: f5bigip_ltm_virtual_source_address_translation
short_description: BIG-IP ltm virtual source address translation module
description:
    - Configures the type of source address translation enabled for the virtual server as well as the pool that the source address translation will use.
version_added: 2.3
author:
    - "Eric Jacob, @erjac77"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    pool:
        description:
            - Specifies the name of a LSN or SNAT pool used by the specified virtual server.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    type:
        description:
            - Specifies the type of source address translation associated with the specified virtual server.
        required: true
        default: null
        choices: ['automap', 'lsn', 'snat', 'none']
        aliases: []
        version_added: 2.3
    virtual:
        description:
            - Specifies the full path of the virtual to which the profile belongs.
        required: true
        default: Common
        choices: []
        aliases: []
        version_added: 2.3
'''

EXAMPLES = '''
- name: Add LTM Source Address Translation
  f5bigip_ltm_virtual_source_address_translation:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    type: snat
    pool: my_snatpool
    virtual: my_http_vs
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_LTM_VIRTUAL_SOURCE_ADDRESS_TRANSLATION_ARGS = dict(
    pool        =   dict(type='str'),
    type        =   dict(type='str', choices=['automap', 'lsn', 'snat', 'none'], required=True),
    virtual     =   dict(type='str')
)

class F5BigIpLtmVirtualSourceAddressTranslation(F5BigIpUnnamedObject):
    def set_crud_methods(self):
        self.virtual = self.mgmt_root.tm.ltm.virtuals.virtual.load(**self._get_resource_id_from_path(self.params['virtual']))
        self.params.pop('virtual', None)

    def _read(self):
        return self.virtual.sourceAddressTranslation
    
    def flush(self):
        has_changed = False
        result = dict()
        sat = self._read()

        if self.state == "absent" and sat['type'] != 'none':
            has_changed = True
            sat['type'] = 'none'

        if self.state == "present":
            if self.params['type'] == 'snat':
                if self.params['pool'] is None:
                    raise AnsibleF5Error("Missing required param 'pool'")

            for key, val in self.params.iteritems():
                if key in sat:
                    if sat[key] != val:
                        has_changed = True
                        sat[key] = val
                else:
                    has_changed = True
                    sat.update({key: val})

        if has_changed:
            self.virtual.sourceAddressTranslation = sat
            self.virtual.update()
            self.virtual.refresh()
        
        result.update(dict(changed=has_changed))
        return result

def main():
    # Translation list for conflictual params
    tr = {}
    
    module = AnsibleModuleF5BigIpUnnamedObject(argument_spec=BIGIP_LTM_VIRTUAL_SOURCE_ADDRESS_TRANSLATION_ARGS, supports_check_mode=False)
    
    try:
        obj = F5BigIpLtmVirtualSourceAddressTranslation(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()