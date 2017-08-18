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
module: f5bigip_ltm_profile_fasthttp
short_description: BIG-IP ltm profile fasthttp module
description:
    - Configures a Fast HTTP profile.
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
    client_close_timeout:
        description:
            - Specifies the number of seconds after which the system closes a client connection, when the system either receives a client FIN packet or sends a FIN packet.
        required: false
        default: 5
        choices: []
        aliases: []
    connpool_idle_timeout_override:
        description:
            - Specifies the number of seconds after which a server-side connection in a OneConnect pool is eligible for deletion, when the connection has no traffic.
        required: false
        default: 0
        choices: []
        aliases: []
    connpool_max_reuse:
        description:
            - Specifies the maximum number of times that the system can re-use a current connection.
        required: false
        default: 0
        choices: []
        aliases: []
    connpool_max_size:
        description:
            - Specifies the maximum number of connections to a load balancing pool.
        required: false
        default: 2048
        choices: []
        aliases: []
    connpool_min_size:
        description:
            - Specifies the minimum number of connections to a load balancing pool.
        required: false
        default: 0
        choices: []
        aliases: []
    connpool_replenish:
        description:
            - When enabled, the system replenishes the number of connections to a load balancing pool to the number of connections that existed when the server closed the connection to the pool.
        required: false
        default: enabled
        choices: ['disabled', 'enabled']
        aliases: []
    connpool_step:
        description:
            - Specifies the increment at which the system makes additional connections available, when all available connections are in use.
        required: false
        default: 4
        choices: []
        aliases: []
    defaults_from:
        description:
            - Specifies the profile that you want to use as the parent profile.
        required: false
        default: fasthttp
        choices: []
        aliases: []
    description:
        description:
            - User defined description.
        required: false
        default: null
        choices: []
        aliases: []
    hardware_syn_cookie:
        description:
            - Specifies whether or not to use hardware SYN Cookie when cross system limit.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
        aliases: []
    header_insert:
        description:
            - Specifies a string that the system inserts as a header in an HTTP request.
        required: false
        default: none
        choices: []
        aliases: []
    idle_timeout:
        description:
            - Specifies the number of seconds after which a connection is eligible for deletion, when the connection has no traffic.
        required: false
        default: 300
        choices: []
        aliases: []
    insert_xforwarded_for:
        description:
            - Specifies whether the system inserts the XForwarded For header in an HTTP request with the client IP address, to use with connection pooling.
        required: false
        default: null
        choices: ['disabled', 'enabled']
        aliases: []
    max_header_size:
        description:
            - Specifies the maximum amount of HTTP header data that the system buffers before making a load balancing decision.
        required: false
        default: 32768
        choices: []
        aliases: []
    max_requests:
        description:
            - Specifies the maximum number of requests that the system can receive on a client connection, before the system closes the connection.
        required: false
        default: 0
        choices: []
        aliases: []
    mss_override:
        description:
            - Specifies a maximum segment size (MSS) override for server connections.
        required: false
        default: 0
        choices: range(536,1461)
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
    receive_window_size:
        description:
            - Specifies the window size to use, minimum and default to 65535 bytes, the maximum is 2^31 for window scale enabling.
        required: false
        default: null
        choices: []
        aliases: []
    reset_on_timeout:
        description:
            - When enabled, the system sends a TCP RESET packet when a connection times out, and deletes the connection.
        required: false
        default: enabled
        choices: ['disabled', 'enabled']
        aliases: []
    server_close_timeout:
        description:
            - Specifies the number of seconds after which the system closes a client connection, when the system either receives a client FIN packet or sends a FIN packet.
        required: false
        default: 5
        choices: []
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
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        required: false
        default: present
        choices: ['absent', 'present']
        aliases: []
    unclean_shutdown:
        description:
            - Specifies how the system handles closing a connection.
        required: false
        default: disabled
        choices: ['disabled', 'enabled', 'fast']
        aliases: []
'''

EXAMPLES = '''
- name: Create LTM Profile Fast HTTP
  f5bigip_ltm_profile_fasthttp:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_fasthttp_profile
    partition: Common
    description: My fasthttp profile
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_LTM_PROFILE_FASTHTTP_ARGS = dict(
    app_service                       =    dict(type='str'),
    client_close_timeout              =    dict(type='int'),
    connpool_idle_timeout_override    =    dict(type='int'),
    connpool_max_reuse                =    dict(type='int'),
    connpool_max_size                 =    dict(type='int'),
    connpool_min_size                 =    dict(type='int'),
    connpool_replenish                =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    connpool_step                     =    dict(type='int'),
    defaults_from                     =    dict(type='str'),
    description                       =    dict(type='str'),
    force_http_10_response            =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    hardware_syn_cookie               =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    header_insert                     =    dict(type='str'),
    http_11_close_workarounds         =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    idle_timeout                      =    dict(type='int'),
    insert_xforwarded_for             =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    layer_7                           =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    max_header_size                   =    dict(type='int'),
    max_requests                      =    dict(type='int'),
    mss_override                      =    dict(type='int', choices=range(536,1461)),
    receive_window_size               =    dict(type='str'),
    reset_on_timeout                  =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    server_close_timeout              =    dict(type='int'),
    server_sack                       =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    server_timestamp                  =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    unclean_shutdown                  =    dict(type='str', choices=['disabled', 'enabled', 'fast'])
)

class F5BigIpLtmProfileFasthttp(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.profile.fasthttps.fasthttp.create,
            'read':     self.mgmt_root.tm.ltm.profile.fasthttps.fasthttp.load,
            'update':   self.mgmt_root.tm.ltm.profile.fasthttps.fasthttp.update,
            'delete':   self.mgmt_root.tm.ltm.profile.fasthttps.fasthttp.delete,
            'exists':   self.mgmt_root.tm.ltm.profile.fasthttps.fasthttp.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}

    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_PROFILE_FASTHTTP_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpLtmProfileFasthttp(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()