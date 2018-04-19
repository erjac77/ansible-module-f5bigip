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
module: f5bigip_ltm_snatpool
short_description: BIG-IP ltm snat pool module
description:
    - Configures a secure network address translation (SNAT) pool.
version_added: "2.4"
author:
    - "Eric Jacob (@erjac77)"
options:
    app_service:
        description:
            - Specifies the application service that the object belongs to.
    description:
        description:
            - Specifies descriptive text that identifies the component.
    members:
        description:
            - Specifies translation IP addresses of the pools in the SNAT pool.
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
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Create LTM SNAT Pool
  f5bigip_ltm_snatpool:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_snatpool
    partition: Common
    members:
      - 10.10.10.251
      - 10.10.10.252
      - 10.10.10.253
    state: present
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_LTM_SNATPOOL_ARGS = dict(
    app_service=dict(type='str'),
    description=dict(type='str'),
    members=dict(type='list')
)


class F5BigIpLtmSnatpool(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create': self.mgmt_root.tm.ltm.snatpools.snatpool.create,
            'read': self.mgmt_root.tm.ltm.snatpools.snatpool.load,
            'update': self.mgmt_root.tm.ltm.snatpools.snatpool.update,
            'delete': self.mgmt_root.tm.ltm.snatpools.snatpool.delete,
            'exists': self.mgmt_root.tm.ltm.snatpools.snatpool.exists
        }

    def _read(self):
        snatpool = self.methods['read'](
            name=self.params['name'],
            partition=self.params['partition']
        )

        result = set()
        for member in snatpool.members:
            member = self._strip_partition(member)
            result.update([member])
        snatpool.members = list(result)

        return snatpool


def main():
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_SNATPOOL_ARGS, supports_check_mode=True)

    try:
        obj = F5BigIpLtmSnatpool(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
