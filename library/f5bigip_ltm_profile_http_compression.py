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
module: f5bigip_ltm_profile_http_compression
short_description: BIG-IP ltm profile http compression module
description:
    - Configures an HTTP Compression profile.
version_added: 2.3
author:
    - "Gabriel Fortin"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    allow_http_10:
        description:
            - Enables or disables compression of HTTP/1.0 server responses.
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
    browser_workarounds:
        description:
            - Enables or disables compression of browser workarounds.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
        aliases: []
    buffer_size:
        description:
            - Specifies the maximum number of uncompressed bytes that the system buffers before determining whether to compress the response.
        required: false
        default: 4096
        choices: []
        aliases: []
    content_type_exclude:
        description:
            - Specifies a string list of HTTP Content-Type responses that you do not want the system to compress.
        required: false
        default: none
        choices: []
        aliases: []
    content_type_include:
        description:
            - Specifies a string list of HTTP Content-Type responses that you want the system to compress.
        required: false
        default: null
        choices: []
        aliases: []
    cpu_saver:
        description:
            - Specifies the percent of CPU usage at which the system resumes content compression at the user-defined rates.
        required: false
        default: enabled
        choices: ['disabled', 'enabled']
        aliases: []
    cpu_saver_high:
        description:
            - Specifies the percent of CPU usage at which the system starts automatically decreasing the amount of content being compressed, as well as the amount of compression that the system is applying.
        required: false
        default: 90
        choices: []
        aliases: []
    cpu_saver_low:
        description:
            - Specifies the percent of CPU usage at which the system resumes content compression at the user-defined rates.
        required: false
        default: 75
        choices: []
        aliases: []
    defaults_from:
        description:
            - Specifies the profile that you want to use as the parent profile.
        required: false
        default: httpcompression
        choices: []
        aliases: []
    description:
        description:
            - User defined description.
        required: false
        default: null
        choices: []
        aliases: []
    gzip_level:
        description:
            - Specifies a value that determines the amount of memory that the system uses when compressing a server response.
        required: false
        default: 1
        choices: []
        aliases: []
    gzip_memory_level:
        description:
            - Specifies the amount of memory (in kilobytes) that the system uses when compressing a server response.
        required: false
        default: 8
        choices: []
        aliases: []
    gzip_window_size:
        description:
            - Specifies the number of kilobytes in the window size that the system uses when compressing a server response.
        required: false
        default: 16k
        choices: []
        aliases: []
    keep_accept_encoding:
        description:
            - Specifies where data compression is performed.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
        aliases: []
    method_prefer:
        description:
            - Specifies the type of compression that the system prefers.
        required: false
        default: gzip
        choices: []
        aliases: []
    min_size:
        description:
            - Specifies the minimum length in bytes of a server response that is acceptable for compression.
        required: false
        default: 1024
        choices: []
        aliases: []
    partition:
        description:
            - Displays the administrative partition within which the profile resides.
        required: false
        default: null
        choices: []
        aliases: []
    selective:
        description:
            - Enables or disables selective compression mode.
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
    uri_exclude:
        description:
            - Disables compression on a specified list of HTTP Request-URI responses.
        required: false
        default: none
        choices: []
        aliases: []
    uri_include:
        description:
            - Enables compression on a specified list of HTTP Request-URI responses.
        required: false
        default: none
        choices: []
        aliases: []
    vary_header:
        description:
            - Enables or disables the insertion of a Vary header into cacheable server responses.
        required: false
        default: enabled
        choices: ['disabled', 'enabled']
        aliases: []
'''

EXAMPLES = '''
- name: Create LTM Profile HTTP Compression
  f5bigip_ltm_profile_http_compression:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_http_compression_profile
    partition: Common
    description: My http compression profile
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_LTM_PROFILE_HTTP_COMPRESSION_ARGS = dict(
    allow_http_10           =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    app_service             =    dict(type='str'),
    browser_workarounds     =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    buffer_size             =    dict(type='int'),
    content_type_exclude    =    dict(type='list'),
    content_type_include    =    dict(type='list'),
    cpu_saver               =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    cpu_saver_high          =    dict(type='int'),
    cpu_saver_low           =    dict(type='int'),
    defaults_from           =    dict(type='str'),
    description             =    dict(type='str'),
    gzip_level              =    dict(type='int'),
    gzip_memory_level       =    dict(type='int'),
    gzip_window_size        =    dict(type='int'),
    keep_accept_encoding    =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    method_prefer           =    dict(type='str', choices=['deflate', 'gzip']),
    min_size                =    dict(type='int'),
    selective               =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    uri_exclude             =    dict(type='list'),
    uri_include             =    dict(type='list'),
    vary_header             =    dict(type='str', choices=F5_ACTIVATION_CHOICES)
)

class F5BigIpLtmProfileHttpCompression(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.profile.http_compressions.http_compression.create,
            'read':     self.mgmt_root.tm.ltm.profile.http_compressions.http_compression.load,
            'update':   self.mgmt_root.tm.ltm.profile.http_compressions.http_compression.update,
            'delete':   self.mgmt_root.tm.ltm.profile.http_compressions.http_compression.delete,
            'exists':   self.mgmt_root.tm.ltm.profile.http_compressions.http_compression.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}

    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_PROFILE_HTTP_COMPRESSION_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpLtmProfileHttpCompression(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()