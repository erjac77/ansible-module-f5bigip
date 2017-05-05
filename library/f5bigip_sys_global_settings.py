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
module: f5bigip_sys_global_settings
short_description: BIG-IP sys global settings module
description:
    - Configures the global system settings for a BIG-IP system.
version_added: 2.3
author:
    - "Eric Jacob, @erjac77"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    aws_access_key:
        description:
            - Amazon Web Services (AWS) supplied access key needed to make secure requests to AWS.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    aws_secret_key:
        description:
            - Amazon Web Services (AWS) supplied secret key needed to make secure requests to AWS.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    aws_api_max_concurrency:
        description:
            - Maximum concurrent connections allowed while making Amazon Web Service (AWS) api calls.
        required: false
        default: 1
        choices: []
        aliases: []
        version_added: 2.3
    console_inactivity_timeout:
        description:
            - Specifies the number of seconds of inactivity before the system logs off a user that is logged on.
        required: false
        default: 0
        choices: []
        aliases: []
        version_added: 2.3
    custom_addr:
        description:
            - Specifies an IP address for the system.
        required: false
        default: ::
        choices: []
        aliases: []
        version_added: 2.3
    description:
        description:
            - Specifies descriptive text that identifies the component.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    failsafe_action:
        description:
            - Specifies the action that the system takes when the switch board fails.
        required: false
        default: go-offline-restart-tm
        choices: ['go-offline', 'reboot', 'resetart-all', 'go-offline-restart-tm', 'failover-restart-tm']
        aliases: []
        version_added: 2.3
    file_local_path_prefix:
        description:
            - Specifies a list of folder prefixes that can be applied for file objects.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    gui_security_banner:
        description:
            - Specifies whether the system presents on the login screen the text you specify in the gui-security-banner-text option.
        required: false
        default: enabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    gui_security_banner_text:
        description:
            - Specifies the text to present on the login screen when the gui-security-banner option is enabled.
        required: false
        default: Welcome to the BIG-IP Configuration Utility
        choices: []
        aliases: []
        version_added: 2.3
    gui_setup:
        description:
            - Enables or disables the Setup utility in the browser-based Configuration utility.
        required: false
        default: enabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    host_addr_mode:
        description:
            - Specifies the type of host address you want to assign to the system.
        required: false
        default: management.
        choices: ['custom', 'management', 'state-mirror']
        aliases: []
        version_added: 2.3
    hostname:
        description:
            - Specifies a local name for the system.
        required: false
        default: bigip1
        choices: []
        aliases: []
        version_added: 2.3
    lcd_display:
        description:
            - Enables or disables the LCD display on the front of the system.
        required: false
        default: enabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    net_reboot:
        description:
            - Enables or disables the network reboot feature.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    password_prompt:
        description:
            - Specifies the text to present above the password field on the system's login screen.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    mgmt_dhcp:
        description:
            - Specifies whether the system uses DHCP client for acquiring the management interface IP address.
        required: false
        default: enabled for VE and disabled for all other platforms
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    quiet_boot:
        description:
            - Enables or disables the quiet boot feature.
        required: false
        default: enabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    username_prompt:
        description:
            - Specifies the text to present above the user name field on the system's login screen.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
'''

EXAMPLES = '''
- name: Disable SYS GLOBAL SETTINGS gui setup
  f5bigip_sys_global_settings:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    gui_setup: disabled
  delegate_to: localhost

- name: Change SYS GLOBAL SETTINGS banner text
  f5bigip_sys_global_settings:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    gui_security_banner: enabled
    gui_security_banner_text: "NOTICE: Improper use of this computer may result in prosecution!"
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_SYS_GLOBAL_SETTINGS_ARGS = dict(
    aws_access_key              =   dict(type='str'),
    aws_secret_key              =   dict(type='str'),
    aws_api_max_concurrency     =   dict(type='int'),
    console_inactivity_timeout  =   dict(type='int'),
    custom_addr                 =   dict(type='str'),
    description                 =   dict(type='str'),
    failsafe_action             =   dict(type='str', choices=['go-offline', 'reboot', 'resetart-all', 'go-offline-restart-tm', 'failover-restart-tm']),
    file_local_path_prefix      =   dict(type='str'),
    gui_security_banner         =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    gui_security_banner_text    =   dict(type='str'),
    gui_setup                   =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    host_addr_mode              =   dict(type='str', choices=['custom', 'management', 'state-mirror']),
    hostname                    =   dict(type='str'),
    hosts_allow_include         =   dict(type='str'),
    lcd_display                 =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    net_reboot                  =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    password_prompt             =   dict(type='str'),
    mgmt_dhcp                   =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    quiet_boot                  =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    #remote_host                 =   dict(type='list'),
    username_prompt             =   dict(type='str')
)

class F5BigIpSysGlobalSettings(F5BigIpUnnamedObject):
    def set_crud_methods(self):
        self.methods = {
            'read':     self.mgmt_root.tm.sys.global_settings.load
        }

def main():
    # Translation list for conflictual params
    tr = {}
    
    module = AnsibleModuleF5BigIpUnnamedObject(argument_spec=BIGIP_SYS_GLOBAL_SETTINGS_ARGS, supports_check_mode=False)
    
    try:
        obj = F5BigIpSysGlobalSettings(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()