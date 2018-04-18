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
module: f5bigip_cm_failover_status
short_description: BIG-IP cm failover status module
description:
    - Display the failover status of the local device.
version_added: "2.4"
author:
    - "Eric Jacob (@erjac77)"
options:
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Get CM failover status of the device
  f5bigip_cm_failover_status:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
  delegate_to: localhost
  register: result

- name: Display the failover status of the device
  debug:
    msg: "Failover Status: {{ result.failover_status }}"
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_CM_FAILOVER_STATUS_ARGS = dict(
)


class F5BigIpCmFailoverStatus(F5BigIpUnnamedObject):
    def set_crud_methods(self):
        self.methods = {
            'read': self.mgmt_root.tm.cm.failover_status
        }

    def get_failover_status(self):
        failover_status_desc = {}
        failover_status = self.methods['read']

        if failover_status._meta_data['uri'].endswith("/mgmt/tm/cm/failover-status/"):
            failover_status.refresh()
            failover_status_desc = \
                failover_status.entries['https://localhost/mgmt/tm/cm/failover-status/0']['nestedStats']['entries'][
                    'status']['description']
        else:
            raise AnsibleF5Error("Unable to retrieve the failover status of the device.")

        return {'failover_status': failover_status_desc}


def main():
    module = AnsibleModuleF5BigIpUnnamedObject(argument_spec=BIGIP_CM_FAILOVER_STATUS_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpCmFailoverStatus(check_mode=module.supports_check_mode, **module.params)
        result = obj.get_failover_status()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()