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

DOCUMENTATION = '''
---
module: f5bigip_ltm_profile_diameter
short_description: BIG-IP ltm profile diameter module
description:
    - Configures a profile to manage Diameter network traffic.
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
            - Specifies the name of the application service to which the profile belongs.
        required: false
        default: none
        choices: []
        aliases: []
    connection_prime:
        description:
            - When enabled, and the system receives a capabilities exchange request from the client, the system will establish connections and perform handshaking with all the servers prior to sending the capabilities exchange answer to the client.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
        aliases: []
    defaults_from:
        description:
            - Specifies the profile that you want to use as the parent profile.
        required: false
        default: diameter
        choices: []
        aliases: []
    description:
        description:
            - User defined description.
        required: false
        default: null
        choices: []
        aliases: []
    destination_realm:
        description:
            - This attribute has been deprecated as of BIG-IP v11.
        required: false
        default: null
        choices: []
        aliases: []
    handshake_timeout:
        description:
            - Specifies the handshake timeout in seconds.
        required: false
        default: 10
        choices: range(0,4294967296)
        aliases: []
    host_ip_rewrite:
        description:
            - When enabled and the message is a capabilities exchange request or capabilities exchange answer, rewrite the host-ip-address attribute with the system's egress IP address.
        required: false
        default: enabled
        choices: ['disabled', 'enabled']
        aliases: []
    max_retransmit_attempts:
        description:
            - Specifies the maximum number of retransmit attempts.
        required: false
        default: 1
        choices: range(0,4294967296)
        aliases: []
    max_watchdog_failure:
        description:
            - Specifies the maximum number of device watchdog failures that the traffic management system can take before it tears down the connection.
        required: false
        default: 10
        choices: range(0,4294967296)
        aliases: []
    name:
        description:
            - Specifies a unique name for the component.
        required: true
        default: null
        choices: []
        aliases: []
    origin_host_to_client:
        description:
            - Specifies the origin host to client of BIG-IP.
        required: false
        default: none
        choices: []
        aliases: []
    origin_host_to_server:
        description:
            - Specifies the origin host to server of BIG-IP.
        required: false
        default: none
        choices: []
        aliases: []
    origin_realm_to_client:
        description:
            - Specifies the origin realm of BIG-IP.
        required: false
        default: none
        choices: []
        aliases: []
    origin_realm_to_server:
        description:
            - Specifies the origin realm to server of BIG-IP.
        required: false
        default: none
        choices: []
        aliases: []
    overwrite_destination_host:
        description:
            - This attribute has been deprecated as of BIG-IP v11.
        required: false
        default: enabled
        choices: ['disabled', 'enabled']
        aliases: []
    parent_avp:
        description:
            - Specifies the name of the Diameter attribute that the system uses to indicate if the persist-avp option is embedded in a grouped avp.
        required: false
        default: none
        choices: range(0, 4294967296)
        aliases: []
    partition:
        description:
            - Displays the administrative partition within which the profile resides.
        required: false
        default: null
        choices: []
        aliases: []
    persist_avp:
        description:
            - Specifies the name of the Diameter attribute that the system persists on.
        required: false
        default: none
        choices: []
        aliases: []
    reset_on_timeout:
        description:
            - When it is enabled and the watchdog failures exceed the max watchdog failure, the system resets the connection.
        required: false
        default: enabled
        choices: ['disabled', 'enabled']
        aliases: []
    retransmit_timeout:
        description:
            - Specifies the retransmit timeout in seconds.
        required: false
        default: 10
        choices: range(0, 4294967296)
        aliases: []
    subscriber_aware:
        description:
            - When you enable this option, the system extracts available subscriber information, such as phone number or phone model, from diameter authentication and/or accounting packets.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
        aliases: []
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        required: false
        default: present
        choices: ['absent', 'present']
        aliases: []
        version_added: 2.3
    watchdog_timeout:
        description:
            - Specifies the watchdog timeout in seconds.
        required: false
        default: 0
        choices: range(0, 4294967296)
        aliases: []
'''

EXAMPLES = '''
- name: Create LTM Profile Diameter
  f5bigip_ltm_profile_diameter:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_diameter_profile
    partition: Common
    description: My diameter profile
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_LTM_PROFILE_DIAMETER_ARGS = dict(
    app_service                   =    dict(type='str'),
    connection_prime              =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    defaults_from                 =    dict(type='str'),
    description                   =    dict(type='str'),
    destination_realm             =    dict(type='str'),
    handshake_timeout             =    dict(type='int'),
    host_ip_rewrite               =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    max_retransmit_attempts       =    dict(type='int'),
    max_watchdog_failure          =    dict(type='int'),
    origin_host_to_client         =    dict(type='str'),
    origin_host_to_server         =    dict(type='str'),
    origin_realm_to_client        =    dict(type='str'),
    origin_realm_to_server        =    dict(type='str'),
    overwrite_destination_host    =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    parent_avp                    =    dict(type='str'),
    persist_avp                   =    dict(type='str'),
    reset_on_timeout              =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    retransmit_timeout            =    dict(type='int'),
    subscriber_aware              =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    watchdog_timeout              =    dict(type='int')
)

class F5BigIpLtmProfileDiameter(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.profile.diameters.diameter.create,
            'read':     self.mgmt_root.tm.ltm.profile.diameters.diameter.load,
            'update':   self.mgmt_root.tm.ltm.profile.diameters.diameter.update,
            'delete':   self.mgmt_root.tm.ltm.profile.diameters.diameter.delete,
            'exists':   self.mgmt_root.tm.ltm.profile.diameters.diameter.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}

    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_PROFILE_DIAMETER_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpLtmProfileDiameter(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()