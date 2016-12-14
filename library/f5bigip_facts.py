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
module: f5bigip_facts
short_description: Gather facts from BIG-IP system
description:
    - Collect facts from BIG-IP system.
version_added: "1.0"
author:
	- "Eric Jacob, @erjac77"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    include:
        description:
            - Specifies the list of objects to collect.
        required: true
        default: null
        choices: [node, vlan]
        aliases: []
        version_added: 1.0
    filter:
        description:
            - Specifies an administrative partition to query for a result set.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 1.0
'''

EXAMPLES = '''
- name: Collect BIG-IP facts
  f5bigip_facts:
    f5bigip_hostname: "172.16.227.35"
    f5bigip_username: "admin"
    f5bigip_password: "admin"
    f5bigip_port: "443"
    object: vlan
  delegate_to: localhost
'''

from ansible_common_f5bigip.f5bigip import *

def get_facts(uri, **params):
    rparams = dict()
    rq_filter = params['filter']
    rq_select = params['select']
    if rq_filter:
        rparams['filter'] = rq_filter.replace(" ", "+")
    if rq_select:
        if 'name' not in rq_select:
            rq_select.append('name')
        rparams['select'] = rq_select

    req_params = ""
    if rparams:
        for k, v in rparams.iteritems():
            req_params += "&$" + k + "=" + v

    resp = open_url(
        'https://' + params['f5bigip_hostname'] + ':' + str(params['f5bigip_port']) + uri + '?expandSubcollections=true' + req_params,
        method="GET",
        url_username=params['f5bigip_username'],
        url_password=params['f5bigip_password'],
        validate_certs=False
    )
    
    return json.loads(resp.read())

def main():
    argument_spec = dict(
        object 	= 	dict(type='str', required=True, choices=['node', 'vlan']),
        filter	=	dict(type='str'),
        select  =	dict(type='str')
    )
    
    module = AnsibleModuleF5BigIpClient(argument_spec=argument_spec, supports_check_mode=False)
    
    try:
        facts = {}
        
       	client = F5BigIpClient(**module.params)
        
        if module.params['object'] == 'node':
        	facts['node'] = get_facts(uri='/mgmt/tm/ltm/node/', **module.params)
        if module.params['object'] == 'vlan':
        	facts['vlan'] = get_facts(uri='/mgmt/tm/net/vlan/', **module.params)
        
        result = { 'ansible_facts': facts }
        
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *
from ansible.module_utils.urls import *

if __name__ == '__main__':  
    main()