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
module: f5bigip_cm_device_group
short_description: BIG-IP cm device-group module
description:
    - Configures device groups.
version_added: "2.4"
author:
    - "Eric Jacob (@erjac77)"
options:
    app_service:
        description:
            - Specifies the application service to which the object belongs.
    asm_sync:
        description:
            - Specifies whether to synchronize ASM configurations of device group members.
        default: disabled
        choices: ['enabled', 'disabled']
    auto_sync:
        description:
            - Specifies whether the device group automatically synchronizes configuration data to its members.
        default: disabled
        choices: ['enabled', 'disabled']
    description:
        description:
            - Specifies descriptive text that identifies the component.
    full_load_on_sync:
        description:
            - Specifies that the entire configuration for a device group is sent when configuration synchronization is performed.
        default: false
        choices: [true, false]
    incremental_config_sync_size_max:
        description:
            - Specifies the maximum size (in KB) to devote to incremental config sync cached transactions.
        default: 1024
    name:
        description:
            - Specifies unique name for the component.
        required: true
    network_failover:
        description:
            - When the device group type is failover, specifies whether network failover is used.
        default: enabled
        choices: ['enabled', 'disabled']
    partition:
        description:
            - Displays the administrative partition in which the component object resides.
        default: Common
    save_on_auto_sync:
        description:
            - Specifies whether to save the configuration on the remote devices following an automatic configuration synchronization.
        default: false
        choices: [true, false]
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    type:
        description:
            - Specifies the type of device group.
        default: sync-only
        choices: ['sync-only', 'sync-failover']
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Create CM Device Group
  f5bigip_cm_device_group:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_device_group
    network_failover: enabled
    type: sync-failover
    state: present
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_CM_DEVICE_GROUP_ARGS = dict(
    app_service                         =   dict(type='str'),
    asm_sync                            =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    auto_sync                           =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    description                         =   dict(type='str'),
    full_load_on_sync                   =   dict(type='bool'),
    incremental_config_sync_size_max    =   dict(type='int'),
    network_failover                    =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    save_on_auto_sync                   =   dict(type='bool'),
    type                                =   dict(type='str', choices=['sync-only', 'sync-failover'])
)

class F5BigIpCmDeviceGroup(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.cm.device_groups.device_group.create,
            'read':     self.mgmt_root.tm.cm.device_groups.device_group.load,
            'update':   self.mgmt_root.tm.cm.device_groups.device_group.update,
            'delete':   self.mgmt_root.tm.cm.device_groups.device_group.delete,
            'exists':   self.mgmt_root.tm.cm.device_groups.device_group.exists
        }

def main():
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_CM_DEVICE_GROUP_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpCmDeviceGroup(check_mode=module.supports_check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

if __name__ == '__main__':
    main()