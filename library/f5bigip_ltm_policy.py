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
module: f5bigip_ltm_policy
short_description: BIG-IP ltm policy module
description:
    - Configures a policy for Centralized Policy Manager.
version_added: "2.4"
author:
    - "Eric Jacob (@erjac77)"
options:
    app_service:
        description:
            - Specifies the application service to which the object belongs.
    controls:
        description:
            - Specifies the set of features the policy controls. Not normally set by end user.
    description:
        description:
            - Specifies descriptive text that identifies the component.
    draft:
        description:
            - Makes it possible to create drafts from an existing, published policy.
    name:
        description:
            - Specifies unique name for the component.
        required: true
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        default: Common
    published:
        description:
            - Moves a draft policy into a published state.
    requires:
        description:
            - Specifies the required profile types. Not normally set by end user.
    strategy:
        description:
            - Specifies the match strategy to use for this policy.
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
- name: Create LTM Policy
  f5bigip_ltm_policy:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_policy
    partition: Common
    sub_path: Drafts
    description: My ltm policy
    strategy: /Common/first-match
    state: present
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_LTM_POLICY_ARGS = dict(
    app_service=dict(type='str'),
    controls=dict(type='list'),
    description=dict(type='str'),
    draft=dict(type=bool),
    #legacy=dict(type=bool),
    publish=dict(type=bool),
    requires=dict(type='list'),
    strategy=dict(type='str')
)


class F5BigIpLtmPolicy(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create': self.mgmt_root.tm.ltm.policys.policy.create,
            'read': self.mgmt_root.tm.ltm.policys.policy.load,
            'update': self.mgmt_root.tm.ltm.policys.policy.update,
            'delete': self.mgmt_root.tm.ltm.policys.policy.delete,
            'exists': self.mgmt_root.tm.ltm.policys.policy.exists
        }

    def _present(self):
        has_changed = False

        if self._exists():
            publish = self.params.pop('publish', None)
            draft = self.params.pop('draft', None)
            has_changed = self._update()
            if publish:
                pol = self._read()
                if pol.status == 'draft':
                    pol.publish()
                    has_changed = True
            if draft:
                pol = self._read()
                if pol.status == 'published':
                    pol.draft()
                    has_changed = True
        else:
            has_changed = self._create()

        return has_changed


def main():
    module = AnsibleModuleF5BigIpNamedObject(
        argument_spec=BIGIP_LTM_POLICY_ARGS,
        supports_check_mode=False,
        mutually_exclusive=[
            ['draft', 'publish']
        ]
    )

    try:
        obj = F5BigIpLtmPolicy(check_mode=module.supports_check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
