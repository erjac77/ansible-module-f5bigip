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
module: f5bigip_ltm_monitor_ldap
short_description: BIG-IP ltm monitor ldap module
description:
    - Configures a Lightweight Directory Access Protocol (LDAP) monitor.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    app_service:
        description:
            - Specifies the name of the application service to which the monitor belongs.
    base:
        description:
            - Specifies the location in the LDAP tree from which the monitor starts the health check.
    chase_referrals:
        description:
            - Specifies whether the monitor upon receipt of an LDAP referral entry chases that referral.
        default: yes
        choices: ['no', 'yes']
    debug:
        description:
            - Specifies whether the monitor sends error messages and additional information to a log file created and labeled specifically for this monitor.
        default: no
        choices: ['no', 'yes']
    defaults_from:
        description:
            - Specifies the name of the monitor from which you want your custom monitor to inherit settings.
        default: ldap
    description:
        description:
            - Specifies descriptive text that identifies the component.
    destination:
        description:
            - Specifies the IP address and service port of the resource that is the destination of this monitor.
    filter:
        description:
            - Specifies an LDAP key for which the monitor searches.
    interval:
        description:
            - Specifies, in seconds, the frequency at which the system issues the monitor check when either the resource is down or the status of the resource is unknown.
        default: 10
    mandatory_attributes:
        description:
            - Specifies whether the target must include attributes in its response to be considered up.
        default: no
        choices: ['no', 'yes']
    manual_resume:
        description:
            - Specifies whether the system automatically changes the status of a resource to up at the next successful monitor check.
        default: disabled
        choices: ['disabled', 'enabled']
    name:
        description:
            - Specifies a unique name for the component.
        required: true
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        default: Common
    password:
        description:
            - Specifies the password if the monitored target requires authentication.
    security:
        description:
            - Specifies the secure communications protocol that the monitor uses to communicate with the target.
        choices: ['none', 'ssl', 'tls']
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    time_until_up:
        description:
            - Specifies the amount of time, in seconds, after the first successful response before a node is marked up.
        default: 0
    timeout:
        description:
            - Specifies the number of seconds the target has in which to respond to the monitor request.
        default: 31
    up_interval:
        description:
            - Specifies, in seconds, the frequency at which the system issues the monitor check when the resource is up.
        default: 0
    username:
        description:
            - Specifies the username, if the monitored target requires authentication.
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Create LTM Monitor LDAP
  f5bigip_ltm_monitor_ldap:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_ldap_monitor
    partition: Common
    description: My ldap monitor
    state: present
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_LTM_MONITOR_LDAP_ARGS = dict(
    app_service             =   dict(type='str'),
    base                    =   dict(type='str'),
    chase_referrals         =   dict(type='str', choices=F5_POLAR_CHOICES),
    debug                   =   dict(type='str', choices=F5_POLAR_CHOICES),
    defaults_from           =   dict(type='str'),
    description             =   dict(type='str'),
    destination             =   dict(type='str'),
    filter                  =   dict(type='str'),
    interval                =   dict(type='int'),
    mandatory_attributes    =   dict(type='str', choices=F5_POLAR_CHOICES),
    manual_resume           =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    password                =   dict(type='str', no_log=True),
    security                =   dict(type='str', choices=['none', 'ssl', 'tls']),
    time_until_up           =   dict(type='int'),
    timeout                 =   dict(type='int'),
    up_interval             =   dict(type='int'),
    username                =   dict(type='str')
)

class F5BigIpLtmMonitorLdap(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.monitor.ldaps.ldap.create,
            'read':     self.mgmt_root.tm.ltm.monitor.ldaps.ldap.load,
            'update':   self.mgmt_root.tm.ltm.monitor.ldaps.ldap.update,
            'delete':   self.mgmt_root.tm.ltm.monitor.ldaps.ldap.delete,
            'exists':   self.mgmt_root.tm.ltm.monitor.ldaps.ldap.exists
        }

def main():
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_MONITOR_LDAP_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpLtmMonitorLdap(check_mode=module.supports_check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

if __name__ == '__main__':
    main()