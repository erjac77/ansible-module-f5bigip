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
module: f5bigip_cm_device
short_description: BIG-IP cm device module
description:
    - Manages a device.
version_added: "2.4"
author:
    - "Eric Jacob (@erjac77)"
options:
    comment:
        description:
            - Specifies user comments about the device.
    configsync_ip:
        description:
            - Specifies the IP address used for configuration synchronization.
    contact:
        description:
            - Specifies administrator contact information.
    description:
        description:
            - Specifies a user-defined description of the device.
    ha_capacity:
        description:
            - Specifies a number that represents the relative capacity of the device to be active for a number of traffic groups.
        default: 0
        choices: range(0, 100000)
    hostname:
        description:
            - Specifies a hostname for the device.
    location:
        description:
            - Specifies the physical location of the device.
    mirror_ip:
        description:
            - Specifies the IP address used for state mirroring.
    mirror_secondary_ip:
        description:
            - Specifies the secondary IP address used for state mirroring.
    multicast_interface:
        description:
            - Specifies the interface name used for the failover multicast IP address.
    multicast_ip:
        description:
            - Specifies the multicast IP address used for failover.
    multicast_port:
        description:
            - Specifies the multicast port used for failover.
    name:
        description:
            - Specifies unique name for the component.
        required: true
    partition:
        description:
            - Displays the administrative partition in which the component object resides.
        default: Common
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
- name: Configure CM Device Properties
  f5bigip_cm_device:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: bigip01.localhost
    comment: My lab device
    configsync_ip: 10.10.30.11
    contact: 'admin@localhost'
    description: My device
    location: Central Office
    mirror_ip: 10.10.30.11
    mirror_secondary_ip: 10.10.10.11
    multicast_interface: eth0
    multicast_ip: 224.0.0.245
    multicast_port: 62960
    unicast_address: 10.10.30.11
    state: present
  delegate_to: localhost
'''

RETURN = '''
'''

from six.moves import range
from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_CM_DEVICE_ARGS = dict(
    comment             =   dict(type='str'),
    configsync_ip       =   dict(type='str'),
    contact             =   dict(type='str'),
    description         =   dict(type='str'),
    ha_capacity         =   dict(type='int', choices=range(0, 100000)),
    hostname            =   dict(type='str'),
    location            =   dict(type='str'),
    mirror_ip           =   dict(type='str'),
    mirror_secondary_ip =   dict(type='str'),
    multicast_interface =   dict(type='str'),
    multicast_ip        =   dict(type='str'),
    multicast_port      =   dict(type='int'),
    unicast_address     =   dict(type='list')
)

class F5BigIpCmDevice(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.cm.devices.device.create,
            'read':     self.mgmt_root.tm.cm.devices.device.load,
            'update':   self.mgmt_root.tm.cm.devices.device.update,
            'delete':   self.mgmt_root.tm.cm.devices.device.delete,
            'exists':   self.mgmt_root.tm.cm.devices.device.exists
        }

def main():
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_CM_DEVICE_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpCmDevice(check_mode=module.supports_check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

if __name__ == '__main__':
    main()