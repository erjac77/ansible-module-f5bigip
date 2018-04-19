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
module: f5bigip_gtm_pool_member
short_description: BIG-IP gtm pool member module
description:
    - Configures a GTM pool member.
version_added: "2.4"
author:
    - "Eric Jacob (@erjac77)"
options:
    depends_on:
        description:
            - Specifies the name of the virtual server on which this pool member depends.
    description:
        description:
            - Specifies a user-defined description.
    disabled:
        description:
            - Specifies whether this pool member is available for load balancing.
        default: false
    enabled:
        description:
            - Specifies whether this pool member is available for load balancing.
        default: true
    limit_max_bps:
        description:
            - Specifies the maximum allowable data throughput rate, in bits per second, for the pool member.
        default: 0
    limit_max_bps_status:
        description:
            - Enables or disables the limit-max-bps option for this pool member.
        default: disabled
        choices: ['disabled', 'enabled']
    limit_max_connections:
        description:
            - Specifies the number of current connections allowed for this pool member.
        default: 0
    limit_max_connections_status:
        description:
            - Enables or disables the limit-max-connections option for this pool member.
        default: disabled
        choices: ['disabled', 'enabled']
    limit_max_pps:
        description:
            - Specifies the maximum allowable data transfer rate, in packets per second, for this pool member.
        default: 0
    limit_max_pps_status:
        description:
            - Enables or disables the limit-max-pps option for this pool member.
        default: disabled
        choices: ['disabled', 'enabled']
    monitor:
        description:
            - Enables or disables the monitor assigned to this pool member.
        default: enabled
        choices: ['disabled', 'enabled']
    name:
        description:
            - Specifies unique name for the component.
        required: true
    order:
        description:
            - Specifies the order number of the pool member.
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        default: Common
    pool:
        description:
            - Specifies the pool in which the member belongs.
        required: true
    ratio:
        description:
            - Specifies the weight of the pool member for load balancing purposes.
    vs_name:
        description:
            - Displays the name of the corresponding virtual server.
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Create GTM Pool Member
  f5bigip_gtm_pool_member:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: 'my_server:my_vs1'
    partition: Common
    pool: /Common/my_pool
    state: present
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *
from f5.bigip.resource import OrganizingCollection

BIGIP_GTM_POOL_MEMBER_ARGS = dict(
    app_service=dict(type='str'),
    depends_on=dict(type='list'),
    description=dict(type='str'),
    disabled=dict(type='bool'),
    enabled=dict(type='bool'),
    limit_max_bps=dict(type='int'),
    limit_max_bps_status=dict(type='str', choices=[F5_ACTIVATION_CHOICES]),
    limit_max_connections=dict(type='int'),
    limit_max_connections_status=dict(type='str', choices=[F5_ACTIVATION_CHOICES]),
    limit_max_pps=dict(type='int'),
    limit_max_pps_status=dict(type='str', choices=[F5_ACTIVATION_CHOICES]),
    monitor=dict(type='str', choices=[F5_ACTIVATION_CHOICES]),
    pool=dict(type='str'),
    order=dict(type='int'),
    ratio=dict(type='str', choices=[F5_ACTIVATION_CHOICES])
)


class F5BigIpGtmPoolMember(F5BigIpNamedObject):
    def set_crud_methods(self):
        if isinstance(self.mgmt_root.tm.gtm.pools, OrganizingCollection):
            self.pool = self.mgmt_root.tm.gtm.pools.a_s.a.load(**self._get_resource_id_from_path(self.params['pool']))
        else:
            self.pool = self.mgmt_root.tm.gtm.pools.pool.load(**self._get_resource_id_from_path(self.params['pool']))
        self.methods = {
            'create': self.pool.members_s.member.create,
            'read': self.pool.members_s.member.load,
            'update': self.pool.members_s.member.update,
            'delete': self.pool.members_s.member.delete,
            'exists': self.pool.members_s.member.exists
        }
        del self.params['pool']


def main():
    module = AnsibleModuleF5BigIpNamedObject(
        argument_spec=BIGIP_GTM_POOL_MEMBER_ARGS,
        supports_check_mode=True,
        mutually_exclusive=[
            ['disabled', 'enabled']
        ]
    )

    try:
        obj = F5BigIpGtmPoolMember(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
