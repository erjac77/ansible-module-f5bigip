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
module: f5bigip_ltm_snat
short_description: BIG-IP ltm snat module
description:
    - You can use the snat component to configure a SNAT.
    - A SNAT defines the relationship between an externally visible IP address, SNAT IP address, or translated address,
      and a group of internal IP addresses, or originating addresses, of individual servers at your site.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    automap:
        description:
            - Specifies that the system translates the source IP address to an available self IP address when
              establishing connections through the virtual server.
        default: enabled
        choices: ['none', 'enabled']
    app_service:
        description:
            - Specifies the name of the application service to which this object belongs.
    description:
        description:
            - User-defined description.
    metadata:
        description:
            - Associates user defined data, each of which has name and value pair and persistence.
    mirror:
        description:
            - Enables or disables mirroring of SNAT connections.
    name:
        description:
            - Specifies unique name for the component.
        required: true
    origins:
        description:
            - Specifies a set of IP addresses and subnets from which connections originate.
        required: true
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        default: Common
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    snatpool:
        description:
            - Specifies the name of a SNAT pool.
    source_port:
        description:
            - Specifies whether the system preserves the source port of the connection.
        default: preserve
        choices: ['change', 'preserve', 'preserve-strict']
    translation:
        description:
            - Specifies the name of a translated IP address.
    vlans:
        description:
            - Specifies the name of the VLAN to which you want to assign the SNAT.
    vlans_disabled:
        description:
            - Disables the SNAT on all VLANs.
    vlans_enabled:
        description:
            - Enables the SNAT on all VLANs.
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Create LTM Snat
  f5bigip_ltm_snat:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_snat
    partition: Common
    description: My snat
    vlans: external
    vlans_enabled: true
    state: present
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_LTM_SNAT_ARGS = dict(
    auto_lasthop=dict(type='str', default='default'),
    automap=dict(type='bool'),
    app_service=dict(type='str'),
    description=dict(type='str'),
    metadata=dict(type='list'),
    mirror=dict(type='str', choices=['none', 'enabled', 'disabled'], default='disabled'),
    origins=dict(type='list'),
    snatpool=dict(type='str'),
    source_port=dict(type='str', choices=['change', 'preserve', 'preserve-strict'], default='preserve'),
    translation=dict(type='str'),
    vlans=dict(type='str'),
    vlans_disabled=dict(type='bool', default=True),
    vlans_enabled=dict(type='bool')
)


class F5BigIpLtmSnat(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create': self.mgmt_root.tm.ltm.snats.snat.create,
            'read': self.mgmt_root.tm.ltm.snats.snat.load,
            'update': self.mgmt_root.tm.ltm.snats.snat.update,
            'delete': self.mgmt_root.tm.ltm.snats.snat.delete,
            'exists': self.mgmt_root.tm.ltm.snats.snat.exists
        }


def main():
    module = AnsibleModuleF5BigIpNamedObject(
        argument_spec=BIGIP_LTM_SNAT_ARGS,
        supports_check_mode=False,
        mutually_exclusive=[
            ['vlans_disabled', 'vlans_enabled'],
            ['automap', 'snatpool']
        ]
    )

    try:
        obj = F5BigIpLtmSnat(check_mode=module.supports_check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
