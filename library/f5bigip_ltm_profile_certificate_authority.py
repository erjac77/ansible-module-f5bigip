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
module: f5bigip_ltm_profile_certificate_authority
short_description: BIG-IP ltm profile certificate authority module
description:
    - Defines the settings necessary to authenticate the client certificate.
version_added: 2.3
author:
    - "Gabriel Fortin"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    authenticate_depth:
        description:
            - Specifies the authenticate depth.
        required: false
        default: null
        choices: []
        aliases: []
    ca_file:
        description:
            - Specifies the certificate authority file name or, you can use default for the default certificate authority file name.
        required: false
        default: null
        choices: []
        aliases: []
    crl_file:
        description:
            - Specifies the certificate revocation list file name.
        required: false
        default: null
        choices: []
        aliases: []
    default_name:
        description:
            - Specifies the profile that you want to use as the parent profile.
        required: false
        default: null
        choices: []
        aliases: []
    description:
        description:
            - User defined description.
        required: false
        default: null
        choices: []
        aliases: []
    name:
        description:
            - Specifies a unique name for the component.
        required: true
        default: null
        choices: []
        aliases: []
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        required: false
        default: Common
        choices: []
        aliases: []
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        required: false
        default: present
        choices: ['absent', 'present']
        aliases: []
    update_crl:
        description:
            - Automatically updates the CRL file.
        required: false
        default: null
        choices: []
        aliases: []
'''

EXAMPLES = '''
- name: Create LTM Profile Certificate Authority
  f5bigip_ltm_profile_certificate_authority:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_certificate_authority_profile
    partition: Common
    description: My certificate authority profile
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_LTM_PROFILE_CERTIFICATE_AUTHORITY_ARGS = dict(
    authenticate_depth    =    dict(type='str'),
    ca_file               =    dict(type='str'),
    crl_file              =    dict(type='str'),
    default_name          =    dict(type='str'),
    description           =    dict(type='str'),
    update_crl            =    dict(type='str')
)

class F5BigIpLtmProfileCertificateAuthority(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.profile.certificate_authoritys.certificate_authority.create,
            'read':     self.mgmt_root.tm.ltm.profile.certificate_authoritys.certificate_authority.load,
            'update':   self.mgmt_root.tm.ltm.profile.certificate_authoritys.certificate_authority.update,
            'delete':   self.mgmt_root.tm.ltm.profile.certificate_authoritys.certificate_authority.delete,
            'exists':   self.mgmt_root.tm.ltm.profile.certificate_authoritys.certificate_authority.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}

    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_PROFILE_CERTIFICATE_AUTHORITY_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpLtmProfileCertificateAuthority(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()