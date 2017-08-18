#!/usr/bin/python
#
# Copyright 2016, Eric Jacob <erjac77@gmail.com>
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
module: f5bigip_sys_failover
short_description: BIG-IP sys failover module
description:
    - Configures failover for a BIG-IP unit in a redundant system configuration..
version_added: 2.3
author:
    - "Gabriel Fortin"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    offline:
        description:
            - Changes the status of a unit or cluster to Forced Offline.
        required: false
        default: null
        choices: ['false', 'true']
        aliases: []
    online:
        description:
            - Changes the status of a unit or cluster from Forced Offline to either Active or Standby, depending upon the status of the other unit or cluster in a redundant system configuration.
        required: false
        default: null
        choices: ['false', 'true']
        aliases: []
    standby:
        description:
            - Specifies that the active unit or cluster fails over to a Standby state, causing the standby unit or cluster to become Active.
        required: false
        default: null
        choices: ['false', 'true']
        aliases: []
    traffic_group:
        description:
            - Specifies the traffic-group that should fail over to the Standby state, the traffic-group will become Active on another device.
        required: false
        default: null
        choices: []
        aliases: []
'''

EXAMPLES = '''
- name: Run SYS Failover
  f5bigip_sys_failover:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    online: True
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *
import re
import time

BIGIP_SYS_FAILOVER_ARGS = dict(
    online          =   dict(type='bool'),
    offline         =   dict(type='bool'),
    standby         =   dict(type='bool'),
    traffic_group   =   dict(type='str')
)

class F5BigIpSysFailover(F5BigIpUnnamedObject):
    def set_crud_methods(self):
        self.methods = {
            'read':             self.mgmt_root.tm.sys.failover.load,
            'update':           self.mgmt_root.tm.sys.failover.update,
            'run':              self.mgmt_root.tm.sys.failover.exec_cmd
        }
  
    def get_failover_state(self):
        return re.findall('[A-z]+', self.methods['read']().attrs['apiRawValues']['apiAnonymous'])[1]
    
    def run(self):
        # Remove empty params
        params = dict((k, v) for k, v in self.params.iteritems() if v is not None)

        before = self.get_failover_state()

        self.methods['run']('run', **params)
        time.sleep(0.3)

        if self.get_failover_state() != before:
            has_changed = True
        else:
            has_changed = False

        return { 'Failover state': self.get_failover_state(), 'changed': has_changed }

def main():
    # Translation list for conflictual params
    tr = {}

    module = AnsibleModuleF5BigIpUnnamedObject(argument_spec=BIGIP_SYS_FAILOVER_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpSysFailover(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.run()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()