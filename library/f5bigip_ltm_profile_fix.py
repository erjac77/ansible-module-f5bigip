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
module: f5bigip_ltm_profile_fix
short_description: BIG-IP ltm profile fix module
description:
    - Configures a Financial Information eXchange Protocol (FIX) profile.
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
            - Specifies the name of the application service to which this object belongs.
        required: false
        default: none
        choices: []
        aliases: []
    error_action:
        description:
            - Specifies the error handling method.
        required: false
        default: null
        choices: ['drop_connection', 'dont_forward']
        aliases: []
    full_logon_parsing:
        description:
            - Enable or disable logon message is always fully parsed.
        required: false
        default: true
        choices: ['true', 'false']
        aliases: []
    message_log_publisher:
        description:
            - Specifies the publisher for message logging.
        required: false
        default: null
        choices: []
        aliases: []
    partition:
        description:
            - Specifies the administrative partition within which the profile resides.
        required: false
        default: null
        choices: []
        aliases: []
    quick_parsing:
        description:
            - Enable or disable quick parsing which parses the basic standard fields and validates message length and checksum.
        required: false
        default: false
        choices: ['true', 'false']
        aliases: []
    report_log_publisher:
        description:
            - Specifies the publisher for error message and status report.
        required: false
        default: null
        choices: []
        aliases: []
    response_parsing:
        description:
            - Enable or disable response parsing which parses the messages from FIX server.
        required: false
        default: false
        choices: ['true', 'false']
        aliases: []
    sender_tag_class:
        description:
            - Specifies the tag substitution map between sender id and tag substitution data group.
        required: false
        default: null
        choices: []
        aliases: []
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        required: false
        default: present
        choices: ['absent', 'present']
        aliases: []
    statistics_sample_interval:
        description:
            - Specifies the sample interval in seconds of the message rate.
        required: false
        default: null
        choices: []
        aliases: []
'''

EXAMPLES = '''
- name: Create LTM Profile FIX
  f5bigip_ltm_profile_fix:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_fix_profile
    partition: Common
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_LTM_PROFILE_FIX_ARGS = dict(
    app_service                   =    dict(type='str'),
    error_action                  =    dict(type='str', choices=['drop_connection', 'dont_forward']),
    full_logon_parsing            =    dict(type='str', choices=['true', 'false']),
    message_log_publisher         =    dict(type='str'),
    quick_parsing                 =    dict(type='str', choices=['true', 'false']),
    report_log_publisher          =    dict(type='str'),
    response_parsing              =    dict(type='str', choices=['true', 'false']),
    sender_tag_class              =    dict(type='dict'),
    statistics_sample_interval    =    dict(type='int')
)

class F5BigIpLtmProfileFix(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.profile.fixs.fix.create,
            'read':     self.mgmt_root.tm.ltm.profile.fixs.fix.load,
            'update':   self.mgmt_root.tm.ltm.profile.fixs.fix.update,
            'delete':   self.mgmt_root.tm.ltm.profile.fixs.fix.delete,
            'exists':   self.mgmt_root.tm.ltm.profile.fixs.fix.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}

    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_PROFILE_FIX_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpLtmProfileFix(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()