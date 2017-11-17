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
module: f5bigip_shared_bigip_failover_state
short_description: BIG-IP shared bigip failover state module
description:
    - Displays bigip failover state.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
notes:
    - Requires BIG-IP software version >= 12.0.0
requirements:
    - ansible-common-f5
    - f5-sdk
options:
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Get Shared Bigip failover state
  f5bigip_shared_bigip_failover_state:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_SHARED_BIGIP_FAILOVER_STATE_ARGS = dict(
)

class F5BigIpSharedBigipFailoverState(F5BigIpUnnamedObject):
    def set_crud_methods(self):
        self.methods = {
            'read':     self.mgmt_root.tm.shared.bigip_failover_state.load
        }

    def get_failover_state(self):
        return { 'bigip_failover_state': self.methods['read']().attrs }

def main():
    module = AnsibleModuleF5BigIpUnnamedObject(argument_spec=BIGIP_SHARED_BIGIP_FAILOVER_STATE_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpSharedBigipFailoverState(check_mode=module.supports_check_mode, **module.params)
        result = obj.get_failover_state()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

if __name__ == '__main__':
    main()