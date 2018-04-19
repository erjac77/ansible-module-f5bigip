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
module: f5bigip_ltm_monitor_soap
short_description: BIG-IP ltm monitor soap module
description:
    - Configures a Simple Object Access Protocol (SOAP) monitor.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    app_service:
        description:
            - Specifies the name of the application service to which the monitor belongs.
    debug:
        description:
            - Specifies whether the monitor sends error messages and additional information to a log file created and
              labeled specifically for this monitor.
        default: no
        choices: ['no', 'yes']
    defaults_from:
        description:
            - Specifies the type of monitor you want to use to create the new monitor.
        default: soap
    description:
        description:
            - User defined description.
    destination:
        description:
            - Specifies the IP address and service port of the resource that is the destination of this monitor.
    expect_fault:
        description:
            - Specifies whether the value of the method option causes the monitor to expect a SOAP fault message.
        default: no
        choices: ['no', 'yes']
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
    method:
        description:
            - Specifies the method by which the monitor contacts the resource.
    name:
        description:
            - Specifies a unique name for the component.
        required: true
    namespace:
        description:
            - Specifies the name space for the Web service you are monitoring, for example, http://example.com/.
    parameter_name:
        description:
            - If the method has a parameter, specifies the name of that parameter.
    parameter_type:
        description:
            - Specifies the parameter type.
        default: bool
        choices: ['bool', 'int', 'long', 'string']
    parameter_value:
        description:
            - Specifies the value for the parameter.
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        default: Common
    password:
        description:
            - Specifies the password if the monitored target requires authentication.
    protocol:
        description:
            - Specifies the protocol that the monitor uses to communicate with the target, http or https.
        default: http
        choices: ['http', 'https']
    return_type:
        description:
            - ['bool', 'char', 'double', 'int', 'long', 'short', 'string']
        default: bool
    return_value:
        description:
            - Specifies the value for the returned parameter.
    soap_action:
        description:
            - Specifies the value for the SOAPAction header.
        default: ''
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
    up_interval:
        description:
            - Specifies, in seconds, the frequency at which the system issues the monitor check when the resource is up.
        default: 0
    url_path:
        description:
            - Specifies the URL for the Web service that you are monitoring, for example, /services/myservice.aspx.
    username:
        description:
            - Specifies the user name if the monitored target requires authentication.
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
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

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_LTM_MONITOR_SOAP_ARGS = dict(
    app_service=dict(type='str'),
    debug=dict(type='str', choices=F5_POLAR_CHOICES),
    defaults_from=dict(type='str'),
    description=dict(type='str'),
    destination=dict(type='str'),
    expect_fault=dict(type='str', choices=F5_POLAR_CHOICES),
    interval=dict(type='int'),
    manual_resume=dict(type='str', choices=F5_ACTIVATION_CHOICES),
    method=dict(type='str'),
    namespace=dict(type='str'),
    parameter_name=dict(type='str'),
    parameter_type=dict(type='str', choices=['bool', 'int', 'long', 'string']),
    parameter_value=dict(type='str'),
    password=dict(type='str', no_log=True),
    protocol=dict(type='str', choices=['http', 'https']),
    return_type=dict(type='str', choices=['bool', 'char', 'double', 'int', 'long', 'short', 'string']),
    return_value=dict(type='str'),
    soap_action=dict(type='str'),
    time_until_up=dict(type='int'),
    timeout=dict(type='int'),
    up_interval=dict(type='int'),
    url_path=dict(type='str'),
    username=dict(type='str')
)


class F5BigIpLtmMonitorSoap(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create': self.mgmt_root.tm.ltm.monitor.soaps.soap.create,
            'read': self.mgmt_root.tm.ltm.monitor.soaps.soap.load,
            'update': self.mgmt_root.tm.ltm.monitor.soaps.soap.update,
            'delete': self.mgmt_root.tm.ltm.monitor.soaps.soap.delete,
            'exists': self.mgmt_root.tm.ltm.monitor.soaps.soap.exists
        }


def main():
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_MONITOR_SOAP_ARGS, supports_check_mode=True)

    try:
        obj = F5BigIpLtmMonitorSoap(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
