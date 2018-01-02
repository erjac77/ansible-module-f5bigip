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
module: f5bigip_ltm_monitor_sip
short_description: BIG-IP ltm monitor sip module
description:
    - Configures a Session Initiation Protocol (SIP) monitor.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    app_service:
        description:
            - Specifies the name of the application service to which the monitor belongs.
    cert:
        description:
            - Specifies a fully-qualified path for a client certificate that the monitor sends to the target SSL server.
    cipherlist:
        description:
            - Specifies the list of ciphers for this monitor.
        default: DEFAULT:+SHA:+3DES:+kEDH
    compatibility:
        description:
            - Specifies, when enabled, that the SSL options setting (in OpenSSL) is set to ALL.
        default: enabled
        choices: ['disabled', 'enabled']
    debug:
        description:
            - Specifies whether the monitor sends error messages and additional information to a log file created and
              labeled specifically for this monitor.
        default: no
        choices: ['no', 'yes']
    defaults_from:
        description:
            - Specifies the name of the monitor from which you want your custom monitor to inherit settings.
        default: sip
    description:
        description:
            - User defined description.
    destination:
        description:
            - Specifies the IP address and service port of the resource that is the destination of this monitor.
    filter:
        description:
            - Specifies the SIP status codes that the target can return to be considered up.
        choices: ['any', 'none', 'status']
    filter_neg:
        description:
            - Specifies the SIP status codes that the target can return to be considered down.
        choices: ['any', 'none', 'status']
    headers:
        description:
            - Specifies the set of SIP headers in the SIP message that is sent to the target
    interval:
        description:
            - Specifies, in seconds, the frequency at which the system issues the monitor check when either the resource
              is down or the status of the resource is unknown.
        default: 5
    key:
        description:
            - Specifies the key if the monitored target requires authentication
    manual_resume:
        description:
            - Specifies whether the system automatically changes the status of a resource to up at the next successful
              monitor check.
        default: disabled
        choices: ['disabled', 'enabled']
    mode:
        description:
            - Specifies the protocol that the monitor uses to communicate with the target.
        default: udp
        choices: ['sips', 'tcp', 'tls', 'udp']
    name:
        description:
            - Specifies a unique name for the component.
        required: true
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        default: Common
    request:
        description:
            - Specifies the SIP request line in the SIP message that is sent to the target.
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    time_until_up:
        description:
            - Specifies the amount of time, in seconds, after the first successful response before a node is marked up.
    up_interval:
        description:
            - Specifies, in seconds, the frequency at which the system issues the monitor check when the resource is up.
        default: 0
    username:
        description:
            - Specifies the username, if the monitored target requires authentication.
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Create LTM Monitor SIP
  f5bigip_ltm_monitor_sip:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_sip_monitor
    partition: Common
    description: My sip monitor
    state: present
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_LTM_MONITOR_SIP_ARGS = dict(
    app_service=dict(type='str'),
    cert=dict(type='str'),
    cipherlist=dict(type='list'),
    compatibility=dict(type='str', choices=F5_ACTIVATION_CHOICES),
    debug=dict(type='str', choices=F5_POLAR_CHOICES),
    defaults_from=dict(type='str'),
    description=dict(type='str'),
    destination=dict(type='str'),
    filter=dict(type='str', choices=['any', 'none', 'status']),
    filter_neg=dict(type='str', choices=['any', 'none', 'status']),
    headers=dict(type='str'),
    interval=dict(type='int'),
    key=dict(type='str'),
    manual_resume=dict(type='str', choices=F5_ACTIVATION_CHOICES),
    mode=dict(type='str', choices=['sips', 'tcp', 'tls', 'udp']),
    request=dict(type='str'),
    time_until_up=dict(type='int'),
    up_interval=dict(type='int'),
    username=dict(type='str')
)


class F5BigIpLtmMonitorSip(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create': self.mgmt_root.tm.ltm.monitor.sips.sip.create,
            'read': self.mgmt_root.tm.ltm.monitor.sips.sip.load,
            'update': self.mgmt_root.tm.ltm.monitor.sips.sip.update,
            'delete': self.mgmt_root.tm.ltm.monitor.sips.sip.delete,
            'exists': self.mgmt_root.tm.ltm.monitor.sips.sip.exists
        }


def main():
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_MONITOR_SIP_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpLtmMonitorSip(check_mode=module.supports_check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
