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
module: f5bigip_sys_global_settings
short_description: BIG-IP sys global settings module
description:
    - Configures the global system settings for a BIG-IP system.
version_added: "2.4"
author:
    - "Eric Jacob (@erjac77)"
options:
    aws_access_key:
        description:
            - Amazon Web Services (AWS) supplied access key needed to make secure requests to AWS.
    aws_secret_key:
        description:
            - Amazon Web Services (AWS) supplied secret key needed to make secure requests to AWS.
    aws_api_max_concurrency:
        description:
            - Maximum concurrent connections allowed while making Amazon Web Service (AWS) api calls.
        default: 1
    console_inactivity_timeout:
        description:
            - Specifies the number of seconds of inactivity before the system logs off a user that is logged on.
        default: 0
    custom_addr:
        description:
            - Specifies an IP address for the system.
        default: '::'
    description:
        description:
            - Specifies descriptive text that identifies the component.
    failsafe_action:
        description:
            - Specifies the action that the system takes when the switch board fails.
        default: go-offline-restart-tm
        choices: ['go-offline', 'reboot', 'resetart-all', 'go-offline-restart-tm', 'failover-restart-tm']
    file_local_path_prefix:
        description:
            - Specifies a list of folder prefixes that can be applied for file objects.
    gui_security_banner:
        description:
            - Specifies whether the system presents on the login screen the text you specify in the
              gui-security-banner-text option.
        default: enabled
        choices: ['enabled', 'disabled']
    gui_security_banner_text:
        description:
            - Specifies the text to present on the login screen when the gui-security-banner option is enabled.
        default: Welcome to the BIG-IP Configuration Utility
    gui_setup:
        description:
            - Enables or disables the Setup utility in the browser-based Configuration utility.
        default: enabled
        choices: ['enabled', 'disabled']
    host_addr_mode:
        description:
            - Specifies the type of host address you want to assign to the system.
        default: management.
        choices: ['custom', 'management', 'state-mirror']
    hostname:
        description:
            - Specifies a local name for the system.
        default: bigip1
    lcd_display:
        description:
            - Enables or disables the LCD display on the front of the system.
        default: enabled
        choices: ['enabled', 'disabled']
    net_reboot:
        description:
            - Enables or disables the network reboot feature.
        default: disabled
        choices: ['enabled', 'disabled']
    password_prompt:
        description:
            - Specifies the text to present above the password field on the system's login screen.
    mgmt_dhcp:
        description:
            - Specifies whether the system uses DHCP client for acquiring the management interface IP address.
        default: enabled for VE and disabled for all other platforms
        choices: ['enabled', 'disabled']
    quiet_boot:
        description:
            - Enables or disables the quiet boot feature.
        default: enabled
        choices: ['enabled', 'disabled']
    username_prompt:
        description:
            - Specifies the text to present above the user name field on the system's login screen.
requirements:
    - BIG-IP >= 12.0
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Disable SYS Global Settings gui setup
  f5bigip_sys_global_settings:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    gui_setup: disabled
  delegate_to: localhost

- name: Change Global Settings banner text
  f5bigip_sys_global_settings:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    gui_security_banner: enabled
    gui_security_banner_text: "NOTICE: Improper use of this computer may result in prosecution!"
  delegate_to: localhost
'''

RETURN = ''' # '''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.base import F5_ACTIVATION_CHOICES
from ansible_common_f5.base import F5_PROVIDER_ARGS
from ansible_common_f5.bigip import F5BigIpUnnamedObject


class ModuleParams(object):
    @property
    def argument_spec(self):
        argument_spec = dict(
            aws_access_key=dict(type='str'),
            aws_secret_key=dict(type='str'),
            aws_api_max_concurrency=dict(type='int'),
            console_inactivity_timeout=dict(type='int'),
            custom_addr=dict(type='str'),
            description=dict(type='str'),
            failsafe_action=dict(type='str', choices=['go-offline', 'reboot', 'resetart-all', 'go-offline-restart-tm',
                                                      'failover-restart-tm']),
            file_local_path_prefix=dict(type='str'),
            gui_security_banner=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            gui_security_banner_text=dict(type='str'),
            gui_setup=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            host_addr_mode=dict(type='str', choices=['custom', 'management', 'state-mirror']),
            hostname=dict(type='str'),
            hosts_allow_include=dict(type='str'),
            lcd_display=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            net_reboot=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            password_prompt=dict(type='str', no_log=True),
            mgmt_dhcp=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            quiet_boot=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            # remote_host=dict(type='list'),
            username_prompt=dict(type='str')
        )
        argument_spec.update(F5_PROVIDER_ARGS)
        return argument_spec

    @property
    def supports_check_mode(self):
        return True


class F5BigIpSysGlobalSettings(F5BigIpUnnamedObject):
    def _set_crud_methods(self):
        self._methods = {
            'read': self._api.tm.sys.global_settings.load,
            'update': self._api.tm.sys.global_settings.update
        }


def main():
    params = ModuleParams()
    module = AnsibleModule(argument_spec=params.argument_spec, supports_check_mode=params.supports_check_mode)

    try:
        obj = F5BigIpSysGlobalSettings(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
