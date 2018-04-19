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
module: f5bigip_sys_dns
short_description: BIG-IP sys dns module
description:
    - Configures the Domain Name System (DNS) for the BIG-IP system.
version_added: "2.4"
author:
    - "Eric Jacob (@erjac77)"
options:
    description:
        description:
            - Specifies descriptive text that identifies the component.
    name_servers:
        description:
            - Configures a group of DNS name servers for the BIG-IP system.
    search:
        description:
            - Configures a list of domain names in a specific order.
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Add SYS DNS Name Servers
  f5bigip_sys_dns:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name_servers:
      - 10.20.20.21
      - 10.20.20.22
    state: present
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_SYS_DNS_ARGS = dict(
    description=dict(type='str'),
    name_servers=dict(type='list'),
    search=dict(type='list')
)


class F5BigIpSysDns(F5BigIpUnnamedObject):
    def set_crud_methods(self):
        self.methods = {
            'read': self.mgmt_root.tm.sys.dns.load,
            'update': self.mgmt_root.tm.sys.dns.update
        }


def main():
    module = AnsibleModuleF5BigIpUnnamedObject(argument_spec=BIGIP_SYS_DNS_ARGS, supports_check_mode=True)

    try:
        obj = F5BigIpSysDns(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
