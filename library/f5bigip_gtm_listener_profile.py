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
module: f5bigip_gtm_listener_profile
short_description: BIG-IP gtm listener profile module
description:
    - Specifies the DNS, statistics and protocol profiles to use for this listener.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    context:
        description:
            - Specifies that the profile is either a clientside or serverside (or both) profile.
        default: all
        choices: ['all', 'clientside', 'serverside']
    listener:
        description:
            - Specifies the name of the listener to which the profile belongs.
        required: true
        default: Common
    name:
        description:
            - Specifies unique name for the component.
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
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Add GTM Listener Profile
  f5bigip_gtm_listener_profile:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: dns
    partition: Common
    context: all
    listener: /Common/my_listener
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
            context=dict(type='str', choices=['all', 'clientside', 'serverside']),
            listener=dict(type='str')
        )
        argument_spec.update(F5_PROVIDER_ARGS)
        argument_spec.update(F5_NAMED_OBJ_ARGS)
        return argument_spec

    @property
    def supports_check_mode(self):
        return True


class F5BigIpGtmListenerProfile(F5BigIpNamedObject):
    def _set_crud_methods(self):
        listener = self._api.tm.gtm.listeners.listener.load(
            **self._get_resource_id_from_path(self._params['listener']))
        self._methods = {
            'create': listener.profiles_s.profile.create,
            'read': listener.profiles_s.profile.load,
            'update': listener.profiles_s.profile.update,
            'delete': listener.profiles_s.profile.delete,
            'exists': listener.profiles_s.profile.exists
        }
        del self._params['listener']


def main():
    params = ModuleParams()
    module = AnsibleModule(argument_spec=params.argument_spec, supports_check_mode=params.supports_check_mode)

    try:
        obj = F5BigIpGtmListenerProfile(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
