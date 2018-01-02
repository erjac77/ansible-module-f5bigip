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
module: f5bigip_gtm_listener
short_description: BIG-IP gtm listener module
description:
    - Configures a Global Traffic Manager listener.
version_added: "2.4"
author:
    - "Eric Jacob (@erjac77)"
options:
    address:
        description:
            - Specifies the IP address on which the system listens.
        required: true
    advertise:
        description:
            - Specifies whether to advertise the listener address to surrounding routers.
        default: no
        choices: ['yes', 'no']
    app_service:
        description:
            - Specifies the application service that the object belongs to.
    auto_lasthop:
        description:
            - Specifies whether to automatically map last hop for pools or not.
        default: default
        choices: ['default', 'enabled', 'disabled']
    description:
        description:
            - Specifies a user-defined description.
    disabled:
        description:
            - Specifies the state of the listener.
        default: false
    enabled:
        description:
            - Specifies the state of the listener.
        default: true
    fallback_persistence:
        description:
            - Specifies a fallback persistence profile for the listener to use when the default persistence profile is
              not available.
    ip_protocol:
        description:
            - Specifies the protocol on which this listener receives network traffic.
        default: udp
        choices: ['tcp', 'udp']
    last_hop_pool:
        description:
            - Specifies the name of the last hop pool that you want the listener to use to direct reply traffic to the
              last hop router.
    mask:
        description:
            - Specifies the netmask for a network listener only.
        default: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
    name:
        description:
            - Specifies unique name for the component.
        required: true
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        default: Common
    persist:
        description:
            - Specifies a list of profiles separated by spaces that the listener uses to manage connection persistence.
    pool:
        description:
            - Specifies a default pool to which you want the listener to automatically direct traffic.
        default: 5
    port:
        description:
            - Specifies the port on which the listener listens for connections.
    profiles:
        description:
            - Specifies the DNS, statistics and protocol profiles to use for this listener.
    rules:
        description:
            - Specifies a list of iRules, separated by spaces, that customize the listener to direct and manage traffic.
    source_address_translation:
        description:
            - Specifies the type of source address translation enabled for the listener as well as the pool that the
              source address translation will use.
    source_port:
        description:
            - Specifies whether the system preserves the source port of the connection.
        default: preserve
        choices: ['change', 'preserve', 'preserve-strict']
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    translate_address:
        description:
            - Enables or disables address translation for the listener.
        default: disabled
        choices: ['enabled', 'disabled']
    translate_port:
        description:
            - Enables or disables port translation.
        default: disabled
        choices: ['enabled', 'disabled']
    vlans:
        description:
            - Specifies a list of VLANs on which traffic is either disabled or enabled, based on the vlans-disabled and
              vlans-enabled settings.
    vlans_disabled:
        description:
            - Specifies that traffic will not be accepted by this listener on the VLANS specified in the vlans option.
    vlans_enabled:
        description:
            - Specifies that traffic will be accepted by this listener only on the VLANS specified in the vlans option.
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Create GTM Listener
  f5bigip_gtm_listener:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_listener
    partition: Common
    description: My listener
    address: 10.10.1.1
    persist: 
      - { name: dest_addr, partition: Common, tmDefault: 'yes' }
    source_address_translation: 
      type: automap
    state: present
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_GTM_LISTENER_ARGS = dict(
    address=dict(type='str'),
    advertise=dict(type='str'),
    app_service=dict(type='str'),
    auto_lasthop=dict(type='str', choices=['default', F5_ACTIVATION_CHOICES]),
    description=dict(type='str'),
    disabled=dict(type='bool'),
    enabled=dict(type='bool'),
    fallback_persistence=dict(type='str'),
    ip_protocol=dict(type='str', choices=['tcp', 'udp']),
    last_hop_pool=dict(type='str'),
    mask=dict(type='str'),
    persist=dict(type='list'),
    pool=dict(type='str'),
    port=dict(type='int'),
    profiles=dict(type='list'),
    rules=dict(type='list'),
    source_address_translation=dict(type='dict'),
    source_port=dict(type='str', choices=['change', 'preserve', 'preserve-strict']),
    translate_address=dict(type='str', choices=['default', F5_ACTIVATION_CHOICES]),
    translate_port=dict(type='str', choices=['default', F5_ACTIVATION_CHOICES]),
    vlans=dict(type='list'),
    vlans_disabled=dict(type='str', choices=['default', F5_ACTIVATION_CHOICES]),
    vlans_enabled=dict(type='str', choices=['default', F5_ACTIVATION_CHOICES])
)


class F5BigIpGtmListener(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create': self.mgmt_root.tm.gtm.listeners.listener.create,
            'read': self.mgmt_root.tm.gtm.listeners.listener.load,
            'update': self.mgmt_root.tm.gtm.listeners.listener.update,
            'delete': self.mgmt_root.tm.gtm.listeners.listener.delete,
            'exists': self.mgmt_root.tm.gtm.listeners.listener.exists
        }
        del self.params['partition']

        if self.params['source_address_translation']:
            if self.params['source_address_translation']['type'] == 'automap' and 'pool' in self.params[
                'source_address_translation']:
                raise AnsibleF5Error("Can't specify a pool when using automap")


def main():
    module = AnsibleModuleF5BigIpNamedObject(
        argument_spec=BIGIP_GTM_LISTENER_ARGS,
        supports_check_mode=False,
        mutually_exclusive=[
            ['disabled', 'enabled'],
            ['vlans_disabled', 'vlans_enabled']
        ]
    )

    try:
        obj = F5BigIpGtmListener(check_mode=module.supports_check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
