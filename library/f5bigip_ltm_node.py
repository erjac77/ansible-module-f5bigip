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
module: f5bigip_ltm_node
short_description: BIG-IP ltm node module
description:
    - Configures node addresses and services.
version_added: "2.4"
author:
    - "Eric Jacob (@erjac77)"
options:
    address:
        description:
            - Specifies the IP address for the node.
        required: true
    app_service:
        description:
            - Specifies the application service to which the object belongs.
    connection_limit:
        description:
            - Specifies the maximum number of connections that a node or node address can handle.
        default: 0
    description:
        description:
            - Specifies a user-defined description.
    dynamic_ratio:
        description:
            - Sets the dynamic ratio number for the node.
        default: 1
    fqdn:
        description:
            - Specifies the attributes for defining a fully qualified domain name for the node.
    logging:
        description:
            - Specifies whether the monitor applied should log its actions.
        default: disabled
        choices: ['enabled', 'disabled']
    metadata:
        description:
            - Associates user defined data, each of which has a name and value pair and persistence.
        default: persistent
    monitor:
        description:
            - Specifies the monitors that the BIG-IP system is to associate with the node.
    name:
        description:
            - Specifies unique name for the component.
        required: true
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        default: Common
    rate_limit:
        description:
            - Specifies the maximum number of connections per second allowed for a node or node address.
        default: disabled (or 0)
    ratio:
        description:
            - Specifies the fixed ratio value used for a node during Ratio load balancing.
        default: 1
    session:
        description:
            - Specifies the ability of the client to persist to the node when making new connections.
        default: user-enabled
        choices: ['user-enabled', 'user-disabled']
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    state_user:
        description:
            - Specifies the current state of the node.
        default: user-up
        choices: ['user-down', 'user-up']
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Create LTM Node
  f5bigip_ltm_node:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_node
    partition: Common
    description: My node
    address: 10.10.10.101
    monitor: /Common/icmp
    state: present
  delegate_to: localhost

- name: Force LTM Node Offline
  f5bigip_ltm_node:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_node
    partition: Common
    session: user-disabled
    state_user: user-down
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_LTM_NODE_ARGS = dict(
    address=dict(type='str'),
    app_service=dict(type='str'),
    connection_limit=dict(type='int'),
    description=dict(type='str'),
    dynamic_ratio=dict(type='int'),
    fqdn=dict(type='str'),
    logging=dict(type='str', choices=F5_ACTIVATION_CHOICES),
    metadata=dict(type='list'),
    monitor=dict(type='str'),
    rate_limit=dict(type='str'),
    ratio=dict(type='int'),
    session=dict(type='str', choices=['user-enabled', 'user-disabled']),
    state_user=dict(type='str', choices=['user-down', 'user-up'])
)


class F5BigIpLtmNode(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create': self.mgmt_root.tm.ltm.nodes.node.create,
            'read': self.mgmt_root.tm.ltm.nodes.node.load,
            'update': self.mgmt_root.tm.ltm.nodes.node.update,
            'delete': self.mgmt_root.tm.ltm.nodes.node.delete,
            'exists': self.mgmt_root.tm.ltm.nodes.node.exists
        }


def main():
    # Translation list for conflictual params
    tr = {'state_user': 'state'}

    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_NODE_ARGS, supports_check_mode=True)

    try:
        obj = F5BigIpLtmNode(check_mode=module.check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
