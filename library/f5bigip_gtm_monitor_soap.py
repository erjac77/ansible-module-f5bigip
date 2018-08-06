#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2016-2018, Eric Jacob <erjac77@gmail.com>
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
module: f5bigip_gtm_monitor_soap
short_description: BIG-IP gtm soap monitor module
description:
    - Configures a Simple Object Access Protocol (SOAP) monitor.
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
            - Specifies the type of monitor you want to use to create the new monitor.
        default: soap
    description:
        description:
            - User defined description.
    destination:
        description:
            - Specifies the IP address and service port of the resource that is the destination of this monitor.
        default: '*:*'
    expect_fault:
        description:
            - Specifies whether the value of the method option causes the monitor to expect a SOAP fault message.
        default: no
        choices: ['no', 'yes']
    ignore_down_response:
        description:
            - Specifies whether the monitor ignores a down response from the system it is monitoring.
        default: disabled
        choices: ['enabled', 'disabled']
    interval:
        description:
            - Specifies, in seconds, the frequency at which the system issues the monitor check when either the resource
              is down or the status of the resource is unknown.
        default: 30
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
    probe_timeout:
        description:
            - Specifies the number of seconds after which the BIG-IP system times out the probe request to the BIG-IP system.
        default: 5
    protocol:
        description:
            - Specifies the protocol that the monitor uses to communicate with the target.
    return_type:
        description:
            - Specifies the type for the returned parameter.
        default: bool
    return_value:
        description:
            - Specifies the value for the returned parameter.
    soap_action:
        description:
            - Specifies the value for the SOAPAction header.
        default: ""
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    timeout:
        description:
            - Specifies the number of seconds the target has in which to respond to the monitor request.
        default: 120
    url_path:
        description:
            - Specifies the URL for the Web service that you are monitoring, for example, /services/myservice.aspx.
    username:
        description:
            - Specifies the username, if the monitored target requires authentication.
requirements:
    - BIG-IP >= 12.0
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Create GTM SOAP Monitor
  f5bigip_gtm_monitor_soap:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_soap_monitor
    partition: Common
    state: present
  delegate_to: localhost
'''

RETURN = ''' # '''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.base import F5_ACTIVATION_CHOICES
from ansible_common_f5.base import F5_POLAR_CHOICES
from ansible_common_f5.base import F5_NAMED_OBJ_ARGS
from ansible_common_f5.base import F5_PROVIDER_ARGS
from ansible_common_f5.bigip import F5BigIpNamedObject


class ModuleParams(object):
    @property
    def argument_spec(self):
        argument_spec = dict(
            debug=dict(type='str', choices=F5_POLAR_CHOICES),
            defaults_from=dict(type='str'),
            description=dict(type='str'),
            destination=dict(type='str'),
            expect_fault=dict(type='str', choices=F5_POLAR_CHOICES),
            ignore_down_response=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            interval=dict(type='int'),
            method=dict(type='str'),
            namespace=dict(type='str'),
            parameter_name=dict(type='str'),
            parameter_type=dict(type='str'),
            parameter_value=dict(type='str'),
            password=dict(type='str', no_log=True),
            probe_timeout=dict(type='int'),
            protocol=dict(type='str'),
            return_type=dict(type='str'),
            return_value=dict(type='str'),
            soap_action=dict(type='str'),
            timeout=dict(type='int'),
            url_path=dict(type='str'),
            username=dict(type='str')
        )
        argument_spec.update(F5_PROVIDER_ARGS)
        argument_spec.update(F5_NAMED_OBJ_ARGS)
        return argument_spec

    @property
    def supports_check_mode(self):
        return False


class F5BigIpGtmMonitorHttp(F5BigIpNamedObject):
    def _set_crud_methods(self):
        self._methods = {
            'create': self._api.tm.gtm.monitor.soaps.soap.create,
            'read': self._api.tm.gtm.monitor.soaps.soap.load,
            'update': self._api.tm.gtm.monitor.soaps.soap.update,
            'delete': self._api.tm.gtm.monitor.soaps.soap.delete,
            'exists': self._api.tm.gtm.monitor.soaps.soap.exists
        }


def main():
    params = ModuleParams()
    module = AnsibleModule(argument_spec=params.argument_spec, supports_check_mode=params.supports_check_mode)

    try:
        obj = F5BigIpGtmMonitorHttp(check_mode=module.supports_check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
