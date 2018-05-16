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
module: f5bigip_ltm_monitor_wmi
short_description: BIG-IP ltm monitor wmi module
description:
    - Configures a Windows Management Infrastructure (WMI) monitor.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    agent:
        description:
            - Displays the agent for the monitor.
        default: 'Mozilla/4.0 (compatible: MSIE 5.0; Windows NT)'
    app_service:
        description:
            - Specifies the name of the application service to which the monitor belongs.
    command:
        description:
            - Specifies the command that the system uses to obtain the metrics from the resource.
    defaults_from:
        description:
            - Specifies the name of the monitor from which you want your custom monitor to inherit settings.
        default: wmi
    description:
        description:
            - User defined description.
    interval:
        description:
            - Specifies the frequency at which the system issues the monitor check.
        default: 5
    metrics:
        description:
            - Specifies the performance metrics that the commands collect from the target.
        default: 'LoadPercentage, DiskUsage, PhysicalMemoryUsage:1.5, VirtualMemoryUsage:2.0'
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
    url:
        description:
            - Specifies the URL that the monitor uses.
        default: /scripts/f5Isapi.dll
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
- name: Create LTM Monitor WMI
  f5bigip_ltm_monitor_wmi:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_wmi_monitor
    partition: Common
    description: My wmi monitor
    state: present
  delegate_to: localhost
'''

RETURN = ''' # '''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.base import F5_NAMED_OBJ_ARGS
from ansible_common_f5.base import F5_PROVIDER_ARGS
from ansible_common_f5.bigip import F5BigIpNamedObject


class ModuleParams(object):
    @property
    def argument_spec(self):
        argument_spec = dict(
            agent=dict(type='str'),
            app_service=dict(type='str'),
            command=dict(type='str'),
            defaults_from=dict(type='str'),
            description=dict(type='str'),
            interval=dict(type='int'),
            metrics=dict(type='str'),
            password=dict(type='str', no_log=True),
            time_until_up=dict(type='int'),
            timeout=dict(type='int'),
            url=dict(type='str'),
            username=dict(type='str')
        )
        argument_spec.update(F5_PROVIDER_ARGS)
        argument_spec.update(F5_NAMED_OBJ_ARGS)
        return argument_spec

    @property
    def supports_check_mode(self):
        return True


class F5BigIpLtmMonitorWmi(F5BigIpNamedObject):
    def _set_crud_methods(self):
        self._methods = {
            'create': self._api.tm.ltm.monitor.wmis.wmi.create,
            'read': self._api.tm.ltm.monitor.wmis.wmi.load,
            'update': self._api.tm.ltm.monitor.wmis.wmi.update,
            'delete': self._api.tm.ltm.monitor.wmis.wmi.delete,
            'exists': self._api.tm.ltm.monitor.wmis.wmi.exists
        }


def main():
    params = ModuleParams()
    module = AnsibleModule(argument_spec=params.argument_spec, supports_check_mode=params.supports_check_mode)

    try:
        obj = F5BigIpLtmMonitorWmi(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
