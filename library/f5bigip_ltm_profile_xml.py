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

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: f5bigip_ltm_profile_xml
short_description: BIG-IP ltm profile xml module
description:
    - Configures an XML profile.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    app_service:
        description:
            - Specifies the name of the application service to which the profile belongs.
    defaults_from:
        description:
            - Specifies the profile that you want to use as the parent profile.
        default: xml
    description:
        description:
            - User defined description.
    multiple_query_matches:
        description:
            - Enables or disables multiple matches for a single XPath query.
        choices: ['disabled', 'enabled']
    name:
        description:
            - Specifies a list of mappings between namespaces and prefixes to be used in the XPath queries of the profile.
        required: true
    namespace_mappings:
        description:
            - Specifies a list of mappings between namespaces and prefixes to be used in the XPath queries of the profile.
        required: true
    partition:
        description:
            - Displays the administrative partition within which the component resides.
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    xpath_queries:
        description:
            - Specifies the list of XPath queries that are used by the profile.
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Create LTM Profile xml
  f5bigip_ltm_profile_xml:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_xml_profile
    partition: Common
    description: My xml profile
    state: present
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_LTM_PROFILE_XML_ARGS = dict(
    app_service               =    dict(type='str'),
    defaults_from             =    dict(type='str'),
    description               =    dict(type='str'),
    multiple_query_matches    =    dict(type='str', choices=F5_ACTIVATION_CHOICES),
    namespace_mappings        =    dict(type='list'),
    xpath_queries             =    dict(type='list')
)

class F5BigIpLtmProfileXml(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.profile.xmls.xml.create,
            'read':     self.mgmt_root.tm.ltm.profile.xmls.xml.load,
            'update':   self.mgmt_root.tm.ltm.profile.xmls.xml.update,
            'delete':   self.mgmt_root.tm.ltm.profile.xmls.xml.delete,
            'exists':   self.mgmt_root.tm.ltm.profile.xmls.xml.exists
        }

def main():
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_PROFILE_XML_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpLtmProfileXml(check_mode=module.supports_check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

if __name__ == '__main__':
    main()