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
module: f5bigip_net_selfip
short_description: BIG-IP net selfip module
description:
    - Configures a self IP address for a VLAN.
version_added: "2.4"
author:
    - "Eric Jacob (@erjac77)"
options:
    address [ip address/netmask]:
        description:
            - Specifies the IP address and netmask to be assigned to the system. Must appear in the format [ip
              address/mask].
    allow_service:
        description:
            - Specifies the type of protocol/service that the VLAN handles.
    app_service:
        description:
            - Specifies the application service that the object belongs to.
    description:
        description:
            - Specifies descriptive text that identifies the component.
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
    traffic_group:
        description:
            - Specifies the traffic group of the self IP address.
        default: traffic-group-local-only
    vlan:
        description:
            - Specifies the VLAN for which you are setting a self IP address.
        default: traffic-group-local-only
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Create NET Self IP
  f5bigip_net_selfip:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_self_ip
    address: 10.10.10.11/24
    vlan: internal
    state: present
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_NET_SELFIP_ARGS = dict(
    address=dict(type='str'),
    allow_service=dict(type='list'),
    app_service=dict(type='str'),
    description=dict(type='str'),
    fw_enforced_policy=dict(type='str'),
    # fw_rules=dict(type='list'),
    fw_staged_policy=dict(type='str'),
    traffic_group=dict(type='str'),
    vlan=dict(type='str')
)


class F5BigIpNetSelfip(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create': self.mgmt_root.tm.net.selfips.selfip.create,
            'read': self.mgmt_root.tm.net.selfips.selfip.load,
            'update': self.mgmt_root.tm.net.selfips.selfip.update,
            'delete': self.mgmt_root.tm.net.selfips.selfip.delete,
            'exists': self.mgmt_root.tm.net.selfips.selfip.exists
        }

    def _read(self):
        selfip = self.methods['read'](
            name=self.params['name'],
            partition=self.params['partition']
        )
        selfip.vlan = self._strip_partition(selfip.vlan)
        return selfip


def main():
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_NET_SELFIP_ARGS, supports_check_mode=True)

    try:
        obj = F5BigIpNetSelfip(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
