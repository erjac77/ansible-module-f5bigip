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
module: f5bigip_ltm_profile_rewrite
short_description: BIG-IP ltm profile rewrite module
description:
    - Configures a rewrite profile.
version_added: 2.3
author:
    - "Gabriel Fortin"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    app_service:
        description:
            - Specifies the name of the application service to which the object belongs.
        required: false
        default: none
        choices: []
        aliases: []
    bypass_list:
        description:
            - Specifies a list of URIs that are bypassesed inside a web page when the page is accessed using Portal Access.
        required: false
        default: null
        choices: []
        aliases: []
    client_caching_type:
        description:
            - Specifies one of four options for client caching.
        required: false
        default: cache-css-js
        choices: ['cache-all', 'cache-css-js', 'cache-img-css-js', 'no-cache']
        aliases: []
    defaults_from:
        description:
            - Specifies the profile from which the Rewrite profile inherits properties.
        required: false
        default: null
        choices: []
        aliases: []
    java_ca_file:
        description:
            - Specifies a CA against which to verify signed Java applets signatures.
        required: false
        default: ca-bundle.crt
        choices: []
        aliases: []
    java_crl:
        description:
            - Specifies a CRL against which to verify signed Java applets signature certificates.
        required: false
        default: none
        choices: []
        aliases: []
    java_sign_key:
        description:
            - Specifies a private key for re-signing of signed Java applets after patching.
        required: false
        default: default.key
        choices: []
        aliases: []
    java_sign_key_passphrase:
        description:
            - Specifies a passphrase for the private key to be encrypted with.
        required: false
        default: none
        choices: []
        aliases: []
    java_signer:
        description:
            - Specifies a certificate to use for re-signing of signed Java applets after patching.
        required: false
        default: default
        choices: []
        aliases: []
    location_specific:
        description:
            - Specifies whether or not this object contains one or more attributes with values that are specific to the location where the BIG-IP device resides.
        required: false
        default: false
        choices: ['false', 'true']
        aliases: []
    rewrite_list:
        description:
            - Specifies a list of URIs that are rewritten inside a web page when the page is accessed using Portal Access.
        required: false
        default: none
        choices: []
        aliases: []
    rewrite_mode:
        description:
            - Specifies the mode of rewriting.
        required: false
        default: null
        choices: []
        aliases: []
    set_cookie_rules:
        description:
            - Used with uri-translation mode.
        required: false
        default: null
        choices: []
        aliases: []
    split_tunneling:
        description:
            - Specifies whether the profile provides for split tunneling.
        required: false
        default: false
        choices: ['false', 'true']
        aliases: []
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        required: false
        default: present
        choices: ['absent', 'present']
        aliases: []
    uri_rules:
        description:
            - Used with uri-translation mode.
        required: false
        default: null
        choices: []
        aliases: []
'''

EXAMPLES = '''
- name: Create LTM Profile Rewrite
  f5bigip_ltm_profile_rewrite:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_rewrite_profile
    partition: Common
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_LTM_PROFILE_REWRITE_ARGS = dict(
    app_service                 =    dict(type='str'),
    bypass_list                 =    dict(type='list'),
    client_caching_type         =    dict(type='str', choices=['cache-all', 'cache-css-js', 'cache-img-css-js', 'no-cache']),
    defaults_from               =    dict(type='str'),
    java_ca_file                =    dict(type='str'),
    java_crl                    =    dict(type='str'),
    java_sign_key               =    dict(type='str'),
    java_sign_key_passphrase    =    dict(type='str'),
    java_signer                 =    dict(type='str'),
    location_specific           =    dict(type='str', choices=['false', 'true']),
    rewrite_list                =    dict(type='list'),
    rewrite_mode                =    dict(type='str', chocies=['portal', 'uri-translation']),
    set_cookie_rules            =    dict(type='list'),
    split_tunneling             =    dict(type='str', choices=['false', 'true']),
    uri_rules                   =    dict(type='list')
)

class F5BigIpLtmProfileRewrite(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.profile.rewrites.rewrite.create,
            'read':     self.mgmt_root.tm.ltm.profile.rewrites.rewrite.load,
            'update':   self.mgmt_root.tm.ltm.profile.rewrites.rewrite.update,
            'delete':   self.mgmt_root.tm.ltm.profile.rewrites.rewrite.delete,
            'exists':   self.mgmt_root.tm.ltm.profile.rewrites.rewrite.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}

    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_PROFILE_REWRITE_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpLtmProfileRewrite(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()