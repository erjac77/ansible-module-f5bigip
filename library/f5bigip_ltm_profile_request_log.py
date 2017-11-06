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
module: f5bigip_ltm_profile_request_log
short_description: BIG-IP ltm profile request log module
description:
    - Configures a Request-Logging profile.
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
    defaults_from:
        description:
            - Specifies the default values from this profile.
        required: false
        default: null
        choices: []
        aliases: []
    description:
        description:
            - User defined description.
        required: false
        default: null
        choices: []
        aliases: []
    log_request_logging_errors:
        description:
            - Enables secondary logging should the primary lack sufficient available bandwidth.
        required: false
        default: null
        choices: ['disabled', 'enabled']
        aliases: []
    log_response_by_default:
        description:
            - Indicates if response logging may be overridden via iRule.
        required: false
        default: null
        choices: ['disabled', 'enabled']
        aliases: []
    log_response_logging_error:
        description:
            - Enables secondary logging should the primary lack sufficient available bandwidth.
        required: false
        default: null
        choices: ['disabled', 'enabled']
        aliases: []
    partition:
        description:
            - Displays the administrative partition within which the profile resides.
        required: false
        default: null
        choices: []
        aliases: []
    proxy_close_on_error:
        description:
            - Specifies, if enabled, that the logging profile will close the connection after sending its proxy-response.
        required: false
        default: null
        choices: ['disabled', 'enabled']
        aliases: []
    proxy_respond_on_logging_error:
        description:
            - Specifies that the logging profile respond directly (for example, with an HTTP 502) if the logging fails.
        required: false
        default: null
        choices: ['disabled', 'enabled']
        aliases: []
    proxy_response:
        description:
            - Specifies the response to send on logging errors.
        required: false
        default: null
        choices: []
        aliases: []
    request_log_error_pool:
        description:
            - Specifies the name of the pool from which to select log servers.
        required: false
        default: null
        choices: []
        aliases: []
    request_log_error_protocol:
        description:
            - Specifies the HighSpeedLogging protocol to use when logging.
        required: false
        default: null
        choices: ['TCP', 'UDP', 'none']
        aliases: []
    request_log_error_template:
        description:
            - Specifies the template to use when generating log messages.
        required: false
        default: null
        choices: []
        aliases: []
    request_log_pool:
        description:
            - Specifies the name of the pool from which to select log servers.
        required: false
        default: null
        choices: []
        aliases: []
    request_log_protocol:
        description:
            - Specifies the HighSpeedLogging protocol to use when logging.
        required: false
        default: null
        choices: ['TCP', 'UDP', 'none']
        aliases: []
    request_log_template:
        description:
            - Specifies the template to use when generating log messages.
        required: false
        default: null
        choices: []
        aliases: []
    request_logging:
        description:
            - Enables or disables logging before the response is returned to the client.
        required: false
        default: null
        choices: ['disabled', 'enabled']
        aliases: []
    response_log_error_pool:
        description:
            - Specifies the name of the pool from which to select log servers.
        required: false
        default: null
        choices: ['TCP', 'UDP', 'none']
        aliases: []
    response_log_error_protocol:
        description:
            - Specifies the HighSpeedLogging protocol to use when logging.
        required: false
        default: null
        choices: []
        aliases: []
    response_log_error_template:
        description:
            - Specifies the template to use when generating log messages.
        required: false
        default: null
        choices: []
        aliases: []
    response_log_pool:
        description:
            - Specifies the name of the pool from which to select log servers.
        required: false
        default: null
        choices: []
        aliases: []
    response_log_protocol:
        description:
            - Specifies the HighSpeedLogging protocol to use when logging.
        required: false
        default: null
        choices: ['TCP', 'UDP', 'none']
        aliases: []
    response_log_template:
        description:
            - Specifies the template to use when generating log messages.
        required: false
        default: null
        choices: []
        aliases: []
    response_logging:
        description:
            - Enables or disables logging before the response is returned to the client.
        required: false
        default: null
        choices: ['disabled', 'enabled']
        aliases: []
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        required: false
        default: present
        choices: ['absent', 'present']
        aliases: []
'''

EXAMPLES = '''
- name: Create LTM Profile Request Log
  f5bigip_ltm_profile_request_log:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_request_log_profile
    partition: Common
    description: My request log profile
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_LTM_PROFILE_REQUEST_LOG_ARGS = dict(
    app_service                       =    dict(type='str'),
    defaults_from                     =    dict(type='str'),
    description                       =    dict(type='str'),
    log_request_logging_errors        =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    log_response_by_default           =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    log_response_logging_error        =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    proxy_close_on_error              =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    proxy_respond_on_logging_error    =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    proxy_response                    =    dict(type='str'),
    request_log_error_pool            =    dict(type='str'),
    request_log_error_protocol        =    dict(type='str', choices=['TCP', 'UDP', 'none']),
    request_log_error_template        =    dict(type='str'),
    request_log_pool                  =    dict(type='str'),
    request_log_protocol              =    dict(type='str', choices=['TCP', 'UDP', 'none']),
    request_log_template              =    dict(type='str'),
    request_logging                   =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    response_log_error_pool           =    dict(type='str'),
    response_log_error_protocol       =    dict(type='str', choices=['TCP', 'UDP', 'none']),
    response_log_error_template       =    dict(type='str'),
    response_log_pool                 =    dict(type='str'),
    response_log_protocol             =    dict(type='str', choices=['TCP', 'UDP', 'none']),
    response_log_template             =    dict(type='str'),
    response_logging                  =    dict(type='str', choices=F5_ACTIVATION_CHOICES)
)

class F5BigIpLtmProfileRequestLog(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.profile.request_logs.request_log.create,
            'read':     self.mgmt_root.tm.ltm.profile.request_logs.request_log.load,
            'update':   self.mgmt_root.tm.ltm.profile.request_logs.request_log.update,
            'delete':   self.mgmt_root.tm.ltm.profile.request_logs.request_log.delete,
            'exists':   self.mgmt_root.tm.ltm.profile.request_logs.request_log.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}

    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_PROFILE_REQUEST_LOG_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpLtmProfileRequestLog(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()