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
module: f5bigip_ltm_profile_sctp
short_description: BIG-IP ltm profile sctp module
description:
    - Configures a Stream Control Transmission Protocol (SCTP) profile.
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
    cookie_expiration:
        description:
            - Specifies how many seconds the cookie is valid.
        required: false
        default: 60
        choices: []
        aliases: []
    defaults_from:
        description:
            - Specifies the profile that you want to use as the parent profile.
        required: false
        default: sctp
        choices: []
        aliases: []
    description:
        description:
            - User defined description.
        required: false
        default: null
        choices: []
        aliases: []
    heartbeat_interval:
        description:
            - Specifies the number of seconds to wait before sending a heartbeat chunk.
        required: false
        default: 30
        choices: []
        aliases: []
    heartbeat_max_burst:
        description:
            - Specifies the number of heartbeat packets to be sent in a single burst.
        required: false
        default: 1
        choices: []
        aliases: []
    idle_timeout:
        description:
            - Specifies the number of seconds without traffic before a connection is eligible for deletion.
        required: false
        default: 300
        choices: []
        aliases: []
    in_streams:
        description:
            - Specifies the number of inbound streams.
        required: false
        default: 2
        choices: []
        aliases: []
    init_max_retries:
        description:
            - Specifies the maximum number of retries to establish a connection.
        required: false
        default: 4
        choices: []
        aliases: []
    ip_tos:
        description:
            - Specifies the Type of Service (ToS) that is set in packets sent to the peer.
        required: false
        default: 0
        choices: []
        aliases: []
    link_qos:
        description:
            - Specifies the Link Quality of Service (QoS) that is set in sent packets.
        required: false
        default: 0
        choices: []
        aliases: []
    max_burst:
        description:
            - Specifies the maximum number of data packets to send in a single burst.
        required: false
        default: 4
        choices: []
        aliases: []
    name:
        description:
            - Specifies a unique name for the component.
        required: true
        default: none
        choices: []
        aliases: []
    out_streams:
        description:
            - Specifies the number of outbound streams.
        required: false
        default: 2
        choices: []
        aliases: []
    partition:
        description:
            - Displays the administrative partition within which the component resides.
        required: false
        default: null
        choices: []
        aliases: []
    proxy_buffer_high:
        description:
            - Specifies the proxy buffer level after which the system closes the receive window.
        required: false
        default: 16384
        choices: []
        aliases: []
    proxy_buffer_low:
        description:
            - Specifies the proxy buffer level after which the system opens the receive window.
        required: false
        default: 4096
        choices: []
        aliases: []
    receive_chunks:
        description:
            - Specifies the size (in chunks) of the rx_chunk buffer.
        required: false
        default: 65535
        choices: []
        aliases: []
    receive_ordered:
        description:
            - When enabled, the default, the system delivers messages to the application layer in order.
        required: false
        default: enabled
        choices: ['disabled', 'enabled']
        aliases: []
    receive_window_size:
        description:
            - Specifies the size (in bytes) of the receive window.
        required: false
        default: 65535
        choices: []
        aliases: []
    reset_on_timeout:
        description:
            - When enabled, the default, the system resets the connection when the connection times out.
        required: false
        default: enabled
        choices: ['disabled', 'enabled']
        aliases: []
    secret:
        description:
            - Specifies the internal secret string used for HTTP Message Authenticated Code (HMAC) cookies.
        required: false
        default: null
        choices: []
        aliases: []
    send_buffer_size:
        description:
            - Specifies the size in bytes of the buffer.
        required: false
        default: 65536
        choices: []
        aliases: []
    send_max_retries:
        description:
            - Specifies the maximum number of time the system tries again to send the data.
        required: false
        default: 8
        choices: []
        aliases: []
    send_partial:
        description:
            - When enabled, the default, the system accepts partial application data.
        required: false
        default: enabled
        choices: ['disabled', 'enabled']
        aliases: []
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        required: false
        default: present
        choices: ['absent', 'present']
        aliases: []
    tcp_shutdown:
        description:
            - When enabled, the system emulates the closing of a TCP connection.
        required: false
        default: enabled
        choices: ['disabled', 'enabled']
        aliases: []
    transmit_chunks:
        description:
            - Specifies the size of the tx_chunk buffer.
        required: false
        default: 256
        choices: []
        aliases: []
'''

EXAMPLES = '''
- name: Create LTM Profile SCTP
  f5bigip_ltm_profile_sctp:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_sctp_profile
    partition: Common
    description: My sctp profile
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_LTM_PROFILE_SCTP_ARGS = dict(
    app_service            =    dict(type='str'),
    cookie_expiration      =    dict(type='int'),
    defaults_from          =    dict(type='str'),
    description            =    dict(type='str'),
    heartbeat_interval     =    dict(type='int'),
    heartbeat_max_burst    =    dict(type='int'),
    idle_timeout           =    dict(type='int'),
    in_streams             =    dict(type='int'),
    init_max_retries       =    dict(type='int'),
    ip_tos                 =    dict(type='int'),
    link_qos               =    dict(type='int'),
    max_burst              =    dict(type='int'),
    out_streams            =    dict(type='int'),
    proxy_buffer_high      =    dict(type='int'),
    proxy_buffer_low       =    dict(type='int'),
    receive_chunks         =    dict(type='int'),
    receive_ordered        =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    receive_window_size    =    dict(type='int'),
    reset_on_timeout       =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    secret                 =    dict(type='str'),
    send_buffer_size       =    dict(type='int'),
    send_max_retries       =    dict(type='int'),
    send_partial           =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    tcp_shutdown           =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    transmit_chunks        =    dict(type='int')
)

class F5BigIpLtmProfileSctp(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.profile.sctps.sctp.create,
            'read':     self.mgmt_root.tm.ltm.profile.sctps.sctp.load,
            'update':   self.mgmt_root.tm.ltm.profile.sctps.sctp.update,
            'delete':   self.mgmt_root.tm.ltm.profile.sctps.sctp.delete,
            'exists':   self.mgmt_root.tm.ltm.profile.sctps.sctp.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}

    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_PROFILE_SCTP_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpLtmProfileSctp(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()