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
module: f5bigip_gtm_server_virtual_server
short_description: BIG-IP GTM server virtual-server module
description:
    - Configures virtual servers that are resources for this server.
version_added: "1.0"
author:
    - "Eric Jacob, @erjac77"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    depends_on:
        description:
            - Specifies the vs-name of the server on which this virtual server depends.
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
    destination:
        description:
            - Specifies the IP address and port of the virtual server.
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
            - Specifies the monitor you want to assign to this virtual server.
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
    server:
        description:
            - Specifies the server in which the virtual-server belongs.
        required: true
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
    translation_address:
        description:
            - Specifies the public address that this virtual server translates into when the Global Traffic Manager communicates between the network and the Internet.
        required: false
        default: ::
        choices: []
        aliases: []
        version_added: 1.0
    translation_port:
        description:
            - Specifies the translation port number or service name for the virtual server, if necessary.
        required: false
        default: 0
        choices: []
        aliases: []
        version_added: 1.0
'''

EXAMPLES = '''
- name: Create GTM Server VS
  f5bigip_gtm_server_virtual_server:
    f5bigip_hostname: 172.16.227.35
    f5bigip_username: admin
    f5bigip_password: admin
    f5bigip_port: 443
    name: my_vs
    partition: Common
    destination: '10.10.1.200:80'
    server: my_server
    state: present
  delegate_to: localhost

- name: Delete GTM Server VS
  f5bigip_gtm_server_virtual_server:
    f5bigip_hostname: 172.16.227.35
    f5bigip_username: admin
    f5bigip_password: admin
    f5bigip_port: 443
    name: my_vs
    partition: Common
    state: absent
  delegate_to: localhost
'''

from ansible_common_f5bigip.f5bigip import *

BIGIP_GTM_SERVER_VIRTUAL_SERVER_ARGS = dict(
    #app_service                     =   dict(type='str'),
    depends_on                      =   dict(type='list'),
    description                     =   dict(type='str'),
    destination                     =   dict(type='str'),
    disabled                        =   dict(type='bool'),
    enabled                         =   dict(type='bool'),
    #explicit_link_name              =   dict(type='str'),
    #limit_max_bps                   =   dict(type='int'),
    #limit_max_bps_status            =   dict(type='str', choices=[F5BIGIP_ACTIVATION_CHOICES]),
    #limit_max_connections           =   dict(type='int'),
    #limit_max_connections_status    =   dict(type='str', choices=[F5BIGIP_ACTIVATION_CHOICES]),
    #limit_max_pps                   =   dict(type='int'),
    #limit_max_pps_status            =   dict(type='str', choices=[F5BIGIP_ACTIVATION_CHOICES]),
    #ltm_name                        =   dict(type='str'),
    server                          =   dict(type='str'),
    translation_address             =   dict(type='str'),
    translation_port                =   dict(type='str')
)

class F5BigIpGtmServerVirtualServer(F5BigIpObject):
    def _set_crud_methods(self):
        self.server = self.mgmt.tm.gtm.servers.server.load(
            name=self.params['server'],
            partition=self.params['partition']
        )
        self.methods = {
            'create':self.server.virtual_servers_s.virtual_server.create,
            'read':self.server.virtual_servers_s.virtual_server.load,
            'update':self.server.virtual_servers_s.virtual_server.update,
            'delete':self.server.virtual_servers_s.virtual_server.delete,
            'exists':self.server.virtual_servers_s.virtual_server.exists
        }
        self.params.pop('partition', None)
        self.params.pop('server', None)

    # exists() returns always True...
    def _exists(self):
        exists = False
        
        try:
            vs = self._read()
            
            if hasattr(vs, 'destination'):
                exists = True
        except Exception as exc:
            pass
        
        return exists

    def _read(self):
        """Load an already configured object from the BIG-IP system."""
        self._check_load_params()
        return self.methods['read'](
            name=self.params['name']
        )

def main():
    # Translation list for conflictual params
    tr = {}
    
    module = AnsibleModuleF5BigIpObject(
        argument_spec=BIGIP_GTM_SERVER_VIRTUAL_SERVER_ARGS,
        supports_check_mode=False,
        mutually_exclusive=[
            ['disabled', 'enabled']
        ]
    )
    
    try:
        obj = F5BigIpGtmServerVirtualServer(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()