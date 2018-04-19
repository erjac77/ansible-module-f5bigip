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
module: f5bigip_gtm_topology
short_description: BIG-IP gtm topology module
description:
    - Configures a topology statement.
version_added: "2.4"
author:
    - "Eric Jacob (@erjac77)"
options:
    app_service:
        description:
            - Specifies the application service that the object belongs to.
    description:
        description:
            - Specifies a user-defined description.
    name:
        description:
            - Specifies unique name for the component.
        required: true
    order:
        description:
            - Specifies the order in which the system processes the topology record.
        default: 0
    score:
        description:
            - Specifies the weight of the topology item.
        default: 1
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
- name: Create GTM Topology
  f5bigip_gtm_topology:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: 'ldns: country US server: datacenter /Common/DC1'
    description: My topology
    state: present
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_GTM_TOPOLOGY_ARGS = dict(
    app_service=dict(type='str'),
    description=dict(type='str'),
    order=dict(type='list'),
    score=dict(type='int')
)


class F5BigIpGtmTopology(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create': self.mgmt_root.tm.gtm.topology_s.topology.create,
            'read': self.mgmt_root.tm.gtm.topology_s.topology.load,
            'update': self.mgmt_root.tm.gtm.topology_s.topology.update,
            'delete': self.mgmt_root.tm.gtm.topology_s.topology.delete,
            'exists': self.mgmt_root.tm.gtm.topology_s.topology.exists
        }
        del self.params['partition']

    def _update(self):
        raise AnsibleF5Error("%s does not support update" % self.__class__.__name__)


def main():
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_GTM_TOPOLOGY_ARGS, supports_check_mode=True)

    try:
        obj = F5BigIpGtmTopology(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
