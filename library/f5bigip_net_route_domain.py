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

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: f5bigip_net_route_domain
short_description: BIG-IP net route-domain module
description:
    - Configures route-domains for traffic management.
version_added: 2.3
author:
    - "Eric Jacob, @erjac77"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    app_service:
        description:
            - Specifies the application service that the object belongs to.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    bwc_policy:
        description:
            - Configures the bandwidth control policy for the route-domain.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    connection_limit:
        description:
            - Configures the connection limit for the route domain.
        required: false
        default: 0
        choices: []
        aliases: []
        version_added: 2.3
    description:
        description:
            - Specifies descriptive text that identifies the component.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    flow_eviction_policy:
        description:
            - Specifies a flow eviction policy for the route domain to use, to select which flows to evict when the number of connections approaches the connection limit on the route domain.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    id:
        description:
            - Specifies a unique numeric identifier for the route-domain.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    name:
        description:
            - Specifies unique name for the component.
        required: true
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    parent:
        description:
            - Specifies the route domain the system searches when it cannot find a route in the configured domain.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        required: false
        default: Common
        choices: []
        aliases: []
        version_added: 2.3
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        required: false
        default: present
        choices: ['absent', 'present']
        aliases: []
        version_added: 2.3
    strict:
        description:
            - Specifies whether the system allows a connection to span route domains.
        required: false
        default: enabled
        choices: ['disabled', 'enabled']
        aliases: []
        version_added: 2.3
    vlans:
        description:
            - Specifies VLANs, by name, for the system to use in the route domain.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
'''

EXAMPLES = '''
- name: Create NET Route-Domain
  f5bigip_net_route_domain:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_route_domain
    partition: Common
    id: 1234
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_NET_ROUTE_DOMAIN_ARGS = dict(
    app_service             =   dict(type='str'),
    bwc_policy              =   dict(type='str'),
    connection_limit        =   dict(type='int'),
    description             =   dict(type='str'),
    flow_eviction_policy    =   dict(type='str'),
    fw_enforced_policy      =   dict(type='str'),
    #fw_rules                =   dict(type='list'),
    fw_staged_policy        =   dict(type='str'),
    id                      =   dict(type='int'),
    parent                  =   dict(type='str'),
    routing_protocol        =   dict(type='list'),
    strict                  =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    vlans                   =   dict(type='list')
)

class F5BigIpNetRouteDomain(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.net.route_domains.route_domain.create,
            'read':     self.mgmt_root.tm.net.route_domains.route_domain.load,
            'update':   self.mgmt_root.tm.net.route_domains.route_domain.update,
            'delete':   self.mgmt_root.tm.net.route_domains.route_domain.delete,
            'exists':   self.mgmt_root.tm.net.route_domains.route_domain.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}
    
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_NET_ROUTE_DOMAIN_ARGS, supports_check_mode=False)
    
    try:
        obj = F5BigIpNetRouteDomain(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()