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
module: f5bigip_sys_crypto_cert
short_description: BIG-IP sys crypto cert module
description:
    - Manage cryptographic certificates on the BIG-IP system.
version_added: "2.4"
author:
    - "Eric Jacob (@erjac77)"
options:
    city:
        description:
            - Specifies the x509 city field to be used in creation of the certificate associated with the given key.
    command:
        description:
            - Specifies the command to execute.
        choices: ['install']
    common_name:
        description:
            - Specifies the x509 common-name to be used in creation of the certificate associated with the given key.
    consumer:
        description:
            - Specifies the system component by which a key and/or associated cryptographic file will be consumed.
        default: ltm
        choices: ['enterprise-manager', 'iquery', 'iquery-big3d', 'ltm', 'webserver']
    country:
        description:
            - Specifies the x509 country to be used in creation of the certificate associated with the given key.
    email_address:
        description:
            - Specifies the x509 email-address to be used in creation of the certificate associated with the given key.
    from_editor:
        description:
            - Specifies that the key should be obtained from a text editor session.
    from_local_file:
        description:
            - Specifies a local file path from which a key is to be copied.
    from_url:
        description:
            - Specifies a URI which is to be used to obtain a key for import into the configuration of the system.
    key:
        description:
            - Specifies a key from which a certificate should be generated when using the create command.
        required: true
    lifetime:
        description:
            - Specifies the certificate life time to be used in creation of the certificate associated with the given
              key.
        default: 365
    organization:
        description:
            - Specifies the x509 organization to be used in creation of the certificate associated with the given key.
    ou:
        description:
            - Specifies the x509 organizational unit to be used in creation of the certificate associated with the given
              key.
    name:
        description:
            - Specifies unique name for the component.
        required: true
    no_overwrite:
        description:
            - Specifies option of not overwriting a key if it is in the scope.
        default: true
        choices: [true, false]
    partition:
        description:
            - Displays the administrative partition in which the component object resides.
        default: Common
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    state_province:
        description:
            - Specifies the x509 state or province of the certificate associated with the given key.
    subject_alternative_name:
        description:
            - Specifies standard X.509 extensions as shown in RFC 2459.
requirements:
    - BIG-IP >= 12.0
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Install SYS Crypto Cert from local file
  f5bigip_sys_crypto_cert:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: exemple.localhost.crt
    partition: Common
    from_local_file: /tmp/exemple.localhost.crt
    state: present
  delegate_to: localhost

- name: Create SYS Crypto Cert
  f5bigip_sys_crypto_cert:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: exemple.localhost.crt
    partition: Common
    key: exemple.localhost.key
    common_name: exemple.localhost
    city: city
    state_province: state
    country: US
    email_address: 'admin@localhost'
    organization: My Org
    ou: My Div
    state: present
  delegate_to: localhost
'''

RETURN = ''' # '''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.base import AnsibleF5Error
from ansible_common_f5.base import F5_NAMED_OBJ_ARGS
from ansible_common_f5.base import F5_PROVIDER_ARGS
from ansible_common_f5.bigip import F5BigIpNamedObject


class ModuleParams(object):
    @property
    def argument_spec(self):
        argument_spec = dict(
            consumer=dict(type='str', choices=['enterprise-manager', 'iquery', 'iquery-big3d', 'ltm', 'webserver']),
            # create
            city=dict(type='str'),
            common_name=dict(type='str'),
            country=dict(type='str'),
            email_address=dict(type='str'),
            key=dict(type='str'),
            lifetime=dict(type='int'),
            organization=dict(type='str'),
            ou=dict(type='str'),
            state_province=dict(type='str'),
            subject_alternative_name=dict(type='str'),
            # install
            command=dict(type='str', choices=['install']),
            from_editor=dict(type='str'),
            from_local_file=dict(type='str'),
            from_url=dict(type='str'),
            no_overwrite=dict(type='bool')
        )
        argument_spec.update(F5_PROVIDER_ARGS)
        argument_spec.update(F5_NAMED_OBJ_ARGS)
        return argument_spec

    @property
    def supports_check_mode(self):
        return True

    @property
    def mutually_exclusive(self):
        return [
            ['from_editor', 'from_local_file', 'from_url']
        ]

    @property
    def tr(self):
        # Translation dict for conflictual params
        return {'state_province': 'state'}


class F5BigIpSysCryptoCert(F5BigIpNamedObject):
    def _set_crud_methods(self):
        self._methods = {
            'create': self._api.tm.sys.crypto.certs.cert.create,
            'read': self._api.tm.sys.crypto.certs.cert.load,
            'update': self._api.tm.sys.crypto.certs.cert.update,
            'delete': self._api.tm.sys.crypto.certs.cert.delete,
            'exists': self._api.tm.sys.crypto.certs.cert.exists,
            'exec_cmd': self._api.tm.sys.crypto.certs.exec_cmd
        }

    def _install(self):
        """Upload the key on the BIG-IP system."""
        name = self._params['name']
        param_set = {}

        if self._params['fromEditor']:
            param_set = {'from-editor': self._params['fromEditor']}
        if self._params['fromLocalFile']:
            param_set = {'from-local-file': self._params['fromLocalFile']}
        if self._params['fromUrl']:
            param_set = {'from-url': self._params['fromUrl']}

        if param_set:
            param_set.update({'name': name})
            if self._params['consumer']:
                param_set.update({'consumer': self._params['consumer']})
            if self._params['noOverwrite']:
                param_set.update({'no-overwrite': self._params['noOverwrite']})

            # Install the key
            self._methods['exec_cmd']('install', **param_set)
        else:
            raise AnsibleF5Error("Missing required parameter 'from-*' to install the cert.")

        # Make sure it is installed
        if not self._exists():
            raise AnsibleF5Error("Failed to create the object.")

        return True

    def _present(self):
        has_changed = False

        if self._params['command'] == 'install':
            if not self._exists() or (self._params['noOverwrite'] is not None and self._params['noOverwrite'] is False):
                has_changed = self._install()
        else:
            if not self._exists():
                has_changed = self._create()

        return has_changed


def main():
    params = ModuleParams()
    module = AnsibleModule(argument_spec=params.argument_spec, supports_check_mode=params.supports_check_mode,
                           mutually_exclusive=params.mutually_exclusive)

    try:
        obj = F5BigIpSysCryptoCert(check_mode=module.check_mode, tr=params.tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
