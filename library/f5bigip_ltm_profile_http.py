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
module: f5bigip_ltm_profile_http
short_description: BIG-IP ltm http profie module
description:
    - You can use the http component to create, modify, display, or delete an HTTP profile.
version_added: 2.3
author:
    - "Gabriel Fortin"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    accept_xff:
        description:
            - Enables or disables trusting the client IP address, and statistics from the client IP address, based on the request's XFF (X-forwarded-for) headers, if they exist.
        required: false
        default: null
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
    basic_auth_realm:
        description:
            - Specifies a quoted string for the basic authentication realm.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    defaults_from:
        description:
            - Specifies the profile that you want to use as the parent profile.
        required: false
        default: http
        choices: []
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
    encrypt_cookie_secret:
        description:
            - Specifies a passphrase for the cookie encryption.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    encrypt_cookies:
        description:
            - Specifies to encrypt specific cookies that the BIG-IP system sends to a client system.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    enforcement:
        description:
            - Specifies protocol enforcement options for the HTTP profile.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    fallback_host:
        description:
            - Specifies an HTTP fallback host.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    fallback_status_codes
        description:
            - Specifies one or more three-digit status codes that can be returned by an HTTP server.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    header_erase:
        description:
            - Specifies the header string that you want to erase from an HTTP request.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
        version_added: 2.3
    header_insert:
        description:
            - Specifies a quoted header string that you want to insert into an HTTP request.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    insert_xforwarded_for:
        description:
            - Enables or disables insertion of an X-Forwarded-For header.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    lws_separator:
        description:
            - Specifies the linear white space separator that the system uses between HTTP headers when a header exceeds the maximum width specified in the lws-width option.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    lws_width:
        description:
            - Specifies the maximum number of columns that a header that is inserted into an HTTP request can have.
        required: false
        default: 80
        choices: []
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
    oneconnect_transformations:
        description:
            - Specifies whether the system performs HTTP header transformations for the purpose of keeping server-side connections open.
        required: false
        default: enabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    partition:
        description:
            - Displays the partition within which the component resides.
        required: false
        default: Common
        choices: []
        aliases: []
        version_added: 2.3
    redirect_rewrite:
        description:
            - Specifies which of the application HTTP redirects the system rewrites to HTTPS.
        required: false
        default: null
        choices: ['all', 'matching', 'nodes', 'none']
        aliases: []
        version_added: 2.3
    request_chunking:
        description:
            - Specifies how to handle chunked and unchunked requests.
        required: false
        default: selective
        choices: ['unchunk', 'rechunk', 'preserve', 'selective']
        aliases: []
        version_added: 2.3
    response_chunking:
        description:
            - Specifies how to handle chunked and unchunked responses.
        required: false
        default: selective
        choices: ['unchunk', 'rechunk', 'preserve', 'selective']
        aliases: []
        version_added: 2.3
    response_headers_permitted:
        description:
            - Specifies headers that the BIG-IP system allows in an HTTP response.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    server_agent_name:
        description:
            - Specifies the string used as the server name in traffic generated by LTM.
        required: false
        default: BigIP
        choices: []
        aliases: []
        version_added: 2.3
    explicit_proxy:
        description:
            - Specifies explicit settings for the HTTP profile.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    sflow:
        description:
            - Specifies sFlow settings for the HTTP profile:
        required: false
        default: null
        choices: []
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
    via_host_name:
        description:
            - Specifies the hostname that will be used in the Via: HTTP header.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    via_request:
        description:
            - Specifies how you want to process Via: HTTP header in requests sent to OWS.
        required: false
        default: remove
        choices: ['append', 'preserve', 'remove']
        aliases: []
        version_added: 2.3
    via_response:
        description:
            - Specifies how you want to process Via: HTTP header in responses sent to clients.
        required: false
        default: remove
        choices: ['append', 'preserve', 'remove']
        aliases: []
        version_added: 2.3
    xff_alternative_names:
        description:
            - Specifies alternative XFF headers instead of the default X-forwarded-for header.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3

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

from ansible_common_f5.f5_bigip import *

BIGIP_LTM_PROFILE_HTTP_ARGS = dict(
    accept_xff                  =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    app_service                 =   dict(type='str'),
    basic_auth_realm            =   dict(type='str'),
    defaults_from               =   dict(type='str'),
    description                 =   dict(type='str'),
    encrypt_cookie_secret       =   dict(type='str'),
    encrypt_cookies             =   dict(type='str'),
    #enforcement                =   dict(type='list'),
    fallback_host               =   dict(type='str'),
    fallback_status_codes       =   dict(type='int'),
    header_erase                =   dict(type='str'),
    header_insert               =   dict(type='str'),
    insert_xforwarded_for       =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    lws_separator               =   dict(type='str'),
    lws_width                   =   dict(type='int'),
    oneconnect_transformations  =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    redirect_rewrite            =   dict(type='str', choices=['all', 'matching', 'nodes', 'none']),
    request_chunking            =   dict(type='str', choices=['unchunk', 'rechunk', 'preserve', 'selective']),
    response_chunking           =   dict(type='str', choices=['unchunk', 'rechunk', 'preserve', 'selective']),
    response_headers_permitted  =   dict(type='str'),
    server_agent_name           =   dict(type='str'),
    #explicit_proxy             =   dict(type='list'),
    #sflow                      =   dict(type='list'),
    via_host_name               =   dict(type='str'),
    via_request                 =   dict(type='str', choices=['append', 'preserve', 'remove']),
    via_response                =   dict(type='str', choices=['append', 'preserve', 'remove']),
    xff_alternative_names       =   dict(type='str')
)

class F5BigIpLtmProfileHttp(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.profile.https.http.create,
            'read':     self.mgmt_root.tm.ltm.profile.https.http.load,
            'update':   self.mgmt_root.tm.ltm.profile.https.http.update,
            'delete':   self.mgmt_root.tm.ltm.profile.https.http.delete,
            'exists':   self.mgmt_root.tm.ltm.profile.https.http.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}
    
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_PROFILE_HTTP_ARGS, supports_check_mode=False)
    
    try:
        obj = F5BigIpLtmProfileHttp(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()