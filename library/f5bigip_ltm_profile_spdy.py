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
module: f5bigip_ltm_profile_spdy
short_description: BIG-IP ltm profile spdy module
description:
    - Configures a SPDY protocol profile.
version_added: 2.3
author:
    - "Gabriel Fortin"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    activation_mode:
        description:
            - Specifies what will cause a connection to be treated as a SPDY connection.
        required: false
        default: npn
        choices: ['npn', 'always']
        aliases: []
    compression_level:
        description:
            - Specifies the level of compression used by default.
        required: false
        default: 5
        choices: []
        aliases: []
    compression_window_size:
        description:
            - Specifies the size of the compression window, in KB.
        required: false
        default: 8
        choices: []
        aliases: []
    concurrent_streams_per_connection:
        description:
            - Specifies how many concurrent requests are allowed to be outstanding on a single SPDY connection.
        required: false
        default: null
        choices: []
        aliases: []
    connection_idle_timeout:
        description:
            - Specifies how many seconds a SPDY connection is left open idly before it is shutdown.
        required: false
        default: null
        choices: []
        aliases: []
    defaults_from:
        description:
            - Specifies the profile that you want to use as the parent profile.
        required: false
        default: spdy
        choices: []
        aliases: []
    description:
        description:
            - User defined description.
        required: false
        default: null
        choices: []
        aliases: []
    frame_size:
        description:
            - Specifies the size of the data frames, in bytes, that SPDY will send to the client.
        required: false
        default: 2048
        choices: []
        aliases: []
    insert_header:
        description:
            - Specifies the name of the HTTP header controlled by insert-header.
        required: true
        default: disabled
        choices: ['disabled', 'enabled']
        aliases: []
    insert_header_name:
        description:
            - Specifies the name of the HTTP header controlled by insert-header.
        required: true
        default: X-SPDY
        choices: []
        aliases: []
    name:
        description:
            - Specifies a unique name for the component.
        required: true
        default: null
        choices: []
        aliases: []
    priority_handling:
        description:
            - Specifies how SPDY should handle priorities of concurrent streams within the same connection.
        required: false
        default: strict
        choices: ['strict', 'fair']
        aliases: []
    protocol_versions:
        description:
            - Specifies which SPDY protocols clients are allowed to use.
        required: false
        default: { spdy3 spdy2 http1.1 }
        choices: ['spdy3', 'spdy2', 'http1.1']
        aliases: []
    receive_window:
        description:
            - Specifies the receive window, in KB.
        required: false
        default: 32
        choices: []
        aliases: []
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        required: false
        default: present
        choices: ['absent', 'present']
        aliases: []
    write_size:
        description:
            - Specifies the total size of combined data frames, in bytes, SPDY will send in a single write.
        required: false
        default: 16384
        choices: []
        aliases: []
'''

EXAMPLES = '''
- name: Create LTM Profile spdy
  f5bigip_ltm_profile_spdy:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_spdy_profile
    partition: Common
    description: My spdy profile
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_LTM_PROFILE_SPDY_ARGS = dict(
    activation_mode                      =    dict(type='str', choices=['npn', 'always']),
    compression_level                    =    dict(type='int'),
    compression_window_size              =    dict(type='int'),
    concurrent_streams_per_connection    =    dict(type='int'),
    connection_idle_timeout              =    dict(type='int'),
    defaults_from                        =    dict(type='str'),
    description                          =    dict(type='str'),
    frame_size                           =    dict(type='int'),
    insert_header                        =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    insert_header_name                   =    dict(type='str'),
    priority_handling                    =    dict(type='str', choices=['strict', 'fair']),
    protocol_versions                    =    dict(type='dict'),
    receive_window                       =    dict(type='int'),
    write_size                           =    dict(type='int')
)

class F5BigIpLtmProfileSpdy(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.profile.spdys.spdy.create,
            'read':     self.mgmt_root.tm.ltm.profile.spdys.spdy.load,
            'update':   self.mgmt_root.tm.ltm.profile.spdys.spdy.update,
            'delete':   self.mgmt_root.tm.ltm.profile.spdys.spdy.delete,
            'exists':   self.mgmt_root.tm.ltm.profile.spdys.spdy.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}

    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_PROFILE_SPDY_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpLtmProfileSpdy(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()