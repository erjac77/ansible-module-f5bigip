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
module: f5bigip_sys_db
short_description: BIG-IP sys db module
description:
    - Displays or modifies bigdb database entries.
version_added: 2.3
author:
    - "Eric Jacob, @erjac77"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    name:
        description:
            - Specifies unique name for the component.
        required: true
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    value:
        description:
            - Specifies the value to which you want to set the specified database entry.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
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

from ansible_common_f5.f5_bigip import *

BIGIP_SYS_DB_ARGS = dict(
    #reset_to_default    =   dict(type='bool'),
    value               =   dict(type='str')
)

class F5BigIpSysDb(F5BigIpNamedObject):
    #def __init__(self, *args, **kwargs):
    #    super(F5BigIpSysDb, self).__init__(*args, **kwargs)
    #    self.params.pop('partition', None)
    
    def set_crud_methods(self):
        self.methods = {
            'read':     self.mgmt_root.tm.sys.dbs.db.load,
            'update':   self.mgmt_root.tm.sys.dbs.db.update,
            'exists':   self.mgmt_root.tm.sys.dbs.db.exists
        }
        self.params.pop('partition', None)
    
    def _exists(self):
        if self._read():
            return True
        else:
            return False
    
    def _read(self):
        return self.methods['read'](
            name=self.params['name']
        )
    
    def _create(self):
        raise AnsibleModuleF5BigIpError("%s does not support create" % self.__class__.__name__)
    
    def _delete(self):
        raise AnsibleModuleF5BigIpError("%s does not support delete" % self.__class__.__name__)
    
    def flush(self):
        result = dict()
        
        has_changed = self._present()
        
        result.update(dict(changed=has_changed))
        return result

def main():
    # Translation list for conflictual params
    tr = {}
    
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_SYS_DB_ARGS, supports_check_mode=False)
    
    try:
        obj = F5BigIpSysDb(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()