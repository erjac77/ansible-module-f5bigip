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
module: f5bigip_gtm_monitor_udp
short_description: BIG-IP gtm monitor udp module
description:
    - Configures a User Datagram Protocol (UDP) monitor.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    debug:
        description:
            - Specifies whether the monitor sends error messages and additional information to a log file created and
              labeled specifically for this monitor.
        default: no
        choices: ['no', 'yes']
    defaults_from:
        description:
            - Specifies the name of the monitor from which you want your custom monitor to inherit settings.
        default: udp
    description:
        description:
            - User defined description.
    destination:
        description:
            - Specifies the IP address and service port of the resource that is the destination of this monitor.
    ignore_down_response:
        description:
            - Specifies whether the monitor ignores a down response from the system it is monitoring.
        default: disabled
        choices: ['disabled', 'enabled']
    interval:
        description:
            - Specifies, in seconds, the frequency at which the system issues the monitor check when either the resource
              is down or the status of the resource is unknown.
        default: 30
    name:
        description:
            - Specifies a unique name for the component.
        required: true
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        default: Common
    probe_attempts:
        description:
            - Specifies the number of times the BIG-IP system attempts to probe the host server, after which the BIG-IP 
              system considers the host server down or unavailable.
        default: 3
    probe_interval:
        description:
            - Specifies the frequency at which the BIG-IP system probes the host server.
        default: 1
    probe_timeout:
        description:
            - Specifies the number of seconds after which the BIG-IP system times out the probe request to the BIG-IP system.
        default: 5
    reverse:
        description:
            - Specifies whether the monitor operates in reverse mode.
        default: disabled
        choices: ['disabled', 'enabled']
    send:
        description:
            - Specifies the text string that the monitor sends to the target object.
        default: GET/
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    timeout:
        description:
            - Specifies the number of seconds the target has in which to respond to the monitor request.
        default: 120
    transparent:
        description:
            - Specifies whether the monitor operates in transparent mode.
        default: disabled
        choices: ['disabled', 'enabled']
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Create GTM Monitor UDP
  f5bigip_gtm_monitor_udp:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_udp_monitor
    partition: Common
    description: My udp monitor
    state: present
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_GTM_MONITOR_UDP_ARGS = dict(
    debug=dict(type='str', choices=F5_POLAR_CHOICES),
    defaults_from=dict(type='str'),
    description=dict(type='str'),
    destination=dict(type='str'),
    ignore_down_response=dict(type='str', choices=F5_ACTIVATION_CHOICES),
    interval=dict(type='int'),
    probe_attempts=dict(type='int'),
    probe_interval=dict(type='int'),
    probe_timeout=dict(type='int'),
    reverse=dict(type='str', choices=F5_ACTIVATION_CHOICES),
    send=dict(type='str'),
    timeout=dict(type='int'),
    transparent=dict(type='str', choices=F5_ACTIVATION_CHOICES)
)


class F5BigIpGtmMonitorUdp(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create': self.mgmt_root.tm.gtm.monitor.udps.udp.create,
            'read': self.mgmt_root.tm.gtm.monitor.udps.udp.load,
            'update': self.mgmt_root.tm.gtm.monitor.udps.udp.update,
            'delete': self.mgmt_root.tm.gtm.monitor.udps.udp.delete,
            'exists': self.mgmt_root.tm.gtm.monitor.udps.udp.exists
        }


def main():
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_GTM_MONITOR_UDP_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpGtmMonitorUdp(check_mode=module.supports_check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
