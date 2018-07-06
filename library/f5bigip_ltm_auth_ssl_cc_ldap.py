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
module: f5bigip_ltm_auth_ssl_cc_ldap
short_description: BIG-IP ltm auth ssl cc ldap module
description:
    - Configure the ssl-cc-ldap component within the ltm auth module using the syntax shown in the following sections.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    admin_dn:
        description:
            - Specifies the distinguished name of an account to which to bind to perform searches.
    admin_password:
        description:
            - Specifies the password for the admin account.
    cache_size:
        description:
            - Specifies the maximum size, in bytes, allowed for the SSL session cache.
        default: 20000
    cache_timeout:
        description:
            - Specifies the number of usable lifetime seconds of negotiable SSL session IDs.
        default: 300
    certmap_base:
        description:
            - Specifies the search base for the subtree used by the certmap search method.
    certmap_key:
        description:
            - Specifies the name of the certificate map that the certmap search method uses.
    certmap_user_serial:
        description:
            - Specifies whether the system uses the client certificate's subject or serial number (in conjunction with
              the certificate's issuer) when trying to match an entry in the certificate map subtree.
        default: no
        choices: ['yes', 'no']
    description:
        description:
            - User defined description.
    group_base:
        description:
            - Specifies the search base for the subtree used by group searches.
    group_key:
        description:
            - Specifies the name of the attribute in the LDAP database that specifies the group name in the group
              subtree.
    group_member_key:
        description:
            - Specifies the name of the attribute in the LDAP database that specifies members (DNs) of a group.
    name:
        description:
            - Specifies a unique name for the component.
        required: true
    partition:
        description:
            - Displays the administrative partition within which the component resides.
        default: Common
    role_key:
        description:
            - Specifies the name of the attribute in the LDAP database that specifies a user's authorization roles.
    search_type:
        description:
            - Specifies the type of LDAP search that is performed based on the client's certificate.
        default: user
        choices: ['cert', 'certmap', 'user']
    secure:
        description:
            - Specifies whether the system attempts to use secure LDAP.
        default: no
        choices: ['yes', 'no']
    servers:
        description:
            - Specifies a list of LDAP servers you want to search.
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    user_base:
        description:
            - Specifies the search base for the subtree used when you select for the search option either of the values
              user or cert.
    user_class:
        description:
            - Specifies the object class in the LDAP database to which the user must belong to be authenticated.
    user_key:
        description:
            - Specifies the key that denotes a user ID in the LDAP database.
    valid_groups:
        description:
            - Specifies a space-delimited list of the names of groups to which the client must belong in order to be
              authorized.
    valid_roles:
        description:
            - Specifies a space-delimited list of the valid roles that clients must have to be authorized.
        required: true
requirements:
    - BIG-IP >= 12.0
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Create LTM AUTH SSL CC LDAP
  f5bigip_ltm_auth_ssl_cc_ldap:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_ssl_cc_ldap
    partition: Common
    servers:
      - localhost
    user_key: Key
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
            admin_dn=dict(type='str'),
            admin_password=dict(type='str', no_log=True),
            cache_size=dict(type='int'),
            cache_timeout=dict(type='int'),
            certmap_base=dict(type='str'),
            certmap_key=dict(type='str'),
            certmap_user_serial=dict(type='str', choices=['yes', 'no']),
            description=dict(type='str'),
            group_base=dict(type='str'),
            group_key=dict(type='str'),
            group_member_key=dict(type='str'),
            role_key=dict(type='str'),
            search_type=dict(type='str', choices=['cert', 'certmap', 'user']),
            secure=dict(type='str', choices=['yes', 'no']),
            servers=dict(type='list'),
            user_base=dict(type='str'),
            user_class=dict(type='str'),
            user_key=dict(type='str'),
            valid_groups=dict(type='list'),
            valid_roles=dict(type='list')
        )
        argument_spec.update(F5_PROVIDER_ARGS)
        argument_spec.update(F5_NAMED_OBJ_ARGS)
        return argument_spec

    @property
    def supports_check_mode(self):
        return True


class F5BigIpLtmAuthSslCcLdap(F5BigIpNamedObject):
    def _set_crud_methods(self):
        self._methods = {
            'create': self._api.tm.ltm.auth.ssl_cc_ldaps.ssl_cc_ldap.create,
            'read': self._api.tm.ltm.auth.ssl_cc_ldaps.ssl_cc_ldap.load,
            'update': self._api.tm.ltm.auth.ssl_cc_ldaps.ssl_cc_ldap.update,
            'delete': self._api.tm.ltm.auth.ssl_cc_ldaps.ssl_cc_ldap.delete,
            'exists': self._api.tm.ltm.auth.ssl_cc_ldaps.ssl_cc_ldap.exists
        }


def main():
    params = ModuleParams()
    module = AnsibleModule(argument_spec=params.argument_spec, supports_check_mode=params.supports_check_mode)

    try:
        obj = F5BigIpLtmAuthSslCcLdap(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
