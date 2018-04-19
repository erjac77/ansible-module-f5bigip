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
module: f5bigip_ltm_profile_spdy
short_description: BIG-IP ltm profile spdy module
description:
    - Configures a SPDY protocol profile.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    activation_mode:
        description:
            - Specifies what will cause a connection to be treated as a SPDY connection.
        default: npn
        choices: ['npn', 'always']
    compression_level:
        description:
            - Specifies the level of compression used by default.
        default: 5
    compression_window_size:
        description:
            - Specifies the size of the compression window, in KB.
        default: 8
    concurrent_streams_per_connection:
        description:
            - Specifies how many concurrent requests are allowed to be outstanding on a single SPDY connection.
    connection_idle_timeout:
        description:
            - Specifies how many seconds a SPDY connection is left open idly before it is shutdown.
    defaults_from:
        description:
            - Specifies the profile that you want to use as the parent profile.
        default: spdy
    description:
        description:
            - User defined description.
    frame_size:
        description:
            - Specifies the size of the data frames, in bytes, that SPDY will send to the client.
        default: 2048
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
        default: X-SPDY
    name:
        description:
            - Specifies a unique name for the component.
        required: true
    priority_handling:
        description:
            - Specifies how SPDY should handle priorities of concurrent streams within the same connection.
        default: strict
        choices: ['strict', 'fair']
    protocol_versions:
        description:
            - Specifies which SPDY protocols clients are allowed to use.
        default: { spdy3 spdy2 http1.1 }
        choices: ['spdy3', 'spdy2', 'http1.1']
    receive_window:
        description:
            - Specifies the receive window, in KB.
        default: 32
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    write_size:
        description:
            - Specifies the total size of combined data frames, in bytes, SPDY will send in a single write.
        default: 16384
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
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

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_LTM_PROFILE_SPDY_ARGS = dict(
    activation_mode=dict(type='str', choices=['npn', 'always']),
    compression_level=dict(type='int'),
    compression_window_size=dict(type='int'),
    concurrent_streams_per_connection=dict(type='int'),
    connection_idle_timeout=dict(type='int'),
    defaults_from=dict(type='str'),
    description=dict(type='str'),
    frame_size=dict(type='int'),
    insert_header=dict(type='str', choices=F5_ACTIVATION_CHOICES),
    insert_header_name=dict(type='str'),
    priority_handling=dict(type='str', choices=['strict', 'fair']),
    protocol_versions=dict(type='dict'),
    receive_window=dict(type='int'),
    write_size=dict(type='int')
)


class F5BigIpLtmProfileSpdy(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create': self.mgmt_root.tm.ltm.profile.spdys.spdy.create,
            'read': self.mgmt_root.tm.ltm.profile.spdys.spdy.load,
            'update': self.mgmt_root.tm.ltm.profile.spdys.spdy.update,
            'delete': self.mgmt_root.tm.ltm.profile.spdys.spdy.delete,
            'exists': self.mgmt_root.tm.ltm.profile.spdys.spdy.exists
        }


def main():
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_PROFILE_SPDY_ARGS, supports_check_mode=True)

    try:
        obj = F5BigIpLtmProfileSpdy(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
