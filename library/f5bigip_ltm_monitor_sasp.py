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
module: f5bigip_ltm_monitor_sasp
short_description: BIG-IP ltm monitor sasp module
description:
    - Configures a Server Application State Protocol (SASP) monitor.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    app_service:
        description:
            - Specifies the name of the application service to which the monitor belongs.
    defaults_from:
        description:
            - Specifies the name of the monitor from which you want your custom monitor to inherit settings.
        default: sasp
    description:
        description:
            - User defined description.
    interval:
        description:
            - Specifies the frequency at which the system issues the monitor check.
        default: auto
    mode:
        description:
            - Specifies whether the load balancer should send Get Weight Request messages (pull) or receive Send Weights
              messages (push) from the GWM.
        default: pull
        choices: ['pull', 'push']
    name:
        description:
            - Specifies a unique name for the component.
        required: true
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        default: Common
    primary_address:
        description:
            - Specifies the IP address of the primary Group Workload Manager.
    protocol:
        description:
            - Specifies the protocol that the monitor uses to communicate with the target.
        default: tcp
        choices: ['tcp', 'udp']
    secondary_address:
        description:
            - Specifies the IP address of the secondary Group Workload Manager.
    service:
        description:
            - Specifies the port through which the SASP monitor communicates with the Group Workload Manager.
        default: 3860
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
        default: 100
requirements:
    - BIG-IP >= 12.0
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Create LTM Monitor SASP
  f5bigip_ltm_monitor_sasp:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_sasp_monitor
    partition: Common
    description: My sasp monitor
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
            app_service=dict(type='str'),
            defaults_from=dict(type='str'),
            description=dict(type='str'),
            interval=dict(type='int'),
            mode=dict(type='str', choices=['pull', 'push']),
            primary_address=dict(type='str'),
            protocol=dict(type='str', choices=['tcp', 'udp']),
            secondary_address=dict(type='str'),
            service=dict(type='int'),
            time_until_up=dict(type='int'),
            timeout=dict(type='int')
        )
        argument_spec.update(F5_PROVIDER_ARGS)
        argument_spec.update(F5_NAMED_OBJ_ARGS)
        return argument_spec

    @property
    def supports_check_mode(self):
        return True


class F5BigIpLtmMonitorSasp(F5BigIpNamedObject):
    def _set_crud_methods(self):
        self._methods = {
            'create': self._api.tm.ltm.monitor.sasps.sasp.create,
            'read': self._api.tm.ltm.monitor.sasps.sasp.load,
            'update': self._api.tm.ltm.monitor.sasps.sasp.update,
            'delete': self._api.tm.ltm.monitor.sasps.sasp.delete,
            'exists': self._api.tm.ltm.monitor.sasps.sasp.exists
        }


def main():
    params = ModuleParams()
    module = AnsibleModule(argument_spec=params.argument_spec, supports_check_mode=params.supports_check_mode)

    try:
        obj = F5BigIpLtmMonitorSasp(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
