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
module: f5bigip_ltm_persistence_cookie
short_description: BIG-IP ltm persistence cookie module
description:
    - Configures a cookie persistence profile.
version_added: 2.3
author:
	- "Eric Jacob, @erjac77"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    always_send:
        description:
            - Send the cookie persistence entry on every reply, even if the entry has previously been supplied to the client.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    app_service:
        description:
            - Specifies the application service to which the object belongs.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    cookie_name:
        description:
            - Specifies a unique name for the cookie.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    cookie_encryption:
        description:
            - Specifies the way in which cookie format will be used.
        required: false
        default: required
        choices: ['required', 'preferred', 'disabled']
        aliases: []
        version_added: 2.3
    cookie_encryption_passphrase:
        description:
            - Specifies a passphrase to be used for cookie encryption.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    defaults_from:
        description:
            - Specifies the existing profile from which the system imports settings for the new profile.
        required: false
        default: cookie
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
    expiration:
        description:
            - Specifies the cookie expiration date in the format d:h:m:s, h:m:s, m:s or seconds.
        required: false
        default: session cookie
        choices: []
        aliases: []
        version_added: 2.3
    hash_length:
        description:
            - Specifies the cookie hash length.
        required: false
        default: 0
        choices: []
        aliases: []
        version_added: 2.3
    hash_offset:
        description:
            - Specifies the cookie hash offset.
        required: false
        default: 0
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
    method:
        description:
            - Specifies the type of cookie processing that the system uses.
        required: false
        default: insert
        choices: ['hash', 'insert', 'passive', 'rewrite']
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
        default: 0
        choices: []
        aliases: []
        version_added: 2.3
'''

EXAMPLES = '''
- name: Create LTM Cookie Persistence profile
  f5bigip_ltm_persistence_cookie:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_cookie_persistence
    partition: Common
    description: My cookie persistence profile
    defaults_from: /Common/cookie
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_LTM_PERSISTENCE_COOKIE_ARGS = dict(
    always_send                     =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    app_service                     =   dict(type='str'),
    cookie_name                     =   dict(type='str'),
    cookie_encryption               =   dict(type='str', choices=['required', 'preferred', 'disabled']),
    cookie_encryption_passphrase    =   dict(type='str'),
    defaults_from                   =   dict(type='str'),
    description                     =   dict(type='str'),
    expiration                      =   dict(type='str'),
    hash_length                     =   dict(type='int'),
    hash_offset                     =   dict(type='int'),
    match_across_pools              =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    match_across_services           =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    match_across_virtuals           =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    method                          =   dict(type='str', choices=['hash', 'insert', 'passive', 'rewrite']),
    mirror                          =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    override_connection_limit       =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    timeout                         =   dict(type='int')
)

class F5BigIpLtmPersistenceCookie(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.persistence.cookies.cookie.create,
            'read':     self.mgmt_root.tm.ltm.persistence.cookies.cookie.load,
            'update':   self.mgmt_root.tm.ltm.persistence.cookies.cookie.update,
            'delete':   self.mgmt_root.tm.ltm.persistence.cookies.cookie.delete,
            'exists':   self.mgmt_root.tm.ltm.persistence.cookies.cookie.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}
    
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_PERSISTENCE_COOKIE_ARGS, supports_check_mode=False)
    
    try:
        obj = F5BigIpLtmPersistenceCookie(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()