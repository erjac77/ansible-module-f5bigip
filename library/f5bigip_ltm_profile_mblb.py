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
module: f5bigip_ltm_profile_mblb
short_description: BIG-IP ltm profile mblb module
description:
    - Configures an MBLB profile (experimental).
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
            - Specifies the profile that you want to use as the parent profile.
        required: false
        default: mblb
        choices: []
        aliases: []
    description:
        description:
            - User defined description.
        required: false
        default: null
        choices: []
        aliases: []
    egress_high:
        description:
            - Specify the high water mark for egress message queue.
        required: false
        default: 50
        choices: []
        aliases: []
    egress_low:
        description:
            - Specify the low water mark for egress message queue.
        required: false
        default: 5
        choices: []
        aliases: []
    ingress_high:
        description:
            - Specify the high water mark for ingress message queue.
        required: false
        default: 50
        choices: []
        aliases: []
    ingress_low:
        description:
            - Specify the low water mark for ingress message queue.
        required: false
        default: 5
        choices: []
        aliases: []
    isolate_abort:
        description:
            - Specify whether to isolate abort event propagation.
        required: false
        default: null
        choices: ['disabled', 'enabled']
        aliases: []
    isolate_client:
        description:
            - Specify whether to isolate clientside shutdown event propagation.
        required: false
        default: null
        choices: ['disabled', 'enabled']
        aliases: []
    isolate_expire:
        description:
            - Specify whether to isolate expiration event propagation.
        required: false
        default: null
        choices: ['disabled', 'enabled']
        aliases: []
    isolate_server:
        description:
            - Specify whether to isolate serverside shutdown event propagation.
        required: false
        default: null
        choices: ['disabled', 'enabled']
        aliases: []
    min_conn:
        description:
            - Specify the minimum number of serverside connections.
        required: false
        default: 0
        choices: []
        aliases: []
    name:
        description:
            - Specifies a unique name for the component.
        required: true
        default: none
        choices: []
        aliases: []
    shutdown_timeout:
        description:
            - Delays sending FIN when BIGIP receives the first FIN packet from either the client or the server.
        required: false
        default: 5
        choices: []
        aliases: []
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        required: false
        default: present
        choices: ['absent', 'present']
        aliases: []
    tag_ttl:
        description:
            - Specify the TTL (time to live) for message TAG.
        required: false
        default: 60
        choices: []
        aliases: []
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

from ansible_common_f5.f5_bigip import *

BIGIP_LTM_PROFILE_MBLB_ARGS = dict(
    app_service         =    dict(type='str'),
    defaults_from       =    dict(type='str'),
    description         =    dict(type='str'),
    egress_high         =    dict(type='int'),
    egress_low          =    dict(type='int'),
    ingress_high        =    dict(type='int'),
    ingress_low         =    dict(type='int'),
    isolate_abort       =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    isolate_client      =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    isolate_expire      =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    isolate_server      =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    min_conn            =    dict(type='int'),
    shutdown_timeout    =    dict(type='int'),
    tag_ttl             =    dict(type='int')
)

class F5BigIpLtmProfileMblb(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.profile.mblbs.mblb.create,
            'read':     self.mgmt_root.tm.ltm.profile.mblbs.mblb.load,
            'update':   self.mgmt_root.tm.ltm.profile.mblbs.mblb.update,
            'delete':   self.mgmt_root.tm.ltm.profile.mblbs.mblb.delete,
            'exists':   self.mgmt_root.tm.ltm.profile.mblbs.mblb.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}

    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_PROFILE_MBLB_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpLtmProfileMblb(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()