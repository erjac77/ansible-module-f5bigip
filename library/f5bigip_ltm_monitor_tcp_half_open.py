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
module: f5bigip_ltm_monitor_tcp_half_open
short_description: BIG-IP ltm monitor tcp half open module
description:
    - Configures a Transmission Control Protocol (TCP) Half Open monitor.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    app_service:
        description:
            - Specifies the name of the application service to which the monitor belongs
    defaults_from:
        description:
            - Specifies the name of the monitor from which you want your custom monitor to inherit settings.
        default: tcp_half_open
    description:
        description:
            - Specifies descriptive text that identifies the component.
    destination:
        description:
            - Specifies the IP address and service port of the resource that is the destination of this monitor.
    interval:
        description:
            - Specifies, in seconds, the frequency at which the system issues the monitor check when either the resource
              is down or the status of the resource is unknown.
        default: 5
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
        default: 16
    transparent:
        description:
            - Specifies whether the monitor operates in transparent mode.
        default: disabled
        choices: ['disabled', 'enabled']
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
- name: Create LTM Monitor TCP Half Open
  f5bigip_ltm_monitor_tcp_half_open:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_tcp_half_open_monitor
    partition: Common
    description: My tcp half open monitor
    state: present
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_LTM_MONITOR_TCP_HALF_OPEN_ARGS = dict(
    app_service=dict(type='str'),
    defaults_from=dict(type='str'),
    description=dict(type='str'),
    destination=dict(type='str'),
    interval=dict(type='int'),
    manual_resume=dict(type='str', choices=F5_ACTIVATION_CHOICES),
    time_until_up=dict(type='int'),
    timeout=dict(type='int'),
    transparent=dict(type='str', choices=F5_ACTIVATION_CHOICES),
    up_interval=dict(type='int')
)


class F5BigIpLtmMonitorTcpHalfOpen(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create': self.mgmt_root.tm.ltm.monitor.tcp_half_opens.tcp_half_open.create,
            'read': self.mgmt_root.tm.ltm.monitor.tcp_half_opens.tcp_half_open.load,
            'update': self.mgmt_root.tm.ltm.monitor.tcp_half_opens.tcp_half_open.update,
            'delete': self.mgmt_root.tm.ltm.monitor.tcp_half_opens.tcp_half_open.delete,
            'exists': self.mgmt_root.tm.ltm.monitor.tcp_half_opens.tcp_half_open.exists
        }


def main():
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_MONITOR_TCP_HALF_OPEN_ARGS,
                                             supports_check_mode=False)

    try:
        obj = F5BigIpLtmMonitorTcpHalfOpen(check_mode=module.supports_check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
