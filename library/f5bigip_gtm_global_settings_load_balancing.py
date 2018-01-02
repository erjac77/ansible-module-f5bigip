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
module: f5bigip_gtm_global_settings_load_balancing
short_description: BIG-IP gtm global-settings load-balancing module
description:
    - Configures the load-balancing settings for the Global Traffic Manager.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    ignore_path_ttl:
        description:
            - Specifies, when set to yes, that dynamic load balancing methods can use path data, even after the
              time-to-live (TTL) for the path data expires.
        default: no
        choices: ['yes', 'no']
    respect_fallback_dependency:
        description:
            - Specifies, when set to yes, that the system accepts virtual server status when the load balancing mode
              changes to the mode specified by the fallback-mode option of the pool.
        default: no
        choices: ['yes', 'no']
    topology_longest_match:
        description:
            - Specifies, when set to yes, that the system evaluates all topology records in the topology statement, and
              then selects the topology record that most specifically matches the IP address in an LDNS request.
        choices: ['yes', 'no']
    verify_vs_availability:
        description:
            - Specifies, when set to yes, that the system checks the availability of virtual servers before sending a
              connection to those virtual servers.
        default: no
        choices: ['yes', 'no']
    port:
        description:
            - Specifies the port on which the listener listens for connections.
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Enable GTM Global Load-Balancing Settings ignore path ttl
  f5bigip_gtm_global_settings_load_balancing:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    ignore_path_ttl: yes
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_GTM_GLOBAL_SETTINGS_LOAD_BALANCING_ARGS = dict(
    ignore_path_ttl=dict(type='str', choices=F5_POLAR_CHOICES),
    respect_fallback_dependency=dict(type='str', choices=F5_POLAR_CHOICES),
    topology_longest_match=dict(type='str', choices=F5_POLAR_CHOICES),
    verify_vs_availability=dict(type='str', choices=F5_POLAR_CHOICES)
)


class F5BigIpGtmGlobalSettingsLoadBalancing(F5BigIpUnnamedObject):
    def set_crud_methods(self):
        self.methods = {
            'read': self.mgmt_root.tm.gtm.global_settings.load_balancing.load,
            'update': self.mgmt_root.tm.gtm.global_settings.load_balancing.update
        }


def main():
    module = AnsibleModuleF5BigIpUnnamedObject(argument_spec=BIGIP_GTM_GLOBAL_SETTINGS_LOAD_BALANCING_ARGS,
                                               supports_check_mode=False)

    try:
        obj = F5BigIpGtmGlobalSettingsLoadBalancing(check_mode=module.supports_check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
