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
module: f5bigip_ltm_profile_request_adapt
short_description: BIG-IP ltm profile request adapt module
description:
    - Configures a HTTP request adaptation profile.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    allow_http_10:
        description:
            - Specifies whether to forward HTTP version 1.0 requests for adaptation.
        default: no
        choices: ['no', 'yes']
    defaults_from:
        description:
            - Specifies the profile that you want to use as the parent profile.
        default: requestadapt
    enabled:
        description:
            - Enables adaptation of HTTP requests.
        default: yes
        choices: ['no', 'yes']
    internal_virtual:
        description:
            - Specifies the name of the internal virtual server to use for adapting the HTTP request.
    name:
        description:
            - Specifies a unique name for the component.
        required: true
    preview_size:
        description:
            - Specifies the maximum size of the preview buffer.
        default: 1024
    service_down_action:
        description:
            - Specifies the action to take if the internal virtual server does not exist or returns an error.
        default: ignore
        choices: ['ignore', 'reset', 'drop']
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    timeout:
        description:
            - Specifies a timeout in milliseconds.
        default: 0
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Create LTM Profile Request Adapt
  f5bigip_ltm_profile_request_adapt:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_request_adapt_profile
    partition: Common
    state: present
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_LTM_PROFILE_REQUEST_ADAPT_ARGS = dict(
    allow_http_10=dict(type='str', choices=F5_POLAR_CHOICES),
    defaults_from=dict(type='str'),
    enabled=dict(type='str', choices=F5_POLAR_CHOICES),
    internal_virtual=dict(type='str'),
    preview_size=dict(type='int'),
    service_down_action=dict(type='str', choices=['ignore', 'reset', 'drop']),
    timeout=dict(type='int')
)


class F5BigIpLtmProfileRequestAdapt(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create': self.mgmt_root.tm.ltm.profile.request_adapts.request_adapt.create,
            'read': self.mgmt_root.tm.ltm.profile.request_adapts.request_adapt.load,
            'update': self.mgmt_root.tm.ltm.profile.request_adapts.request_adapt.update,
            'delete': self.mgmt_root.tm.ltm.profile.request_adapts.request_adapt.delete,
            'exists': self.mgmt_root.tm.ltm.profile.request_adapts.request_adapt.exists
        }


def main():
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_PROFILE_REQUEST_ADAPT_ARGS,
                                             supports_check_mode=True)

    try:
        obj = F5BigIpLtmProfileRequestAdapt(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
