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
module: f5bigip_gtm_rule
short_description: BIG-IP gtm rule module
description:
    - Configures iRules for traffic management system configuration.
version_added: 2.3
author:
    - "Gabriel Fortin"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    api_anonymous:
        description:
            - Specifies the definition of the rule.
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
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        required: false
        default: Common
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
- name: Create GTM Rule
  f5bigip_gtm_rule:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_rule
    partition: Common
    api_anonymous: when DNS_REQUEST { if {[IP::addr [IP::remote_addr]/24 equals 10.10.1.0/24] } {cname cname.siterequest.com } else { host 10.20.20.20}}
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_GTM_RULE_ARGS = dict(
    api_anonymous   =    dict(type='str')
)

class F5BigIpGtmRule(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.gtm.rules.rule.create,
            'read':     self.mgmt_root.tm.gtm.rules.rule.load,
            'update':   self.mgmt_root.tm.gtm.rules.rule.update,
            'delete':   self.mgmt_root.tm.gtm.rules.rule.delete,
            'exists':   self.mgmt_root.tm.gtm.rules.rule.exists
        }

def main():
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_GTM_RULE_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpGtmRule(check_mode=module.supports_check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()