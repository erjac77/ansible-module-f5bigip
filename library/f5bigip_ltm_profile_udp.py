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
module: f5bigip_ltm_profile_udp
short_description: BIG-IP ltm profile udp module
description:
    - Configures a User Datagram Protocol (UDP) profile.
version_added: 2.3
author:
    - "Gabriel Fortin"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    allow_no_payload:
        description:
            - Provides the ability to allow the passage of datagrams that contain header information, but no essential data.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
        aliases: []
    app_service:
        description:
            - Specifies the name of the application service to which the profile belongs.
        required: false
        default: none
        choices: []
        aliases: []
    datagram_load_balancing:
        description:
            - Provides the ability to load balance UDP datagram by datagram.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
        aliases: []
    defaults_from:
        description:
            - Specifies the profile that you want to use as the parent profile.
        required: false
        default: udp
        choices: []
        aliases: []
    description:
        description:
            - User defined description.
        required: false
        default: null
        choices: []
        aliases: []
    idle_timeout:
        description:
            - Specifies the number of seconds that a connection is idle before the connection is eligible for deletion.
        required: false
        default: 60
        choices: []
        aliases: []
    ip_tos_to_client:
        description:
            - Specifies the Type of Service level that the traffic management system assigns to UDP packets when sending them to clients.
        required: false
        default: null
        choices: []
        aliases: []
    link_qos_to_client:
        description:
            - Specifies the Quality of Service level that the system assigns to UDP packets when sending them to clients.
        required: false
        default: 0
        choices: []
        aliases: []
    name:
        description:
            - Specifies a unique name for the component.
        required: true
        default: none
        choices: []
        aliases: []
    no_checksum:
        description:
            - Enables or disables checksum processing.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
        aliases: []
    partition:
        description:
            - Displays the administrative partition within which the profile resides.
        required: false
        default: null
        choices: []
        aliases: []
    proxy_mss:
        description:
            - Specifies, when enabled, that the system advertises the same mss to the server as was negotiated with the client.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
        aliases: []
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        required: false
        default: present
        choices: ['absent', 'present']
        aliases: []
'''

EXAMPLES = '''
- name: Create LTM Profile UDP
  f5bigip_ltm_profile_udp:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_udp_profile
    partition: Common
    description: My udp profile
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_LTM_PROFILE_UDP_ARGS = dict(
    allow_no_payload           =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    app_service                =    dict(type='str'),
    datagram_load_balancing    =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    defaults_from              =    dict(type='str'),
    description                =    dict(type='str'),
    idle_timeout               =    dict(type='int'),
    ip_tos_to_client           =    dict(type='int'),
    link_qos_to_client         =    dict(type='int'),
    no_checksum                =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    proxy_mss                  =    dict(type='str', choices=F5_ACTIVATION_CHOICES)
)

class F5BigIpLtmProfileUdp(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.profile.udps.udp.create,
            'read':     self.mgmt_root.tm.ltm.profile.udps.udp.load,
            'update':   self.mgmt_root.tm.ltm.profile.udps.udp.update,
            'delete':   self.mgmt_root.tm.ltm.profile.udps.udp.delete,
            'exists':   self.mgmt_root.tm.ltm.profile.udps.udp.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}

    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_PROFILE_UDP_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpLtmProfileUdp(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()