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
module: f5bigip_gtm_datacenter
short_description: BIG-IP GTM datacenter module
description:
    - Configures a Global Traffic Manager data center.
version_added: "1.0"
author:
    - "Eric Jacob, @erjac77"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    contact:
        description:
            - Specifies the name of the administrator or the name of the department that manages the data center.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 1.0
    description:
        description:
            - Specifies a user-defined description.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 1.0
    disabled:
        description:
            - Specifies whether the data center and its resources are available for load balancing.
        required: false
        default: false
        choices: []
        aliases: []
        version_added: 1.0
    enabled:
        description:
            - Specifies whether the data center and its resources are available for load balancing.
        required: false
        default: true
        choices: []
        aliases: []
        version_added: 1.0
    location:
        description:
            - Specifies the physical location of the data center.
        required: false
        default: null
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
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        required: false
        default: Common
        choices: []
        aliases: []
        version_added: 1.0
    prober_pool:
        description:
            - Specifies a prober pool to use to monitor servers defined in this data center.
        required: false
        default: null
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
'''

EXAMPLES = '''
- name: Create GTM Datacenter
  f5bigip_gtm_datacenter:
    f5bigip_hostname: 172.16.227.35
    f5bigip_username: admin
    f5bigip_password: admin
    f5bigip_port: 443
    name: my_datacenter
    partition: Common
    contact: 'admin@root.local'
    description: My datacenter
    location: Somewhere
    state: present
  delegate_to: localhost

- name: Delete GTM Datacenter
  f5bigip_gtm_datacenter:
    f5bigip_hostname: 172.16.227.35
    f5bigip_username: admin
    f5bigip_password: admin
    f5bigip_port: 443
    name: my_datacenter
    partition: Common
    state: absent
  delegate_to: localhost
'''

from ansible_common_f5bigip.f5bigip import *

BIGIP_GTM_DATACENTER_ARGS = dict(
    #app_service     =   dict(type='str'),
    contact         =   dict(type='str'),
    description     =   dict(type='str'),
    disabled        =   dict(type='bool'),
    enabled         =   dict(type='bool'),
    location        =   dict(type='str'),
    #metadata        =   dict(type='list'),
    prober_pool     =   dict(type='str')
)

class F5BigIpGtmDatacenter(F5BigIpObject):
    def _set_crud_methods(self):
        self.methods = {
            'create':self.mgmt.tm.gtm.datacenters.datacenter.create,
            'read':self.mgmt.tm.gtm.datacenters.datacenter.load,
            'update':self.mgmt.tm.gtm.datacenters.datacenter.update,
            'delete':self.mgmt.tm.gtm.datacenters.datacenter.delete,
            'exists':self.mgmt.tm.gtm.datacenters.datacenter.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}
    
    module = AnsibleModuleF5BigIpObject(
        argument_spec=BIGIP_GTM_DATACENTER_ARGS,
        supports_check_mode=False,
        mutually_exclusive=[
            ['disabled', 'enabled']
        ]
    )
    
    try:
        obj = F5BigIpGtmDatacenter(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()