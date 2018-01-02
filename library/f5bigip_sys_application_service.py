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
module: f5bigip_sys_application_service
short_description: BIG-IP sys application service module
description:
    - Configures traffic management application services.
version_added: "2.4"
author:
    - "Eric Jacob (@erjac77)"
options:
    description:
        description:
            - User defined description.
    device_group:
        description:
            - Specifies the name of the device group to which the application service is assigned.
    execute_action:
        description:
            - Runs the specified template action associated with the service.
    lists:
        description:
            - Provides the set of list variables and values that are passed to template scripts.
    name:
        description:
            - Specifies unique name for the component.
        required: true
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    strict_updates:
        description:
            - Specifies whether configuration objects contained in the application service can be directly modified
              outside the context of the system's application service management interfaces.
        default: enabled
        choices: ['enabled', 'disabled']
    tables:
        description:
            - Provides the set of table variables and values that are passed to template scripts.
    template:
        description:
            - The template defines the configuration for the application service.
    traffic_group:
        description:
            - Adds this folder and its configuration items to an existing traffic group.
        default: false
    variables:
        description:
            - The set of atomic variables and values that are passed to template scripts.
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Create SYS App Service
  f5bigip_sys_application_service:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: www.mycompany.com_http_80
    partition: Common
    template: /Common/f5.http
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
          - 10.10.10.21
          - '80'
          - '0'
        - row:
          - 10.10.10.22
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
        value: 10.10.20.201
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
    state: present
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_SYS_APPLICATION_SERVICE_ARGS = dict(
    description=dict(type='str'),
    device_group=dict(type='str'),
    execute_action=dict(type='str'),
    lists=dict(type='list'),
    # metadata=dict(type='list'),
    strict_updates=dict(type='str', choices=F5_ACTIVATION_CHOICES),
    tables=dict(type='list'),
    template=dict(type='str'),
    traffic_group=dict(type='str'),
    variables=dict(type='list')
)


class F5BigIpSysApplicationService(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create': self.mgmt_root.tm.sys.application.services.service.create,
            'read': self.mgmt_root.tm.sys.application.services.service.load,
            'update': self.mgmt_root.tm.sys.application.services.service.update,
            'delete': self.mgmt_root.tm.sys.application.services.service.delete,
            'exists': self.mgmt_root.tm.sys.application.services.service.exists
        }


def main():
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_SYS_APPLICATION_SERVICE_ARGS,
                                             supports_check_mode=False)

    try:
        obj = F5BigIpSysApplicationService(check_mode=module.supports_check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
