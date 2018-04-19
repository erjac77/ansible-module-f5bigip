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
module: f5bigip_ltm_monitor_oracle
short_description: BIG-IP ltm monitor oracle module
description:
    - Configures an Oracle monitor.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    app_service:
        description:
            - Specifies the name of the application service to which the monitor belongs.
    count:
        description:
            - Specifies the number of monitor probes after which the connection to the database will be terminated.
        default: 0
    database:
        description:
            - Specifies the name of the database with which the monitor attempts to communicate.
    debug:
        description:
            - Specifies whether the monitor sends error messages and additional information to a log file created and
              labeled specifically for this monitor.
        default: no
        choices: ['no', 'yes']
    defaults_from:
        description:
            - Specifies the name of the monitor from which you want your custom monitor to inherit settings.
        default: oracle
    description:
        description:
            - User defined description.
    destination:
        description:
            - Specifies the IP address and service port of the resource that is the destination of this monitor.
    interval:
        description:
            - Specifies, in seconds, the frequency at which the system issues the monitor check when either the resource
              is down or the status of the resource is unknown.
        default: 30
    manual_resume:
        description:
            - Specifies whether the system automatically changes the status of a resource to up at the next successful
              monitor check.
        default: disabled
        choices: ['disabled', 'enabled']
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
    recv_column:
        description:
            - Specifies the column in the database where the system expects the specified Receive String to be located.
    recv_row:
        description:
            - Specifies the row in the database where the system expects the specified Receive String to be located.
    send:
        description:
            - Specifies the SQL query that the monitor sends to the target database, for example, SELECT count(*) FROM
              mytable.
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
        default: 91
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
- name: Create LTM Monitor Oracle
  f5bigip_ltm_monitor_oracle:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_oracle_monitor
    partition: Common
    description: My oracle monitor
    state: present
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_LTM_MONITOR_ORACLE_ARGS = dict(
    app_service=dict(type='str'),
    count=dict(type='int'),
    database=dict(type='str'),
    debug=dict(type='str', choices=F5_POLAR_CHOICES),
    defaults_from=dict(type='str'),
    description=dict(type='str'),
    destination=dict(type='str'),
    interval=dict(type='int'),
    manual_resume=dict(type='str', choices=F5_ACTIVATION_CHOICES),
    password=dict(type='str', no_log=True),
    recv=dict(type='str'),
    recv_column=dict(type='str'),
    recv_row=dict(type='str'),
    send=dict(type='str'),
    time_until_up=dict(type='int'),
    timeout=dict(type='int'),
    up_interval=dict(type='int'),
    username=dict(type='str')
)


class F5BigIpLtmMonitorOracle(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create': self.mgmt_root.tm.ltm.monitor.oracles.oracle.create,
            'read': self.mgmt_root.tm.ltm.monitor.oracles.oracle.load,
            'update': self.mgmt_root.tm.ltm.monitor.oracles.oracle.update,
            'delete': self.mgmt_root.tm.ltm.monitor.oracles.oracle.delete,
            'exists': self.mgmt_root.tm.ltm.monitor.oracles.oracle.exists
        }


def main():
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_MONITOR_ORACLE_ARGS, supports_check_mode=True)

    try:
        obj = F5BigIpLtmMonitorOracle(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
