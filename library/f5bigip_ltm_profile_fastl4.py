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
module: f5bigip_ltm_profile_fastl4
short_description: BIG-IP ltm profile fastl4 module
description:
    - Configures a Fast Layer 4 profile.
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
    client_timeout:
        description:
            - Specifies late binding client timeout in seconds.
        required: false
        default: 30
        choices: []
        aliases: []
    defaults_from:
        description:
            - Specifies the profile that you want to use as the parent profile.
        required: false
        default: fastl4
        choices: []
        aliases: []
    description:
        description:
            - User defined description.
        required: false
        default: null
        choices: []
        aliases: []
    explicit_flow_migration:
        description:
            - Specifies whether to have the iRule code determine exactly when the FIX stream drops down to the ePVA hardware.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
        aliases: []
    hardware_syn_cookie:
        description:
            - Enables or disables hardware SYN cookie support when PVA10 is present on the system.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
        aliases: []
    idle_timeout:
        description:
            - Specifies the number of seconds that a connection is idle before the connection is eligible for deletion.
        required: false
        default: 300
        choices: []
        aliases: []
    ip_tos_to_client:
        description:
            - Specifies an IP Type of Service (ToS) number for the client-side.
        required: false
        default: 65535
        choices: []
        aliases: []
    ip_tos_to_server:
        description:
            - Specifies an IP ToS number for the server side.
        required: false
        default: 65535
        choices: []
        aliases: []
    keep_alive_interval:
        description:
            - Specifies the keep-alive probe interval, in seconds.
        required: false
        default: 0
        choices: []
        aliases: []
    late_binding:
        description:
            - Specifies whether to enable or disable intelligent selection of a back-end server pool.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
        aliases: []
    link_qos_to_client:
        description:
            - Specifies a Link Quality of Service (QoS) (VLAN priority) number for the client side.
        required: false
        default: 65535
        choices: []
        aliases: []
    link_qos_to_server:
        description:
            - Specifies internal packet priority for the server side.
        required: false
        default: 65535
        choices: []
        aliases: []
    loose_close:
        description:
            - Specifies that the system closes a loosely-initiated connection when the system receives the first FIN packet from either the client or the server.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
        aliases: []
    loose_initialization:
        description:
            - Specifies that the system initializes a connection when it receives any Transmission Control Protocol (TCP) packet, rather than requiring a SYN packet for connection initiation.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
        aliases: []
    mss_override:
        description:
            - Specifies a maximum segment size (MSS) override for server connections.
        required: false
        default: 0
        choices: range(256,9163)
        aliases: []
    name:
        description:
            - Specifies a unique name for the component.
        required: true
        default: null
        choices: []
        aliases: []
    partition:
        description:
            - Displays the administrative partition within which the component resides.
        required: false
        default: null
        choices: []
        aliases: []
    priority_to_client:
        description:
            - Specifies internal packet priority for the client side.
        required: false
        default: 65535
        choices: []
        aliases: []
    priority_to_server:
        description:
            - Specifies internal packet priority for the server side.
        required: false
        default: 65535
        choices: []
        aliases: []
    pva_acceleration:
        description:
            - Specifies the Packet Velocity ASIC acceleration policy.
        required: false
        default: full
        choices: ['full', 'none', 'partial', 'guaranteed']
        aliases: []
    pva_dynamic_client_packets:
        description:
            - Specifies the number of client packets before dynamic ePVA hardware re-offloading occurs.
        required: false
        default: 2
        choices: []
        aliases: []
    pva_dynamic_server_packets:
        description:
            - Specifies the number of server packets before dynamic ePVA hardware re-offloading occurs.
        required: false
        default: 2
        choices: []
        aliases: []
    pva_flow_aging:
        description:
            - Specifies if automatic aging from ePVA flow cache upon inactive and idle for a period, default to enabled.
        required: false
        default: enabled
        choices: ['disabled', 'enabled']
        aliases: []
    pva_flow_evict:
        description:
            - Specifies if this flow can be evicted upon hash collision with a new flow learn snoop request, defaults to enabled.
        required: false
        default: enabled
        choices: ['disabled', 'enabled']
        aliases: []
    pva_offload_dynamic:
        description:
            - Specifies whether PVA flow dynamic offloading is enabled or not.
        required: false
        default: enabled
        choices: ['disabled', 'enabled']
        aliases: []
    pva_offload_state:
        description:
            - Specifies at what stage the ePVA performs hardware offload.
        required: false
        default: embryonic
        choices: ['embryonic', 'establish']
        aliases: []
    reassemble_fragments:
        description:
            - Specifies whether to reassemble fragments.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
        aliases: []
    receive_window_size:
        description:
            - Specifies the window size to use, minimum and default to 65535 bytes, the maximum is 2^31 for window scale enabling.
        required: false
        default: null
        choices: []
        aliases: []
    reset_on_timeout:
        description:
            - Specifies whether you want to reset connections on timeout.
        required: false
        default: null
        choices: ['disabled', 'enabled']
        aliases: []
    rtt_from_client:
        description:
            - Enables or disables the TCP timestamp options to measure the round trip time to the client.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
        aliases: []
    rtt_from_server:
        description:
            - Enables or disables the TCP timestamp options to measure the round trip time to the server.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
        aliases: []
    server_sack:
        description:
            - Specifies whether to support server sack option in cookie response by default.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
        aliases: []
    server_timestamp:
        description:
            - Specifies whether to support server timestamp option in cookie response by default.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
        aliases: []
    software_syn_cookie:
        description:
            - Enables or disables software SYN cookie support when PVA10 is not present on the system.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
        aliases: []
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        required: false
        default: disabled
        choices: ['absent', 'present']
        aliases: []
    syn_cookie_whitelist:
        description:
            - Specifies whether or not to use a SYN Cookie WhiteList when doing software SYN Cookies.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
        aliases: []
    tcp_close_timeout:
        description:
            - Specifies a TCP close timeout in seconds.
        required: false
        default: 5
        choices: []
        aliases: []
    tcp_generate_is:
        description:
            - Specifies whether you want to generate TCP sequence numbers on all SYNs that conform with RFC1948, and allow timestamp recycling.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
        aliases: []
    tcp_handshake_timeout:
        description:
            - Specifies a TCP handshake timeout in seconds.
        required: false
        default: 5
        choices: []
        aliases: []
    tcp_strip_sack:
        description:
            - Specifies whether you want to block the TCP SackOK option from passing to the server on an initiating SYN.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
        aliases: []
    tcp_timestamp_mode:
        description:
            - Specifies how you want to handle the TCP timestamp.
        required: false
        default: null
        choices: ['preserve', 'rewrite', 'strip']
        aliases: []
    tcp_wscale_mode:
        description:
            - Specifies how you want to handle the TCP window scale.
        required: false
        default: null
        choices: ['preserve', 'rewrite', 'strip']
        aliases: []
    timeout_recovery:
        description:
            - Specifies late binding timeout recovery mode.
        required: false
        default: null
        choices: ['disconnect', 'fallback']
        aliases: []
'''

EXAMPLES = '''
- name: Create LTM Profile FastL4
  f5bigip_ltm_profile_fastl4:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_fastl4_profile
    partition: Common
    description: My fastl4 profile
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_LTM_PROFILE_FASTL4_ARGS = dict(
    app_service                   =    dict(type='str'),
    client_timeout                =    dict(type='int'),
    defaults_from                 =    dict(type='str'),
    description                   =    dict(type='str'),
    explicit_flow_migration       =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    hardware_syn_cookie           =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    idle_timeout                  =    dict(type='int'),
    ip_tos_to_client              =    dict(type='int'),
    ip_tos_to_server              =    dict(type='int'),
    keep_alive_interval           =    dict(type='int'),
    late_binding                  =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    link_qos_to_client            =    dict(type='int'),
    link_qos_to_server            =    dict(type='int'),
    loose_close                   =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    loose_initialization          =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    mss_override                  =    dict(type='int', choices=range(256,9163)),
    priority_to_client            =    dict(type='int'),
    priority_to_server            =    dict(type='int'),
    pva_acceleration              =    dict(type='str', choices=['full', 'none', 'partial', 'guaranteed']),
    pva_dynamic_client_packets    =    dict(type='int'),
    pva_dynamic_server_packets    =    dict(type='int'),
    pva_flow_aging                =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    pva_flow_evict                =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    pva_offload_dynamic           =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    pva_offload_state             =    dict(type='str', choices=['embryonic', 'establish']),
    reassemble_fragments          =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    receive_window_size           =    dict(type='str'),
    reset_on_timeout              =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    rtt_from_client               =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    rtt_from_server               =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    server_sack                   =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    server_timestamp              =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    software_syn_cookie           =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    syn_cookie_whitelist          =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    tcp_close_timeout             =    dict(type='int'),
    tcp_generate_is               =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    tcp_handshake_timeout         =    dict(type='int'),
    tcp_strip_sack                =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    tcp_timestamp_mode            =    dict(type='str', chocies=['preserve', 'rewrite', 'strip']),
    tcp_wscale_mode               =    dict(type='str', chocies=['preserve', 'rewrite', 'strip']),
    timeout_recovery              =    dict(type='str', choices=['disconnect', 'fallback'])
)

class F5BigIpLtmProfileFastl4(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.profile.fastl4s.fastl4.create,
            'read':     self.mgmt_root.tm.ltm.profile.fastl4s.fastl4.load,
            'update':   self.mgmt_root.tm.ltm.profile.fastl4s.fastl4.update,
            'delete':   self.mgmt_root.tm.ltm.profile.fastl4s.fastl4.delete,
            'exists':   self.mgmt_root.tm.ltm.profile.fastl4s.fastl4.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}

    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_PROFILE_FASTL4_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpLtmProfileFastl4(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()