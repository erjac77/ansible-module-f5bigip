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
module: f5bigip_ltm_profile_http2
short_description: BIG-IP ltm profile http2 module
description:
    - Configures a HTTP/2 protocol profile.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    activation_modes:
        description:
            - Specifies what will cause a connection to be treated as a HTTP/2 connection.
        default: { npn alpn }
        choices: ['npn', 'alpn', 'always']
    concurrent_streams_per_connection:
        description:
            - Specifies how many concurrent requests are allowed to be outstanding on a single HTTP/2 connection.
    connection_idle_timeout:
        description:
            - Specifies how many seconds a HTTP/2 connection is left open idly before it is shutdown.
    defaults_from:
        description:
            - Specifies the profile that you want to use as the parent profile.
        default: http2
    description:
        description:
            - User defined description.
    frame_size:
        description:
            - Specifies the size of the data frames, in bytes, that HTTP/2 will send to the client.
        default: 2048
    header_table_size:
        description:
            - Specifies the size of the header table, in KB.
    insert_header:
        description:
            - Specifies the name of the HTTP header controlled by insert-header.
        required: true
        default: disabled
        choices: ['disabled', 'enabled']
    insert_header_name:
        description:
            - Specifies the name of the HTTP header controlled by insert-header.
        required: true
    name:
        description:
            - Specifies a unique name for the component.
        required: true
    receive_window:
        description:
            - Specifies the receive window, in KB.
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    write_size:
        description:
            - Specifies the total size of combined data frames, in bytes, HTTP/2 will send in a single write.
        default: 16384
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
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

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_LTM_PROFILE_HTTP2_ARGS = dict(
    activation_modes=dict(type='str', choices=['npn', 'alpn', 'always']),
    concurrent_streams_per_connection=dict(type='int'),
    connection_idle_timeout=dict(type='int'),
    defaults_from=dict(type='str'),
    description=dict(type='str'),
    frame_size=dict(type='int'),
    header_table_size=dict(type='int'),
    insert_header=dict(type='str', choices=F5_ACTIVATION_CHOICES),
    insert_header_name=dict(type='str'),
    receive_window=dict(type='int'),
    write_size=dict(type='int')
)


class F5BigIpLtmProfileHttp2(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create': self.mgmt_root.tm.ltm.profile.http2s.http2.create,
            'read': self.mgmt_root.tm.ltm.profile.http2s.http2.load,
            'update': self.mgmt_root.tm.ltm.profile.http2s.http2.update,
            'delete': self.mgmt_root.tm.ltm.profile.http2s.http2.delete,
            'exists': self.mgmt_root.tm.ltm.profile.http2s.http2.exists
        }


def main():
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_PROFILE_HTTP2_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpLtmProfileHttp2(check_mode=module.supports_check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
