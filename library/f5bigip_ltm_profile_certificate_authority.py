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
module: f5bigip_ltm_profile_certificate_authority
short_description: BIG-IP ltm profile certificate authority module
description:
    - Defines the settings necessary to authenticate the client certificate.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    authenticate_depth:
        description:
            - Specifies the authenticate depth.
    ca_file:
        description:
            - Specifies the certificate authority file name or, you can use default for the default certificate authority file name.
    crl_file:
        description:
            - Specifies the certificate revocation list file name.
    default_name:
        description:
            - Specifies the profile that you want to use as the parent profile.
    description:
        description:
            - User defined description.
    name:
        description:
            - Specifies a unique name for the component.
        required: true
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        default: Common
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    update_crl:
        description:
            - Automatically updates the CRL file.
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
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

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
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
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_PROFILE_CERTIFICATE_AUTHORITY_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpLtmProfileCertificateAuthority(check_mode=module.supports_check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

if __name__ == '__main__':
    main()