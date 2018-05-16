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
module: f5bigip_ltm_profile_fasthttp
short_description: BIG-IP ltm profile fasthttp module
description:
    - Configures a Fast HTTP profile.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    app_service:
        description:
            - Specifies the name of the application service to which the profile belongs.
    client_close_timeout:
        description:
            - Specifies the number of seconds after which the system closes a client connection, when the system either
              receives a client FIN packet or sends a FIN packet.
        default: 5
    connpool_idle_timeout_override:
        description:
            - Specifies the number of seconds after which a server-side connection in a OneConnect pool is eligible for
              deletion, when the connection has no traffic.
        default: 0
    connpool_max_reuse:
        description:
            - Specifies the maximum number of times that the system can re-use a current connection.
        default: 0
    connpool_max_size:
        description:
            - Specifies the maximum number of connections to a load balancing pool.
        default: 2048
    connpool_min_size:
        description:
            - Specifies the minimum number of connections to a load balancing pool.
        default: 0
    connpool_replenish:
        description:
            - When enabled, the system replenishes the number of connections to a load balancing pool to the number of
              connections that existed when the server closed the connection to the pool.
        default: enabled
        choices: ['disabled', 'enabled']
    connpool_step:
        description:
            - Specifies the increment at which the system makes additional connections available, when all available
              connections are in use.
        default: 4
    defaults_from:
        description:
            - Specifies the profile that you want to use as the parent profile.
        default: fasthttp
    description:
        description:
            - User defined description.
    hardware_syn_cookie:
        description:
            - Specifies whether or not to use hardware SYN Cookie when cross system limit.
        default: disabled
        choices: ['disabled', 'enabled']
    header_insert:
        description:
            - Specifies a string that the system inserts as a header in an HTTP request.
    idle_timeout:
        description:
            - Specifies the number of seconds after which a connection is eligible for deletion, when the connection has
              no traffic.
        default: 300
    insert_xforwarded_for:
        description:
            - Specifies whether the system inserts the XForwarded For header in an HTTP request with the client IP
              address, to use with connection pooling.
        choices: ['disabled', 'enabled']
    max_header_size:
        description:
            - Specifies the maximum amount of HTTP header data that the system buffers before making a load balancing
              decision.
        default: 32768
    max_requests:
        description:
            - Specifies the maximum number of requests that the system can receive on a client connection, before the
              system closes the connection.
        default: 0
    mss_override:
        description:
            - Specifies a maximum segment size (MSS) override for server connections.
        default: 0
        choices: range(536,1461)
    name:
        description:
            - Specifies a unique name for the component.
        required: true
    partition:
        description:
            - Displays the administrative partition within which the component resides.
    receive_window_size:
        description:
            - Specifies the window size to use, minimum and default to 65535 bytes, the maximum is 2^31 for window scale
              enabling.
    reset_on_timeout:
        description:
            - When enabled, the system sends a TCP RESET packet when a connection times out, and deletes the connection.
        default: enabled
        choices: ['disabled', 'enabled']
    server_close_timeout:
        description:
            - Specifies the number of seconds after which the system closes a client connection, when the system either
              receives a client FIN packet or sends a FIN packet.
        default: 5
    server_sack:
        description:
            - Specifies whether to support server sack option in cookie response by default.
        default: disabled
        choices: ['disabled', 'enabled']
    server_timestamp:
        description:
            - Specifies whether to support server timestamp option in cookie response by default.
        default: disabled
        choices: ['disabled', 'enabled']
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    unclean_shutdown:
        description:
            - Specifies how the system handles closing a connection.
        default: disabled
        choices: ['disabled', 'enabled', 'fast']
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
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

RETURN = ''' # '''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.six.moves import range
from ansible_common_f5.base import F5_ACTIVATION_CHOICES
from ansible_common_f5.base import F5_NAMED_OBJ_ARGS
from ansible_common_f5.base import F5_PROVIDER_ARGS
from ansible_common_f5.bigip import F5BigIpNamedObject


class ModuleParams(object):
    @property
    def argument_spec(self):
        argument_spec = dict(
            app_service=dict(type='str'),
            client_close_timeout=dict(type='int'),
            connpool_idle_timeout_override=dict(type='int'),
            connpool_max_reuse=dict(type='int'),
            connpool_max_size=dict(type='int'),
            connpool_min_size=dict(type='int'),
            connpool_replenish=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            connpool_step=dict(type='int'),
            defaults_from=dict(type='str'),
            description=dict(type='str'),
            force_http_10_response=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            hardware_syn_cookie=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            header_insert=dict(type='str'),
            http_11_close_workarounds=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            idle_timeout=dict(type='int'),
            insert_xforwarded_for=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            layer_7=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            max_header_size=dict(type='int'),
            max_requests=dict(type='int'),
            mss_override=dict(type='int', choices=range(536, 1461)),
            receive_window_size=dict(type='str'),
            reset_on_timeout=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            server_close_timeout=dict(type='int'),
            server_sack=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            server_timestamp=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            unclean_shutdown=dict(type='str', choices=['disabled', 'enabled', 'fast'])
        )
        argument_spec.update(F5_PROVIDER_ARGS)
        argument_spec.update(F5_NAMED_OBJ_ARGS)
        return argument_spec

    @property
    def supports_check_mode(self):
        return True


class F5BigIpLtmProfileFasthttp(F5BigIpNamedObject):
    def _set_crud_methods(self):
        self._methods = {
            'create': self._api.tm.ltm.profile.fasthttps.fasthttp.create,
            'read': self._api.tm.ltm.profile.fasthttps.fasthttp.load,
            'update': self._api.tm.ltm.profile.fasthttps.fasthttp.update,
            'delete': self._api.tm.ltm.profile.fasthttps.fasthttp.delete,
            'exists': self._api.tm.ltm.profile.fasthttps.fasthttp.exists
        }


def main():
    params = ModuleParams()
    module = AnsibleModule(argument_spec=params.argument_spec, supports_check_mode=params.supports_check_mode)

    try:
        obj = F5BigIpLtmProfileFasthttp(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
