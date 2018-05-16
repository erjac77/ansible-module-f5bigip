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
module: f5bigip_sys_db
short_description: BIG-IP sys db module
description:
    - Displays or modifies bigdb database entries.
version_added: "2.4"
author:
    - "Eric Jacob (@erjac77)"
options:
    name:
        description:
            - Specifies unique name for the component.
        required: true
    value:
        description:
            - Specifies the value to which you want to set the specified database entry.
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Disable SYS DB Setup Utility Wizard
  f5bigip_sys_db:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: 'setup.run'
    value: 'false'
  delegate_to: localhost
'''

RETURN = ''' # '''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.base import AnsibleF5Error
from ansible_common_f5.base import F5_NAMED_OBJ_ARGS
from ansible_common_f5.base import F5_PROVIDER_ARGS
from ansible_common_f5.bigip import F5BigIpNamedObject


class ModuleParams(object):
    @property
    def argument_spec(self):
        argument_spec = dict(
            # reset_to_default=dict(type='bool'),
            value=dict(type='str')
        )
        argument_spec.update(F5_PROVIDER_ARGS)
        argument_spec.update(F5_NAMED_OBJ_ARGS)
        del argument_spec['partition']
        return argument_spec

    @property
    def supports_check_mode(self):
        return True


class F5BigIpSysDb(F5BigIpNamedObject):
    def _set_crud_methods(self):
        self._methods = {
            'read': self._api.tm.sys.dbs.db.load,
            'update': self._api.tm.sys.dbs.db.update,
            'exists': self._api.tm.sys.dbs.db.exists
        }

    def _create(self):
        raise AnsibleF5Error("%s does not support create" % self.__class__.__name__)

    def _delete(self):
        raise AnsibleF5Error("%s does not support delete" % self.__class__.__name__)

    def flush(self):
        result = dict()

        has_changed = self._present()

        result.update(dict(changed=has_changed))
        return result


def main():
    params = ModuleParams()
    module = AnsibleModule(argument_spec=params.argument_spec, supports_check_mode=params.supports_check_mode)

    try:
        obj = F5BigIpSysDb(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
