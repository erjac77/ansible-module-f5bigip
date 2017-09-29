#!/usr/bin/python
#
# Copyright 2016, Eric Jacob <erjac77@gmail.com>
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
module: f5bigip_ltm_profile_sip
short_description: BIG-IP ltm profile sip module
description:
    - Configures a Session Initiation Protocol (SIP) profile.
version_added: 2.3
author:
    - "Gabriel Fortin"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    alg_enable:
        description:
            - Enables or disables the SIP ALG (Application Level Gateway) feature.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
        aliases: []
    app_service:
        description:
            - Specifies the name of the application service to which the object belongs.
        required: false
        default: none
        choices: []
        aliases: []
    community:
        description:
            - Specifies the community to which you want to assign the virtual server that you associate with this profile.
        required: false
        default: none
        choices: []
        aliases: []
    defaults_from:
        description:
            - Specifies the profile that you want to use as the parent profile.
        required: false
        default: sip
        choices: []
        aliases: []
    description:
        description:
            - User defined description.
        required: false
        default: null
        choices: []
        aliases: []
    dialog_aware:
        description:
            - Enables or disables the ability for the system to be aware of unauthorized use of the SIP dialog.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
        aliases: []
    dialog_establishment_timeout:
        description:
            - Indicates the timeout value for dialog establishment in a sip session.
        required: false
        default: 10
        choices: []
        aliases: []
    enable_sip_firewall:
        description:
            - Indicates whether to enable SIP firewall functionality or not.
        required: false
        default: no
        choices: ['no', 'yes']
        aliases: []
    insert_record_route_header:
        description:
            - Enables or disables the insertion of a Record-Route header, which indicates the next hop for the following SIP request messages.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
        aliases: []
    insert_via_header:
        description:
            - Enables or disables the insertion of a Via header, which indicates where the message originated.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
        aliases: []
    log_profile:
        description:
            - Specify the name of the ALG log profile which controls the logging of ALG .
        required: false
        default: null
        choices: []
        aliases: []
    log_publisher:
        description:
            - Specify the name of the log publisher which logs translation events.
        required: false
        default: null
        choices: []
        aliases: []
    max_media_sessions:
        description:
            - Indicates the maximum number of SDP media sessions that the BIG-IP system accepts.
        required: false
        default: 6
        choices: []
        aliases: []
    max_registrations:
        description:
            - Indicates the maximum number of registrations, the maximum allowable REGISTER messages can be recorded that the BIG-IP system accepts.
        required: false
        default: 100
        choices: []
        aliases: []
    max_sessions_per_registration:
        description:
            - Indicates the maximum number of calls or sessions can be made by a user for a single registration that the BIG-IP system accepts.
        required: false
        default: 50
        choices: []
        aliases: []
    max_size:
        description:
            - Specifies the maximum SIP message size that the BIG-IP system accepts.
        required: false
        default: 65535
        choices: []
        aliases: []
    name:
        description:
            - Specifies a unique name for the component.
        required: true
        default: none
        choices: []
        aliases: []
    partition:
        description:
            - Displays the administrative partition within which the component resides.
        required: false
        default: null
        choices: []
        aliases: []
    registration_timeout:
        description:
            - Indicates the timeout value for a sip registration.
        required: false
        default: 3600
        choices: []
        aliases: []
    rtp_proxy_style:
        description:
            - Indicates the style in which the RTP will proxy the data.
        required: false
        default: symmetric
        choices: ['symmetric', 'restricted-by-ip-address', 'any-location']
        aliases: []
    secure_via_header:
        description:
            - Enables or disables the insertion of a Secure Via header, which indicates where the message originated.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
        aliases: []
    security:
        description:
            - Enables or disables security for the SIP profile.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
        aliases: []
    sip_session_timeout:
        description:
            - Indicates the timeout value for a sip session.
        required: false
        default: 300
        choices: []
        aliases: []
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        required: false
        default: present
        choices: ['absent', 'present']
        aliases: []
    terminate_on_bye:
        description:
            - Enables or disables the termination of a connection when a BYE transaction finishes.
        required: false
        default: enabled
        choices: ['disabled', 'enabled']
        aliases: []
    user_via_header:
        description:
            - Enables or disables the insertion of a Via header specified by a system administrator.
        required: false
        default: none
        choices: []
        aliases: []
'''

EXAMPLES = '''
- name: Create LTM Profile sip
  f5bigip_ltm_profile_sip:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_sip_profile
    partition: Common
    description: My sip profile
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_LTM_PROFILE_SIP_ARGS = dict(
    alg_enable                       =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    app_service                      =    dict(type='str'),
    community                        =    dict(type='str'),
    defaults_from                    =    dict(type='str'),
    description                      =    dict(type='str'),
    dialog_aware                     =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    dialog_establishment_timeout     =    dict(type='int'),
    enable_sip_firewall              =    dict(type='str', choices=F5_POLAR_CHOICES),
    insert_record_route_header       =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    insert_via_header                =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    log_profile                      =    dict(type='str'),
    log_publisher                    =    dict(type='str'),
    max_media_sessions               =    dict(type='int'),
    max_registrations                =    dict(type='int'),
    max_sessions_per_registration    =    dict(type='int'),
    max_size                         =    dict(type='int'),
    registration_timeout             =    dict(type='int'),
    rtp_proxy_style                  =    dict(type='str', choices=['symmetric', 'restricted-by-ip-address', 'any-location']),
    secure_via_header                =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    security                         =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    sip_session_timeout              =    dict(type='int'),
    terminate_on_bye                 =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    user_via_header                  =    dict(type='str')
)

class F5BigIpLtmProfileSip(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.profile.sips.sip.create,
            'read':     self.mgmt_root.tm.ltm.profile.sips.sip.load,
            'update':   self.mgmt_root.tm.ltm.profile.sips.sip.update,
            'delete':   self.mgmt_root.tm.ltm.profile.sips.sip.delete,
            'exists':   self.mgmt_root.tm.ltm.profile.sips.sip.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}

    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_PROFILE_SIP_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpLtmProfileSip(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()