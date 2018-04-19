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
module: f5bigip_ltm_profile_ftp
short_description: BIG-IP ltm ftp profile module
description:
    - Configures an FTP profile.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    app_service:
        description:
            - Specifies the name of the application service to which the profile belongs. 
    defaults_from:
        description:
            - Specifies the profile that you want to use as the parent profile.
        default: ftp
    description:
        description:
            - User defined description.
    name:
        description:
            - Specifies a unique name for the component.
        required: true
    partition:
        description:
            - Displays the administrative partition within which the component resides.
    port:
        description:
            - Specifies a service for the data channel port used for this FTP profile.
        default: ftp-data
    security:
        description:
            - Enables or disables secure FTP traffic for the BIG-IP Application Security Manager. 
        default: disabled
        choices: ['enabled', 'disabled']
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    translate_extended:
        description:
            - Translates RFC2428 extended requests EPSV and EPRT to PASV and PORT when communicating with IPv4 servers.
        default: enabled
        choices: ['enabled', 'disabled']
    inherit_parent_profile:
        description:
            - Enables the FTP data channel to inherit the TCP profile used by the control channel. If disabled, the data
              channel uses FastL4 (BigProto) only.
        choices: ['enabled', 'disabled']
   log_publisher:
        description:
            - Specify the name of the log publisher which logs translation events.
   log_profile:
        description:
            - Specify the name of the ALG log profile which controls the logging of ALG.
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = ''' 
- name: Create LTM FTP Profile
  f5bigip_ltm_profile_ftp:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_ftp_profile
    partition: Common
    security: enabled
    translate_extended: disabled
    state: present
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_LTM_PROFILE_FTP_ARGS = dict(
    app_service=dict(type='str'),
    defaults_from=dict(type='str'),
    description=dict(type='str'),
    security=dict(type='str', choices=F5_ACTIVATION_CHOICES),
    translate_extented=dict(type='str', choices=F5_ACTIVATION_CHOICES),
    inherit_parent_profile=dict(type='str', choices=F5_ACTIVATION_CHOICES),
    log_publisher=dict(type='str'),
    log_profile=dict(type='str')
)


class F5BigIpLtmProfileFtp(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create': self.mgmt_root.tm.ltm.profile.ftps.ftp.create,
            'read': self.mgmt_root.tm.ltm.profile.ftps.ftp.load,
            'update': self.mgmt_root.tm.ltm.profile.ftps.ftp.update,
            'delete': self.mgmt_root.tm.ltm.profile.ftps.ftp.delete,
            'exists': self.mgmt_root.tm.ltm.profile.ftps.ftp.exists
        }


def main():
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_PROFILE_FTP_ARGS, supports_check_mode=True)

    try:
        obj = F5BigIpLtmProfileFtp(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
