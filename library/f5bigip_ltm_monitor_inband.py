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
module: f5bigip_ltm_monitor_inband
short_description: BIG-IP ltm monitor inband module
description:
    - Configures an Inband (passive) monitor.
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
        default: inband
    description:
        description:
            - Specifies descriptive text that identifies the component.
    failure_interval:
        description:
            - Specifies an interval, in seconds. If the number of failures specified in the failures option occurs
              within this interval, the system marks the pool member as being unavailable.
        default: 30
    failures:
        description:
            - Specifies the number of failures that the system allows to occur, within the time period specified in the
              failure-interval option, before marking a pool member unavailable.
        default: 3
    name:
        description:
            - Specifies a unique name for the component.
        required: true
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        default: Common
    response_time:
        description:
            - Specfies an amount of time, in seconds.
        default: 0
    retry_time:
        description:
            - Specifies the amount of time in seconds after the pool member has been marked unavailable before the
              system retries to connect to the pool member.
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Create LTM Monitor Inband
  f5bigip_ltm_monitor_inband:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_inband_monitor
    partition: Common
    description: My inband monitor
    state: present
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_LTM_MONITOR_INBAND_ARGS = dict(
    app_service=dict(type='str'),
    defaults_from=dict(type='str'),
    description=dict(type='str'),
    failure_interval=dict(type='int'),
    failures=dict(type='int'),
    response_time=dict(type='int'),
    retry_time=dict(type='int')
)


class F5BigIpLtmMonitorInband(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create': self.mgmt_root.tm.ltm.monitor.inbands.inband.create,
            'read': self.mgmt_root.tm.ltm.monitor.inbands.inband.load,
            'update': self.mgmt_root.tm.ltm.monitor.inbands.inband.update,
            'delete': self.mgmt_root.tm.ltm.monitor.inbands.inband.delete,
            'exists': self.mgmt_root.tm.ltm.monitor.inbands.inband.exists
        }


def main():
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_MONITOR_INBAND_ARGS, supports_check_mode=True)

    try:
        obj = F5BigIpLtmMonitorInband(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
