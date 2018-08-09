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
module: f5bigip_gtm_monitor_ldap
short_description: BIG-IP gtm monitor ldap module
description:
    - Configures a Lightweight Directory Access Protocol (LDAP) monitor.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
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
            - Specifies whether the monitor sends error messages and additional information to a log file created and
              labeled specifically for this monitor.
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
        default: '*:*'
    filter:
        description:
            - Specifies an LDAP key for which the monitor searches.
    ignore_down_response:
        description:
            - Specifies whether the monitor ignores a down response from the system it is monitoring.
        default: disabled
        choices: ['enabled', 'disabled']
    interval:
        description:
            - Specifies, in seconds, the frequency at which the system issues the monitor check when either the resource
              is down or the status of the resource is unknown.
        default: 10
    mandatory_attributes:
        description:
            - Specifies whether the target must include attributes in its response to be considered up.
        default: no
        choices: ['no', 'yes']
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
    probe_timeout:
        description:
            - Specifies the number of seconds after which the BIG-IP system times out the probe request to the BIG-IP system.
        default: 5
    security:
        description:
            - Specifies the secure communications protocol that the monitor uses to communicate with the target.
        choices: ['none', 'ssl', 'tls']
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    timeout:
        description:
            - Specifies the number of seconds the target has in which to respond to the monitor request.
        default: 31
    username:
        description:
            - Specifies the username, if the monitored target requires authentication.
requirements:
    - BIG-IP >= 12.0
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Create GTM Monitor LDAP
  f5bigip_gtm_monitor_ldap:
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

RETURN = ''' # '''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.base import F5_ACTIVATION_CHOICES
from ansible_common_f5.base import F5_NAMED_OBJ_ARGS
from ansible_common_f5.base import F5_POLAR_CHOICES
from ansible_common_f5.base import F5_PROVIDER_ARGS
from ansible_common_f5.bigip import F5BigIpNamedObject


class ModuleParams(object):
    @property
    def argument_spec(self):
        argument_spec = dict(
            base=dict(type='str'),
            chase_referrals=dict(type='str', choices=F5_POLAR_CHOICES),
            debug=dict(type='str', choices=F5_POLAR_CHOICES),
            defaults_from=dict(type='str'),
            description=dict(type='str'),
            destination=dict(type='str'),
            filter=dict(type='str'),
            ignore_down_response=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            interval=dict(type='int'),
            mandatory_attributes=dict(type='str', choices=F5_POLAR_CHOICES),
            password=dict(type='str', no_log=True),
            probe_timeout=dict(type='int'),
            security=dict(type='str', choices=['none', 'ssl', 'tls']),
            timeout=dict(type='int'),
            username=dict(type='str')
        )
        argument_spec.update(F5_PROVIDER_ARGS)
        argument_spec.update(F5_NAMED_OBJ_ARGS)
        return argument_spec

    @property
    def supports_check_mode(self):
        return True


class F5BigIpGtmMonitorLdap(F5BigIpNamedObject):
    def _set_crud_methods(self):
        self._methods = {
            'create': self._api.tm.gtm.monitor.ldaps.ldap.create,
            'read': self._api.tm.gtm.monitor.ldaps.ldap.load,
            'update': self._api.tm.gtm.monitor.ldaps.ldap.update,
            'delete': self._api.tm.gtm.monitor.ldaps.ldap.delete,
            'exists': self._api.tm.gtm.monitor.ldaps.ldap.exists
        }


def main():
    params = ModuleParams()
    module = AnsibleModule(argument_spec=params.argument_spec, supports_check_mode=params.supports_check_mode)

    try:
        obj = F5BigIpGtmMonitorLdap(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
