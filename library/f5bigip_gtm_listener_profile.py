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
module: f5bigip_gtm_listener_profile
short_description: BIG-IP gtm listener profile module
description:
    - Specifies the DNS, statistics and protocol profiles to use for this listener.
version_added: 2.3
author:
    - "Gabriel Fortin"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    context:
        description:
            - Specifies that the profile is either a clientside or serverside (or both) profile.
        required: false
        default: all
        choices: ['all', 'clientside', 'serverside']
        aliases: []
        version_added: 2.3
    listener:
        description:
            - Specifies the name of the listener to which the profile belongs.
        required: true
        default: Common
        choices: []
        aliases: []
        version_added: 2.3
    name:
        description:
            - Specifies unique name for the component.
        required: true
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        required: false
        default: Common
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
    listener: my_listener
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_GTM_LISTENER_PROFILE_ARGS = dict(
    context          =   dict(type='str', choices=['all', 'clientside', 'serverside']),
    listener         =   dict(type='str')
)

class F5BigIpGtmListenerProfile(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.listener = self.mgmt_root.tm.gtm.listeners.listener.load(**self._get_resource_id_from_path(self.params['listener']))
        self.methods = {
            'create':   self.listener.profiles_s.profile.create,
            'read':     self.listener.profiles_s.profile.load,
            'update':   self.listener.profiles_s.profile.update,
            'delete':   self.listener.profiles_s.profile.delete,
            'exists':   self.listener.profiles_s.profile.exists
        }
        self.params.pop('listener', None)

    def _exists(self):
        keys = self.listener.profiles_s.get_collection()
        for key in keys:
            name = self.params['name']
            if key.name == name:
                return True

        return False

def main():
    # Translation list for conflictual params
    tr = {}

    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_GTM_LISTENER_PROFILE_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpGtmListenerProfile(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()