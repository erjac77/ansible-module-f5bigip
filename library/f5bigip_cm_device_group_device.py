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

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: f5bigip_cm_device_group_device
short_description: BIG-IP cm device-group device module
description:
    - Configures a set of devices to the device group.
version_added: 2.3
author:
    - "Eric Jacob, @erjac77"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    device_group:
        description:
            - Specifies the device group in which the device belongs.
        required: true
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
- name: Add CM Device Group member
  f5bigip_cm_device_group_device:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: bigip01.localhost
    partition: Common
    device_group: my_device_group
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_CM_DEVICE_GROUP_DEVICE_ARGS = dict(
    device_group    =   dict(type='str')
)

class F5BigIpCmDeviceGroupDevice(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.device_group = self.mgmt_root.tm.cm.device_groups.device_group.load(
            name=self.params['device_group'],
            partition=self.params['partition']
        )
        self.methods = {
            'create':   self.device_group.devices_s.devices.create,
            'read':     self.device_group.devices_s.devices.load,
            'update':   self.device_group.devices_s.devices.update,
            'delete':   self.device_group.devices_s.devices.delete,
            'exists':   self.device_group.devices_s.devices.exists
        }
        self.params.pop('device_group', None)

    def _exists(self):
        keys = self.device_group.devices_s.get_collection()
        for key in keys:
            name = self.params['name']
            if key.name == name:
                return True

        return False

def main():
    # Translation list for conflictual params
    tr = {}
    
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_CM_DEVICE_GROUP_DEVICE_ARGS, supports_check_mode=False)
    
    try:
        obj = F5BigIpCmDeviceGroupDevice(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()