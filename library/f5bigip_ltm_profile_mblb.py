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
module: f5bigip_ltm_profile_mblb
short_description: BIG-IP ltm profile mblb module
description:
    - Configures an MBLB profile (experimental).
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
        default: mblb
    description:
        description:
            - User defined description.
    egress_high:
        description:
            - Specify the high water mark for egress message queue.
        default: 50
    egress_low:
        description:
            - Specify the low water mark for egress message queue.
        default: 5
    ingress_high:
        description:
            - Specify the high water mark for ingress message queue.
        default: 50
    ingress_low:
        description:
            - Specify the low water mark for ingress message queue.
        default: 5
    isolate_abort:
        description:
            - Specify whether to isolate abort event propagation.
        choices: ['disabled', 'enabled']
    isolate_client:
        description:
            - Specify whether to isolate clientside shutdown event propagation.
        choices: ['disabled', 'enabled']
    isolate_expire:
        description:
            - Specify whether to isolate expiration event propagation.
        choices: ['disabled', 'enabled']
    isolate_server:
        description:
            - Specify whether to isolate serverside shutdown event propagation.
        choices: ['disabled', 'enabled']
    min_conn:
        description:
            - Specify the minimum number of serverside connections.
        default: 0
    name:
        description:
            - Specifies a unique name for the component.
        required: true
    shutdown_timeout:
        description:
            - Delays sending FIN when BIGIP receives the first FIN packet from either the client or the server.
        default: 5
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    tag_ttl:
        description:
            - Specify the TTL (time to live) for message TAG.
        default: 60
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Create LTM Profile MBLB
  f5bigip_ltm_profile_mblb:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_mblb_profile
    partition: Common
    description: My mblb profile
    state: present
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_LTM_PROFILE_MBLB_ARGS = dict(
    app_service=dict(type='str'),
    defaults_from=dict(type='str'),
    description=dict(type='str'),
    egress_high=dict(type='int'),
    egress_low=dict(type='int'),
    ingress_high=dict(type='int'),
    ingress_low=dict(type='int'),
    isolate_abort=dict(type='str', choices=F5_ACTIVATION_CHOICES),
    isolate_client=dict(type='str', choices=F5_ACTIVATION_CHOICES),
    isolate_expire=dict(type='str', choices=F5_ACTIVATION_CHOICES),
    isolate_server=dict(type='str', choices=F5_ACTIVATION_CHOICES),
    min_conn=dict(type='int'),
    shutdown_timeout=dict(type='int'),
    tag_ttl=dict(type='int')
)


class F5BigIpLtmProfileMblb(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create': self.mgmt_root.tm.ltm.profile.mblbs.mblb.create,
            'read': self.mgmt_root.tm.ltm.profile.mblbs.mblb.load,
            'update': self.mgmt_root.tm.ltm.profile.mblbs.mblb.update,
            'delete': self.mgmt_root.tm.ltm.profile.mblbs.mblb.delete,
            'exists': self.mgmt_root.tm.ltm.profile.mblbs.mblb.exists
        }


def main():
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_PROFILE_MBLB_ARGS, supports_check_mode=True)

    try:
        obj = F5BigIpLtmProfileMblb(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
