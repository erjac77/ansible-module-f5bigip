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
stdout:
    description: The output of the command.
    returned: success
    type: list
    sample:
        - ['...', '...']
stdout_lines:
    description: A list of strings, each containing one item per line from the original output.
    returned: success
    type: list
    sample:
        - [['...', '...'], ['...'], ['...']]
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.base import AnsibleF5Error
from ansible_common_f5.base import F5_PROVIDER_ARGS
from ansible_common_f5.bigip import F5BigIpUnnamedObject
from ansible_common_f5.utils import to_lines


class ModuleParams(object):
    @property
    def argument_spec(self):
        argument_spec = dict(
            name=dict(type='str', choices=['all-stats'], default='all-stats')
        )
        argument_spec.update(F5_PROVIDER_ARGS)
        return argument_spec

    @property
    def supports_check_mode(self):
        return True


class F5BigIpSysPerformance(F5BigIpUnnamedObject):
    def _set_crud_methods(self):
        self._methods = {
            'all_stats_read': self._api.tm.sys.performances.all_stats.load
            # 'connections_read':     self._api.tm.sys.performances.connections.load,
            # 'gtm_read':             self._api.tm.sys.performances.gtm.load,
            # 'ramcache_read':        self._api.tm.sys.performances.ramcache.load,
            # 'system_read':          self._api.tm.sys.performances.system.load,
            # 'throughput_read':      self._api.tm.sys.performances.throughput.load
        }

    def _read(self):
        if self._params['name'] == 'all-stats':
            return self._methods['all_stats_read']()
            # elif self._params['name'] == 'connections':
            #    return self._methods['connections_read']
            # elif self._params['name'] == 'ramcache':
            #    return self._methods['ramcache_read']
            # elif self._params['name'] == 'system' :
            #    return self._methods['system_read']
            # elif self._params['name'] == 'throughput':
            #    return self._methods['throughput_read']

    def flush(self):
        result = dict(changed=False, stdout=list())

        try:
            stats = self._read()
        except Exception:
            raise AnsibleF5Error("Unable to retrieve stats.")

        if hasattr(stats, 'apiRawValues'):
            result['stdout'].append(stats.apiRawValues['apiAnonymous'])

        result['stdout_lines'] = list(to_lines(result['stdout']))

        return result


def main():
    params = ModuleParams()
    module = AnsibleModule(argument_spec=params.argument_spec, supports_check_mode=params.supports_check_mode)

    try:
        obj = F5BigIpSysPerformance(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
