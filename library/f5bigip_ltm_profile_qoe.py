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
module: f5bigip_ltm_profile_qoe
short_description: BIG-IP ltm profile qoe module
description:
    - Configures a Quality of Experience (QoE) Monitoring profile.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    name:
        description:
            - Specifies a unique name for the component.
        required: true
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    video:
        description:
            - Specifies to monitor the QoE MOS score of video streams with the format of MP4 or FLV.
        choices: ['false', 'true']
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Create LTM Profile QoE
  f5bigip_ltm_profile_qoe:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_qoe_profile
    partition: Common
    state: present
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_LTM_PROFILE_QOE_ARGS = dict(
    video=dict(type='str', choices=['false', 'true'])
)


class F5BigIpLtmProfileQoe(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create': self.mgmt_root.tm.ltm.profile.qoes.qoe.create,
            'read': self.mgmt_root.tm.ltm.profile.qoes.qoe.load,
            'update': self.mgmt_root.tm.ltm.profile.qoes.qoe.update,
            'delete': self.mgmt_root.tm.ltm.profile.qoes.qoe.delete,
            'exists': self.mgmt_root.tm.ltm.profile.qoes.qoe.exists
        }


def main():
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_PROFILE_QOE_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpLtmProfileQoe(check_mode=module.supports_check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
