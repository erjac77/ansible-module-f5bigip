#!/usr/bin/python
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
module: f5bigip_ltm_policy_rule
short_description: BIG-IP ltm policy rule module
description:
    - Configures a set of rules.
version_added: "2.4"
author:
    - "Eric Jacob (@erjac77)"
options:
    app_service:
        description:
            - Specifies the application service to which the object belongs.
    description:
        description:
            - Specifies descriptive text that identifies the component.
    name:
        description:
            - Specifies unique name for the component.
        required: true
    ordinal:
        description:
            - Specifies the number used to rank the rules according to precedence.
    policy:
        description:
            - Specifies the policy in which the rule belongs.
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Create LTM Policy Rule
  f5bigip_ltm_policy_rule:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_rule
    description: My policy rule
    policy: /Common/my_policy
    state: present
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_LTM_POLICY_RULE_ARGS = dict(
    app_service=dict(type='str'),
    description=dict(type='str'),
    ordinal=dict(type='int'),
    policy=dict(type='str')
)


class F5BigIpLtmPolicyRule(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.policy = self.mgmt_root.tm.ltm.policys.policy.load(
            **self._get_resource_id_from_path(self.params['policy']))
        self.methods = {
            'create': self.policy.rules_s.rules.create,
            'read': self.policy.rules_s.rules.load,
            'update': self.policy.rules_s.rules.update,
            'delete': self.policy.rules_s.rules.delete,
            'exists': self.policy.rules_s.rules.exists
        }
        del self.params['partition']
        del self.params['policy']


def main():
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_POLICY_RULE_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpLtmPolicyRule(check_mode=module.supports_check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
