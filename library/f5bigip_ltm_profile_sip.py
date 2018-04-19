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
module: f5bigip_ltm_profile_sip
short_description: BIG-IP ltm profile sip module
description:
    - Configures a Session Initiation Protocol (SIP) profile.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    alg_enable:
        description:
            - Enables or disables the SIP ALG (Application Level Gateway) feature.
        default: disabled
        choices: ['disabled', 'enabled']
    app_service:
        description:
            - Specifies the name of the application service to which the object belongs.
    community:
        description:
            - Specifies the community to which you want to assign the virtual server that you associate with this
              profile.
    defaults_from:
        description:
            - Specifies the profile that you want to use as the parent profile.
        default: sip
    description:
        description:
            - User defined description.
    dialog_aware:
        description:
            - Enables or disables the ability for the system to be aware of unauthorized use of the SIP dialog.
        default: disabled
        choices: ['disabled', 'enabled']
    dialog_establishment_timeout:
        description:
            - Indicates the timeout value for dialog establishment in a sip session.
        default: 10
    enable_sip_firewall:
        description:
            - Indicates whether to enable SIP firewall functionality or not.
        default: no
        choices: ['no', 'yes']
    insert_record_route_header:
        description:
            - Enables or disables the insertion of a Record-Route header, which indicates the next hop for the following
              SIP request messages.
        default: disabled
        choices: ['disabled', 'enabled']
    insert_via_header:
        description:
            - Enables or disables the insertion of a Via header, which indicates where the message originated.
        default: disabled
        choices: ['disabled', 'enabled']
    log_profile:
        description:
            - Specify the name of the ALG log profile which controls the logging of ALG .
    log_publisher:
        description:
            - Specify the name of the log publisher which logs translation events.
    max_media_sessions:
        description:
            - Indicates the maximum number of SDP media sessions that the BIG-IP system accepts.
        default: 6
    max_registrations:
        description:
            - Indicates the maximum number of registrations, the maximum allowable REGISTER messages can be recorded
              that the BIG-IP system accepts.
        default: 100
    max_sessions_per_registration:
        description:
            - Indicates the maximum number of calls or sessions can be made by a user for a single registration that the
              BIG-IP system accepts.
        default: 50
    max_size:
        description:
            - Specifies the maximum SIP message size that the BIG-IP system accepts.
        default: 65535
    name:
        description:
            - Specifies a unique name for the component.
        required: true
    partition:
        description:
            - Displays the administrative partition within which the component resides.
    registration_timeout:
        description:
            - Indicates the timeout value for a sip registration.
        default: 3600
    rtp_proxy_style:
        description:
            - Indicates the style in which the RTP will proxy the data.
        default: symmetric
        choices: ['symmetric', 'restricted-by-ip-address', 'any-location']
    secure_via_header:
        description:
            - Enables or disables the insertion of a Secure Via header, which indicates where the message originated.
        default: disabled
        choices: ['disabled', 'enabled']
    security:
        description:
            - Enables or disables security for the SIP profile.
        default: disabled
        choices: ['disabled', 'enabled']
    sip_session_timeout:
        description:
            - Indicates the timeout value for a sip session.
        default: 300
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    terminate_on_bye:
        description:
            - Enables or disables the termination of a connection when a BYE transaction finishes.
        default: enabled
        choices: ['disabled', 'enabled']
    user_via_header:
        description:
            - Enables or disables the insertion of a Via header specified by a system administrator.
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
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

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_LTM_PROFILE_SIP_ARGS = dict(
    alg_enable=dict(type='str', choices=F5_ACTIVATION_CHOICES),
    app_service=dict(type='str'),
    community=dict(type='str'),
    defaults_from=dict(type='str'),
    description=dict(type='str'),
    dialog_aware=dict(type='str', choices=F5_ACTIVATION_CHOICES),
    dialog_establishment_timeout=dict(type='int'),
    enable_sip_firewall=dict(type='str', choices=F5_POLAR_CHOICES),
    insert_record_route_header=dict(type='str', choices=F5_ACTIVATION_CHOICES),
    insert_via_header=dict(type='str', choices=F5_ACTIVATION_CHOICES),
    log_profile=dict(type='str'),
    log_publisher=dict(type='str'),
    max_media_sessions=dict(type='int'),
    max_registrations=dict(type='int'),
    max_sessions_per_registration=dict(type='int'),
    max_size=dict(type='int'),
    registration_timeout=dict(type='int'),
    rtp_proxy_style=dict(type='str', choices=['symmetric', 'restricted-by-ip-address', 'any-location']),
    secure_via_header=dict(type='str', choices=F5_ACTIVATION_CHOICES),
    security=dict(type='str', choices=F5_ACTIVATION_CHOICES),
    sip_session_timeout=dict(type='int'),
    terminate_on_bye=dict(type='str', choices=F5_ACTIVATION_CHOICES),
    user_via_header=dict(type='str')
)


class F5BigIpLtmProfileSip(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create': self.mgmt_root.tm.ltm.profile.sips.sip.create,
            'read': self.mgmt_root.tm.ltm.profile.sips.sip.load,
            'update': self.mgmt_root.tm.ltm.profile.sips.sip.update,
            'delete': self.mgmt_root.tm.ltm.profile.sips.sip.delete,
            'exists': self.mgmt_root.tm.ltm.profile.sips.sip.exists
        }


def main():
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_PROFILE_SIP_ARGS, supports_check_mode=True)

    try:
        obj = F5BigIpLtmProfileSip(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
