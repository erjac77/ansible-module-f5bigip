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
module: f5bigip_sys_application_service
short_description: BIG-IP sys application service module
description:
    - Configures traffic management application services.
version_added: "1.0"
author:
    - "Eric Jacob, @erjac77"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    description:
        description:
            - User defined description.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 1.0
    device_group:
        description:
            - Specifies the name of the device group to which the application service is assigned.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 1.0
    execute_action:
        description:
            - Runs the specified template action associated with the service.
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
    strict_updates:
        description:
            - Specifies whether configuration objects contained in the application service can be directly modified outside the context of the system’s application service management interfaces.
        required: false
        default: enabled
        choices: ['enabled', 'disabled']
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
    template:
        description:
            - The template defines the configuration for the application service.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 1.0
    traffic_group:
        description:
            - Adds this folder and its configuration items to an existing traffic group.
        required: false
        default: false
        choices: []
        aliases: []
        version_added: 1.0
'''

EXAMPLES = '''
- name: Create SYS App Service
  f5bigip_sys_application_service:
    f5bigip_hostname: "172.16.227.35"
    f5bigip_username: "admin"
    f5bigip_password: "admin"
    f5bigip_port: "443"
    name: "www.mycompany.com_http_80"
    partition: "Common"
    template: "/Common/f5.http"
    tables:
      - name: basic__snatpool_members
      - name: net__snatpool_members
      - name: optimizations__hosts
      - name: pool__hosts
        columnNames:
        - name
        rows:
        - row:
          - www.mycompany.com
      - name: pool__members
        columnNames:
        - addr
        - port
        - connection_limit
        rows:
        - row:
          - 172.16.227.21
          - '80'
          - '0'
        - row:
          - 172.16.227.22
          - '80'
          - '0'
      - name: server_pools__servers
    variables:
      - name: client__http_compression
        encrypted: 'no'
        value: "/#create_new#"
      - name: monitor__monitor
        encrypted: 'no'
        value: "/#create_new#"
      - name: monitor__response
        encrypted: 'no'
        value: 200 OK
      - name: monitor__uri
        encrypted: 'no'
        value: "/"
      - name: net__client_mode
        encrypted: 'no'
        value: wan
      - name: net__server_mode
        encrypted: 'no'
        value: lan
      - name: pool__addr
        encrypted: 'no'
        value: 172.16.227.201
      - name: pool__pool_to_use
        encrypted: 'no'
        value: "/#create_new#"
      - name: pool__port
        encrypted: 'no'
        value: '80'
      - name: ssl__mode
        encrypted: 'no'
        value: no_ssl
      - name: ssl_encryption_questions__advanced
        encrypted: 'no'
        value: 'no'
      - name: ssl_encryption_questions__help
        encrypted: 'no'
        value: hide
    state: "present"
  delegate_to: localhost
'''

from ansible_common_f5bigip.f5bigip import *

BIGIP_SYS_APPLICATION_SERVICE_ARGS = dict(
    description     =   dict(type='str'),
    device_group    =   dict(type='str'),
    execute_action  =   dict(type='str'),
    lists           =   dict(type='list'),
    #metadata        =   dict(type='list'),
    strict_updates  =   dict(type='str'),
    tables          =   dict(type='list'),
    template        =   dict(type='str'),
    traffic_group   =   dict(type='str'),
    variables       =   dict(type='list')
)

class F5BigIpSysApplicationService(F5BigIpObject):
    def _set_crud_methods(self):
        self.methods = {
            'create':self.mgmt.tm.sys.application.services.service.create,
            'read':self.mgmt.tm.sys.application.services.service.load,
            'update':self.mgmt.tm.sys.application.services.service.update,
            'delete':self.mgmt.tm.sys.application.services.service.delete,
            'exists':self.mgmt.tm.sys.application.services.service.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}
    
    module = AnsibleModuleF5BigIpObject(argument_spec=BIGIP_SYS_APPLICATION_SERVICE_ARGS, supports_check_mode=False)
    
    try:
        obj = F5BigIpSysApplicationService(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()