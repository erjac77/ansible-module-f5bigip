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
module: f5bigip_ltm_virtual
short_description: BIG-IP ltm virtual server module
description:
    - Configures a virtual server.
version_added: 2.3
author:
    - "Eric Jacob, @erjac77"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
	all:
        description:
            - Specifies that you want to modify all of the existing components of the specified type.
        required: false
        default: null
        choices: [true, false]
        aliases: []
        version_added: 2.3
    address_status:
        description:
            - Specifies whether the virtual will contribute to the operational status of the associated virtual-address.
        required: false
        default: yes
        choices: ['yes', 'no']
        aliases: []
        version_added: 2.3
    auth:
        description:
            - Specifies a list of authentication profile names, separated by spaces, that the virtual server uses to manage authentication.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    auto_lasthop:
        description:
            - TODO
        required: false
        default: default
        choices: ['default', 'enabled', 'disabled']
        aliases: []
        version_added: 2.3
    cmp_enabled:
        description:
            - Enables or disables clustered multi-processor (CMP) acceleration.
        required: false
        default: yes
        choices: ['yes', 'no']
        aliases: []
        version_added: 2.3
    connection_limit:
        description:
            - Specifies the maximum number of concurrent connections you want to allow for the virtual server.
        required: false
        default: null
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
    destination:
        description:
            - Specifies the name of the virtual address and service on which the virtual server listens for connections.
        required: false
        default: any:any
        choices: []
        aliases: []
        version_added: 2.3
    dhcp_relay:
        description:
            - Specifies a virtual server that relays all received dhcp requests to all pool members.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    disabled:
        description:
            - Specifies the state of the virtual server.
        required: false
        default: false
        choices: [true, false]
        aliases: []
        version_added: 2.3
    enabled:
        description:
            - Specifies the state of the virtual server.
        required: false
        default: true
        choices: [true, false]
        aliases: []
        version_added: 2.3
    fallback_persistence:
        description:
            - Specifies a fallback persistence profile for the virtual server to use when the default persistence profile is not available.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    flow_eviction_policy:
        description:
            - Specifies a flow eviction policy for the virtual server to use, to select which flows to terminate when the number of connections approaches the connection limit on the virtual server.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    fw_enforced_policy:
        description:
            - Specifies an enforced firewall policy.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    fw_staged_policy:
        description:
            - Specifies a staged firewall policy.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    gtm_score:
        description:
            - Specifies a score that is associated with the virtual server.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    http_class:
        description:
            - Specifies a list of HTTP class profiles, separated by spaces, with which the virtual server works to increase the speed at which the virtual server processes HTTP requests.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    ip_forward:
        description:
            - Specifies a virtual server that has no pool members to load balance, but instead, forwards the packet directly to the destination IP address specified in the client request.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    ip_protocol:
        description:
            - Specifies the IP protocol for which you want the virtual server to direct traffic.
        required: false
        default: any
        choices: []
        aliases: []
        version_added: 2.3
    internal:
        description:
            - Specifies an internal virtual server that handles requests for a parent virtual server, such as content adaptation.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    l2_forward:
        description:
            - Specifies a virtual server that shares the same IP address as a node in an associated VLAN.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    last_hop_pool:
        description:
            - Specifies the name of the last hop pool that you want the virtual server to use to direct reply traffic to the last hop router.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    mask:
        description:
            - Specifies the netmask for a network virtual server only.
        required: false
        default: 255.255.255.255 for IPv4 or ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff for IPv6
        choices: []
        aliases: []
        version_added: 2.3
    mirror:
        description:
            - Enables or disables mirroring.
        required: false
        default: none
        choices: ['disabled', 'enabled', 'none']
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
    nat64:
        description:
            - Enable or disable NAT64.
        required: false
        default: disabled
        choices: ['disabled', 'enabled']
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
    pool:
        description:
            - Specifies a default pool to which you want the virtual server to automatically direct traffic.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    rate_class:
        description:
            - Specifies the name of an existing rate class that you want the virtual server to use to enforce a throughput policy for incoming network traffic.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    rate_limit:
        description:
            - Specifies the maximum number of connections per second allowed for a virtual server.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    rate_limit_mode:
        description:
            - Indicates whether the rate limit is applied per virtual object, per source address, per destination address, or some combination thereof.
        required: false
        default: object
        choices: ['destination', 'object', 'object-destination', 'object-source', 'object-source-destination', 'source', 'source-destination']
        aliases: []
        version_added: 2.3
    rate_limit_dst_mask:
        description:
            - Specifies a mask, in bits, to be applied to the destination address as part of the rate limiting.
        required: false
        default: 0
        choices: []
        aliases: []
        version_added: 2.3
    rate_limit_src_mask:
        description:
            - Specifies a mask, in bits, to be applied to the source address as part of the rate limiting.
        required: false
        default: 0
        choices: []
        aliases: []
        version_added: 2.3
    related_rules:
        description:
            - Specifies a list of iRules, that customize the behavior of secondary channels (for instance the data channel on FTP) opened on behalf of the virtual server.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    reject:
        description:
            - Specifies that the BIG-IP system rejects any traffic destined for the virtual server IP address.
        required: false
        default: null
        choices: [true, false]
        aliases: []
        version_added: 2.3
    rules:
        description:
            - Specifies a list of iRules, that customize the virtual server to direct and manage traffic.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    source:
        description:
            - Specifies an IP address or network from which the virtual server will accept traffic.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    source_port:
        description:
            - Specifies whether the system preserves the source port of the connection.
        required: false
        default: preserve
        choices: ['change', 'preserve', 'preserve-strict']
        aliases: []
        version_added: 2.3
    traffic_classes:
        description:
            - Specifies a list of traffic classes that are associated with the virtual server.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    translate_address:
        description:
            - Enables or disables address translation for the virtual server.
        required: false
        default: disabled.
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    translate_port:
        description:
            - Enables or disables port translation.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    vlans:
        description:
            - Specifies a list of VLANs on which the virtual server is either enabled or disabled.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    vlans_disabled:
        description:
            - Disables the virtual server on the VLANs specified in the vlans option.
        required: false
        default: true
        choices: [true, false]
        aliases: []
        version_added: 2.3
    vlans_enabled:
        description:
            - Enables the virtual server on the VLANs specified in the vlans option.
        required: false
        default: false
        choices: [true, false]
        aliases: []
        version_added: 2.3
'''

EXAMPLES = '''
- name: Create LTM Virtual Server
  f5bigip_ltm_virtual:
    f5bigip_hostname: 172.16.227.35
    f5bigip_username: admin
    f5bigip_password: admin
    f5bigip_port: 443
    name: my_http_vs
    description: my http vs
    partition: Common
    destination: 10.10.20.201:80
    state: present
  delegate_to: localhost
'''

from ansible_common_f5bigip.f5bigip import *

BIGIP_LTM_VIRTUAL_ARGS = dict(
    all                 		=    dict(type='bool'),
    address_status      		=    dict(type='str', choices=F5BIGIP_POLAR_CHOICES),
    #app_service        	 	 =    dict(type='str'),
    auth                		=    dict(type='list'),
    auto_lasthop        		=    dict(type='str', choices=['default', 'enabled', 'disabled']),
    #clone_pools         		 =    dict(type='list'),
    cmp_enabled         		=    dict(type='str', choices=F5BIGIP_POLAR_CHOICES),
    connection_limit    		=    dict(type='int'),
    description 				=    dict(type='str'),
    destination 				=    dict(type='str'),
    dhcp_relay          		=    dict(type='bool'),
    disabled             	 	=    dict(type='bool'),
    enabled              		=    dict(type='bool'),
    fallback_persistence		=    dict(type='str'),
    flow_eviction_policy		=    dict(type='str'),
    fw_enforced_policy			=    dict(type='str'),
    #fw_rules 					 =    dict(type='list'),
    fw_staged_policy			=    dict(type='list'),
    gtm_score					=    dict(type='int'),
    http_class					=    dict(type='str'),
    ip_forward					=    dict(type='bool'),
    ip_protocol					=    dict(type='str'),
    internal					=    dict(type='bool'),
    l2_forward					=    dict(type='bool'),
    last_hop_pool 				=    dict(type='str'),
    #metadata                    =    dict(type='list'),
    mask 						=    dict(type='str'),
    mirror 						=    dict(type='str', choices=['disabled', 'enabled', 'none']),
    nat64 						=    dict(type='str', choices=F5BIGIP_ACTIVATION_CHOICES),
    #persist 					 =    dict(type='list'),
    pool 						=    dict(type='str'),
    #profiles 					=    dict(type='list'),
    rate_class 					=    dict(type='str'),
    rate_limit 					=    dict(type='int'),
    rate_limit_mode 			=    dict(type='str', choices=['destination', 'object', 'object-destination', 'object-source', 'object-source-destination', 'source', 'source-destination']),
    rate_limit_dst_mask			=    dict(type='int'),
    rate_limit_src_mask			=    dict(type='int'),
    related_rules 				=    dict(type='str'),
    reject						=    dict(type='bool'),
    rules 						=    dict(type='list'),
    source 						=    dict(type='str'),
    #source_address_translation  =    dict(type='list'),
    source_port 				=    dict(type='str', choices=['change', 'preserve', 'preserve-strict']),
    traffic_classes 			=    dict(type='list'),
    translate_address 			=    dict(type='str', choices=F5BIGIP_ACTIVATION_CHOICES),
    translate_port 				=    dict(type='str', choices=F5BIGIP_ACTIVATION_CHOICES),
    vlans 						=    dict(type='list'),
    vlans_disabled				=    dict(type='bool'),
    vlans_enabled				=    dict(type='bool')
)

class F5BigIpLtmVirtual(F5BigIpObject):
    def _set_crud_methods(self):
        self.methods = {
            'create':self.mgmt.tm.ltm.virtuals.virtual.create,
            'read':self.mgmt.tm.ltm.virtuals.virtual.load,
            'update':self.mgmt.tm.ltm.virtuals.virtual.update,
            'delete':self.mgmt.tm.ltm.virtuals.virtual.delete,
            'exists':self.mgmt.tm.ltm.virtuals.virtual.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}
    
    module = AnsibleModuleF5BigIpObject(
        argument_spec=BIGIP_LTM_VIRTUAL_ARGS,
        supports_check_mode=False,
        mutually_exclusive=[
            ['dhcp_relay', 'ip_forward', 'l2_forward', 'reject'],
            ['enabled', 'disabled'],
            ['vlans_enabled', 'vlans_disabled']
        ]
    )
    
    try:
        obj = F5BigIpLtmVirtual(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':  
    main()