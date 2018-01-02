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
module: f5bigip_ltm_auth_crldp_server
short_description: BIG-IP ltm auth crldp server
description:
    - Creates a Certificate Revocation List Distribution Point (CRDLP) server for implementing a CRLDP authentication
      module.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    app_service:
        description:
            - Specifies the application service to which the object belongs.
    base_dn:
        description:
            - Specifies the LDAP base directory name for certificates that specify the CRL distribution point in
              directory name format (dirName).
    description:
        description:
            - User defined description.
    host:
        description:
            - Specifies an IP address for the CRLDP server.
        required: true
    name:
        description:
            - Specifies a unique name for the component.
        required: true
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        default: Common
    port:
        description:
            - Specifies the port for CRLDP authentication traffic.
        default: 389
    reverse_dn:
        description:
            - Specifies in which order the system attempts to match the value of the base-dn option to the value of the
              X509v3 attribute crlDistributionPoints.
        default: disabled
        choices: ['enabled', 'disabled']
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
- name: Create LTM AUTH CRLDP Server
  f5bigip_ltm_auth_crldp_server:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_crldp_server
    partition: Common
    host: 10.0.0.4
    port: 389
    state: present
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_LTM_AUTH_CRLDP_SERVER_ARGS = dict(
    app_service=dict(type='str'),
    base_dn=dict(type='str'),
    description=dict(type='str'),
    host=dict(type='str'),
    port=dict(type='int'),
    reverse_dn=dict(type='str', choices=F5_ACTIVATION_CHOICES)
)


class F5BigIpLtmAuthCrldpServer(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create': self.mgmt_root.tm.ltm.auth.crldp_servers.crldp_server.create,
            'read': self.mgmt_root.tm.ltm.auth.crldp_servers.crldp_server.load,
            'update': self.mgmt_root.tm.ltm.auth.crldp_servers.crldp_server.update,
            'delete': self.mgmt_root.tm.ltm.auth.crldp_servers.crldp_server.delete,
            'exists': self.mgmt_root.tm.ltm.auth.crldp_servers.crldp_server.exists
        }


def main():
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_AUTH_CRLDP_SERVER_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpLtmAuthCrldpServer(check_mode=module.supports_check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
