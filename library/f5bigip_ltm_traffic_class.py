#!/usr/bin/python
#
# Copyright 2016, Eric Jacob <erjac77@gmail.com>
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

DOCUMENTATION = '''
---
module: f5bigip_ltm_traffic_class
short_description: BIG-IP ltm traffic class module
description:
    - Configures a traffic class.
version_added: 2.3
author:
	- "Gabriel Fortin"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    app_service:
        description:
            - Specifies the application service to which the object belongs.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    classification:
        description:
            - Specifies the actual textual tag to be associated with the flow if the traffic class is matched.
        required: true
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    description:
        description:
            - Specifies descriptive text that identifies the component.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    destination_address:
        description:
            - Specifies destination IP addresses for the system to use when evaluating traffic flow.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    destination_mask:
        description:
            - Specifies a destination IP address mask for the system to use when evaluating traffic flow.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    destination_port:
        description:
            - Specifies a destination port for the system to use when evaluating traffic flow.
        required: false
        default: 0
        choices: []
        aliases: []
        version_added: 2.3
    name:
        description:
            - Specifies a unique name for the component.
        required: true
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        required: false
        default: Common
        choices: []
        aliases: []
        version_added: 2.3
    protocol:
        description:
            - Specifies a protocol for the system to use when evaluating traffic flow.
        required: false
        default: any
        choices: []
        aliases: []
        version_added: 2.3
    source_address:
        description:
            - Specifies source IP addresses for the system to use when evaluating traffic flow.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    source_mask:
        description:
            - Specifies a source IP address mask for the system to use when evaluating traffic flow.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    source_port:
        description:
            - Specifies a source port for the system to use when evaluating traffic flow.
        required: false
        default: 0
        choices: []
        aliases: []
        version_added: 2.3
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        required: false
        default: present
        choices: ['absent', 'present']
        aliases: []
        version_added: 2.3
'''

EXAMPLES = '''
- name: Create LTM Traffic Class
  f5bigip_ltm_traffic_class:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_traffic_class
    partition: Common
    classification: traffic_class
    description: My ltm traffic class
    destination_port: 21
    protocol: tcp
    source_port: 21
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_LTM_TRAFFIC_CLASS_ARGS = dict(
    app_service             =   dict(type='str'),
    classification          =   dict(type='str'),
    description             =   dict(type='str'),
    destination_address     =   dict(type='str'),
    destination_mask        =   dict(type='str'),
    destination_port        =   dict(type='int'),
    file_name               =   dict(type='str'),
    protocol                =   dict(type='str'),
    source_address          =   dict(type='str'),
    source_mask             =   dict(type='str'),
    source_port             =   dict(type='int')
)

class F5BigIpLtmTrafficClass(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.traffic_class_s.traffic_class.create,
            'read':     self.mgmt_root.tm.ltm.traffic_class_s.traffic_class.load,
            'update':   self.mgmt_root.tm.ltm.traffic_class_s.traffic_class.update,
            'delete':   self.mgmt_root.tm.ltm.traffic_class_s.traffic_class.delete,
            'exists':   self.mgmt_root.tm.ltm.traffic_class_s.traffic_class.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}

    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_TRAFFIC_CLASS_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpLtmTrafficClass(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()