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
module: f5bigip_ltm_profile_one_connect
short_description: BIG-IP ltm one-connect profile module
description:
    - Configures a one-connect profile.
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
            - Specifies the name of the application service to which the profile belongs.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    defaults_from:
        description:
            - Specifies the profile that you want to use as the parent profile.
        required: false
        default: oneconnect
        choices: []
        aliases: []
        version_added: 2.3
    description:
        description:
            - User defined description.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    idle_timeout_override:
        description:
            - Specifies the number of seconds that a connection is idle before the connection flow is eligible for deletion.
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
    partition:
        description:
            - Displays the administrative partition within which the component resides.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    port:
        description:
            - Specifies a service for the data channel port used for this one-connect profile.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
   share_pools:
        description:
            - Indicates that connections may be shared not only within a virtual server, but also among similar virtual servers (e.g. those that differ only in destination address).
        required: false
        default: null
        choices: ['enabled', 'disabled']
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
    max_age:
        description:
            - Specifies the maximum age, in number of seconds, of a connection in the connection reuse pool.
        required: false
        default: 86400
        choices: []
        aliases: []
        version_added: 2.3
    max_reuse:
        description:
            - Specifies the maximum number of times that a server connection can be reused.
        required: false
        default: 1000
        choices: []
        aliases: []
        version_added: 2.3
   max_size:
        description:
            - Specifies the maximum number of connections that the system holds in the connection reuse pool.
        required: false
        default: 10000
        choices: []
        aliases: []
        version_added: 2.3
   source_mask:
        description:
            - Specifies a source IP mask.
        required: false
        default: 0.0.0.0
        choices: []
        aliases: []
        version_added: 2.3
   limit_type:
        description:
            - Connection limits with OneConnect are different from straight TCP connection limits.
        required: false
        default: null
        choices: ['none', 'idle', 'strict']
        aliases: []
        version_added: 2.3
'''

EXAMPLES = ''' 
- name: Create LTM OneConnect profile
  f5bigip_ltm_profile_one_connect:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_one_connect_profile
    partition: Common
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_LTM_PROFILE_ONE_CONNECT_ARGS = dict(
    app_service     =   dict(type='str'),
    defaults_from   =   dict(type='str'),
    description     =   dict(type='str'),
    share_pools     =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    max_age         =   dict(type='int'),
    max_reuse       =   dict(type='int'),
    max_size        =   dict(type='int'),
    source_mask     =   dict(type='str'),
    limit_type      =   dict(type='str', choices=['none', 'idle', 'strict'])
)

class F5BigIpLtmProfileOneConnect(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.profile.one_connects.one_connect.create,
            'read':     self.mgmt_root.tm.ltm.profile.one_connects.one_connect.load,
            'update':   self.mgmt_root.tm.ltm.profile.one_connects.one_connect.update,
            'delete':   self.mgmt_root.tm.ltm.profile.one_connects.one_connect.delete,
            'exists':   self.mgmt_root.tm.ltm.profile.one_connects.one_connect.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}
    
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_PROFILE_ONE_CONNECT_ARGS, supports_check_mode=False)
    
    try:
        obj = F5BigIpLtmProfileOneConnect(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()