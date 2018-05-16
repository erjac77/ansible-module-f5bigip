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
module: f5bigip_ltm_traffic_class
short_description: BIG-IP ltm traffic class module
description:
    - Configures a traffic class.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    app_service:
        description:
            - Specifies the application service to which the object belongs.
    classification:
        description:
            - Specifies the actual textual tag to be associated with the flow if the traffic class is matched.
        required: true
    description:
        description:
            - Specifies descriptive text that identifies the component.
    destination_address:
        description:
            - Specifies destination IP addresses for the system to use when evaluating traffic flow.
    destination_mask:
        description:
            - Specifies a destination IP address mask for the system to use when evaluating traffic flow.
    destination_port:
        description:
            - Specifies a destination port for the system to use when evaluating traffic flow.
        default: 0
    name:
        description:
            - Specifies a unique name for the component.
        required: true
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        default: Common
    protocol:
        description:
            - Specifies a protocol for the system to use when evaluating traffic flow.
        default: any
    source_address:
        description:
            - Specifies source IP addresses for the system to use when evaluating traffic flow.
    source_mask:
        description:
            - Specifies a source IP address mask for the system to use when evaluating traffic flow.
    source_port:
        description:
            - Specifies a source port for the system to use when evaluating traffic flow.
        default: 0
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Create LTM Traffic Class
  f5bigip_ltm_traffic_class:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_traffic_class
    partition: Common
    classification: traffic_class
    description: My ltm traffic class
    destination_port: 21
    protocol: tcp
    source_port: 21
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
            app_service=dict(type='str'),
            classification=dict(type='str'),
            description=dict(type='str'),
            destination_address=dict(type='str'),
            destination_mask=dict(type='str'),
            destination_port=dict(type='int'),
            file_name=dict(type='str'),
            protocol=dict(type='str'),
            source_address=dict(type='str'),
            source_mask=dict(type='str'),
            source_port=dict(type='int')
        )
        argument_spec.update(F5_PROVIDER_ARGS)
        argument_spec.update(F5_NAMED_OBJ_ARGS)
        return argument_spec

    @property
    def supports_check_mode(self):
        return True


class F5BigIpLtmTrafficClass(F5BigIpNamedObject):
    def _set_crud_methods(self):
        self._methods = {
            'create': self._api.tm.ltm.traffic_class_s.traffic_class.create,
            'read': self._api.tm.ltm.traffic_class_s.traffic_class.load,
            'update': self._api.tm.ltm.traffic_class_s.traffic_class.update,
            'delete': self._api.tm.ltm.traffic_class_s.traffic_class.delete,
            'exists': self._api.tm.ltm.traffic_class_s.traffic_class.exists
        }


def main():
    params = ModuleParams()
    module = AnsibleModule(argument_spec=params.argument_spec, supports_check_mode=params.supports_check_mode)

    try:
        obj = F5BigIpLtmTrafficClass(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
