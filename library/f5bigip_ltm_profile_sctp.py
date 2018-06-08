#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2016-2018, Eric Jacob <erjac77@gmail.com>
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
module: f5bigip_ltm_profile_sctp
short_description: BIG-IP ltm profile sctp module
description:
    - Configures a Stream Control Transmission Protocol (SCTP) profile.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    app_service:
        description:
            - Specifies the name of the application service to which the profile belongs.
    cookie_expiration:
        description:
            - Specifies how many seconds the cookie is valid.
        default: 60
    defaults_from:
        description:
            - Specifies the profile that you want to use as the parent profile.
        default: sctp
    description:
        description:
            - User defined description.
    heartbeat_interval:
        description:
            - Specifies the number of seconds to wait before sending a heartbeat chunk.
        default: 30
    heartbeat_max_burst:
        description:
            - Specifies the number of heartbeat packets to be sent in a single burst.
        default: 1
    idle_timeout:
        description:
            - Specifies the number of seconds without traffic before a connection is eligible for deletion.
        default: 300
    in_streams:
        description:
            - Specifies the number of inbound streams.
        default: 2
    init_max_retries:
        description:
            - Specifies the maximum number of retries to establish a connection.
        default: 4
    ip_tos:
        description:
            - Specifies the Type of Service (ToS) that is set in packets sent to the peer.
        default: 0
    link_qos:
        description:
            - Specifies the Link Quality of Service (QoS) that is set in sent packets.
        default: 0
    max_burst:
        description:
            - Specifies the maximum number of data packets to send in a single burst.
        default: 4
    name:
        description:
            - Specifies a unique name for the component.
        required: true
    out_streams:
        description:
            - Specifies the number of outbound streams.
        default: 2
    partition:
        description:
            - Displays the administrative partition within which the component resides.
    proxy_buffer_high:
        description:
            - Specifies the proxy buffer level after which the system closes the receive window.
        default: 16384
    proxy_buffer_low:
        description:
            - Specifies the proxy buffer level after which the system opens the receive window.
        default: 4096
    receive_chunks:
        description:
            - Specifies the size (in chunks) of the rx_chunk buffer.
        default: 65535
    receive_ordered:
        description:
            - When enabled, the default, the system delivers messages to the application layer in order.
        default: enabled
        choices: ['disabled', 'enabled']
    receive_window_size:
        description:
            - Specifies the size (in bytes) of the receive window.
        default: 65535
    reset_on_timeout:
        description:
            - When enabled, the default, the system resets the connection when the connection times out.
        default: enabled
        choices: ['disabled', 'enabled']
    secret:
        description:
            - Specifies the internal secret string used for HTTP Message Authenticated Code (HMAC) cookies.
    send_buffer_size:
        description:
            - Specifies the size in bytes of the buffer.
        default: 65536
    send_max_retries:
        description:
            - Specifies the maximum number of time the system tries again to send the data.
        default: 8
    send_partial:
        description:
            - When enabled, the default, the system accepts partial application data.
        default: enabled
        choices: ['disabled', 'enabled']
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    tcp_shutdown:
        description:
            - When enabled, the system emulates the closing of a TCP connection.
        default: enabled
        choices: ['disabled', 'enabled']
    transmit_chunks:
        description:
            - Specifies the size of the tx_chunk buffer.
        default: 256
requirements:
    - BIG-IP >= 12.0
    - ansible-common-f5
    - f5-sdk
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

RETURN = ''' # '''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.base import F5_ACTIVATION_CHOICES
from ansible_common_f5.base import F5_NAMED_OBJ_ARGS
from ansible_common_f5.base import F5_PROVIDER_ARGS
from ansible_common_f5.bigip import F5BigIpNamedObject


class ModuleParams(object):
    @property
    def argument_spec(self):
        argument_spec = dict(
            app_service=dict(type='str'),
            cookie_expiration=dict(type='int'),
            defaults_from=dict(type='str'),
            description=dict(type='str'),
            heartbeat_interval=dict(type='int'),
            heartbeat_max_burst=dict(type='int'),
            idle_timeout=dict(type='int'),
            in_streams=dict(type='int'),
            init_max_retries=dict(type='int'),
            ip_tos=dict(type='int'),
            link_qos=dict(type='int'),
            max_burst=dict(type='int'),
            out_streams=dict(type='int'),
            proxy_buffer_high=dict(type='int'),
            proxy_buffer_low=dict(type='int'),
            receive_chunks=dict(type='int'),
            receive_ordered=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            receive_window_size=dict(type='int'),
            reset_on_timeout=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            secret=dict(type='str'),
            send_buffer_size=dict(type='int'),
            send_max_retries=dict(type='int'),
            send_partial=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            tcp_shutdown=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            transmit_chunks=dict(type='int')
        )
        argument_spec.update(F5_PROVIDER_ARGS)
        argument_spec.update(F5_NAMED_OBJ_ARGS)
        return argument_spec

    @property
    def supports_check_mode(self):
        return True


class F5BigIpLtmProfileSctp(F5BigIpNamedObject):
    def _set_crud_methods(self):
        self._methods = {
            'create': self._api.tm.ltm.profile.sctps.sctp.create,
            'read': self._api.tm.ltm.profile.sctps.sctp.load,
            'update': self._api.tm.ltm.profile.sctps.sctp.update,
            'delete': self._api.tm.ltm.profile.sctps.sctp.delete,
            'exists': self._api.tm.ltm.profile.sctps.sctp.exists
        }


def main():
    params = ModuleParams()
    module = AnsibleModule(argument_spec=params.argument_spec, supports_check_mode=params.supports_check_mode)

    try:
        obj = F5BigIpLtmProfileSctp(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
