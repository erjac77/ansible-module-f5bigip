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
module: f5bigip_ltm_monitor_https
short_description: BIG-IP ltm https monitor module
description:
    - Configures a Hypertext Transfer Protocol over Secure Socket Layer (HTTPS) monitor.
version_added: 2.3
author:
    - "Eric Jacob, @erjac77"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    adaptive:
        description:
            - Specifies whether the adaptive feature is enabled for this monitor.
        required: false
        default: null
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    adaptive_divergence_type:
        description:
            - Specifies whether the adaptive-divergence-value is relative or absolute.
        required: false
        default: null
        choices: ['relative', 'absolute']
        aliases: []
        version_added: 2.3
    adaptive_divergence_value:
        description:
            - Specifies how far from mean latency each monitor probe is allowed to be.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    adaptive_limit:
        description:
            - Specifies the hard limit, in milliseconds, which the probe is not allowed to exceed, regardless of the divergence value.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    adaptive_sampling_timespan:
        description:
            - Specifies the size of the sliding window, in seconds, which records probe history.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    app_service:
        description:
            - Specifies the application service to which the object belongs.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    cert:
        description:
            - Specifies a file object for a client certificate that the monitor sends to the target SSL server.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    cipherlist:
        description:
            - Specifies the list of ciphers for this monitor.
        required: false
        default: DEFAULT:+SHA:+3DES:+kEDH
        choices: []
        aliases: []
        version_added: 2.3
    compatibility:
        description:
            - Specifies, when enabled, that the SSL options setting (in OpenSSL) is set to ALL.
        required: false
        default: enabled.
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    defaults_from:
        description:
            - Specifies the name of the monitor from which you want your custom monitor to inherit settings.
        required: false
        default: http
        choices: []
        aliases: []
        version_added: 2.3
    description:
        description:
            - Specifies descriptive text that identifies the component.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    destination:
        description:
            - Specifies the IP address and service port of the resource that is the destination of this monitor.
        required: false
        default: *:*
        choices: []
        aliases: []
        version_added: 2.3
    interval:
        description:
            - Specifies, in seconds, the frequency at which the system issues the monitor check when either the resource is down or the status of the resource is unknown.
        required: false
        default: 5
        choices: []
        aliases: []
        version_added: 2.3
    ip_dscp:
        description:
            - Specifies the differentiated services code point (DSCP).
        required: false
        default: 0
        choices: []
        aliases: []
        version_added: 2.3
    key:
        description:
            - Specifies the RSA private key if the monitored target requires authentication.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    manual_resume:
        description:
            - Specifies whether the system automatically changes the status of a resource to up at the next successful monitor check.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    name:
        description:
            - Specifies a unique name for the component.
        required: true
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        required: false
        default: Common
        choices: []
        aliases: []
        version_added: 2.3
    password:
        description:
            - Specifies the password if the monitored target requires authentication.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    recv:
        description:
            - Specifies the text string that the monitor looks for in the returned resource.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    recv_disable:
        description:
            - Specifies a text string that the monitor looks for in the returned resource.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    reverse:
        description:
            - Specifies whether the monitor operates in reverse mode.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    send:
        description:
            - Specifies the text string that the monitor sends to the target object.
        required: false
        default: GET /
        choices: []
        aliases: []
        version_added: 2.3
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        required: false
        default: present
        choices: ['absent', 'present']
        aliases: []
        version_added: 2.3
    time_until_up:
        description:
            - Specifies the amount of time, in seconds, after the first successful response before a node is marked up.
        required: false
        default: 0
        choices: []
        aliases: []
        version_added: 2.3
    timeout:
        description:
            - Specifies the number of seconds the target has in which to respond to the monitor request.
        required: false
        default: 16
        choices: []
        aliases: []
        version_added: 2.3
    transparent:
        description:
            - Specifies whether the monitor operates in transparent mode.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    up_interval:
        description:
            - Specifies, in seconds, the frequency at which the system issues the monitor check when the resource is up.
        required: false
        default: 0
        choices: []
        aliases: []
        version_added: 2.3
    username:
        description:
            - Specifies the username, if the monitored target requires authentication.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
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

from ansible_common_f5.f5_bigip import *

BIGIP_LTM_MONITOR_HTTPS_ARGS = dict(
    adaptive                    =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    adaptive_divergence_type    =   dict(type='str', choices=['relative', 'absolute']),
    adaptive_divergence_value   =   dict(type='int'),
    adaptive_limit              =   dict(type='int'),
    adaptive_sampling_timespan  =   dict(type='int'),
    app_service                 =   dict(type='str'),
    cert                        =   dict(type='str'),
    cipherlist                  =   dict(type='str'),
    compatibility               =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    defaults_from               =   dict(type='str'),
    description                 =   dict(type='str'),
    destination                 =   dict(type='str'),
    interval                    =   dict(type='int'),
    ip_dscp                     =   dict(type='int'),
    key                         =   dict(type='str'),
    manual_resume               =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    password                    =   dict(type='str', no_log=True),
    recv                        =   dict(type='str'),
    recv_disable                =   dict(type='str'),
    reverse                     =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    send                        =   dict(type='str'),
    time_until_up               =   dict(type='int'),
    timeout                     =   dict(type='int'),
    transparent                 =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    up_interval                 =   dict(type='int'),
    username                    =   dict(type='str')
)

class F5BigIpLtmMonitorHttps(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.monitor.https_s.https.create,
            'read':     self.mgmt_root.tm.ltm.monitor.https_s.https.load,
            'update':   self.mgmt_root.tm.ltm.monitor.https_s.https.update,
            'delete':   self.mgmt_root.tm.ltm.monitor.https_s.https.delete,
            'exists':   self.mgmt_root.tm.ltm.monitor.https_s.https.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}
    
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_MONITOR_HTTPS_ARGS, supports_check_mode=False)
    
    try:
        obj = F5BigIpLtmMonitorHttps(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()