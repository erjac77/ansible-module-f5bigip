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
module: f5bigip_ltm_profile_tftp
short_description: BIG-IP ltm tftp profile module
description:
    - Configures a TFTP profile.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    app-service:
        description:
            - Specifies the name of the application service to which the profile belongs.
    defaults-from:
        description:
            - Specifies the profile that you want to use as the parent profile. 
    description:
        description:
            - User defined description.
    idle-timeout:
        description:
            - Specifies an idle timeout in seconds.
        default: 300
    log-publisher:
        description:
            - Specify the name of the log publisher which logs translation events.
    log-profile:
        description:
            - Specify the name of the ALG log pro le which controls the logging of ALG events.
    name:
        description:
            - Specifies a unique name for the component.
        required: true
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        default: Common
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
'''
EXAMPLES = '''
- name: Create LTM TFTP Profile
  f5bigip_ltm_profile_tftp:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_tftp_profile
    partition: Common
    state: present
  delegate_to: localhost
'''

RETURN = '''
'''

from six.moves import range
from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_LTM_PROFILE_TFTP_ARGS = dict(
    app_service=dict(type='str'),
    defaults_from=dict(type='str'),
    description=dict(type='str'),
    idle_timeout=dict(type='int'),
    log_publisher=dict(type='str'),
    log_profile=dict(type='str')
)


class F5BigIpLtmProfileTftp(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create': self.mgmt_root.tm.ltm.profile.tftps.tftp.create,
            'read': self.mgmt_root.tm.ltm.profile.tftps.tftp.load,
            'update': self.mgmt_root.tm.ltm.profile.tftps.tftp.update,
            'delete': self.mgmt_root.tm.ltm.profile.tftps.tftp.delete,
            'exists': self.mgmt_root.tm.ltm.profile.tftps.tftp.exists
        }


def main():
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_PROFILE_TFTP_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpLtmProfileTftp(check_mode=module.supports_check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
