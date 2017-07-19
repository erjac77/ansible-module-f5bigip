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
module: f5bigip_ltm_auth_ssl_crldp
short_description: BIG-IP ltm auth ssl crldp module
description:
    - Configures a Secure Socket Layer (SSL) Certificate Revocation List Distribution Point (CRLDP) configuration object for implementing SSL CRLDP to manage certificate revocation.
version_added: 2.3
author:
    - "Gabriel Fortin"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    cache_timeout:
        description:
            - Specifies the number of seconds that CRLs are cached.
        required: false
        default: 86400
        choices: []
        aliases: []
        version_added: 2.3
    connection_timeout:
        description:
            - Specifies the number of seconds before the connection times out.
        required: false
        default: 15
        choices: []
        aliases: []
        version_added: 2.3
    description:
        description:
            - User defined description.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    name:
        description:
            - Specifies a unique name for the component.
        required: true
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    partition:
        description:
            - Displays the administrative partition within which the component resides.
        required: false
        default: Common
        choices: []
        aliases: []
        version_added: 2.3
    servers:
        description:
            - Specifies a host name or IP address for the secure CRLDP server.
        required: false
        default: none
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
    update_interval:
        description:
            - Specifies an update interval for CRL distribution points that ensures that CRL status is checked at regular intervals, regardless of the CRL timeout value.
        required: false
        default: 0
        choices: []
        aliases: []
        version_added: 2.3
    use_issuer:
        description:
            - Specifies whether the system extracts the CRL distribution point from the client certificate.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
'''

EXAMPLES = '''
- name: Create LTM AUTH SSL CRLDP
  f5bigip_ltm_auth_ssl_crldp:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_ssl_crldp
    partition: Common
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_LTM_AUTH_SSL_CRLDP_ARGS = dict(
    cache_timeout       =   dict(type='int'),
    connection_timeout  =   dict(type='int'),
    description         =   dict(type='str'),
    servers             =   dict(type='list'),
    update_interval     =   dict(type='int'),
    use_issuer          =   dict(type='str', choices=F5_ACTIVATION_CHOICES)
)

class F5BigIpLtmAuthSslCrldp(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.auth.ssl_crldps.ssl_crldp.create,
            'read':     self.mgmt_root.tm.ltm.auth.ssl_crldps.ssl_crldp.load,
            'update':   self.mgmt_root.tm.ltm.auth.ssl_crldps.ssl_crldp.update,
            'delete':   self.mgmt_root.tm.ltm.auth.ssl_crldps.ssl_crldp.delete,
            'exists':   self.mgmt_root.tm.ltm.auth.ssl_crldps.ssl_crldp.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}
    
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_AUTH_SSL_CRLDP_ARGS, supports_check_mode=False)
    
    try:
        obj = F5BigIpLtmAuthSslCrldp(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()