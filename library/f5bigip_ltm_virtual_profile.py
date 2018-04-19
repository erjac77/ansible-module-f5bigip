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
module: f5bigip_ltm_virtual_profile
short_description: BIG-IP ltm virtual profile module
description:
    - Configures profiles on the specified virtual server to direct and manage traffic.
version_added: "2.4"
author:
    - "Eric Jacob (@erjac77)"
options:
    context:
        description:
            - Specifies that the profile is either a clientside or serverside (or both) profile.
        default: all
        choices: ['all', 'clientside', 'serverside']
    name:
        description:
            - Specifies unique name for the component.
        required: true
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        default: Common
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    virtual:
        description:
            - Specifies the full path of the virtual to which the profile belongs.
        required: true
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Add LTM HTTP Profile to VS
  f5bigip_ltm_virtual_profile:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: http
    partition: Common
    virtual: /Common/my_http_vs
    state: present
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_LTM_VIRTUAL_PROFILE_ARGS = dict(
    context=dict(type='str', choices=['all', 'clientside', 'serverside']),
    virtual=dict(type='str')
)


class F5BigIpLtmVirtualProfile(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.virtual = self.mgmt_root.tm.ltm.virtuals.virtual.load(
            **self._get_resource_id_from_path(self.params['virtual']))
        self.methods = {
            'create': self.virtual.profiles_s.profiles.create,
            'read': self.virtual.profiles_s.profiles.load,
            'update': self.virtual.profiles_s.profiles.update,
            'delete': self.virtual.profiles_s.profiles.delete,
            'exists': self.virtual.profiles_s.profiles.exists
        }
        del self.params['virtual']


def main():
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_VIRTUAL_PROFILE_ARGS, supports_check_mode=True)

    try:
        obj = F5BigIpLtmVirtualProfile(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
