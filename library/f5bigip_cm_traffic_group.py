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
module: f5bigip_cm_traffic_group
short_description: BIG-IP cm traffic-group module
description:
    - Manages a traffic group.
version_added: 2.3
author:
    - "Eric Jacob, @erjac77"
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
    auto_failback_enabled:
        description:
            - Specifies whether the traffic group fails back to the default device.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    auto_failback_time:
        description:
            - Specifies the time required to fail back.
        required: false
        default: 0
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
    ha_group:
        description:
            - This specifies the name of the HA group that the traffic group uses to decide the active device within the traffic group.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    ha_load_factor:
        description:
            - Specifies a number for this traffic group that represents the load this traffic group presents to the system relative to other traffic groups.
        required: false
        default: 1
        choices: []
        aliases: []
        version_added: 2.3
    ha_order:
        description:
            - This list of devices specifies the order in which the devices will become active for the traffic group when a failure occurs.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    mac:
        description:
            - Specifies a MAC address for the traffic group.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    name:
        description:
            - Specifies unique name for the component.
        required: true
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    partition:
        description:
            - Displays the administrative partition in which the component object resides.
        required: false
        default: Common
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
- name: Create CM Traffic Group
  f5bigip_cm_traffic_group:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_traffic_group
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_CM_TRAFFIC_GROUP_ARGS = dict(
    app_service             =   dict(type='str'),
    auto_failback_enabled   =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    auto_failback_time      =   dict(type='int'),
    description             =   dict(type='str'),
    ha_group                =   dict(type='str'),
    ha_load_factor          =   dict(type='int'),
    ha_order                =   dict(type='list'),
    mac                     =   dict(type='str')
)

class F5BigIpCmTrafficGroup(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.cm.traffic_groups.traffic_group.create,
            'read':     self.mgmt_root.tm.cm.traffic_groups.traffic_group.load,
            'update':   self.mgmt_root.tm.cm.traffic_groups.traffic_group.update,
            'delete':   self.mgmt_root.tm.cm.traffic_groups.traffic_group.delete,
            'exists':   self.mgmt_root.tm.cm.traffic_groups.traffic_group.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}
    
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_CM_TRAFFIC_GROUP_ARGS, supports_check_mode=False)
    
    try:
        obj = F5BigIpCmTrafficGroup(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':  
    main()