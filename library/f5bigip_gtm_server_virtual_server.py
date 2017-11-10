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
module: f5bigip_gtm_server_virtual_server
short_description: BIG-IP gtm server virtual-server module
description:
    - Configures a virtual servers.
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
    depends_on:
        description:
            - Specifies the vs-name of the server on which this virtual server depends.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    description:
        description:
            - Specifies a user-defined description.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    destination:
        description:
            - Specifies the IP address and port of the virtual server.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    disabled:
        description:
            - Specifies whether the data center and its resources are available for load balancing.
        required: false
        default: false
        choices: []
        aliases: []
        version_added: 2.3
    enabled:
        description:
            - Specifies whether the data center and its resources are available for load balancing.
        required: false
        default: true
        choices: []
        aliases: []
        version_added: 2.3
    explicit_link_name:
        description:
            - Specifies the explicit link name for the virtual server.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    limit_max_bps:
        description:
            - Specifies the maximum allowable data throughput rate, in bits per second, for this server.
        required: false
        default: 0
        choices: []
        aliases: []
        version_added: 2.3
    limit_max_bps_status:
        description:
            - Enables or disables the limit-max-bps option for this virtual server.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
        aliases: []
        version_added: 2.3
    limit_max_connections:
        description:
            - Specifies the number of current connections allowed for this virtual server.
        required: false
        default: 0
        choices: []
        aliases: []
        version_added: 2.3
    limit_max_connections_status:
        description:
            - Enables or disables the limit-max-connections option for this virtual server.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
        aliases: []
        version_added: 2.3
    limit_max_pps:
        description:
            - Specifies the maximum allowable data transfer rate, in packets per second, for this virtual server.
        required: false
        default: 0
        choices: []
        aliases: []
        version_added: 2.3
    limit_max_pps_status:
        description:
            - Enables or disables the limit-max-pps option for this virtual server.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
        aliases: []
        version_added: 2.3
    ltm_name:
        description:
            - The virtual server name found on the LTM.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    monitor:
        description:
            - Specifies the monitor you want to assign to this virtual server.
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
            - Specifies the administrative partition in which the component object resides.
        required: false
        default: Common
        choices: []
        aliases: []
        version_added: 2.3
    server:
        description:
            - Specifies the server in which the virtual-server belongs.
        required: true
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
    translation_address:
        description:
            - Specifies the public address that this virtual server translates into when the Global Traffic Manager communicates between the network and the Internet.
        required: false
        default: ::
        choices: []
        aliases: []
        version_added: 2.3
    translation_port:
        description:
            - Specifies the translation port number or service name for the virtual server, if necessary.
        required: false
        default: 0
        choices: []
        aliases: []
        version_added: 2.3
'''

EXAMPLES = '''
- name: Create GTM Server VS
  f5bigip_gtm_server_virtual_server:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_vs
    partition: Common
    destination: '10.10.20.201:80'
    server: my_server
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_GTM_SERVER_VIRTUAL_SERVER_ARGS = dict(
    app_service                     =   dict(type='str'),
    depends_on                      =   dict(type='list'),
    description                     =   dict(type='str'),
    destination                     =   dict(type='str'),
    disabled                        =   dict(type='bool'),
    enabled                         =   dict(type='bool'),
    explicit_link_name              =   dict(type='str'),
    limit_max_bps                   =   dict(type='int'),
    limit_max_bps_status            =   dict(type='str', choices=[F5_ACTIVATION_CHOICES]),
    limit_max_connections           =   dict(type='int'),
    limit_max_connections_status    =   dict(type='str', choices=[F5_ACTIVATION_CHOICES]),
    limit_max_pps                   =   dict(type='int'),
    limit_max_pps_status            =   dict(type='str', choices=[F5_ACTIVATION_CHOICES]),
    ltm_name                        =   dict(type='str'),
    monitor                         =   dict(type='str'),
    server                          =   dict(type='str'),
    translation_address             =   dict(type='str'),
    translation_port                =   dict(type='str')
)

class F5BigIpGtmServerVirtualServer(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.server = self.mgmt_root.tm.gtm.servers.server.load(
            name=self.params['server'],
            partition=self.params['partition']
        )
        self.methods = {
            'create':   self.server.virtual_servers_s.virtual_server.create,
            'read':     self.server.virtual_servers_s.virtual_server.load,
            'update':   self.server.virtual_servers_s.virtual_server.update,
            'delete':   self.server.virtual_servers_s.virtual_server.delete,
            'exists':   self.server.virtual_servers_s.virtual_server.exists
        }
        self.params.pop('partition', None)
        self.params.pop('server', None)

    def _exists(self):
        keys = self.server.virtual_servers_s.get_collection()
        for key in keys:
            name = self.params['name']
            if key.name == name:
                return True

        return False

    def _read(self):
        self._check_load_params()
        return self.methods['read'](
            name=self.params['name']
        )

def main():
    # Translation list for conflictual params
    tr = {}
    
    module = AnsibleModuleF5BigIpNamedObject(
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