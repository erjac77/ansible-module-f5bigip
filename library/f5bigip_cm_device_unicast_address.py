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
module: f5bigip_cm_device_unicast_address
short_description: BIG-IP cm device unicast address module
description:
    - Configures unicast addresses for the device.
version_added: 2.3
author:
    - "Eric Jacob, @erjac77"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    device:
        description:
            - Specifies the device in which the unicast address belongs.
        required: true
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    ip:
        description:
            - Specifies the unicast IP addresses used for failover.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    port:
        description:
            - Specifies the port used for failover.
        required: false
        default: null
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
- name: Add CM Device Failover unicast address
  f5bigip_cm_device_unicast_address:
    f5bigip_hostname: 172.16.227.35
    f5bigip_username: admin
    f5bigip_password: admin
    f5bigip_port: 443
    device: bigip01.localhost
    ip: 10.10.30.11
    port: 1026
    state: present
  delegate_to: localhost
'''

from ansible_common_f5bigip.f5bigip import *

BIGIP_CM_DEVICE_UNICAST_ADDRESS_ARGS = dict(
    device  =   dict(type='str'),
    ip      =   dict(type='str'),
    port    =   dict(type='int')
)

class F5BigIpCmDeviceUnicastAddress(F5BigIpUnnamedObject):
    def _set_crud_methods(self):
        self.device = self.mgmt.tm.cm.devices.device.load(
            name=self.params['device'],
        )
        self.params.pop('device', None)
            
    def _read(self):
        return self.device
    
    def flush(self):
        has_changed = False
        found = False
        result = dict()
        
        for key, val in self.params.iteritems():
            if val is None:
                self.params[key] = 'none'
        
        device = self._read()
        if hasattr(device, 'unicastAddress'):
            for addr in device.unicastAddress:
                
                if addr['ip'] == self.params['ip']:
                    found = True
                    
                    if self.state == "absent":
                        has_changed = True
                        device.unicastAddress.remove(addr)
                        
                    if self.state == "present":
                        for key, val in self.params.iteritems():
                            if addr[key] != val:
                                has_changed = True
                                addr[key] = val
            if not found:
                if self.state == "present":
                    has_changed = True
                    device.unicastAddress.append(self.params)
        else:
            if self.state == "present":
                has_changed = True
                device.unicastAddress = [self.params]
        
        if has_changed:
            device.update()
            device.refresh()
        
        result.update(dict(changed=has_changed))
        return result

def main():
    # Translation list for conflictual params
    tr = {}
    
    module = AnsibleModuleF5BigIpUnnamedObject(argument_spec=BIGIP_CM_DEVICE_UNICAST_ADDRESS_ARGS, supports_check_mode=False)
    
    try:
        obj = F5BigIpCmDeviceUnicastAddress(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':  
    main()