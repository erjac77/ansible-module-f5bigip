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
module: f5bigip_gtm_monitor_external
short_description: BIG-IP gtm monitor external module
description:
    - Configures an external monitor.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    args:
        description:
            - Specifies any command-line arguments that the external program requires.
    defaults_from:
        description:
            - Specifies the name of the monitor from which you want your custom monitor to inherit settings.
        default: external
    description:
        description:
            - Specifies descriptive text that identifies the component.
    destination:
        description:
            - Specifies the IP address and service port of the resource that is the destination of this monitor.
        default: '*:*'
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
    name:
        description:
            - Specifies a unique name for the component.
        required: true
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        default: Common
    probe_timeout:
        description:
            - Specifies the number of seconds after which the BIG-IP system times out the probe request to the BIG-IP system.
        default: 5
    run:
        description:
            - Specifies the path and file name of a program to run as the external monitor, for example
              /config/monitors/myMonitor.
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    timeout:
        description:
            - Specifies the number of seconds the target has in which to respond to the monitor request.
        default: 120
    user_defined:
        description:
            - Specifies any user-defined command-line arguments and variables that the external program requires.
requirements:
    - BIG-IP >= 12.0
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Create GTM Monitor External
  f5bigip_gtm_monitor_external:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_external_monitor
    partition: Common
    description: My external monitor
    state: present
  delegate_to: localhost
'''

RETURN = ''' # '''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.base import F5_ACTIVATION_CHOICES
from ansible_common_f5.base import F5_NAMED_OBJ_ARGS
from ansible_common_f5.base import F5_PROVIDER_ARGS
from ansible_common_f5.bigip import F5BigIpNamedObject


class ModuleParams(object):
    @property
    def argument_spec(self):
        argument_spec = dict(
            args=dict(type='str'),
            defaults_from=dict(type='str'),
            description=dict(type='str'),
            destination=dict(type='str'),
            ignore_down_response=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            interval=dict(type='int'),
            probe_timeout=dict(type='int'),
            run=dict(type='str'),
            timeout=dict(type='int'),
            user_defined=dict(type='str')
        )
        argument_spec.update(F5_PROVIDER_ARGS)
        argument_spec.update(F5_NAMED_OBJ_ARGS)
        return argument_spec

    @property
    def supports_check_mode(self):
        return True


class F5BigIpGtmMonitorExternal(F5BigIpNamedObject):
    def _set_crud_methods(self):
        self._methods = {
            'create': self._api.tm.gtm.monitor.externals.external.create,
            'read': self._api.tm.gtm.monitor.externals.external.load,
            'update': self._api.tm.gtm.monitor.externals.external.update,
            'delete': self._api.tm.gtm.monitor.externals.external.delete,
            'exists': self._api.tm.gtm.monitor.externals.external.exists
        }


def main():
    params = ModuleParams()
    module = AnsibleModule(argument_spec=params.argument_spec, supports_check_mode=params.supports_check_mode)

    try:
        obj = F5BigIpGtmMonitorExternal(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
