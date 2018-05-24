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
module: f5bigip_ltm_profile_http
short_description: BIG-IP ltm http profile module
description:
    - You can use the http component to create, modify, display, or delete an HTTP profile.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    accept_xff:
        description:
            - Enables or disables trusting the client IP address, and statistics from the client IP address, based on
              the request's XFF (X-forwarded-for) headers, if they exist.
        choices: ['enabled', 'disabled']
    app_service:
        description:
            - Specifies the name of the application service to which the profile belongs.
    basic_auth_realm:
        description:
            - Specifies a quoted string for the basic authentication realm.
    defaults_from:
        description:
            - Specifies the profile that you want to use as the parent profile.
        default: http
    description:
        description:
            - User defined description.
    encrypt_cookie_secret:
        description:
            - Specifies a passphrase for the cookie encryption.
    encrypt_cookies:
        description:
            - Specifies to encrypt specific cookies that the BIG-IP system sends to a client system.
    enforcement:
        description:
            - Specifies protocol enforcement options for the HTTP profile.
        suboptions:
            excess_client_headers:
                description:
                    - Specifies the pass-through behavior when max-header-count is exceeded by the client.
                default: disabled
                choices: ['enabled', 'disabled']
            excess_server_headers:
                description:
                    - Specifies the pass-through behavior when max-header-count is exceeded by the server.
                default: disabled
                choices: ['enabled', 'disabled']
            known_methods:
                description:
                    - Specifies the HTTP methods known by the HTTP filter.
            max_header_size:
                description:
                    - Specifies the maximum header size.
                default: 32768
            max_header_count:
                description:
                    - Specifies the maximum number of headers in HTTP request or response that will be handled.
                default: 64
            max_requests:
                description:
                    - Specifies the number of requests that the system accepts on a per-connection basis.
                default: 0
            oversize_client_headers:
                description:
                    - Specifies the pass-through behavior when max-header-size is exceeded by the client.
                default: disabled
                choices: ['enabled', 'disabled']
            oversize_server_headers:
                description:
                    - Specifies the pass-through behavior when max-header-size is exceeded by the server.
                default: disabled
                choices: ['enabled', 'disabled']
            pipeline:
                description:
                    - Enables or disables HTTP/1.1 pipelining.
                default: allow
                choices: ['allow', 'pass-through', 'reject']
            truncated_redirects:
                description:
                    - Specifies the pass-through behavior when a redirect lacking the trailing carriage-return and line feed
                      pair at the end of the headers is parsed.
                default: disabled
                choices: ['enabled', 'disabled']
            unknown_method:
                description:
                    - Specifies the behavior when an unknown method is seen.
                default: allow
                choices: ['allow', 'pass-through', 'reject']
    explicit_proxy:
        description:
            - Specifies explicit settings for the HTTP profile.
        suboptions:
            enabled:
                description:
                    - Specifies whether the explicit proxy service is enabled or disabled.
                default: no
                choices: ['no', 'yes']
            dns_resolver:
                description:
                    - Specifies the dns-resolver object that will be used to resolve hostnames in proxy requests.
                default: dns-resolver
            tunnel_name:
                description:
                    - Specifies the tunnel that will be used for outbound proxy requests.
                default: http-tunnel
            route_domain:
                description:
                    - Specifies the route-domain that will be used for outbound proxy requests.
                default: 0
            default_connect_handling:
                description:
                    - Specifies the behavior of the proxy service for CONNECT requests.
                default: deny
                choices: ['deny', 'allow']
            connect_error_message:
                description:
                    - Specifies the error message that will be returned to the browser when a proxy request can't be
                      completed because of a failure to establish the outbound connection.
            dns_error_message:
                description:
                    - Specifies the error message that will be returned to the browser when a proxy request can't be
                      completed because of a failure to resolve the hostname in the request.
            bad_request_message:
                description:
                    - Specifies the error message that will be returned to the browser when a proxy request can't be
                      completed because the request was malformed.
            bad_response_message:
                description:
                    - Specifies the error message that will be returned to the browser when a proxy request can't be
                      completed because the response was malformed.
    fallback_host:
        description:
            - Specifies an HTTP fallback host.
    fallback_status_codes:
        description:
            - Specifies one or more three-digit status codes that can be returned by an HTTP server.
    header_erase:
        description:
            - Specifies the header string that you want to erase from an HTTP request.
    header_insert:
        description:
            - Specifies a quoted header string that you want to insert into an HTTP request.
    insert_xforwarded_for:
        description:
            - Enables or disables insertion of an X-Forwarded-For header.
        default: disabled
        choices: ['enabled', 'disabled']
    lws_separator:
        description:
            - Specifies the linear white space separator that the system uses between HTTP headers when a header exceeds
              the maximum width specified in the lws-width option.
    lws_width:
        description:
            - Specifies the maximum number of columns that a header that is inserted into an HTTP request can have.
        default: 80
    name:
        description:
            - Specifies a unique name for the component.
        required: true
    oneconnect_transformations:
        description:
            - Specifies whether the system performs HTTP header transformations for the purpose of keeping server-side
              connections open.
        default: enabled
        choices: ['enabled', 'disabled']
    partition:
        description:
            - Displays the partition within which the component resides.
        default: Common
    redirect_rewrite:
        description:
            - Specifies which of the application HTTP redirects the system rewrites to HTTPS.
        choices: ['all', 'matching', 'nodes', 'none']
    request_chunking:
        description:
            - Specifies how to handle chunked and unchunked requests.
        default: selective
        choices: ['unchunk', 'rechunk', 'preserve', 'selective']
    response_chunking:
        description:
            - Specifies how to handle chunked and unchunked responses.
        default: selective
        choices: ['unchunk', 'rechunk', 'preserve', 'selective']
    response_headers_permitted:
        description:
            - Specifies headers that the BIG-IP system allows in an HTTP response.
    server_agent_name:
        description:
            - Specifies the string used as the server name in traffic generated by LTM.
        default: BigIP
    sflow:
        description:
            - Specifies sFlow settings for the HTTP profile.
        suboptions:
            poll_interval:
                description:
                    - Specifies the maximum interval in seconds between two pollings.
                default: 0
            poll_interval_global:
                description:
                    - Specifies whether the global HTTP poll-interval setting, which is available under sys sflow
                      global-settings module, overrides the object-level poll-interval setting.
                default: yes
                choices: ['no', 'yes']
            sampling_rate:
                description:
                    - Specifies the ratio of packets observed to the samples generated.
                default: 0
            sampling_rate_global:
                description:
                    - Specifies whether the global HTTP sampling-rate setting, which is available under sys sflow
                      global-settings module, overrides the object-level sampling-rate setting.
                default: yes
                choices: ['no', 'yes']
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    via_host_name:
        description:
            - Specifies the hostname that will be used in the Via HTTP header.
    via_request:
        description:
            - Specifies how you want to process Via HTTP header in requests sent to OWS.
        default: remove
        choices: ['append', 'preserve', 'remove']
    via_response:
        description:
            - Specifies how you want to process Via HTTP header in responses sent to clients.
        default: remove
        choices: ['append', 'preserve', 'remove']
    xff_alternative_names:
        description:
            - Specifies alternative XFF headers instead of the default X-forwarded-for header.
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Create LTM HTTP profile
  f5bigip_ltm_profile_http:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_http_profile
    partition: Common
    insert_xforwarded_for: enabled
    lws_width: 82
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
            accept_xff=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            app_service=dict(type='str'),
            basic_auth_realm=dict(type='str'),
            defaults_from=dict(type='str'),
            description=dict(type='str'),
            encrypt_cookie_secret=dict(type='str'),
            encrypt_cookies=dict(type='str'),
            enforcement=dict(type='dict'),
            explicit_proxy=dict(type='dict'),
            fallback_host=dict(type='str'),
            fallback_status_codes=dict(type='int'),
            header_erase=dict(type='str'),
            header_insert=dict(type='str'),
            insert_xforwarded_for=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            lws_separator=dict(type='str'),
            lws_width=dict(type='int'),
            oneconnect_transformations=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            redirect_rewrite=dict(type='str', choices=['all', 'matching', 'nodes', 'none']),
            request_chunking=dict(type='str', choices=['unchunk', 'rechunk', 'preserve', 'selective']),
            response_chunking=dict(type='str', choices=['unchunk', 'rechunk', 'preserve', 'selective']),
            response_headers_permitted=dict(type='str'),
            server_agent_name=dict(type='str'),
            sflow=dict(type='dict'),
            via_host_name=dict(type='str'),
            via_request=dict(type='str', choices=['append', 'preserve', 'remove']),
            via_response=dict(type='str', choices=['append', 'preserve', 'remove']),
            xff_alternative_names=dict(type='str')
        )
        argument_spec.update(F5_PROVIDER_ARGS)
        argument_spec.update(F5_NAMED_OBJ_ARGS)
        return argument_spec

    @property
    def supports_check_mode(self):
        return True


class F5BigIpLtmProfileHttp(F5BigIpNamedObject):
    def _set_crud_methods(self):
        self._methods = {
            'create': self._api.tm.ltm.profile.https.http.create,
            'read': self._api.tm.ltm.profile.https.http.load,
            'update': self._api.tm.ltm.profile.https.http.update,
            'delete': self._api.tm.ltm.profile.https.http.delete,
            'exists': self._api.tm.ltm.profile.https.http.exists
        }


def main():
    params = ModuleParams()
    module = AnsibleModule(argument_spec=params.argument_spec, supports_check_mode=params.supports_check_mode)

    try:
        obj = F5BigIpLtmProfileHttp(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
