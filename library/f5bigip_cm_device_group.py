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
module: f5bigip_cm_device_group
short_description: BIG-IP cm device group module
description:
    - Configures device groups.
version_added: "1.0"
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
        version_added: 1.0
    asm_sync:
        description:
            - Specifies whether to synchronize ASM configurations of device group members.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 1.0
    auto_sync:
        description:
            - Specifies whether the device group automatically synchronizes configuration data to its members.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 1.0
    description:
        description:
            - Specifies descriptive text that identifies the component.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 1.0
    full_load_on_sync:
        description:
            - Specifies that the entire configuration for a device group is sent when configuration synchronization is performed.
        required: false
        default: false
        choices: [true, false]
        aliases: []
        version_added: 1.0
    incremental_config_sync_size_max:
        description:
            - Specifies the maximum size (in KB) to devote to incremental config sync cached transactions.
        required: false
        default: 1024
        choices: []
        aliases: []
        version_added: 1.0
    name:
        description:
            - Specifies unique name for the component.
        required: true
        default: null
        choices: []
        aliases: []
        version_added: 1.0
    network_failover:
        description:
            - When the device group type is failover, specifies whether network failover is used.
        required: false
        default: enabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 1.0
    partition:
        description:
            - Displays the administrative partition in which the component object resides.
        required: false
        default: Common
        choices: []
        aliases: []
        version_added: 1.0
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        required: false
        default: present
        choices: ['absent', 'present']
        aliases: []
        version_added: 1.0
    save_on_auto_sync:
        description:
            - Specifies whether to save the configuration on the remote devices following an automatic configuration synchronization.
        required: false
        default: false
        choices: [true, false]
        aliases: []
        version_added: 1.0
    type:
        description:
            - Specifies the type of device group.
        required: false
        default: sync-only
        choices: ['sync-only', 'sync-failover']
        aliases: []
        version_added: 1.0
'''

EXAMPLES = '''
- name: Create CM Device Group
  f5bigip_cm_device_group:
    f5bigip_hostname: 172.16.227.35
    f5bigip_username: admin
    f5bigip_password: admin
    f5bigip_port: 443
    name: my_device_group
    network_failover: enabled
    type: sync-failover
    state: present
  delegate_to: localhost
'''

from ansible_common_f5bigip.f5bigip import *

BIGIP_CM_DEVICE_GROUP_ARGS = dict(
    #app_service                         =   dict(type='str'),
    asm_sync                            =   dict(type='str', choices=F5BIGIP_ACTIVATION_CHOICES),
    auto_sync                           =   dict(type='str', choices=F5BIGIP_ACTIVATION_CHOICES),
    description                         =   dict(type='str'),
    #devices                             =   dict(type='list'),
    full_load_on_sync                   =   dict(type='bool'),
    incremental_config_sync_size_max    =   dict(type='int'),
    network_failover                    =   dict(type='str', choices=F5BIGIP_ACTIVATION_CHOICES),
    save_on_auto_sync                   =   dict(type='bool'),
    type                                =   dict(type='str', choices=['sync-only', 'sync-failover'])
)

class F5BigIpCmDeviceGroup(F5BigIpObject):
    def _set_crud_methods(self):
        self.methods = {
            'create':self.mgmt.tm.cm.device_groups.device_group.create,
            'read':self.mgmt.tm.cm.device_groups.device_group.load,
            'update':self.mgmt.tm.cm.device_groups.device_group.update,
            'delete':self.mgmt.tm.cm.device_groups.device_group.delete,
            'exists':self.mgmt.tm.cm.device_groups.device_group.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}
    
    module = AnsibleModuleF5BigIpObject(argument_spec=BIGIP_CM_DEVICE_GROUP_ARGS, supports_check_mode=False)
    
    try:
        obj = F5BigIpCmDeviceGroup(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':  
    main()