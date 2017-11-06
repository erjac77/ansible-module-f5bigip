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
module: f5bigip_ltm_snat_translation
short_description: BIG-IP ltm snat-translation module
description:
    - Explicitly defines the properties of a SNAT translation address.
version_added: 2.3
author:
    - "Gabriel Fortin"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    address:
        description:
            - The translation IP address.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    arp:
        description:
            - Indicates whether the system responds to ARP requests or sends gratuitous ARPs.
        required: false
        default: enabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    app_service:
        description:
            - Specifies the name of the application service to which this object belongs.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    connection_limit:
        description:
            - Specifies the number of connections a translation address must reach before it no longer initiates a connection.
        required: false
        default: 0
        choices: []
        aliases: []
        version_added: 2.3
    description:
        description:
            - User-defined description.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    disabled:
        description:
            - Disables SNAT translation.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    enabled:
        description:
            - Enables SNAT translation.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    ip_idle_timeout:
        description:
            - Specifies the number of seconds that IP connections initiated using a SNAT address are allowed to remain idle before being automatically disconnected.
        required: false
        default: indefinite
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
   tcp_idle_timeout:
        description:
            - Specifies the number of seconds that TCP connections initiated using a SNAT address are allowed to remain idle before being automatically disconnected.
        required: false
        default: indefinite
        choices: []
        aliases: []
        version_added: 2.3
    traffic_group:
        description:
            - Specifies the traffic group of the failover device group on which the SNAT is active.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    udp_idle_timeout:
        description:
            - Specifies the number of seconds that UDP connections initiated using a SNAT address are allowed to remain idle before being automatically disconnected.
        required: false
        default: indefinite
        choices: []
        aliases: []
        version_added: 2.3
'''

EXAMPLES = '''
- name: Create LTM Snat translation
  f5bigip_ltm_snat_translation:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_snat_translation
    partition: Common
    description: My snat translation
    address: 10.0.1.4
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_LTM_SNAT_TRANSLATION_ARGS = dict(
    address             =   dict(type='str'),
    arp                 =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    app_service         =   dict(type='str'),
    connection_limit    =   dict(type='int'),
    description         =   dict(type='str'),
    disabled            =   dict(type='bool'),
    enabled             =   dict(type='bool'),
    ip_idle_timeout     =   dict(type='int'),
    tcp_idle_timeout    =   dict(type='int'),
    traffic_group       =   dict(type='str'),
    udp_idle_timeout    =   dict(type='int')
)

class F5BigIpLtmSnatTranslation(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.snat_translations.snat_translation.create,
            'read':     self.mgmt_root.tm.ltm.snat_translations.snat_translation.load,
            'update':   self.mgmt_root.tm.ltm.snat_translations.snat_translation.update,
            'delete':   self.mgmt_root.tm.ltm.snat_translations.snat_translation.delete,
            'exists':   self.mgmt_root.tm.ltm.snat_translations.snat_translation.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}
    
    module = AnsibleModuleF5BigIpNamedObject(
        argument_spec=BIGIP_LTM_SNAT_TRANSLATION_ARGS,
        supports_check_mode=False,
        mutually_exclusive=[
            ['disabled', 'enabled']
        ]
    )
    
    try:
        obj = F5BigIpLtmSnatTranslation(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()