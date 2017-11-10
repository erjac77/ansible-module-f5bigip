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
module: f5bigip_ltm_monitor_soap
short_description: BIG-IP ltm monitor soap module
description:
    - Configures a Simple Object Access Protocol (SOAP) monitor.
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
            - Specifies the name of the application service to which the monitor belongs.
        required: false
        default: none
        choices: []
        aliases: []
    debug:
        description:
            - Specifies whether the monitor sends error messages and additional information to a log file created and labeled specifically for this monitor.
        required: false
        default: no
        choices: ['no', 'yes']
        aliases: []
    defaults_from:
        description:
            - Specifies the type of monitor you want to use to create the new monitor.
        required: false
        default: soap
        choices: []
        aliases: []
    description:
        description:
            - User defined description.
        required: false
        default: null
        choices: []
        aliases: []
    destination:
        description:
            - Specifies the IP address and service port of the resource that is the destination of this monitor.
        required: false
        default: null
        choices: []
        aliases: []
    expect_fault:
        description:
            - Specifies whether the value of the method option causes the monitor to expect a SOAP fault message.
        required: false
        default: no
        choices: ['no', 'yes']
        aliases: []
    interval:
        description:
            - Specifies, in seconds, the frequency at which the system issues the monitor check when either the resource is down or the status of the resource is unknown.
        required: false
        default: 5
        choices: []
        aliases: []
    manual_resume:
        description:
            - Specifies whether the system automatically changes the status of a resource to up at the next successful monitor check.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
        aliases: []
    method:
        description:
            - Specifies the method by which the monitor contacts the resource.
        required: false
        default: null
        choices: []
        aliases: []
    name:
        description:
            - Specifies a unique name for the component.
        required: true
        default: null
        choices: []
        aliases: []
    namespace:
        description:
            - Specifies the name space for the Web service you are monitoring, for example, http://example.com/.
        required: false
        default: none
        choices: []
        aliases: []
    parameter_name:
        description:
            - If the method has a parameter, specifies the name of that parameter.
        required: false
        default: none
        choices: []
        aliases: []
    parameter_type:
        description:
            - Specifies the parameter type.
        required: false
        default: bool
        choices: ['bool', 'int', 'long', 'string']
        aliases: []
    parameter_value:
        description:
            - Specifies the value for the parameter..
        required: false
        default: none
        choices: []
        aliases: []
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        required: false
        default: Common
        choices: []
        aliases: []
    password:
        description:
            - Specifies the password if the monitored target requires authentication.
        required: false
        default: none
        choices: []
        aliases: []
    protocol:
        description:
            - Specifies the protocol that the monitor uses to communicate with the target, http or https.
        required: false
        default: http
        choices: ['http', 'https']
        aliases: []
    return_type:
        description:
            - ['bool', 'char', 'double', 'int', 'long', 'short', 'string']
        required: false
        default: bool
        choices: []
        aliases: []
    return_value:
        description:
            - Specifies the value for the returned parameter.
        required: false
        default: none
        choices: []
        aliases: []
    soap_action:
        description:
            - Specifies the value for the SOAPAction header.
        required: false
        default: ''
        choices: []
        aliases: []
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        required: false
        default: present
        choices: ['absent', 'present']
        aliases: []
    time_until_up:
        description:
            - Specifies the amount of time, in seconds, after the first successful response before a node is marked up.
        required: false
        default: 0
        choices: []
        aliases: []
    timeout:
        description:
            - Specifies the number of seconds the target has in which to respond to the monitor request.
        required: false
        default: 16
        choices: []
        aliases: []
    up_interval:
        description:
            - Specifies, in seconds, the frequency at which the system issues the monitor check when the resource is up.
        required: false
        default: 0
        choices: []
        aliases: []
    url_path:
        description:
            - Specifies the URL for the Web service that you are monitoring, for example, /services/myservice.aspx.
        required: false
        default: none
        choices: []
        aliases: []
    username:
        description:
            - Specifies the user name if the monitored target requires authentication.
        required: false
        default: none
        choices: []
        aliases: []
'''

EXAMPLES = '''
- name: Create LTM Monitor SOAP
  f5bigip_ltm_monitor_soap:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_soap_monitor
    partition: Common
    description: My soap monitor
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_LTM_MONITOR_SOAP_ARGS = dict(
    app_service        =    dict(type='str'),
    debug              =    dict(type='str', choices=F5_POLAR_CHOICES),
    defaults_from      =    dict(type='str'),
    description        =    dict(type='str'),
    destination        =    dict(type='str'),
    expect_fault       =    dict(type='str', choices=F5_POLAR_CHOICES),
    interval           =    dict(type='int'),
    manual_resume      =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    method             =    dict(type='str'),
    namespace          =    dict(type='str'),
    parameter_name     =    dict(type='str'),
    parameter_type     =    dict(type='str', choices=['bool', 'int', 'long', 'string']),
    parameter_value    =    dict(type='str'),
    password           =    dict(type='str'),
    protocol           =    dict(type='str', choices=['http', 'https']),
    return_type        =    dict(type='str', choices=['bool', 'char', 'double', 'int', 'long', 'short', 'string']),
    return_value       =    dict(type='str'),
    soap_action        =    dict(type='str'),
    time_until_up      =    dict(type='int'),
    timeout            =    dict(type='int'),
    up_interval        =    dict(type='int'),
    url_path           =    dict(type='str'),
    username           =    dict(type='str')
)

class F5BigIpLtmMonitorSoap(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.monitor.soaps.soap.create,
            'read':     self.mgmt_root.tm.ltm.monitor.soaps.soap.load,
            'update':   self.mgmt_root.tm.ltm.monitor.soaps.soap.update,
            'delete':   self.mgmt_root.tm.ltm.monitor.soaps.soap.delete,
            'exists':   self.mgmt_root.tm.ltm.monitor.soaps.soap.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}

    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_MONITOR_SOAP_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpLtmMonitorSoap(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()