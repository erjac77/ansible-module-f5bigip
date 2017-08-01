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
version_added: 2.3
author:
    - "Eric Jacob, @erjac77"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    filter:
        description:
            - Specifies an administrative partition to query for a result set.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    component:
        description:
            - Specifies the component to collect.
        required: true
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    module:
        description:
            - Specifies the module.
        required: true
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    select:
        description:
            - Specifies a subset of the properties that will appear in the result set.
        required: false
        default: ltm
        choices: []
        aliases: []
        version_added: 2.3
    sub_module:
        description:
            - Specifies the sub-module.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    skip:
        description:
            - Specifies the number of rows to skip in the result set.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    top:
        description:
            - Specifies the first N rows of the result set.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
'''

EXAMPLES = '''
- name: Collect BIG-IP facts
  f5bigip_facts:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    module: ltm
    component: pool
    filter: partition eq Common
    select: name,partition
  delegate_to: localhost
'''

from ansible_common_f5.f5_bigip import *

def get_facts(uri, **params):
    rparams = dict()
    rq_filter = params['filter']
    rq_select = params['select']
    rq_skip = params['skip']
    rq_top = params['top']
    if rq_filter:
        rparams['filter'] = rq_filter.replace(" ", "+")
    if rq_select:
        if 'name' not in rq_select:
            rq_select.append('name')
        rparams['select'] = rq_select
    if rq_skip:
        rparams['skip'] = rq_skip
    if rq_top:
        rparams['top'] = rq_top

    req_params = ""
    if rparams:
        for k, v in rparams.iteritems():
            req_params += "&$" + k + "=" + str(v)

    resp = open_url(
        'https://' + params['f5_hostname'] + ':' + str(params['f5_port']) + uri + '?expandSubcollections=true' + req_params,
        method="GET",
        url_username=params['f5_username'],
        url_password=params['f5_password'],
        validate_certs=False
    )
    
    return json.loads(resp.read())

def main():
    argument_spec = dict(
        component   =   dict(type='str', required=True),
        filter      =   dict(type='str'),
        module      =   dict(type='str', required=True, choices=['actions', 'analytics', 'apm', 'asm', 'auth', 'cli', 'cm',
            'gtm', 'ltm', 'net', 'pem', 'security', 'sys', 'transaction', 'util', 'vcmp', 'wam', 'wom']),
        select      =   dict(type='str'),
        sub_module  =   dict(type='str'),
        skip        =   dict(type='int'),
        top         =   dict(type='int')
    )
    
    module = AnsibleModuleF5BigIpUnnamedObject(argument_spec=argument_spec, supports_check_mode=False)
    
    try:
        facts = {}
        
        resource = module.params['module']
        if module.params['sub_module'] is not None:
            resource += '/' + module.params['sub_module']
        resource += '/' + module.params['component']

        facts[resource.replace('/', '_')] = get_facts(uri='/mgmt/tm/' + resource + '/', **module.params)
        result = { 'ansible_facts': facts }
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *
from ansible.module_utils.urls import *

if __name__ == '__main__':
    main()