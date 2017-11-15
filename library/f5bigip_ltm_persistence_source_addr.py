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
module: f5bigip_ltm_persistence_source_addr
short_description: BIG-IP ltm persistence source address module
description:
    - Configures a source address affinity persistence profile.
version_added: "2.4"
author:
    - "Eric Jacob (@erjac77)"
options:
    app_service:
        description:
            - Specifies the application service to which the object belongs.
    defaults_from:
        description:
            - Specifies the existing profile from which the system imports settings for the new profile.
        default: source_addr
    description:
        description:
            - Specifies descriptive text that identifies the component.
    hash_algorithm:
        description:
            - Specifies the system uses hash persistence load balancing.
        default: default
        choices: ['carp', 'default']
    map_proxies:
        description:
            - Enables or disables the map proxies attribute.
        default: disabled
        choices: ['enabled', 'disabled']
    map_proxy_address:
        description:
            - Specifies the single IP address to use when the source address matches the proxy data-group/class.
        default: any
    map_proxy_class:
        description:
            - Specifies the data-group/class to use for determining whether a source address is from a proxy.
    mask:
        description:
            - Specifies an IP mask.
        default: ::
    match_across_pools:
        description:
            - Specifies, when enabled, that the system can use any pool that contains this persistence record.
        default: disabled
        choices: ['enabled', 'disabled']
    match_across_services:
        description:
            - Specifies, when enabled, that all persistent connections from a client IP address, which go to the same virtual IP address, also go to the same node.
        default: disabled
        choices: ['enabled', 'disabled']
    match_across_virtuals:
        description:
            - Specifies, when enabled, that all persistent connections from the same client IP address go to the same node.
        default: disabled
        choices: ['enabled', 'disabled']
    mirror:
        description:
            - Specifies whether the system mirrors persistence records to the high-availability peer.
        default: disabled
        choices: ['enabled', 'disabled']
    name:
        description:
            - Specifies a unique name for the component.
        required: true
    override_connection_limit:
        description:
            - Specifies, when enabled, that the pool member connection limits are not enforced for persisted clients.
        default: disabled
        choices: ['enabled', 'disabled']
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        default: Common
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    timeout:
        description:
            - Specifies the duration of the persistence entries.
        default: 180
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Create LTM Source Address Persistence profile
  f5bigip_ltm_persistence_source_addr:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_source_addr_persistence
    partition: Common
    description: My source address persistence profile
    defaults_from: /Common/source_addr
    state: present
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_LTM_PERSISTENCE_SOURCE_ADDR_ARGS = dict(
    app_service                 =   dict(type='str'),
    defaults_from               =   dict(type='str'),
    description                 =   dict(type='str'),
    hash_algorithm              =   dict(type='str', choices=['carp', 'default']),
    map_proxies                 =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    mask                        =   dict(type='str'),
    map_proxy_address           =   dict(type='str'),
    map_proxy_class             =   dict(type='str'),
    match_across_pools          =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    match_across_services       =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    match_across_virtuals       =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    mirror                      =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    override_connection_limit   =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    timeout                     =   dict(type='int')
)

class F5BigIpLtmPersistenceSourceAddr(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.persistence.source_addrs.source_addr.create,
            'read':     self.mgmt_root.tm.ltm.persistence.source_addrs.source_addr.load,
            'update':   self.mgmt_root.tm.ltm.persistence.source_addrs.source_addr.update,
            'delete':   self.mgmt_root.tm.ltm.persistence.source_addrs.source_addr.delete,
            'exists':   self.mgmt_root.tm.ltm.persistence.source_addrs.source_addr.exists
        }

def main():
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_PERSISTENCE_SOURCE_ADDR_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpLtmPersistenceSourceAddr(check_mode=module.supports_check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

if __name__ == '__main__':
    main()