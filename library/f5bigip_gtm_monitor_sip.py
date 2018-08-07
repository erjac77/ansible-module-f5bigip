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
module: f5bigip_gtm_monitor_sip
short_description: BIG-IP gtm monitor sip module
description:
    - Configures a Session Initiation Protocol (SIP) monitor.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    cert:
        description:
            - Specifies a fully-qualified path for a client certificate that the monitor sends to the target SSL server.
    cipherlist:
        description:
            - Specifies the list of ciphers for this monitor.
    compatibility:
        description:
            - Specifies, when enabled, that the SSL options setting (in OpenSSL) is set to ALL.
        default: enabled
        choices: ['disabled', 'enabled']
    debug:
        description:
            - Specifies whether the monitor sends error messages and additional information to a log file created and
              labeled specifically for this monitor.
        default: no
        choices: ['no', 'yes']
    defaults_from:
        description:
            - Specifies the name of the monitor from which you want your custom monitor to inherit settings.
        default: sip
    description:
        description:
            - User defined description.
    destination:
        description:
            - Specifies the IP address and service port of the resource that is the destination of this monitor.
        default: '*:*'
    filter:
        description:
            - Specifies the SIP status codes that the target can return to be considered up.
        choices: ['any', 'none', 'status']
    filter_neg:
        description:
            - Specifies the SIP status codes that the target can return to be considered down.
        choices: ['any', 'none', 'status']
    headers:
        description:
            - Specifies the set of SIP headers in the SIP message that is sent to the target
    ignore_down_response:
        description:
            - Specifies whether the monitor ignores a down response from the system it is monitoring.
        default: disabled
        choices: ['disabled', 'enabled']
    interval:
        description:
            - Specifies the frequency at which the system issues the monitor check.
        default: 30
    key:
        description:
            - Specifies the key if the monitored target requires authentication
    mode:
        description:
            - Specifies the protocol that the monitor uses to communicate with the target.
        default: udp
        choices: ['sips', 'tcp', 'tls', 'udp']
    name:
        description:
            - Specifies a unique name for the component.
        required: true
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        default: Common
    probe_timeout:
        description:
            - Specifies the number of seconds after which the BIG-IP system times out the probe request to the
              BIG-IP system.
        default: 5
    request:
        description:
            - Specifies the SIP request line in the SIP message that is sent to the target.
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    username:
        description:
            - Specifies the username, if the monitored target requires authentication.
requirements:
    - BIG-IP >= 12.0
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Create GTM Monitor SIP
  f5bigip_gtm_monitor_sip:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_sip_monitor
    partition: Common
    description: My sip monitor
    state: present
  delegate_to: localhost
'''

RETURN = ''' # '''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.base import F5_ACTIVATION_CHOICES
from ansible_common_f5.base import F5_POLAR_CHOICES
from ansible_common_f5.base import F5_NAMED_OBJ_ARGS
from ansible_common_f5.base import F5_PROVIDER_ARGS
from ansible_common_f5.bigip import F5BigIpNamedObject


class ModuleParams(object):
    @property
    def argument_spec(self):
        argument_spec = dict(
            cert=dict(type='str'),
            cipherlist=dict(type='list'),
            compatibility=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            debug=dict(type='str', choices=F5_POLAR_CHOICES),
            defaults_from=dict(type='str'),
            description=dict(type='str'),
            destination=dict(type='str'),
            filter=dict(type='str', choices=['any', 'none', 'status']),
            filter_neg=dict(type='str', choices=['any', 'none', 'status']),
            headers=dict(type='str'),
            ignore_down_response=dict(type='str', chocies=F5_ACTIVATION_CHOICES),
            interval=dict(type='int'),
            key=dict(type='str'),
            mode=dict(type='str', choices=['sips', 'tcp', 'tls', 'udp']),
            probe_timeout=dict(type='int'),
            request=dict(type='str'),
            username=dict(type='str')
        )
        argument_spec.update(F5_PROVIDER_ARGS)
        argument_spec.update(F5_NAMED_OBJ_ARGS)
        return argument_spec

    @property
    def supports_check_mode(self):
        return False


class F5BigIpGtmMonitorSip(F5BigIpNamedObject):
    def _set_crud_methods(self):
        self._methods = {
            'create': self._api.tm.gtm.monitor.sips.sip.create,
            'read': self._api.tm.gtm.monitor.sips.sip.load,
            'update': self._api.tm.gtm.monitor.sips.sip.update,
            'delete': self._api.tm.gtm.monitor.sips.sip.delete,
            'exists': self._api.tm.gtm.monitor.sips.sip.exists
        }


def main():
    params = ModuleParams()
    module = AnsibleModule(argument_spec=params.argument_spec, supports_check_mode=params.supports_check_mode)

    try:
        obj = F5BigIpGtmMonitorSip(check_mode=module.supports_check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
