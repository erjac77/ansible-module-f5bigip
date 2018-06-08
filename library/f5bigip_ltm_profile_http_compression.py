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
module: f5bigip_ltm_profile_http_compression
short_description: BIG-IP ltm profile http compression module
description:
    - Configures an HTTP Compression profile.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    allow_http_10:
        description:
            - Enables or disables compression of HTTP/1.0 server responses.
        default: disabled
        choices: ['disabled', 'enabled']
    app_service:
        description:
            - Specifies the name of the application service to which the profile belongs.
    browser_workarounds:
        description:
            - Enables or disables compression of browser workarounds.
        default: disabled
        choices: ['disabled', 'enabled']
    buffer_size:
        description:
            - Specifies the maximum number of uncompressed bytes that the system buffers before determining whether to
              compress the response.
        default: 4096
    content_type_exclude:
        description:
            - Specifies a string list of HTTP Content-Type responses that you do not want the system to compress.
    content_type_include:
        description:
            - Specifies a string list of HTTP Content-Type responses that you want the system to compress.
    cpu_saver:
        description:
            - Specifies the percent of CPU usage at which the system resumes content compression at the user-defined
              rates.
        default: enabled
        choices: ['disabled', 'enabled']
    cpu_saver_high:
        description:
            - Specifies the percent of CPU usage at which the system starts automatically decreasing the amount of
              content being compressed, as well as the amount of compression that the system is applying.
        default: 90
    cpu_saver_low:
        description:
            - Specifies the percent of CPU usage at which the system resumes content compression at the user-defined
              rates.
        default: 75
    defaults_from:
        description:
            - Specifies the profile that you want to use as the parent profile.
        default: httpcompression
    description:
        description:
            - User defined description.
    gzip_level:
        description:
            - Specifies a value that determines the amount of memory that the system uses when compressing a server
              response.
        default: 1
    gzip_memory_level:
        description:
            - Specifies the amount of memory (in kilobytes) that the system uses when compressing a server response.
        default: 8
    gzip_window_size:
        description:
            - Specifies the number of kilobytes in the window size that the system uses when compressing a server
              response.
        default: 16k
    keep_accept_encoding:
        description:
            - Specifies where data compression is performed.
        default: disabled
        choices: ['disabled', 'enabled']
    method_prefer:
        description:
            - Specifies the type of compression that the system prefers.
        default: gzip
    min_size:
        description:
            - Specifies the minimum length in bytes of a server response that is acceptable for compression.
        default: 1024
    partition:
        description:
            - Displays the administrative partition within which the profile resides.
    selective:
        description:
            - Enables or disables selective compression mode.
        default: disabled
        choices: ['disabled', 'enabled']
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    uri_exclude:
        description:
            - Disables compression on a specified list of HTTP Request-URI responses.
    uri_include:
        description:
            - Enables compression on a specified list of HTTP Request-URI responses.
    vary_header:
        description:
            - Enables or disables the insertion of a Vary header into cacheable server responses.
        default: enabled
        choices: ['disabled', 'enabled']
requirements:
    - BIG-IP >= 12.0
    - ansible-common-f5
    - f5-sdk
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
            allow_http_10=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            app_service=dict(type='str'),
            browser_workarounds=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            buffer_size=dict(type='int'),
            content_type_exclude=dict(type='list'),
            content_type_include=dict(type='list'),
            cpu_saver=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            cpu_saver_high=dict(type='int'),
            cpu_saver_low=dict(type='int'),
            defaults_from=dict(type='str'),
            description=dict(type='str'),
            gzip_level=dict(type='int'),
            gzip_memory_level=dict(type='int'),
            gzip_window_size=dict(type='int'),
            keep_accept_encoding=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            method_prefer=dict(type='str', choices=['deflate', 'gzip']),
            min_size=dict(type='int'),
            selective=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            uri_exclude=dict(type='list'),
            uri_include=dict(type='list'),
            vary_header=dict(type='str', choices=F5_ACTIVATION_CHOICES)
        )
        argument_spec.update(F5_PROVIDER_ARGS)
        argument_spec.update(F5_NAMED_OBJ_ARGS)
        return argument_spec

    @property
    def supports_check_mode(self):
        return True


class F5BigIpLtmProfileHttpCompression(F5BigIpNamedObject):
    def _set_crud_methods(self):
        self._methods = {
            'create': self._api.tm.ltm.profile.http_compressions.http_compression.create,
            'read': self._api.tm.ltm.profile.http_compressions.http_compression.load,
            'update': self._api.tm.ltm.profile.http_compressions.http_compression.update,
            'delete': self._api.tm.ltm.profile.http_compressions.http_compression.delete,
            'exists': self._api.tm.ltm.profile.http_compressions.http_compression.exists
        }


def main():
    params = ModuleParams()
    module = AnsibleModule(argument_spec=params.argument_spec, supports_check_mode=params.supports_check_mode)

    try:
        obj = F5BigIpLtmProfileHttpCompression(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
