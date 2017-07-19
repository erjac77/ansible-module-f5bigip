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
module: f5bigip_ltm_auth_ocsp_responder
short_description: BIG-IP ltm auth ocsp responder
description:
    - Configures Online Certificate System Protocol (OCSP) responder objects.
version_added: 2.3
author:
    - "Gabriel Fortin"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    allow_certs:
        description:
            - Enables or disables the addition of certificates to an OCSP request.
        required: false
        default: enabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    app_service:
        description:
            - Specifies the application service to which the object belongs.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    ca_file:
        description:
            - Specifies the name of the file containing trusted CA certificates used to verify the signature on the OCSP response.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    ca_path:
        description:
            - Specifies the name of the path containing trusted CA certificates used to verify the signature on the OCSP response.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    cert_id_digest:
        description:
            - Specifies a specific algorithm identifier, either sha1 or md5.
        required: false
        default: sha1
        choices: ['sha1', 'md5']
        aliases: []
        version_added: 2.3
    chain:
        description:
            - Specifies whether the system constructs a chain from certificates in the OCSP response.
        required: false
        default: enabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    check_certs:
        description:
            - Enables or disables verification of an OCSP response certificate.
        required: false
        default: enabled
        choices: ['enabled', 'disabled']
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
    explicit:
        description:
            - Specifies that the Local Traffic Manager explicitly trusts that the OCSP response signer's certificate is authorized for OCSP response signing.
        required: false
        default: enabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    ignore_aia:
        description:
            - Specifies whether the system ignores the URL contained in the certificate's AIA fields, and always uses the URL specified by the responder instead.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    intern:
        description:
            - Specifies whether the system ignores certificates contained in an OCSP response when searching for the signer's certificate.
        required: false
        default: enabled
        choices: ['enabled', 'disabled']
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
    nonce:
        description:
            - Specifies whether the system verifies an OCSP response signature or the nonce values.
        required: false
        default: enabled
        choices: ['enabled', 'disabled']
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
    sign_digest:
        description:
            - Specifies the algorithm for signing the request, using the signing certificate and key.
        required: false
        default: sha1
        choices: []
        aliases: []
        version_added: 2.3
    sign_key:
        description:
            - Specifies the key that the system uses to sign an OCSP request.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    sign_key_pass_phrase:
        description:
            - Specifies the passphrase that the system uses to encrypt the sign key.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    sign_other:
        description:
            - Adds a list of additional certificates to an OCSP request.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    signer:
        description:
            - Specifies a certificate used to sign an OCSP request.
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
    status_age:
        description:
            - Specifies the age of the status of the OCSP responder.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    trust_other:
        description:
            - Instructs the BIG-IP local traffic management system to trust the certificates specified with the verify-other option.
        required: false
        default: 0
        choices: []
        aliases: []
        version_added: 2.3
    url:
        description:
            - Specifies the URL used to contact the OCSP service on the responder.
        required: true
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    va_file:
        description:
            - Specifies the name of the file containing explicitly trusted responder certificates.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    validity_period:
        description:
            - Specifies the number of seconds used to specify an acceptable error range.
        required: false
        default: 300
        choices: []
        aliases: []
        version_added: 2.3
    verify:
        description:
            - Enables or disables verification of an OCSP response signature or the nonce values.
        required: false
        default: enabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    verify_cert:
        description:
            - Specifies that the system makes additional checks to see if the signer's certificate is authorized to provide the necessary status information.
        required: false
        default: enabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    verify_other:
        description:
            - Specifies the name of the file used to search for an OCSP response signing certificate when the certificate has been omitted from the response.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    verify_sig:
        description:
            - Specifies that the system checks the signature on the OCSP response.
        required: false
        default: enabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
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

from ansible_common_f5.f5_bigip import *

BIGIP_LTM_AUTH_OCSP_RESPONDER_ARGS = dict(
    allow_certs             =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    app_service             =   dict(type='str'),
    ca_file                 =   dict(type='str'),
    ca_path                 =   dict(type='str'),
    cert_id_digest          =   dict(type='str', choices=['md5', 'sha1']),
    chain                   =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    check_certs             =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    description             =   dict(type='str'),
    explicit                =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    ignore_aia              =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    intern                  =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    nonce                   =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    sign_digest             =   dict(type='str', choices=['md5', 'sha1']),
    sign_key                =   dict(type='str'),
    sign_key_pass_phrase    =   dict(type='str'),
    sign_other              =   dict(type='list'),
    signer                  =   dict(type='str'),
    status_age              =   dict(type='int'),
    trust_other             =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    url                     =   dict(type='str'),
    va_file                 =   dict(type='str'),
    validity_period         =   dict(type='int'),
    verify                  =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    verify_cert             =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    verify_other            =   dict(type='str'),
    verify_sig              =   dict(type='str', choices=F5_ACTIVATION_CHOICES)
)

class F5BigIpLtmAuthOcspResponder(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.auth.ocsp_responders.ocsp_responder.create,
            'read':     self.mgmt_root.tm.ltm.auth.ocsp_responders.ocsp_responder.load,
            'update':   self.mgmt_root.tm.ltm.auth.ocsp_responders.ocsp_responder.update,
            'delete':   self.mgmt_root.tm.ltm.auth.ocsp_responders.ocsp_responder.delete,
            'exists':   self.mgmt_root.tm.ltm.auth.ocsp_responders.ocsp_responder.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}
    
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_AUTH_OCSP_RESPONDER_ARGS, supports_check_mode=False)
    
    try:
        obj = F5BigIpLtmAuthOcspResponder(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()