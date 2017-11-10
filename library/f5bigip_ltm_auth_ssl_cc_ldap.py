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
module: f5bigip_ltm_auth_ssl_cc_ldap
short_description: BIG-IP ltm auth ssl cc ldap module
description:
    - Configure the ssl-cc-ldap component within the ltm auth module using the syntax shown in the following sections.
version_added: 2.3
author:
    - "Gabriel Fortin"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    admin_dn:
        description:
            - Specifies the distinguished name of an account to which to bind to perform searches.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    admin_password:
        description:
            - Specifies the password for the admin account.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    cache_size:
        description:
            - Specifies the maximum size, in bytes, allowed for the SSL session cache.
        required: false
        default: 20000
        choices: []
        aliases: []
        version_added: 2.3
    cache_timeout:
        description:
            - Specifies the number of usable lifetime seconds of negotiable SSL session IDs.
        required: false
        default: 300
        choices: []
        aliases: []
        version_added: 2.3
    certmap_base:
        description:
            - Specifies the search base for the subtree used by the certmap search method.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    certmap_key:
        description:
            - Specifies the name of the certificate map that the certmap search method uses.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    certmap_user_serial:
        description:
            - Specifies whether the system uses the client certificate's subject or serial number (in conjunction with the certificate's issuer) when trying to match an entry in the certificate map subtree.
        required: false
        default: no
        choices: ['yes', 'no']
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
    group_base:
        description:
            - Specifies the search base for the subtree used by group searches.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    group_key:
        description:
            - Specifies the name of the attribute in the LDAP database that specifies the group name in the group subtree.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    group_member_key:
        description:
            - Specifies the name of the attribute in the LDAP database that specifies members (DNs) of a group.
        required: false
        default: none
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
    role_key:
        description:
            - Specifies the name of the attribute in the LDAP database that specifies a user's authorization roles.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    search_type:
        description:
            - Specifies the type of LDAP search that is performed based on the client's certificate.
        required: false
        default: user
        choices: ['cert', 'certmap', 'user']
        aliases: []
        version_added: 2.3
    secure:
        description:
            - Specifies whether the system attempts to use secure LDAP.
        required: false
        default: no
        choices: ['yes', 'no']
        aliases: []
        version_added: 2.3
    servers:
        description:
            - Specifies a list of LDAP servers you want to search.
        required: false
        default: null
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
    user_base:
        description:
            - Specifies the search base for the subtree used when you select for the search option either of the values user or cert.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    user_class:
        description:
            - Specifies the object class in the LDAP database to which the user must belong to be authenticated.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    user_key:
        description:
            - Specifies the key that denotes a user ID in the LDAP database.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    valid_groups:
        description:
            - Specifies a space-delimited list of the names of groups to which the client must belong in order to be authorized
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    valid_roles:
        description:
            - Specifies a space-delimited list of the valid roles that clients must have to be authorized.
        required: true
        default: none
        choices: []
        aliases: []
        version_added: 2.3
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

from ansible_common_f5.f5_bigip import *

BIGIP_LTM_AUTH_SSL_CC_LDAP_ARGS = dict(
    admin_dn                =   dict(type='str'),
    admin_password          =   dict(type='str'),
    cache_size              =   dict(type='int'),
    cache_timeout           =   dict(type='int'),
    certmap_base            =   dict(type='str'),
    certmap_key             =   dict(type='str'),
    certmap_user_serial     =   dict(type='str', choices=['yes', 'no']),
    description             =   dict(type='str'),
    group_base              =   dict(type='str'),
    group_key               =   dict(type='str'),
    group_member_key        =   dict(type='str'),
    role_key                =   dict(type='str'),
    search_type             =   dict(type='str', choices=['cert', 'certmap', 'user']),
    secure                  =   dict(type='str', choices=['yes', 'no']),
    servers                 =   dict(type='list'),
    user_base               =   dict(type='str'),
    user_class              =   dict(type='str'),
    user_key                =   dict(type='str'),
    valid_groups            =   dict(type='list'),
    valid_roles             =   dict(type='list')
)

class F5BigIpLtmAuthSslCcLdap(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.auth.ssl_cc_ldaps.ssl_cc_ldap.create,
            'read':     self.mgmt_root.tm.ltm.auth.ssl_cc_ldaps.ssl_cc_ldap.load,
            'update':   self.mgmt_root.tm.ltm.auth.ssl_cc_ldaps.ssl_cc_ldap.update,
            'delete':   self.mgmt_root.tm.ltm.auth.ssl_cc_ldaps.ssl_cc_ldap.delete,
            'exists':   self.mgmt_root.tm.ltm.auth.ssl_cc_ldaps.ssl_cc_ldap.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}
    
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_AUTH_SSL_CC_LDAP_ARGS, supports_check_mode=False)
    
    try:
        obj = F5BigIpLtmAuthSslCcLdap(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()