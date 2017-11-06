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
module: f5bigip_ltm_profile_html
short_description: BIG-IP ltm profile html module
description:
    - Configures an HTML profile.
version_added: 2.3
author:
    - "Gabriel Fortin"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    content_detection:
        description:
            - Scans initial HTTP payload to look for HTML signatures and enables HTML profile if HTML-like patterns are detected.
        required: false
        default: null
        choices: ['disabled', 'enabled']
        aliases: []
    content_selection:
        description:
            - Matches content-type from response header against a list of content-types and enables HTML profile if a match is found.
        required: false
        default: null
        choices: []
        aliases: []
    defaults_from:
        description:
            - Specifies the profile that you want to use as the parent profile.
        required: false
        default: html
        choices: []
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
    rules:
        description:
            - Specifies a list of HTML (content rewrite) rules, separated by spaces, that are used for parsing and patching HTML.
        required: false
        default: null
        choices: []
        aliases: []
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        required: false
        default: present
        choices: ['absent', 'present']
        aliases: []
'''

EXAMPLES = '''
- name: Create LTM Profile HTML
  f5bigip_ltm_profile_html:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_html_profile
    partition: Common
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_LTM_PROFILE_HTML_ARGS = dict(
    content_detection    =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    content_selection    =    dict(type='list'),
    defaults_from        =    dict(type='str'),
    rules                =    dict(type='list')
)

class F5BigIpLtmProfileHtml(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.profile.htmls.html.create,
            'read':     self.mgmt_root.tm.ltm.profile.htmls.html.load,
            'update':   self.mgmt_root.tm.ltm.profile.htmls.html.update,
            'delete':   self.mgmt_root.tm.ltm.profile.htmls.html.delete,
            'exists':   self.mgmt_root.tm.ltm.profile.htmls.html.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}

    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_PROFILE_HTML_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpLtmProfileHtml(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()