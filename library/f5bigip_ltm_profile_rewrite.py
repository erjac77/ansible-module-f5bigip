#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2016-2018, Eric Jacob <erjac77@gmail.com>
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
module: f5bigip_ltm_profile_rewrite
short_description: BIG-IP ltm profile rewrite module
description:
    - Configures a rewrite profile.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    app_service:
        description:
            - Specifies the name of the application service to which the object belongs.
    bypass_list:
        description:
            - Specifies a list of URIs that are bypassesed inside a web page when the page is accessed using Portal
              Access.
    client_caching_type:
        description:
            - Specifies one of four options for client caching.
        default: cache-css-js
        choices: ['cache-all', 'cache-css-js', 'cache-img-css-js', 'no-cache']
    defaults_from:
        description:
            - Specifies the profile from which the Rewrite profile inherits properties.
    java_ca_file:
        description:
            - Specifies a CA against which to verify signed Java applets signatures.
        default: ca-bundle.crt
    java_crl:
        description:
            - Specifies a CRL against which to verify signed Java applets signature certificates.
    java_sign_key:
        description:
            - Specifies a private key for re-signing of signed Java applets after patching.
        default: default.key
    java_sign_key_passphrase:
        description:
            - Specifies a passphrase for the private key to be encrypted with.
    java_signer:
        description:
            - Specifies a certificate to use for re-signing of signed Java applets after patching.
        default: default
    location_specific:
        description:
            - Specifies whether or not this object contains one or more attributes with values that are specific to the
              location where the BIG-IP device resides.
        default: false
        choices: ['false', 'true']
    rewrite_list:
        description:
            - Specifies a list of URIs that are rewritten inside a web page when the page is accessed using Portal
              Access.
    rewrite_mode:
        description:
            - Specifies the mode of rewriting.
    set_cookie_rules:
        description:
            - Used with uri-translation mode.
    split_tunneling:
        description:
            - Specifies whether the profile provides for split tunneling.
        default: false
        choices: ['false', 'true']
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    uri_rules:
        description:
            - Used with uri-translation mode.
requirements:
    - BIG-IP >= 12.0
    - ansible-common-f5
    - f5-sdk
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

RETURN = ''' # '''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.base import F5_NAMED_OBJ_ARGS
from ansible_common_f5.base import F5_PROVIDER_ARGS
from ansible_common_f5.bigip import F5BigIpNamedObject


class ModuleParams(object):
    @property
    def argument_spec(self):
        argument_spec = dict(
            app_service=dict(type='str'),
            bypass_list=dict(type='list'),
            client_caching_type=dict(type='str', choices=['cache-all', 'cache-css-js', 'cache-img-css-js', 'no-cache']),
            defaults_from=dict(type='str'),
            java_ca_file=dict(type='str'),
            java_crl=dict(type='str'),
            java_sign_key=dict(type='str'),
            java_sign_key_passphrase=dict(type='str', no_log=True),
            java_signer=dict(type='str'),
            location_specific=dict(type='str', choices=['false', 'true']),
            rewrite_list=dict(type='list'),
            rewrite_mode=dict(type='str', chocies=['portal', 'uri-translation']),
            set_cookie_rules=dict(type='list'),
            split_tunneling=dict(type='str', choices=['false', 'true']),
            uri_rules=dict(type='list')
        )
        argument_spec.update(F5_PROVIDER_ARGS)
        argument_spec.update(F5_NAMED_OBJ_ARGS)
        return argument_spec

    @property
    def supports_check_mode(self):
        return True


class F5BigIpLtmProfileRewrite(F5BigIpNamedObject):
    def _set_crud_methods(self):
        self._methods = {
            'create': self._api.tm.ltm.profile.rewrites.rewrite.create,
            'read': self._api.tm.ltm.profile.rewrites.rewrite.load,
            'update': self._api.tm.ltm.profile.rewrites.rewrite.update,
            'delete': self._api.tm.ltm.profile.rewrites.rewrite.delete,
            'exists': self._api.tm.ltm.profile.rewrites.rewrite.exists
        }


def main():
    params = ModuleParams()
    module = AnsibleModule(argument_spec=params.argument_spec, supports_check_mode=params.supports_check_mode)

    try:
        obj = F5BigIpLtmProfileRewrite(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
