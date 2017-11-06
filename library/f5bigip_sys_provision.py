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

DOCUMENTATION = '''
---
module: f5bigip_sys_provision
short_description: BIG-IP SYS provision module
description:
    - Configures provisioning on the BIG-IP system.
version_added: 2.3
author:
    - "Gabriel Fortin"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    cpu_ratio:
        description:
            - Use this option only when the level option is set to custom.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    disk_ratio:
        description:
            - Use this option only when the level option is set to custom.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    level:
        description:
            - Specifies the level of resources that you want to provision for a module.
        required: false
        default: null
        choices: ['custom', 'dedicated', 'minimum', 'nominal', 'none']
        aliases: []
        version_added: 2.3
    memory_ratio:
        description:
            - Use this option only when the level option is set to custom.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    name:
        description:
            - Specifies which module to use.
        required: true
        default: null
        choices: []
        aliases: []
        version_added: 2.3
'''

EXAMPLES = '''
- name: 
  f5bigip_sys_provision:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: gtm
    level: minimal
    state: present
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

BIGIP_SYS_PROVISION_ARGS = dict(
    cpu_ratio       =   dict(type='int'),
    disk_ratio      =   dict(type='int'),
    level           =   dict(type='str', choices=['custom', 'dedicated', 'minimum', 'nominal', 'none']),
    memory_ratio    =   dict(type='int'),
    name            =   dict(type='str', choices=['afm', 'am', 'apm', 'asm', 'avr', 'fps', 'gtm', 'lc', 'ltm', 'pem', 'swg']),
)

class F5BigIpSysProvision(F5BigIpUnnamedObject):

    def set_crud_methods(self):
        self.methods = {
            'afm_read':     self.mgmt_root.tm.sys.provision.afm.load,
            'afm_update':   self.mgmt_root.tm.sys.provision.afm.update,
            'am_read':      self.mgmt_root.tm.sys.provision.am.load,
            'am_update':    self.mgmt_root.tm.sys.provision.am.update,
            'apm_read':     self.mgmt_root.tm.sys.provision.apm.load,
            'apm_update':   self.mgmt_root.tm.sys.provision.apm.update,
            'asm_read':     self.mgmt_root.tm.sys.provision.asm.load,
            'asm_update':   self.mgmt_root.tm.sys.provision.asm.update,
            'avr_read':     self.mgmt_root.tm.sys.provision.avr.load,
            'avr_update':   self.mgmt_root.tm.sys.provision.avr.update,
            'fps_read':     self.mgmt_root.tm.sys.provision.fps.load,
            'fps_update':   self.mgmt_root.tm.sys.provision.fps.update,
            'gtm_read':     self.mgmt_root.tm.sys.provision.gtm.load,
            'gtm_update':   self.mgmt_root.tm.sys.provision.gtm.update,
            'lc_read':      self.mgmt_root.tm.sys.provision.lc.load,
            'lc_update':    self.mgmt_root.tm.sys.provision.lc.update,
            'ltm_read':     self.mgmt_root.tm.sys.provision.ltm.load,
            'ltm_update':   self.mgmt_root.tm.sys.provision.ltm.update,
            'pem_read':     self.mgmt_root.tm.sys.provision.pem.load,
            'pem_update':   self.mgmt_root.tm.sys.provision.pem.update,
            'swg_read':     self.mgmt_root.tm.sys.provision.swg.load
        }
        
    def _read(self):
        if self.params['name'] == 'afm':
            return self.methods['afm_read']()
        elif self.params['name'] == 'am':
            return self.methods['am_read']()
        elif self.params['name'] == 'apm':
            return self.methods['apm_read']()
        elif self.params['name'] == 'asm':
            return self.methods['asm_read']()
        elif self.params['name'] == 'avr':
            return self.methods['avr_read']()
        elif self.params['name'] == 'fps':
            return self.methods['fps_read']()
        elif self.params['name'] == 'gtm':
            return self.methods['gtm_read']()
        elif self.params['name'] == 'lc':
            return self.methods['lc_read']()
        elif self.params['name'] == 'ltm':
            return self.methods['ltm_read']()
        elif self.params['name'] == 'pem':
            return self.methods['pem_read']()
        elif self.params['name'] == 'swg':
            return self.methods['swg_read']()

def main():
    # Translation list for conflictual params
    tr = {}

    module = AnsibleModuleF5BigIpUnnamedObject(argument_spec=BIGIP_SYS_PROVISION_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpSysProvision(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()