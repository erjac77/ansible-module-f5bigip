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
module: f5bigip_cm_trust_domain
short_description: BIG-IP cm trust domain module
description:
    - Manages a trust domain.
version_added: "2.4"
author:
    - "Eric Jacob (@erjac77)"
options:
    ca_devices:
        description:
            - Specifies a set of certificate authority devices in the trust domain.
    md5_fingerprint:
        description:
            - Specifies the SSL certificate fingerprint when verifying the identity of a new device.
    name:
        description:
            - Specifies unique name for the component.
        required: true
    non_ca_devices:
        description:
            - Specifies a set of subordinate devices in the trust domain.
    password:
        description:
            - Specifies the password for a new device.
        required: true
    serial:
        description:
            - Specifies the SSL certificate serial number when verifying the identity of a new device.
    sha1_fingerprint:
        description:
            - Specifies the SSL certificate fingerprint when verifying the identity of a new device.
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    username:
        description:
            - Specifies the user name required to log on to a device when adding the device to the trust domain.
        required: true
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Add device to CM Trust-Domain
  f5bigip_cm_trust_domain:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: Root
    ca_devices:
      - /Common/bigip1
    username: admin
    password: admin
    state: present
  delegate_to: localhost
'''

RETURN = ''' # '''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.base import F5_NAMED_OBJ_ARGS
from ansible_common_f5.base import F5_PROVIDER_ARGS
from ansible_common_f5.bigip import F5BigIpNamedObject


class ModuleParams(object):
    @property
    def argument_spec(self):
        argument_spec = dict(
            ca_devices=dict(type='list'),
            md5_fingerprint=dict(type='str'),
            non_ca_devices=dict(type='list'),
            password=dict(type='str', no_log=True),
            serial=dict(type='str'),
            sha1_fingerprint=dict(type='str'),
            username=dict(type='str')
        )
        argument_spec.update(F5_PROVIDER_ARGS)
        argument_spec.update(F5_NAMED_OBJ_ARGS)
        del argument_spec['partition']
        return argument_spec

    @property
    def supports_check_mode(self):
        return True

    @property
    def mutually_exclusive(self):
        return [
            ['ca_devices', 'non_ca_devices']
        ]


class F5BigIpCmTrustDomain(F5BigIpNamedObject):
    def _set_crud_methods(self):
        self._methods = {
            'read': self._api.tm.cm.trust_domains.trust_domain.load,
            'update': self._api.tm.cm.trust_domains.trust_domain.update,
            'exists': self._api.tm.cm.trust_domains.trust_domain.exists
        }


def main():
    params = ModuleParams()
    module = AnsibleModule(argument_spec=params.argument_spec, supports_check_mode=params.supports_check_mode,
                           mutually_exclusive=params.mutually_exclusive)

    try:
        obj = F5BigIpCmTrustDomain(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
