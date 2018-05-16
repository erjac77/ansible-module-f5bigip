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
module: f5bigip_ltm_persistence_hash
short_description: BIG-IP ltm persistence hash module
description:
    - You can use the hash component to configure a hash persistence profile for the BIG-IP system.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    app_service:
        description:
            - Specifies the application service to which the object belongs.
    defaults_from:
        description:
            - Specifies the existing profile from which the system imports settings for the new profile.
        default: hash
    description:
        description:
            - Specifies descriptive text that identifies the component.
    hash_algorithm:
        description:
            - Specifies the system uses hash persistence load balancing.
        default: default
        choices: ['carp', 'default']
    hash_buffer_limit:
        description:
            - Specifies the maximum buffer length the system collects to locate the hashing pattern for hash persistence
              load balancing.
        default: 0
    hash_end_pattern:
        description:
            - Specifies the string that describes the ending location of the hash pattern that the system uses to
              perform hash persistence load balancing.
    hash_length:
        description:
            - Specifies the length of data within the packet in bytes that the system uses to calculate the hash value
              when performing hash persistence load balancing.
        default: 0
    hash_offset:
        description:
            - Specifies the start offset within the packet from which the system begins the hash when performing hash
              persistence load balancing.
        default: 0
    hash_start_pattern:
        description:
            - Specifies the string that describes the start location of the hash pattern that the system uses to perform
              hash persistence load balancing.
    match_across_pools:
        description:
            - Specifies, when enabled, that the system can use any pool that contains this persistence record.
        default: disabled
        choices: ['enabled', 'disabled']
    match_across_services:
        description:
            - Specifies, when enabled, that all persistent connections from a client IP address, which go to the same
              virtual IP address, also go to the same node.
        default: disabled
        choices: ['enabled', 'disabled']
    match_across_virtuals:
        description:
            - Specifies, when enabled, that all persistent connections from the same client IP address go to the same
              node.
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
    rule:
        description:
            - Specifies a rule name, if you are using a rule for universal persistence.
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
- name: Create LTM Hash Persistence profile
  f5bigip_ltm_persistence_hash:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_hash_persistence
    partition: Common
    description: My hash persistence profile
    defaults_from: hash
    state: present
  delegate_to: localhost
'''

RETURN = ''' # '''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.base import F5_ACTIVATION_CHOICES
from ansible_common_f5.base import F5_NAMED_OBJ_ARGS
from ansible_common_f5.base import F5_PROVIDER_ARGS
from ansible_common_f5.bigip import F5BigIpNamedObject


class ModuleParams(object):
    @property
    def argument_spec(self):
        argument_spec = dict(
            app_service=dict(type='str'),
            defaults_from=dict(type='str'),
            description=dict(type='str'),
            hash_algorithm=dict(type='str', choices=['carp', 'default']),
            hash_buffer_limit=dict(type='int'),
            hash_end_pattern=dict(type='str'),
            hash_length=dict(type='int'),
            hash_offset=dict(type='int'),
            hash_start_pattern=dict(type='str'),
            match_across_pools=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            match_across_services=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            match_across_virtuals=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            mirror=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            override_connection_limit=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            rule=dict(type='str'),
            timeout=dict(type='int')
        )
        argument_spec.update(F5_PROVIDER_ARGS)
        argument_spec.update(F5_NAMED_OBJ_ARGS)
        return argument_spec

    @property
    def supports_check_mode(self):
        return True


class F5BigIpLtmPersistenceHash(F5BigIpNamedObject):
    def _set_crud_methods(self):
        self._methods = {
            'create': self._api.tm.ltm.persistence.hashs.hash.create,
            'read': self._api.tm.ltm.persistence.hashs.hash.load,
            'update': self._api.tm.ltm.persistence.hashs.hash.update,
            'delete': self._api.tm.ltm.persistence.hashs.hash.delete,
            'exists': self._api.tm.ltm.persistence.hashs.hash.exists
        }


def main():
    params = ModuleParams()
    module = AnsibleModule(argument_spec=params.argument_spec, supports_check_mode=params.supports_check_mode)

    try:
        obj = F5BigIpLtmPersistenceHash(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
