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
module: f5bigip_ltm_profile_ftp
short_description: BIG-IP ltm ftp profile module
description:
    - Configures an FTP profile.
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
        version_added: 2.3
    defaults_from:
        description:
            - Specifies the profile that you want to use as the parent profile.
        required: false
        default: ftp
        choices: []
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
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    port:
        description:
            - Specifies a service for the data channel port used for this FTP profile.
        required: false
        default: ftp-data
        choices: []
        aliases: []
        version_added: 2.3
    security:
        description:
            - Enables or disables secure FTP traffic for the BIG-IP Application Security Manager. 
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
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
    translate_extended:
        description:
            - Translates RFC2428 extended requests EPSV and EPRT to PASV and PORT when communicating with IPv4 servers.
        required: false
        default: enabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    inherit_parent_profile:
        description:
            - Enables the FTP data channel to inherit the TCP profile used by the control channel. If disabled, the data channel uses FastL4 (BigProto) only.
        required: false
        default: null
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
   log_publisher:
        description:
            - Specify the name of the log publisher which logs translation events.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
   log_profile:
        description:
            - Specify the name of the ALG log profile which controls the logging of ALG .
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
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

from ansible_common_f5.f5_bigip import *

BIGIP_LTM_PROFILE_FTP_ARGS = dict(
    app_service                 =   dict(type='str'),
    defaults_from               =   dict(type='str'),
    description                 =   dict(type='str'),
    security                    =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    translate_extented          =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    inherit_parent_profile      =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    log_publisher               =   dict(type='str'),
    log_profile                 =   dict(type='str')
)

class F5BigIpLtmProfileFtp(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.profile.ftps.ftp.create,
            'read':     self.mgmt_root.tm.ltm.profile.ftps.ftp.load,
            'update':   self.mgmt_root.tm.ltm.profile.ftps.ftp.update,
            'delete':   self.mgmt_root.tm.ltm.profile.ftps.ftp.delete,
            'exists':   self.mgmt_root.tm.ltm.profile.ftps.ftp.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}
    
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_PROFILE_FTP_ARGS, supports_check_mode=False)
    
    try:
        obj = F5BigIpLtmProfileFtp(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()