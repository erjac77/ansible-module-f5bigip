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

DOCUMENTATION = '''
---
module: f5bigip_ltm_persistence_sip
short_description: BIG-IP ltm persistence sip module
description:
    - You can use the sip component to configure a SIP persistence profile for the BIG-IP system.
version_added: 2.3
author:
    - "Gabriel Fortin"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    app_service:
        description:
            - Specifies the application service to which the object belongs.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    defaults_from:
        description:
            - Specifies the existing profile from which the system imports settings for the new profile.
        required: false
        default: sip_info
        choices: []
        aliases: []
        version_added: 2.3
    description:
        description:
            - Specifies descriptive text that identifies the component.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    match_across_pools:
        description:
            - Specifies, when enabled, that the system can use any pool that contains this persistence record.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    match_across_services:
        description:
            - Specifies, when enabled, that all persistent connections from a client IP address, which go to the same virtual IP address, also go to the same node.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    match_across_virtuals:
        description:
            - Specifies, when enabled, that all persistent connections from the same client IP address go to the same node.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    mirror:
        description:
            - Specifies whether the system mirrors persistence records to the high-availability peer.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    name:
        description:
            - Specifies a unique name for the component.
        required: true
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    override_connection_limit:
        description:
            - Specifies, when enabled, that the pool member connection limits are not enforced for persisted clients.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
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
    sip_info:
        description:
            - Specifies the SIP header field on which you want SIP sessions to persist.
        required: false
        default: none
        choices: ['Call-ID', 'From', 'none', 'SIP-ETag', 'Subject', 'To']
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
    timeout:
        description:
            - Specifies the duration of the persistence entries.
        required: false
        default: 180
        choices: []
        aliases: []
        version_added: 2.3
'''

EXAMPLES = '''
- name: Create LTM SIP Persistence profile
  f5bigip_ltm_persistence_sip:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_sip_persistence
    partition: Common
    description: My sip persistence profile
    defaults_from: sip_info
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_LTM_PERSISTENCE_SIP_ARGS = dict(
    app_service                 =   dict(type='str'),
    defaults_from               =   dict(type='str'),
    description                 =   dict(type='str'),
    match_across_pools          =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    match_across_services       =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    match_across_virtuals       =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    mirror                      =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    override_connection_limit   =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    sip_info                    =   dict(type='str', choices=['Call-ID', 'From', 'none', 'SIP-ETag', 'Subject', 'To']),
    timeout                     =   dict(type='int')
)

class F5BigIpLtmPersistenceSip(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.persistence.sips.sip.create,
            'read':     self.mgmt_root.tm.ltm.persistence.sips.sip.load,
            'update':   self.mgmt_root.tm.ltm.persistence.sips.sip.update,
            'delete':   self.mgmt_root.tm.ltm.persistence.sips.sip.delete,
            'exists':   self.mgmt_root.tm.ltm.persistence.sips.sip.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}
    
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_PERSISTENCE_SIP_ARGS, supports_check_mode=False)
    
    try:
        obj = F5BigIpLtmPersistenceSip(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()