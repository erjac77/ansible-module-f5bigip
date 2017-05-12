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
module: f5bigip_ltm_profile_tcp
short_description: BIG-IP ltm tcp profile module
description:
    - Configures a Transmission Control Protocol (TCP) profile.
version_added: 2.3
author:
    - "Gabriel Fortin"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    abc:
        description:
            - When enabled, increases the congestion window by basing the increase amount on the number of previously unacknowledged bytes that each acknowledgement code (ACK) includes.
        required: false
        default: enabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    ack_on_push:
        description:
            - When enabled, significantly improves performance to Microsoft Windows and MacOS peers, who are writing out on a very small send buffer.
        required: false
        default: enabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    app_service:
        description:
            - Specifies the name of the application service to which the profile belongs.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    close_wait_timeout:
        description:
            - Specifies the number of seconds that a connection remains in a LAST-ACK (last acknowledgement code) state before quitting.
        required: false
        default: 5
        choices: []
        aliases: []
        version_added: 2.3
    cmetrics_cache:
        description:
            - Specifies, when enabled, the default value, that the system uses a cache for storing congestion metrics.
        required: false
        default: null
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    congestion_control:
        description:
            - Specifies the algorithm to use to share network resources among competing users to reduce congestion.
        required: false
        default: high-speed
        choices: ['cdg', 'chd', 'cubic', 'high-speed', 'illinois', 'new-reno', 'none', 'reno', 'scalable', 'vegas', 'westwood', 'woodside']
        aliases: []
        version_added: 2.3
    defaults_from:
        description:
            - Specifies the profile that you want to use as the parent profile.
        required: false
        default: tcp
        choices: []
        aliases: []
        version_added: 2.3
    deferred_accept:
        description:
            - Specifies, when enabled, that the system defers allocation of the connection chain context until the system has received the payload from the client.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    delay_window_control:
        description:
            - When enabled, the system uses an estimate of queueing delay as a measure of congestion, in addition to the normal loss-based control, to control the amount of data sent.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    delayed_acks:
        description:
            - Specifies, when enabled, the default value, that the traffic management system allows coalescing of multiple acknowledgement (ACK) responses.
        required: false
        default: enabled
        choices: ['enabled', 'disabled']
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
    dsack:
        description:
            - When enabled, specifies the use of the SACK option to acknowledge duplicate segments.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    early_retransmit:
        description:
            - Specifies, when enabled, that the system uses early retransmit recovery (as specified in RFC 5827) to reduce the recovery time for connections that are receive-buffer or user-data limited.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    ecn:
        description:
            - Specifies, when enabled, that the system uses the TCP flags CWR and ECE to notify its peer of congestion and congestion counter-measures.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    fin_wait_timeout:
        description:
            - Specifies the number of seconds that a connection is in the FIN-WAIT or closing state before quitting.
        required: false
        default: 5
        choices: []
        aliases: []
        version_added: 2.3
    hardware_syn_cookie:
        description:
            - Specifies whether or not to use hardware SYN Cookie when cross system limit.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    idle_timeout:
        description:
            - Specifies the number of seconds that a connection is idle before the connection is eligible for deletion.
        required: false
        default: 300
        choices: []
        aliases: []
        version_added: 2.3
    init_cwnd:
        description:
            - Specifies the initial congestion window size for connections to this destination.
        required: false
        default: 0
        choices: range(0, 17)
        aliases: []
        version_added: 2.3
    init_rwnd:
        description:
            - Specifies the initial receive window size for connections to this destination.
        required: false
        default: 0
        choices: range(0, 17)
        aliases: []
        version_added: 2.3
    ip_tos_to_client:
        description:
            - Specifies the Type of Service (ToS) level that the traffic management system assigns to TCP packets when sending them to clients.
        required: false
        default: 0
        choices: []
        aliases: []
        version_added: 2.3
    keep_alive_interval:
        description:
            - Specifies the keep-alive probe interval, in seconds.
        required: false
        default: 1800
        choices: []
        aliases: []
        version_added: 2.3
   limited_transmit:
        description:
            - Specifies, when enabled, that the system uses limited transmit recovery revisions for fast retransmits to reduce the recovery time for connections on a lossy network.
        default: enabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    link_qos_to_client:
        description:
            - Specifies the Link Quality of Service (QoS) level that the system assigns to TCP packets when sending them to clients.
        required: false
        default: 0
        choices: []
        aliases: []
        version_added: 2.3
    max_retrans:
        description:
            - Specifies the maximum number of retransmissions of data segments that the system allows.
        required: false
        default: 8
        choices: []
        aliases: []
        version_added: 2.3
    md5_signature:
        description:
            - Specifies, when enabled, that the system uses RFC2385 TCP-MD5 signatures to protect TCP traffic against intermediate tampering.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    md5_signature_passphrase:
        description:
            - Specifies a plain text passphrase tnat is used in a shared-secret scheme to implement the spoof-prevention parts of RFC2385.
        required: false
        default: none
        choices: Plain text passphrase between 1 and 80 characters in length
        aliases: []
        version_added: 2.3
    minimum_rto:
        description:
            - Specifies the minimum TCP retransmission timeout in milliseconds.
        required: false
        default: 0
        choices: []
        aliases: []
        version_added: 2.3
    mptcp:
        description:
            - Specifies, when enabled, that the system will accept MPTCP connections.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    mptcp_csum:
        description:
            - Specifies, when enabled, that the system will calculate the checksum for MPTCP connections.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    mptcp_csum_verify:
        description:
            - Specifies, when enabled, that the system verifys checksum for MPTCP connections.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    mptcp_debug:
        description:
            - Specifies, when enabled, that the system provides debug logs and statistics for MPTCP connections.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    mptcp_fallback:
        description:
            - Specifies, MPTCP fallback mode. 
        required: false
        default: reset
        choices: ['accept', 'active-accept', 'reset', 'retransmit']
        aliases: []
        version_added: 2.3
    mptcp_joinmax:
        description:
            - Specifies the max number of MPTCP connections that can join to given one.
        required: false
        default: 5
        choices: []
        aliases: []
        version_added: 2.3
    mptcp_nojoindssack:
        description:
            - Specifies, when enabled, no DSS option is sent on the JOIN ACK.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    mptcp_rtomax:
        description:
            - Specifies, the number of RTOs before declaring subflow dead.
        required: false
        default: 5
        choices: []
        aliases: []
        version_added: 2.3
    mptcp_rxmitmin:
        description:
            - Specifies the minimum value (in msec) of the retransmission timer for these MPTCP flows.
        required: false
        default: 1000
        choices: []
        aliases: []
        version_added: 2.3
    mptcp_subflowmax:
        description:
            - Specifies the maximum number of MPTCP subflows for a single flow.
        required: false
        default: 6
        choices: []
        aliases: []
        version_added: 2.3
    mptcp_makeafterbreak:
        description:
            - Specifies, when enabled, that make-after-break functionality is supported, allowing for long-lived MPTCP sessions.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    mptcp_timeout:
        description:
            - Specifies, the timeout value to discard long-lived sessions that do not have an active flow, in seconds.
        required: false
        default: 3600
        choices: []
        aliases: []
        version_added: 2.3
   mptcp_fastjoin:
        description:
            - Specifies, when enabled, FAST join, allowing data to be sent on the MP_JOIN SYN, which can allow a server response to occur in parallel with the JOIN.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    nagle:
        description:
            - Specifies, when enabled, that the system applies Nagle's algorithm to reduce the number of short segments on the network.
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
            - Specifies the administrative partition in which the component object resides.
        required: false
        default: Common
        choices: []
        aliases: []
        version_added: 2.3
    pkt_loss_ignore_burst:
        description:
            - Specifies the probability of performing congestion control when multiple packets in a row are lost, even if the pkt-loss-ignore-rate was not exceeded.
        required: false
        default: 0
        choices: range(0, 33)
        aliases: []
        version_added: 2.3
    pkt_loss_ignore_rate:
        description:
            - Specifies the threshold of packets lost per million at which the system should perform congestion control.
        required: false
        default: 0
        choices: range(0, 1000001)
        aliases: []
        version_added: 2.3
    proxy_buffer_high:
        description:
            - Specifies the highest level at which the receive window is closed.
        required: false
        default: 49152
        choices: []
        aliases: []
        version_added: 2.3
    proxy_buffer_low:
        description:
            - Specifies the lowest level at which the receive window is closed.
        required: false
        default: 32768
        choices: []
        aliases: []
        version_added: 2.3
    proxy_mss:
        description:
            - Specifies, when enabled, that the system advertises the same mss to the server as was negotiated with the client.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    proxy_options:
        description:
            - Specifies, when enabled, that the system advertises an option, such as a time-stamp to the server only if it was negotiated with the client.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    rate_pace:
        description:
            - Specifies, when enabled, that the system will rate pace TCP data transmissions.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    receive_window_size:
        description:
            - Specifies the size of the receive window, in bytes.
        required: false
        default: 65535
        choices: []
        aliases: []
        version_added: 2.3
    reset_on_timeout:
        description:
            - Specifies whether to reset connections on timeout.
        required: false
        default: enabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    selective_acks:
        description:
            - Specifies, when enabled, that the system negotiates RFC2018-compliant Selective Acknowledgements with peers.
        required: false
        default: enabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    selective_nack:
        description:
            - Specifies whether Selective Negative Acknowledgment is enabled or disabled.
        required: false
        default: enabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    send_buffer_size:
        description:
            - Specifies the size of the buffer, in bytes.
        required: false
        default: 65535
        choices: []
        aliases: []
        version_added: 2.3
    slow_start:
        description:
            - Specifies, when enabled, that the system uses larger initial window sizes (as specified in RFC 3390) to help reduce round trip times.
        required: false
        default: enabled
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
    syn_cookie_whitelist:
        description:
            - Specifies whether or not to use a SYN Cookie WhiteList when doing software SYN Cookies.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    syn_max_retrans:
        description:
            - Specifies the maximum number of retransmissions of SYN segments that the system allows.
        required: false
        default: 3
        choices: []
        aliases: []
        version_added: 2.3
    syn_rto_base:
        description:
            - Specifies the initial RTO (Retransmission TimeOut) base multiplier for SYN retransmission, in milliseconds.
        required: false
        default: 0
        choices: []
        aliases: []
        version_added: 2.3
     tail_loss_probe:
        description:
            - Specifies whether the system uses tail loss probe to reduce the number of retransmission timeouts.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    time_wait_recycle:
        description:
            - Specifies whether the system recycles the connection when a SYN packet is received in a TIME-WAIT state.
        required: false
        default: enabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
     time_wait_timeout:
        description:
            - Specifies the number of milliseconds that a connection is in the TIME-WAIT state before closing.
        required: false
        default: 2000
        choices: range(0, 600001)
        aliases: []
        version_added: 2.3
     timestamps:
        description:
            - Specifies, when enabled, that the system uses the timestamps extension for TCP (as specified in RFC 1323) to enhance high-speed network performance.
        required: false
        default: enabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
     verified_accept:
        description:
            - Specifies, when enabled, that the system can actually communicate with the server before establishing a client connection.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
     zero_window_timeout:
        description:
            - Specifies the timeout in milliseconds for terminating a connection with an effective zero length TCP transmit window.
        required: false
        default: 2000
        choices: []
        aliases: []
        version_added: 2.3
    

'''
EXAMPLES = '''
- name: Create LTM TCP Profile
  f5bigip_ltm_profile_tcp:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_tcp_profile
    partition: Common
    init_cwnd: 10
    pkt_loss_ignore_burst: 15
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_LTM_PROFILE_TCP_ARGS = dict(
    abc                         =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    ack_on_push                 =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    app_service                 =   dict(type='str'),
    close_wait_timeout          =   dict(type='int'),
    cmetrics_cache              =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    congestion_control          =   dict(type='str', choices=['cdg', 'chd', 'cubic', 'high-speed', 'illinois', 'new-reno', 'none', 'reno', 'scalable', 'vegas', 'westwood', 'woodside']),
    defaults_from               =   dict(type='str'),
    deferred_accept             =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    delay_window_control        =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    delayed_acks                =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    description                 =   dict(type='str'),
    dsack                       =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    early_retransmit            =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    ecn                         =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    fin_wait_timeout            =   dict(type='int'),
    hardware_syn_cookie         =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    idle_timeout                =   dict(type='int'),
    init_cwnd                   =   dict(type='int', choices=range(0, 17)),
    init_rwnd                   =   dict(type='int', choices=range(0, 17)),
    ip_tos_to_client            =   dict(type='int'),
    keep_alive_interval         =   dict(type='int'),
    limited_transmit            =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    link_qos_to_client          =   dict(type='int'),
    max_retrans                 =   dict(type='int'),
    md5_signature               =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    md5_signature_passphrase    =   dict(type='str'),
    minimum_rto                 =   dict(type='int'),
    mptcp                       =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    mptcp_csum                  =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    mptcp_csum_verify           =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    mptcp_debug                 =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    mptcp_fallback              =   dict(type='str', choices=['accept', 'active-accept', 'reset', 'retransmit']),
    mptcp_joinmax               =   dict(type='int'),
    mptcp_nojoindssack          =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    mptcp_rtomax                =   dict(type='int'),
    mptcp_rxmitmin              =   dict(type='int'),
    mptcp_subflowmax            =   dict(type='int'),
    mptcp_makeafterbreak        =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    mptcp_timeout               =   dict(type='int'),
    mptcp_fastjoin              =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    nagle                       =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    pkt_loss_ignore_burst       =   dict(type='int', choices=range(0, 33)),
    pkt_loss_ignore_rate        =   dict(type='int', choices=range(0, 1000001)),
    proxy_buffer_high           =   dict(type='int'),
    proxy_buffer_low            =   dict(type='int'),
    proxy_mss                   =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    proxy_options               =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    rate_pace                   =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    receive_window_size         =   dict(type='int'),
    reset_on_timeout            =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    selective_acks              =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    selective_nack              =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    send_buffer_size            =   dict(type='int'),
    slow_start                  =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    syn_cookie_whitelist        =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    syn_max_retrans             =   dict(type='int'),
    syn_rto_base                =   dict(type='int'),
    tail_loss_probe             =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    time_wait_recycle           =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    time_wait_timeout           =   dict(type='int', choices=range(0, 600001)),
    timestamps                  =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    verified_accept             =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    zero_window_timeout         =   dict(type='int')
)

class F5BigIpLtmProfileTcp(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.profile.tcps.tcp.create,
            'read':     self.mgmt_root.tm.ltm.profile.tcps.tcp.load,
            'update':   self.mgmt_root.tm.ltm.profile.tcps.tcp.update,
            'delete':   self.mgmt_root.tm.ltm.profile.tcps.tcp.delete,
            'exists':   self.mgmt_root.tm.ltm.profile.tcps.tcp.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}
    
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_PROFILE_TCP_ARGS, supports_check_mode=False)
    
    try:
        obj = F5BigIpLtmProfileTcp(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()