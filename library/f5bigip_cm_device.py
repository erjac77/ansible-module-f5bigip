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
module: f5bigip_cm_device
short_description: BIG-IP cm device module
description:
    - Configures a device.
version_added: 2.3
author:
    - "Eric Jacob, @erjac77"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    comment:
        description:
            - Specifies user comments about the device.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    configsync_ip:
        description:
            - Specifies the IP address used for configuration synchronization.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    contact:
        description:
            - Specifies administrator contact information.
        required: false
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
    ha_capacity:
        description:
            - Specifies a hostname for the device.
        required: false
        default: 0
        choices: []
        aliases: []
        version_added: 2.3
    hostname:
        description:
            - Specifies a number that represents the relative capacity of the device to be active for a number of traffic groups.
        required: false
        default: 0
        choices: []
        aliases: []
        version_added: 2.3
    location:
        description:
            - Specifies the physical location of the device.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    mirror_ip:
        description:
            - Specifies the IP address used for state mirroring.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    mirror_secondary_ip:
        description:
            - Specifies the secondary IP address used for state mirroring.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    multicast_interface:
        description:
            - Specifies the interface name used for the failover multicast IP address.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    multicast_ip:
        description:
            - Specifies the multicast IP address used for failover.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    multicast_port:
        description:
            - Specifies the multicast port used for failover.
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
- name: Configure CM Device Properties
  f5bigip_cm_device:
    f5bigip_hostname: 172.16.227.35
    f5bigip_username: admin
    f5bigip_password: admin
    f5bigip_port: 443
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
    state: present
  delegate_to: localhost
'''

from ansible_common_f5bigip.f5bigip import *

BIGIP_CM_DEVICE_ARGS = dict(
    comment             =   dict(type='str'),
    configsync_ip       =   dict(type='str'),
    contact             =   dict(type='str'),
    description         =   dict(type='str'),
    ha_capacity         =   dict(type='int'),
    hostname            =   dict(type='str'),
    location            =   dict(type='str'),
    mirror_ip           =   dict(type='str'),
    mirror_secondary_ip =   dict(type='str'),
    multicast_interface =   dict(type='str'),
    multicast_ip        =   dict(type='str'),
    multicast_port      =   dict(type='int'),
    unicast_addresses   =   dict(type='list')
)

class F5BigIpCmDevice(F5BigIpObject):
    def _set_crud_methods(self):
        self.methods = {
            'create':self.mgmt.tm.cm.devices.device.create,
            'read':self.mgmt.tm.cm.devices.device.load,
            'update':self.mgmt.tm.cm.devices.device.update,
            'delete':self.mgmt.tm.cm.devices.device.delete,
            'exists':self.mgmt.tm.cm.devices.device.exists
        }

    def _exists(self):
        return self.methods['exists'](
            name=self.params['name']
        )
    
    def _read(self):
        return self.methods['read'](
            name=self.params['name']
        )

def main():
    # Translation list for conflictual params
    tr = {}
    
    module = AnsibleModuleF5BigIpObject(argument_spec=BIGIP_CM_DEVICE_ARGS, supports_check_mode=False)
    
    try:
        obj = F5BigIpCmDevice(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':  
    main()