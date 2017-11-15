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
module: f5bigip_ltm_profile_tcp
short_description: BIG-IP ltm tcp profile module
description:
    - Configures a Transmission Control Protocol (TCP) profile.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    abc:
        description:
            - When enabled, increases the congestion window by basing the increase amount on the number of previously unacknowledged bytes that each acknowledgement code (ACK) includes.
        default: enabled
        choices: ['enabled', 'disabled']
    ack_on_push:
        description:
            - When enabled, significantly improves performance to Microsoft Windows and MacOS peers, who are writing out on a very small send buffer.
        default: enabled
        choices: ['enabled', 'disabled']
    app_service:
        description:
            - Specifies the name of the application service to which the profile belongs.
    close_wait_timeout:
        description:
            - Specifies the number of seconds that a connection remains in a LAST-ACK (last acknowledgement code) state before quitting.
        default: 5
    cmetrics_cache:
        description:
            - Specifies, when enabled, the default value, that the system uses a cache for storing congestion metrics.
        choices: ['enabled', 'disabled']
    congestion_control:
        description:
            - Specifies the algorithm to use to share network resources among competing users to reduce congestion.
        default: high-speed
        choices: ['cdg', 'chd', 'cubic', 'high-speed', 'illinois', 'new-reno', 'none', 'reno', 'scalable', 'vegas', 'westwood', 'woodside']
    defaults_from:
        description:
            - Specifies the profile that you want to use as the parent profile.
        default: tcp
    deferred_accept:
        description:
            - Specifies, when enabled, that the system defers allocation of the connection chain context until the system has received the payload from the client.
        default: disabled
        choices: ['enabled', 'disabled']
    delay_window_control:
        description:
            - When enabled, the system uses an estimate of queueing delay as a measure of congestion, in addition to the normal loss-based control, to control the amount of data sent.
        default: disabled
        choices: ['enabled', 'disabled']
    delayed_acks:
        description:
            - Specifies, when enabled, the default value, that the traffic management system allows coalescing of multiple acknowledgement (ACK) responses.
        default: enabled
        choices: ['enabled', 'disabled']
    description:
        description:
            - User defined description.
    dsack:
        description:
            - When enabled, specifies the use of the SACK option to acknowledge duplicate segments.
        default: disabled
        choices: ['enabled', 'disabled']
    early_retransmit:
        description:
            - Specifies, when enabled, that the system uses early retransmit recovery (as specified in RFC 5827) to reduce the recovery time for connections that are receive-buffer or user-data limited.
        default: disabled
        choices: ['enabled', 'disabled']
    ecn:
        description:
            - Specifies, when enabled, that the system uses the TCP flags CWR and ECE to notify its peer of congestion and congestion counter-measures.
        default: disabled
        choices: ['enabled', 'disabled']
    fin_wait_timeout:
        description:
            - Specifies the number of seconds that a connection is in the FIN-WAIT or closing state before quitting.
        default: 5
    hardware_syn_cookie:
        description:
            - Specifies whether or not to use hardware SYN Cookie when cross system limit.
        default: disabled
        choices: ['enabled', 'disabled']
    idle_timeout:
        description:
            - Specifies the number of seconds that a connection is idle before the connection is eligible for deletion.
        default: 300
    init_cwnd:
        description:
            - Specifies the initial congestion window size for connections to this destination.
        default: 0
        choices: range(0, 17)
    init_rwnd:
        description:
            - Specifies the initial receive window size for connections to this destination.
        default: 0
        choices: range(0, 17)
    ip_tos_to_client:
        description:
            - Specifies the Type of Service (ToS) level that the traffic management system assigns to TCP packets when sending them to clients.
        default: 0
    keep_alive_interval:
        description:
            - Specifies the keep-alive probe interval, in seconds.
        default: 1800
   limited_transmit:
        description:
            - Specifies, when enabled, that the system uses limited transmit recovery revisions for fast retransmits to reduce the recovery time for connections on a lossy network.
        default: enabled
        choices: ['enabled', 'disabled']
    link_qos_to_client:
        description:
            - Specifies the Link Quality of Service (QoS) level that the system assigns to TCP packets when sending them to clients.
        default: 0
    max_retrans:
        description:
            - Specifies the maximum number of retransmissions of data segments that the system allows.
        default: 8
    md5_signature:
        description:
            - Specifies, when enabled, that the system uses RFC2385 TCP-MD5 signatures to protect TCP traffic against intermediate tampering.
        default: disabled
        choices: ['enabled', 'disabled']
    md5_signature_passphrase:
        description:
            - Specifies a plain text passphrase tnat is used in a shared-secret scheme to implement the spoof-prevention parts of RFC2385.
        choices: Plain text passphrase between 1 and 80 characters in length
    minimum_rto:
        description:
            - Specifies the minimum TCP retransmission timeout in milliseconds.
        default: 0
    mptcp:
        description:
            - Specifies, when enabled, that the system will accept MPTCP connections.
        default: disabled
        choices: ['enabled', 'disabled']
    mptcp_csum:
        description:
            - Specifies, when enabled, that the system will calculate the checksum for MPTCP connections.
        default: disabled
        choices: ['enabled', 'disabled']
    mptcp_csum_verify:
        description:
            - Specifies, when enabled, that the system verifys checksum for MPTCP connections.
        default: disabled
        choices: ['enabled', 'disabled']
    mptcp_debug:
        description:
            - Specifies, when enabled, that the system provides debug logs and statistics for MPTCP connections.
        default: disabled
        choices: ['enabled', 'disabled']
    mptcp_fallback:
        description:
            - Specifies, MPTCP fallback mode. 
        default: reset
        choices: ['accept', 'active-accept', 'reset', 'retransmit']
    mptcp_joinmax:
        description:
            - Specifies the max number of MPTCP connections that can join to given one.
        default: 5
    mptcp_nojoindssack:
        description:
            - Specifies, when enabled, no DSS option is sent on the JOIN ACK.
        default: disabled
        choices: ['enabled', 'disabled']
    mptcp_rtomax:
        description:
            - Specifies, the number of RTOs before declaring subflow dead.
        default: 5
    mptcp_rxmitmin:
        description:
            - Specifies the minimum value (in msec) of the retransmission timer for these MPTCP flows.
        default: 1000
    mptcp_subflowmax:
        description:
            - Specifies the maximum number of MPTCP subflows for a single flow.
        default: 6
    mptcp_makeafterbreak:
        description:
            - Specifies, when enabled, that make-after-break functionality is supported, allowing for long-lived MPTCP sessions.
        default: disabled
        choices: ['enabled', 'disabled']
    mptcp_timeout:
        description:
            - Specifies, the timeout value to discard long-lived sessions that do not have an active flow, in seconds.
        default: 3600
   mptcp_fastjoin:
        description:
            - Specifies, when enabled, FAST join, allowing data to be sent on the MP_JOIN SYN, which can allow a server response to occur in parallel with the JOIN.
        default: disabled
        choices: ['enabled', 'disabled']
    nagle:
        description:
            - Specifies, when enabled, that the system applies Nagle's algorithm to reduce the number of short segments on the network.
        default: disabled
        choices: ['enabled', 'disabled']
    name:
        description:
            - Specifies a unique name for the component.
        required: true
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        default: Common
    pkt_loss_ignore_burst:
        description:
            - Specifies the probability of performing congestion control when multiple packets in a row are lost, even if the pkt-loss-ignore-rate was not exceeded.
        default: 0
        choices: range(0, 33)
    pkt_loss_ignore_rate:
        description:
            - Specifies the threshold of packets lost per million at which the system should perform congestion control.
        default: 0
        choices: range(0, 1000001)
    proxy_buffer_high:
        description:
            - Specifies the highest level at which the receive window is closed.
        default: 49152
    proxy_buffer_low:
        description:
            - Specifies the lowest level at which the receive window is closed.
        default: 32768
    proxy_mss:
        description:
            - Specifies, when enabled, that the system advertises the same mss to the server as was negotiated with the client.
        default: disabled
        choices: ['enabled', 'disabled']
    proxy_options:
        description:
            - Specifies, when enabled, that the system advertises an option, such as a time-stamp to the server only if it was negotiated with the client.
        default: disabled
        choices: ['enabled', 'disabled']
    rate_pace:
        description:
            - Specifies, when enabled, that the system will rate pace TCP data transmissions.
        default: disabled
        choices: ['enabled', 'disabled']
    receive_window_size:
        description:
            - Specifies the size of the receive window, in bytes.
        default: 65535
    reset_on_timeout:
        description:
            - Specifies whether to reset connections on timeout.
        default: enabled
        choices: ['enabled', 'disabled']
    selective_acks:
        description:
            - Specifies, when enabled, that the system negotiates RFC2018-compliant Selective Acknowledgements with peers.
        default: enabled
        choices: ['enabled', 'disabled']
    selective_nack:
        description:
            - Specifies whether Selective Negative Acknowledgment is enabled or disabled.
        default: enabled
        choices: ['enabled', 'disabled']
    send_buffer_size:
        description:
            - Specifies the size of the buffer, in bytes.
        default: 65535
    slow_start:
        description:
            - Specifies, when enabled, that the system uses larger initial window sizes (as specified in RFC 3390) to help reduce round trip times.
        default: enabled
        choices: ['enabled', 'disabled']
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    syn_cookie_whitelist:
        description:
            - Specifies whether or not to use a SYN Cookie WhiteList when doing software SYN Cookies.
        default: disabled
        choices: ['enabled', 'disabled']
    syn_max_retrans:
        description:
            - Specifies the maximum number of retransmissions of SYN segments that the system allows.
        default: 3
    syn_rto_base:
        description:
            - Specifies the initial RTO (Retransmission TimeOut) base multiplier for SYN retransmission, in milliseconds.
        default: 0
     tail_loss_probe:
        description:
            - Specifies whether the system uses tail loss probe to reduce the number of retransmission timeouts.
        default: disabled
        choices: ['enabled', 'disabled']
    time_wait_recycle:
        description:
            - Specifies whether the system recycles the connection when a SYN packet is received in a TIME-WAIT state.
        default: enabled
        choices: ['enabled', 'disabled']
     time_wait_timeout:
        description:
            - Specifies the number of milliseconds that a connection is in the TIME-WAIT state before closing.
        default: 2000
        choices: range(0, 600001)
     timestamps:
        description:
            - Specifies, when enabled, that the system uses the timestamps extension for TCP (as specified in RFC 1323) to enhance high-speed network performance.
        default: enabled
        choices: ['enabled', 'disabled']
     verified_accept:
        description:
            - Specifies, when enabled, that the system can actually communicate with the server before establishing a client connection.
        default: disabled
        choices: ['enabled', 'disabled']
     zero_window_timeout:
        description:
            - Specifies the timeout in milliseconds for terminating a connection with an effective zero length TCP transmit window.
        default: 2000
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

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
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
    md5_signature_passphrase    =   dict(type='str', no_log=True),
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
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_PROFILE_TCP_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpLtmProfileTcp(check_mode=module.supports_check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

if __name__ == '__main__':
    main()