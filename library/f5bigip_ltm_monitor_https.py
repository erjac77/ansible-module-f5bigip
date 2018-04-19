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
module: f5bigip_ltm_monitor_https
short_description: BIG-IP ltm https monitor module
description:
    - Configures a Hypertext Transfer Protocol over Secure Socket Layer (HTTPS) monitor.
version_added: "2.4"
author:
    - "Eric Jacob (@erjac77)"
options:
    adaptive:
        description:
            - Specifies whether the adaptive feature is enabled for this monitor.
        choices: ['enabled', 'disabled']
    adaptive_divergence_type:
        description:
            - Specifies whether the adaptive-divergence-value is relative or absolute.
        choices: ['relative', 'absolute']
    adaptive_divergence_value:
        description:
            - Specifies how far from mean latency each monitor probe is allowed to be.
    adaptive_limit:
        description:
            - Specifies the hard limit, in milliseconds, which the probe is not allowed to exceed, regardless of the
              divergence value.
    adaptive_sampling_timespan:
        description:
            - Specifies the size of the sliding window, in seconds, which records probe history.
    app_service:
        description:
            - Specifies the application service to which the object belongs.
    cert:
        description:
            - Specifies a file object for a client certificate that the monitor sends to the target SSL server.
    cipherlist:
        description:
            - Specifies the list of ciphers for this monitor.
        default: DEFAULT:+SHA:+3DES:+kEDH
    compatibility:
        description:
            - Specifies, when enabled, that the SSL options setting (in OpenSSL) is set to ALL.
        default: enabled.
        choices: ['enabled', 'disabled']
    defaults_from:
        description:
            - Specifies the name of the monitor from which you want your custom monitor to inherit settings.
        default: http
    description:
        description:
            - Specifies descriptive text that identifies the component.
    destination:
        description:
            - Specifies the IP address and service port of the resource that is the destination of this monitor.
        default: *:*
    interval:
        description:
            - Specifies, in seconds, the frequency at which the system issues the monitor check when either the resource
              is down or the status of the resource is unknown.
        default: 5
    ip_dscp:
        description:
            - Specifies the differentiated services code point (DSCP).
        default: 0
    key:
        description:
            - Specifies the RSA private key if the monitored target requires authentication.
    manual_resume:
        description:
            - Specifies whether the system automatically changes the status of a resource to up at the next successful
              monitor check.
        default: disabled
        choices: ['enabled', 'disabled']
    name:
        description:
            - Specifies a unique name for the component.
        required: true
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        default: Common
    password:
        description:
            - Specifies the password if the monitored target requires authentication.
    recv:
        description:
            - Specifies the text string that the monitor looks for in the returned resource.
    recv_disable:
        description:
            - Specifies a text string that the monitor looks for in the returned resource.
    reverse:
        description:
            - Specifies whether the monitor operates in reverse mode.
        default: disabled
        choices: ['enabled', 'disabled']
    send:
        description:
            - Specifies the text string that the monitor sends to the target object.
        default: GET /
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
        choices: ['enabled', 'disabled']
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
- name: Create LTM HTTPS Monitor
  f5bigip_ltm_monitor_https:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_https_monitor
    partition: Common
    send: "http send string"
    recv: "http receive string"
    state: present
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_LTM_MONITOR_HTTPS_ARGS = dict(
    adaptive=dict(type='str', choices=F5_ACTIVATION_CHOICES),
    adaptive_divergence_type=dict(type='str', choices=['relative', 'absolute']),
    adaptive_divergence_value=dict(type='int'),
    adaptive_limit=dict(type='int'),
    adaptive_sampling_timespan=dict(type='int'),
    app_service=dict(type='str'),
    cert=dict(type='str'),
    cipherlist=dict(type='str'),
    compatibility=dict(type='str', choices=F5_ACTIVATION_CHOICES),
    defaults_from=dict(type='str'),
    description=dict(type='str'),
    destination=dict(type='str'),
    interval=dict(type='int'),
    ip_dscp=dict(type='int'),
    key=dict(type='str'),
    manual_resume=dict(type='str', choices=F5_ACTIVATION_CHOICES),
    password=dict(type='str', no_log=True),
    recv=dict(type='str'),
    recv_disable=dict(type='str'),
    reverse=dict(type='str', choices=F5_ACTIVATION_CHOICES),
    send=dict(type='str'),
    time_until_up=dict(type='int'),
    timeout=dict(type='int'),
    transparent=dict(type='str', choices=F5_ACTIVATION_CHOICES),
    up_interval=dict(type='int'),
    username=dict(type='str')
)


class F5BigIpLtmMonitorHttps(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create': self.mgmt_root.tm.ltm.monitor.https_s.https.create,
            'read': self.mgmt_root.tm.ltm.monitor.https_s.https.load,
            'update': self.mgmt_root.tm.ltm.monitor.https_s.https.update,
            'delete': self.mgmt_root.tm.ltm.monitor.https_s.https.delete,
            'exists': self.mgmt_root.tm.ltm.monitor.https_s.https.exists
        }


def main():
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_MONITOR_HTTPS_ARGS, supports_check_mode=True)

    try:
        obj = F5BigIpLtmMonitorHttps(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
