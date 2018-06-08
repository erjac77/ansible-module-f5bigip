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
module: f5bigip_shared_bigip_failover_state
short_description: BIG-IP shared bigip failover state module
description:
    - Displays bigip failover state.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
requirements:
    - BIG-IP >= 12.0
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Get Shared bigip failover state
  f5bigip_shared_bigip_failover_state:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
  delegate_to: localhost
  register: failover_status_resp

- name: Display the failover status of the device
  debug:
    msg: "Failover Status: {{ failover_status_resp.bigip_failover_state.failoverState }}"
'''

RETURN = ''' # '''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.base import AnsibleF5Error
from ansible_common_f5.base import F5_PROVIDER_ARGS
from ansible_common_f5.bigip import F5BigIpUnnamedObject


class ModuleParams(object):
    @property
    def argument_spec(self):
        argument_spec = dict()
        argument_spec.update(F5_PROVIDER_ARGS)
        return argument_spec

    @property
    def supports_check_mode(self):
        return True


class F5BigIpSharedBigipFailoverState(F5BigIpUnnamedObject):
    def _set_crud_methods(self):
        self._methods = {
            'read': self._api.tm.shared.bigip_failover_state.load
        }

    def flush(self):
        result = dict(changed=False)

        try:
            failover_state = self._methods['read']()
        except Exception:
            raise AnsibleF5Error("Cannot retrieve BIG-IP failover state information.")

        result.update(
            failover_state=failover_state.failoverState,
            is_enabled=failover_state.isEnabled,
            last_update_micros=failover_state.lastUpdateMicros,
            next_poll_time=failover_state.nextPollTime,
            poll_cycle_period_millis=failover_state.pollCyclePeriodMillis
        )

        return result


def main():
    params = ModuleParams()
    module = AnsibleModule(argument_spec=params.argument_spec, supports_check_mode=params.supports_check_mode)

    try:
        obj = F5BigIpSharedBigipFailoverState(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
