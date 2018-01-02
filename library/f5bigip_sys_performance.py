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
module: f5bigip_sys_performance
short_description: BIG-IP sys performance module
description:
    - You can use the all-stats component to reset or display all system performance statistics.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    name:
        description:
            - Specifies which module to use. For the moment, only all-stats is available.
        choices: ['all-stats']
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Create SYS Performance
  f5bigip_sys_performance:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: all-stats
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_SYS_PERFORMANCE_ARGS = dict(
    name=dict(type='str', choices=['all-stats'], default='all-stats')
)


class F5BigIpSysPerformance(F5BigIpUnnamedObject):
    def set_crud_methods(self):
        self.methods = {
            'all_stats_read': self.mgmt_root.tm.sys.performances.all_stats.load
            # 'connections_read':     self.mgmt_root.tm.sys.performances.connections.load,
            # 'gtm_read':             self.mgmt_root.tm.sys.performances.gtm.load,
            # 'ramcache_read':        self.mgmt_root.tm.sys.performances.ramcache.load,
            # 'system_read':          self.mgmt_root.tm.sys.performances.system.load,
            # 'throughput_read':      self.mgmt_root.tm.sys.performances.throughput.load
        }

    def _read(self):
        if self.params['name'] == 'all-stats':
            return self.methods['all_stats_read']()
            # elif self.params['name'] == 'connections':
            #    return self.methods['connections_read']
            # elif self.params['name'] == 'ramcache':
            #    return self.methods['ramcache_read']
            # elif self.params['name'] == 'system' :
            #    return self.methods['system_read']
            # elif self.params['name'] == 'throughput':
            #    return self.methods['throughput_read']

    def get_stats(self):
        result = dict()
        stats = self._read()

        if hasattr(stats, 'apiRawValues'):
            result.update(dict(apiRawValues=stats.apiRawValues))
            result.update(dict(changed=True))
        else:
            result.update(dict(changed=False))

        return result


def main():
    module = AnsibleModuleF5BigIpUnnamedObject(argument_spec=BIGIP_SYS_PERFORMANCE_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpSysPerformance(check_mode=module.supports_check_mode, **module.params)
        result = obj.get_stats()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
