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
module: f5bigip_gtm_server
short_description: BIG-IP GTM server module
description:
    - Configures servers for the Global Traffic Manager.
version_added: "1.0"
author:
    - "Eric Jacob, @erjac77"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    addresses:
        description:
            - Specifies the server IP addresses for the server.
        required: true
        default: null
        choices: []
        aliases: []
        version_added: 1.0
    datacenter:
        description:
            - Specifies the data center to which the server belongs.
        required: true
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
    monitor:
        description:
            - Specifies the health monitors that the system uses to determine whether this server is available for load balancing.
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
            - Specifies the name of a prober pool to use to monitor this server's resources.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 1.0
    product:
        description:
            - Specifies the server type.
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
    virtual_server_discovery:
        description:
            - Specifies whether the system auto-discovers the virtual servers for this server.
        required: false
        default: null
        choices: [disabled, enabled, enabled-no-delete]
        aliases: []
        version_added: 1.0
'''

EXAMPLES = '''
- name: Create GTM Server
  f5bigip_gtm_server:
    f5bigip_hostname: 172.16.227.35
    f5bigip_username: admin
    f5bigip_password: admin
    f5bigip_port: 443
    name: my_server
    partition: Common
    addresses:
      - { name: 10.10.1.11, device-name: primary }
      - { name: 10.10.1.12, device-name: secondary }
    datacenter: my_datacenter
    description: My server
    product: redundant-bigip
    state: present
  delegate_to: localhost

- name: Delete GTM Server
  f5bigip_gtm_server:
    f5bigip_hostname: 172.16.227.35
    f5bigip_username: admin
    f5bigip_password: admin
    f5bigip_port: 443
    name: my_server
    partition: Common
    state: absent
  delegate_to: localhost
'''

from ansible_common_f5bigip.f5bigip import *

BIGIP_GTM_SERVER_ARGS = dict(
    addresses                       =   dict(type='list'),
    #app_service                     =   dict(type='str'),
    datacenter                      =   dict(type='str'),
    description                     =   dict(type='str'),
    disabled                        =   dict(type='bool'),
    enabled                         =   dict(type='bool'),
    #expose_route_domains            =   dict(type='str', choices=[F5BIGIP_POLAR_CHOICES]),
    #iq_allow_path                   =   dict(type='str', choices=[F5BIGIP_POLAR_CHOICES]),
    #iq_allow_service_check          =   dict(type='str', choices=[F5BIGIP_POLAR_CHOICES]),
    #iq_allow_snmp                   =   dict(type='str', choices=[F5BIGIP_POLAR_CHOICES]),
    #limit_cpu_usage                 =   dict(type='int'),
    #limit_cpu_usage_status          =   dict(type='str', choices=[F5BIGIP_ACTIVATION_CHOICES]),
    #limit_mem_avail                 =   dict(type='int'),
    #limit_mem_avail_status          =   dict(type='str', choices=[F5BIGIP_ACTIVATION_CHOICES]),
    #limit_max_bps                   =   dict(type='int'),
    #limit_max_bps_status            =   dict(type='str', choices=[F5BIGIP_ACTIVATION_CHOICES]),
    #limit_max_connections           =   dict(type='int'),
    #limit_max_connections_status    =   dict(type='str', choices=[F5BIGIP_ACTIVATION_CHOICES]),
    #limit_max_pps                   =   dict(type='int'),
    #limit_max_pps_status            =   dict(type='str', choices=[F5BIGIP_ACTIVATION_CHOICES]),
    #metadata                        =   dict(type='list'),
    monitor                         =   dict(type='str'),
    prober_pool                     =   dict(type='str'),
    product                         =   dict(type='str'),
    virtual_server_discovery        =   dict(type='str', choices=[F5BIGIP_ACTIVATION_CHOICES, 'enabled-no-delete'])#,
    #virtual-servers                 =   dict(type='list')
)

class F5BigIpGtmServer(F5BigIpObject):
    def _set_crud_methods(self):
        self.methods = {
            'create':self.mgmt.tm.gtm.servers.server.create,
            'read':self.mgmt.tm.gtm.servers.server.load,
            'update':self.mgmt.tm.gtm.servers.server.update,
            'delete':self.mgmt.tm.gtm.servers.server.delete,
            'exists':self.mgmt.tm.gtm.servers.server.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}
    
    module = AnsibleModuleF5BigIpObject(
        argument_spec=BIGIP_GTM_SERVER_ARGS,
        supports_check_mode=False,
        mutually_exclusive=[
            ['disabled', 'enabled']
        ]
    )
    
    try:
        obj = F5BigIpGtmServer(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()