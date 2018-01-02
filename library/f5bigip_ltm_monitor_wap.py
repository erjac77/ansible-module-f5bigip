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
module: f5bigip_ltm_monitor_wap
short_description: BIG-IP ltm monitor wap module
description:
    - Configures a Wireless Application Protocol (WAP) monitor.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    accounting_node:
        description:
            - Specifies the RADIUS server that provides authentication for the WAP target.
    accounting_port:
        description:
            - Specifies the port that the monitor uses for RADIUS accounting.
    app_service:
        description:
            - Specifies the name of the application service to which the monitor belongs.
    call_id:
        description:
            - Specifies the 11-digit phone number for the RADIUS server.
    debug:
        description:
            - Specifies whether the monitor sends error messages and additional information to a log file created and
              labeled specifically for this monitor.
        default: no
        choices: ['no', 'yes']
    defaults_from:
        description:
            - Specifies the name of the monitor from which you want your custom monitor to inherit settings.
        default: wap
    description:
        description:
            - User defined description.
    destination:
        description:
            - Specifies the IP address and service port of the resource that is the destination of this monitor.
    framed_address:
        description:
            - Specifies the RADIUS framed IP address
    interval:
        description:
            - Specifies, in seconds, the frequency at which the system issues the monitor check when either the resource
              is down or the status of the resource is unknown.
        default: 10
    manual_resume:
        description:
            - Specifies whether the system automatically changes the status of a resource to up at the next successful
              monitor check.
        default: disabled
        choices: ['disabled', 'enabled']
    name:
        description:
            - Specifies a unique name for the component.
        required: true
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        default: Common
    recv:
        description:
            - Specifies the text string that the monitor looks for in the returned resource.
    secret:
        description:
            - Specifies the password the monitor needs to access the resource.
    send:
        description:
            - Specifies the text string that the monitor sends to the target object.
        default: GET /
    server_id:
        description:
            - Specifies the RADIUS NAS-ID for this system when configuring a RADIUS server.
    session_id:
        description:
            - Specifies the RADIUS session identification number when configuring a RADIUS server.
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    time_until_up:
        description:
            - Specifies the amount of time, in seconds, after the first successful response before a node is marked up.
        default: 0
    timeout:
        description:
            - Specifies the number of seconds the target has in which to respond to the monitor request.
        default: 31
    up_interval:
        description:
            - Specifies, in seconds, the frequency at which the system issues the monitor check when the resource is up.
        default: 0
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Create LTM Monitor WAP
  f5bigip_ltm_monitor_wap:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_wap_monitor
    partition: Common
    description: My wap monitor
    state: present
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_LTM_MONITOR_WAP_ARGS = dict(
    accounting_node=dict(type='str'),
    accounting_port=dict(type='int'),
    app_service=dict(type='str'),
    call_id=dict(type='str'),
    debug=dict(type='str', choices=F5_POLAR_CHOICES),
    defaults_from=dict(type='str'),
    description=dict(type='str'),
    destination=dict(type='str'),
    framed_address=dict(type='str'),
    interval=dict(type='int'),
    manual_resume=dict(type='str', choices=F5_ACTIVATION_CHOICES),
    recv=dict(type='str'),
    secret=dict(type='str'),
    send=dict(type='str'),
    server_id=dict(type='str'),
    session_id=dict(type='str'),
    time_until_up=dict(type='int'),
    timeout=dict(type='int'),
    up_interval=dict(type='int')
)


class F5BigIpLtmMonitorWap(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create': self.mgmt_root.tm.ltm.monitor.waps.wap.create,
            'read': self.mgmt_root.tm.ltm.monitor.waps.wap.load,
            'update': self.mgmt_root.tm.ltm.monitor.waps.wap.update,
            'delete': self.mgmt_root.tm.ltm.monitor.waps.wap.delete,
            'exists': self.mgmt_root.tm.ltm.monitor.waps.wap.exists
        }


def main():
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_MONITOR_WAP_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpLtmMonitorWap(check_mode=module.supports_check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
