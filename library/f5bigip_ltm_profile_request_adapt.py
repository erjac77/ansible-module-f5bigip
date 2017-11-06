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

DOCUMENTATION = '''
---
module: f5bigip_ltm_profile_request_adapt
short_description: BIG-IP ltm profile request adapt module
description:
    - Configures a HTTP request adaptation profile.
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
            - Specifies whether to forward HTTP version 1.0 requests for adaptation.
        required: false
        default: no
        choices: ['no', 'yes']
        aliases: []
    defaults_from:
        description:
            - Specifies the profile that you want to use as the parent profile.
        required: false
        default: requestadapt
        choices: []
        aliases: []
    enabled:
        description:
            - Enables adaptation of HTTP requests.
        required: false
        default: yes
        choices: ['no', 'yes']
        aliases: []
    internal_virtual:
        description:
            - Specifies the name of the internal virtual server to use for adapting the HTTP request.
        required: false
        default: null
        choices: []
        aliases: []
    name:
        description:
            - Specifies a unique name for the component.
        required: true
        default: null
        choices: []
        aliases: []
    preview_size:
        description:
            - Specifies the maximum size of the preview buffer.
        required: false
        default: 1024
        choices: []
        aliases: []
    service_down_action:
        description:
            - Specifies the action to take if the internal virtual server does not exist or returns an error.
        required: false
        default: ignore
        choices: ['ignore', 'reset', 'drop']
        aliases: []
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        required: false
        default: present
        choices: ['absent', 'present']
        aliases: []
    timeout:
        description:
            - Specifies a timeout in milliseconds.
        required: false
        default: 0
        choices: []
        aliases: []
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

from ansible_common_f5.f5_bigip import *

BIGIP_LTM_PROFILE_REQUEST_ADAPT_ARGS = dict(
    allow_http_10          =    dict(type='str', choices=F5_POLAR_CHOICES),
    defaults_from          =    dict(type='str'),
    enabled                =    dict(type='str', choices=F5_POLAR_CHOICES),
    internal_virtual       =    dict(type='str'),
    preview_size           =    dict(type='int'),
    service_down_action    =    dict(type='str', choices=['ignore', 'reset', 'drop']),
    timeout                =    dict(type='int')
)

class F5BigIpLtmProfileRequestAdapt(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.profile.request_adapts.request_adapt.create,
            'read':     self.mgmt_root.tm.ltm.profile.request_adapts.request_adapt.load,
            'update':   self.mgmt_root.tm.ltm.profile.request_adapts.request_adapt.update,
            'delete':   self.mgmt_root.tm.ltm.profile.request_adapts.request_adapt.delete,
            'exists':   self.mgmt_root.tm.ltm.profile.request_adapts.request_adapt.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}

    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_PROFILE_REQUEST_ADAPT_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpLtmProfileRequestAdapt(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()