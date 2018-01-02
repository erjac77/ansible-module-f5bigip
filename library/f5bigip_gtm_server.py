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
module: f5bigip_gtm_server
short_description: BIG-IP gtm server module
description:
    - Configures servers for the Global Traffic Manager.
version_added: "2.4"
author:
    - "Eric Jacob (@erjac77)"
options:
    addresses:
        description:
            - Specifies the server IP addresses for the server.
        required: true
    app_service:
        description:
            - Specifies the application service to which the object belongs.
    datacenter:
        description:
            - Specifies the data center to which the server belongs.
        required: true
    description:
        description:
            - Specifies a user-defined description.
    disabled:
        description:
            - Specifies whether the data center and its resources are available for load balancing.
        default: false
    enabled:
        description:
            - Specifies whether the data center and its resources are available for load balancing.
        default: true
    expose_route_domains:
        description:
            - Allow the GTM server to auto-discover LTM virtual servers from all route domains.
        default: no
        choices: ['no', 'yes']
    iq_allow_path:
        description:
            - Specifies whether the Global Traffic Manager uses this BIG-IP system to conduct a path probe before
              delegating traffic to it.
        default: yes
        choices: ['no', 'yes']
    iq_allow_service_check:
        description:
            - Specifies whether the Global Traffic Manager uses this BIG-IP system to conduct a service check probe
              before delegating traffic to it.
        default: yes
        choices: ['no', 'yes']
    iq_allow_snmp:
        description:
            - Specifies whether the Global Traffic Manager uses this BIG-IP system to conduct an SNMP probe before
              delegating traffic to it.
        default: yes
        choices: ['no', 'yes']
    limit_cpu_usage:
        description:
            - For a server configured as a generic host, specifies the percent of CPU usage, otherwise has no effect.
        default: 0
    limit_cpu_usage_status:
        description:
            - Enables or disables the limit-cpu-usage option for this server.
        default: disabled
        choices: ['disabled', 'enabled']
    limit_mem_avail:
        description:
            - For a server configured as a generic host, specifies the available memory required by the virtual servers
              on the server.
        default: 0
    limit_mem_avail_status:
        description:
            - Enables or disables the limit-mem-avail option for this server.
        default: disabled
        choices: ['disabled', 'enabled']
    limit_max_bps:
        description:
            - Specifies the maximum allowable data throughput rate, in bits per second, for this server.
        default: 0
    limit_max_bps_status:
        description:
            - Enables or disables the limit-max-bps option for this server.
        default: disabled
        choices: ['disabled', 'enabled']
    limit_max_connections:
        description:
            - Specifies the number of current connections allowed for this server.
        default: 0
    limit_max_connections_status:
        description:
            - Enables or disables the limit-max-connections option for this server.
        default: disabled
        choices: ['disabled', 'enabled']
    limit_max_pps:
        description:
            - Specifies the maximum allowable data transfer rate, in packets per second, for this server.
        default: 0
    limit_max_pps_status:
        description:
            - Enables or disables the limit-max-pps option for this server.
        default: disabled
        choices: ['disabled', 'enabled']
    link_discovery:
        description:
            - Specifies whether the system auto-discovers the links for this server.
        default: disabled
        choices: ['disabled', 'enabled', 'enabled-no-delete']
    monitor:
        description:
            - Specifies the health monitors that the system uses to determine whether this server is available for load
              balancing.
    name:
        description:
            - Specifies unique name for the component.
        required: true
    prober_pool:
        description:
            - Specifies the name of a prober pool to use to monitor this server's resources.
    product:
        description:
            - Specifies the server type.
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    virtual_server_discovery:
        description:
            - Specifies whether the system auto-discovers the virtual servers for this server.
        choices: ['disabled', 'enabled', 'enabled-no-delete']
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Create GTM Server
  f5bigip_gtm_server:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_server
    addresses:
      - { name: 10.10.1.11, device-name: primary }
      - { name: 10.10.1.12, device-name: secondary }
    datacenter: /Common/my_datacenter
    description: My server
    product: redundant-bigip
    state: present
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_GTM_SERVER_ARGS = dict(
    addresses=dict(type='list'),
    app_service=dict(type='str'),
    datacenter=dict(type='str'),
    description=dict(type='str'),
    disabled=dict(type='bool'),
    enabled=dict(type='bool'),
    expose_route_domains=dict(type='str', choices=[F5_POLAR_CHOICES]),
    iq_allow_path=dict(type='str', choices=[F5_POLAR_CHOICES]),
    iq_allow_service_check=dict(type='str', choices=[F5_POLAR_CHOICES]),
    iq_allow_snmp=dict(type='str', choices=[F5_POLAR_CHOICES]),
    limit_cpu_usage=dict(type='int'),
    limit_cpu_usage_status=dict(type='str', choices=[F5_ACTIVATION_CHOICES]),
    limit_mem_avail=dict(type='int'),
    limit_mem_avail_status=dict(type='str', choices=[F5_ACTIVATION_CHOICES]),
    limit_max_bps=dict(type='int'),
    limit_max_bps_status=dict(type='str', choices=[F5_ACTIVATION_CHOICES]),
    limit_max_connections=dict(type='int'),
    limit_max_connections_status=dict(type='str', choices=[F5_ACTIVATION_CHOICES]),
    limit_max_pps=dict(type='int'),
    limit_max_pps_status=dict(type='str', choices=[F5_ACTIVATION_CHOICES]),
    link_discovery=dict(type='str', choices=[F5_ACTIVATION_CHOICES, 'enabled-no-delete']),
    # metadata=dict(type='list'),
    monitor=dict(type='str'),
    prober_pool=dict(type='str'),
    product=dict(type='str'),
    virtual_server_discovery=dict(type='str', choices=[F5_ACTIVATION_CHOICES, 'enabled-no-delete'])
)


class F5BigIpGtmServer(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create': self.mgmt_root.tm.gtm.servers.server.create,
            'read': self.mgmt_root.tm.gtm.servers.server.load,
            'update': self.mgmt_root.tm.gtm.servers.server.update,
            'delete': self.mgmt_root.tm.gtm.servers.server.delete,
            'exists': self.mgmt_root.tm.gtm.servers.server.exists
        }
        del self.params['partition']


def main():
    module = AnsibleModuleF5BigIpNamedObject(
        argument_spec=BIGIP_GTM_SERVER_ARGS,
        supports_check_mode=False,
        mutually_exclusive=[
            ['disabled', 'enabled']
        ]
    )

    try:
        obj = F5BigIpGtmServer(check_mode=module.supports_check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
