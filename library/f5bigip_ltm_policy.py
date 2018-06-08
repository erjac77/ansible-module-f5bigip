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
requirements:
    - BIG-IP >= 12.0
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

RETURN = ''' # '''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.base import F5_NAMED_OBJ_ARGS
from ansible_common_f5.base import F5_PROVIDER_ARGS
from ansible_common_f5.bigip import F5BigIpNamedObject


class ModuleParams(object):
    @property
    def argument_spec(self):
        argument_spec = dict(
            app_service=dict(type='str'),
            controls=dict(type='list'),
            description=dict(type='str'),
            draft=dict(type=bool),
            # legacy=dict(type=bool),
            publish=dict(type=bool),
            requires=dict(type='list'),
            strategy=dict(type='str')
        )
        argument_spec.update(F5_PROVIDER_ARGS)
        argument_spec.update(F5_NAMED_OBJ_ARGS)
        return argument_spec

    @property
    def supports_check_mode(self):
        return True

    @property
    def mutually_exclusive(self):
        return [
            ['draft', 'publish']
        ]


class F5BigIpLtmPolicy(F5BigIpNamedObject):
    def _set_crud_methods(self):
        self._methods = {
            'create': self._api.tm.ltm.policys.policy.create,
            'read': self._api.tm.ltm.policys.policy.load,
            'update': self._api.tm.ltm.policys.policy.update,
            'delete': self._api.tm.ltm.policys.policy.delete,
            'exists': self._api.tm.ltm.policys.policy.exists
        }

    def _present(self):
        if self._exists():
            publish = self._params.pop('publish', None)
            draft = self._params.pop('draft', None)
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
    params = ModuleParams()
    module = AnsibleModule(argument_spec=params.argument_spec, supports_check_mode=params.supports_check_mode,
                           mutually_exclusive=params.mutually_exclusive)

    try:
        obj = F5BigIpLtmPolicy(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
