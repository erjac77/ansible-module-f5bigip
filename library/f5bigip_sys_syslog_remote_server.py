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
module: f5bigip_sys_syslog_remote_server
short_description: BIG-IP sys syslog remote server module
description:
    - Configures the remote servers, identified by IP address, to which syslog sends messages.
version_added: 2.3
author:
    - "Eric Jacob, @erjac77"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    host:
        description:
            - Specifies the IP address of a remote server to which syslog sends messages.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    local_ip:
        description:
            - Specifies the IP address of the interface syslog binds with in order to log messages to a remote host.
        required: false
        default: null
        choices: []
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
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        required: false
        default: Common
        choices: []
        aliases: []
        version_added: 2.3
    remote_port:
        description:
            - Specifies the port number of a remote server to which syslog sends messages.
        required: false
        default: 514
        choices: []
        aliases: []
        version_added: 2.3
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        required: false
        default: present
        choices: ['absent', 'present']
        aliases: []
        version_added: 2.3
'''

EXAMPLES = '''
- name: Add SYS Syslog Remote Server
  f5bigip_sys_syslog_remote_server:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: remotesyslog1
    host: 10.20.20.21
    remote_port: 514
    state: present
  delegate_to: localhost
'''

import json, ast

from ansible_common_f5.f5_bigip import *

BIGIP_SYS_SYSLOG_REMOTE_SERVER_ARGS = dict(
    host        =   dict(type='str'),
    local_ip    =   dict(type='str'),
    remote_port =   dict(type='int', default=514)
)

class F5BigIpSysSyslogRemoteServer(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'read':     self.mgmt_root.tm.sys.syslog.load
        }
        self.params.pop('sub_path', None)

        if self._strip_partition(self.params['name']) == self.params['name']:
            self.name = '/' + self.params['partition'] + '/' + self.params['name']
        else:
            self.name = self.params['name']

    def _read(self):
        return self.methods['read']()

    def flush(self):
        has_changed = False
        found = False
        result = dict()

        for key, val in self.params.iteritems():
            if val is None:
                self.params[key] = 'none'
                
        syslog = self._read()
        if hasattr(syslog, 'remoteServers'):
            for remote_server in syslog.remoteServers:
                encoded_remote_server = ast.literal_eval(json.dumps(remote_server))
                
                if encoded_remote_server['name'] == self.name:
                    found = True
                    
                    if self.state == "absent":
                        has_changed = True
                        syslog.remoteServers.remove(remote_server)
                        
                    if self.state == "present":
                        for key, val in self.params.iteritems():
                            if key in encoded_remote_server and key != 'name':
                                if encoded_remote_server[key] != val:
                                    has_changed = True
                                    remote_server[key] = val
            if not found:
                if self.state == "present":
                    has_changed = True
                    syslog.remoteServers.append(self.params)
        else:
            has_changed = True
            syslog.remoteServers = [self.params]
            
        if has_changed:
            syslog.update()
            syslog.refresh()

        result.update(dict(changed=has_changed))
        return result

def main():
    # Translation list for conflictual params
    tr = {}
    
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_SYS_SYSLOG_REMOTE_SERVER_ARGS, supports_check_mode=False)
    
    try:
        obj = F5BigIpSysSyslogRemoteServer(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()