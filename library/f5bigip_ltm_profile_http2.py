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
module: f5bigip_ltm_profile_http2
short_description: BIG-IP ltm profile http2 module
description:
    - Configures a HTTP/2 protocol profile.
version_added: 2.3
author:
    - "Gabriel Fortin"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    activation_modes:
        description:
            - Specifies what will cause a connection to be treated as a HTTP/2 connection.
        required: false
        default: { npn alpn }
        choices: ['npn', 'alpn', 'always']
        aliases: []
    concurrent_streams_per_connection:
        description:
            - Specifies how many concurrent requests are allowed to be outstanding on a single HTTP/2 connection.
        required: false
        default: null
        choices: []
        aliases: []
    connection_idle_timeout:
        description:
            - Specifies how many seconds a HTTP/2 connection is left open idly before it is shutdown.
        required: false
        default: null
        choices: []
        aliases: []
    defaults_from:
        description:
            - Specifies the profile that you want to use as the parent profile.
        required: false
        default: http2
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
            - Specifies the size of the data frames, in bytes, that HTTP/2 will send to the client.
        required: false
        default: 2048
        choices: []
        aliases: []
    header_table_size:
        description:
            - Specifies the size of the header table, in KB.
        required: false
        default: null
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
        default: null
        choices: []
        aliases: []
    name:
        description:
            - Specifies a unique name for the component.
        required: true
        default: null
        choices: []
        aliases: []
    receive_window:
        description:
            - Specifies the receive window, in KB.
        required: false
        default: null
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
            - Specifies the total size of combined data frames, in bytes, HTTP/2 will send in a single write.
        required: false
        default: 16384
        choices: []
        aliases: []
'''

EXAMPLES = '''
- name: Create LTM Profile HTTP2
  f5bigip_ltm_profile_http2:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_http2_profile
    partition: Common
    description: My http2 profile
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_LTM_PROFILE_HTTP2_ARGS = dict(
    activation_modes                     =    dict(type='str', choices=['npn', 'alpn', 'always']),
    concurrent_streams_per_connection    =    dict(type='int'),
    connection_idle_timeout              =    dict(type='int'),
    defaults_from                        =    dict(type='str'),
    description                          =    dict(type='str'),
    frame_size                           =    dict(type='int'),
    header_table_size                    =    dict(type='int'),
    insert_header                        =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    insert_header_name                   =    dict(type='str'),
    receive_window                       =    dict(type='int'),
    write_size                           =    dict(type='int')
)

class F5BigIpLtmProfileHttp2(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.profile.http2s.http2.create,
            'read':     self.mgmt_root.tm.ltm.profile.http2s.http2.load,
            'update':   self.mgmt_root.tm.ltm.profile.http2s.http2.update,
            'delete':   self.mgmt_root.tm.ltm.profile.http2s.http2.delete,
            'exists':   self.mgmt_root.tm.ltm.profile.http2s.http2.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}

    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_PROFILE_HTTP2_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpLtmProfileHttp2(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()