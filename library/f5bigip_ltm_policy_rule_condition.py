#!/usr/bin/python
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
module: f5bigip_ltm_policy_rule_condition
short_description: BIG-IP ltm policy rule condition module
description:
    - Configures the conditions specified for the rule.
version_added: "2.4"
author:
    - "Eric Jacob (@erjac77)"
options:
    address:
        description:
            - 
    all:
        description:
            - Specifies that all items should be selected.
    app_service:
        description:
            - Specifies the application service to which the object belongs.
    browser_type:
        description:
            - 
    browser_version:
        description:
            - 
    case_insensitive:
        description:
            - The value matched on is case insensitive.
    case_sensitive:
        description:
            - The value matched on is case sensitive.
    cipher:
        description:
            - Specifies that a cipher should be selected.
    cipher_bits:
        description:
            - Specifies that cipher bits should be selected.
    client_ssl:
        description:
            - Specifies that Client SSL profile should be selected.
    code:
        description:
            - Specifies that code should be selected.
    common_name:
        description:
            - 
    contains:
        description:
            - The value matches if it contains a certain string.
    continent:
        description:
            - 
    country_code:
        description:
            - 
    country_name:
        description:
            - 
    cpu_usage:
        description:
            - Specifies a condition based upon CPU usage percentage for the past 15 seconds, 1 minute or 5 minutes
              intervals.
    device_make:
        description:
            - 
    device_model:
        description:
            - 
    domain:
        description:
            - Specifies that a domain should be selected.
    ends_with:
        description:
            - The value matches if it ends with a certain string.
    equals:
        description:
            - The value matches if it equals a certain value.
    expiry:
        description:
            - Specifies that an expiry should be selected.
    extension:
        description:
            - Specifies that an extension should be selected.
    external:
        description:
            - The value matched on is from the external side of a connection.
    geoip:
        description:
            - Specifies a condition based upon properties of the geographical location of the IP address, such as
              continent code, country code, city, region, or organization.
    greater:
        description:
            - The value matches if it is greater than a given value.
    greater_or_equal:
        description:
            - The value matches if it is greater than or equal to a given value
    header:
        description:
            - Specifies that a header should be selected.
    host:
        description:
            - Specifies that a host should be selected.
    http_basic_auth:
        description:
            - Specifies that HTTP basic authorization should be examined.
    http_cookie:
        description:
            - Specifies that HTTP cookies should be examined.
    http_header:
        description:
            - Specifies that HTTP headers should be examined.
    http_host:
        description:
            - Specifies that HTTP hosts should be examined.
    http_method:
        description:
            - Specifies that HTTP methods should be examined.
    http_referer:
        description:
            - Specifies that HTTP referers should be examined.
    http_set_cookie:
        description:
            - Specifies that HTTP set cookies should be examined.
    http_status:
        description:
            - Specifies that HTTP statuses should be examined.
    http_uri:
        description:
            - Specifies that HTTP URIs should be examined.
    http_user_agent:
        description:
            - Specifies a condition based upon User Agent sub-string, i.e. version, browser type, or mobile device
              make and model.
    http_version:
        description:
            - Specifies that HTTP versions should be examined.
    index:
        description:
            - The specified index is used to match.
    internal:
        description:
            - The value matched on is from the internal side of a connection.
    isp:
        description:
            - 
    last_15secs:
        description:
            - 
    last_1min:
        description:
            - 
    last_5mins:
        description:
            - 
    less:
        description:
            - The value matches if it is less than a given value.
    less_or_equal:
        description:
            - The value matches if it is less than or equal to a given value
    local:
        description:
            - The value matches on local connections.
    major:
        description:
            - Specifies that a major should be selected.
    matches:
        description:
            - 
    minor:
        description:
            - Specifies that a minor should be selected.
    missing:
        description:
            - The value matches if a value is missing.
    mss:
        description:
            - Specifies that the maximum segment size should be selected.
    name:
        description:
            - Specifies unique name for the component.
        required: true
    tm_name:
        description:
            - Specifies that the name should be selected.
    tm_not:
        description:
            - The opposite of this condition matches.
    org:
        description:
            - 
    password:
        description:
            - Specifies that a password should be selected.
    path:
        description:
            - Specifies that a path should be selected.
    path_segment:
        description:
            - Specifies that a path segment should be selected.
    policy:
        description:
            - Specifies the policy in which the rule condition belongs.
        required: true
    port:
        description:
            - Specifies that a port should be selected.
    present:
        description:
            - The value matches if an item is present.
    protocol:
        description:
            - Specifies that a protocol should be selected.
    query_parameter:
        description:
            - Specifies that a query parameter should be selected.
    query_string:
        description:
            - Specifies that a query string should be selected.
    region_code:
        description:
            - 
    region_name:
        description:
            - 
        default: false
    remote:
        description:
            - The value matches on remote conditions.
        default: false
    request:
        description:
            - The condition is matched on a request to the Virtual Server.
        default: false
    response:
        description:
            - The condition is matched on a response to the Virtual Server.
    route_domain:
        description:
            - Specifies that the route domain should be selected.
    rtt:
        description:
            - Specifies that the round trip time should be selected.
    rule:
        description:
            - Specifies the rule in which the rule condition belongs.
        required: true
    scheme:
        description:
            - Specifies that a scheme should be selected.
    server_name:
        description:
            - 
    ssl_cert:
        description:
            - 
    ssl_client_hello:
        description:
            - 
    ssl_extension:
        description:
            - 
    ssl_server_handshake:
        description:
            - 
    ssl_server_hello:
        description:
            - 
    starts_with:
        description:
            - The value matches if it starts with a certain string.
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    tcp:
        description:
            - Specifies that tcp connections should be examined.
    text:
        description:
            - Specifies that text should be selected.
    unnamed_query_parameter:
        description:
            - Specifies that an unnamed query parameter should be selected.
    user_agent_token:
        description:
            - 
    username:
        description:
            - Specifies that a username should be selected.
    value:
        description:
            - Specifies that a value should be selected.
    values:
        description:
            - The specified values will be matched on.
    version:
        description:
            - Specifies that a version should be selected.
    vlan:
        description:
            - Specifies that the Vlan should be selected.
    vlan_id:
        description:
            - Specifies that the Vlan ID should be selected.
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Create LTM Policy Rule Condition
  f5bigip_ltm_policy_rule_condition:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: 0
    policy: /Common/my_policy
    rule: my_rule
    http_uri: True
    contains: True
    values:
      - private
      - secure
    state: present
  delegate_to: localhost
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_LTM_POLICY_RULE_CONDITION_ARGS = dict(
    policy=dict(type='str', required=True),
    rule=dict(type='str', required=True),
    # The conditions permitted for the rule
    address=dict(type='bool'),
    all=dict(type='bool'),
    app_service=dict(type='str'),
    browser_type=dict(type='bool'),
    browser_version=dict(type='bool'),
    case_insensitive=dict(type='bool'),
    case_sensitive=dict(type='bool'),
    cipher=dict(type='bool'),
    cipher_bits=dict(type='bool'),
    client_ssl=dict(type='bool'),
    code=dict(type='bool'),
    common_name=dict(type='bool'),
    contains=dict(type='bool'),
    continent=dict(type='bool'),
    country_code=dict(type='bool'),
    country_name=dict(type='bool'),
    cpu_usage=dict(type='bool'),
    device_make=dict(type='bool'),
    device_model=dict(type='bool'),
    domain=dict(type='bool'),
    ends_with=dict(type='bool'),
    equals=dict(type='bool'),
    expiry=dict(type='bool'),
    extension=dict(type='bool'),
    external=dict(type='bool'),
    geoip=dict(type='bool'),
    greater=dict(type='bool'),
    greater_or_equal=dict(type='bool'),
    #header=dict(type='bool'),
    host=dict(type='bool'),
    http_basic_auth=dict(type='bool'),
    http_cookie=dict(type='bool'),
    http_header=dict(type='bool'),
    http_host=dict(type='bool'),
    http_method=dict(type='bool'),
    http_referer=dict(type='bool'),
    http_set_cookie=dict(type='bool'),
    http_status=dict(type='bool'),
    http_uri=dict(type='bool'),
    http_user_agent=dict(type='bool'),
    http_version=dict(type='bool'),
    index=dict(type='int'),
    internal=dict(type='bool'),
    isp=dict(type='bool'),
    last_15secs=dict(type='bool'),
    last_1min=dict(type='bool'),
    last_5mins=dict(type='bool'),
    less=dict(type='bool'),
    less_or_equal=dict(type='bool'),
    local=dict(type='bool'),
    major=dict(type='bool'),
    matches=dict(type='bool'),
    minor=dict(type='bool'),
    missing=dict(type='bool'),
    mss=dict(type='bool'),
    tm_name=dict(type='str'),
    tm_not=dict(type='bool'),
    org=dict(type='bool'),
    password=dict(type='bool'),
    path=dict(type='bool'),
    path_segment=dict(type='bool'),
    port=dict(type='bool'),
    present=dict(type='bool'),
    protocol=dict(type='bool'),
    query_parameter=dict(type='bool'),
    query_string=dict(type='bool'),
    region_code=dict(type='bool'),
    region_name=dict(type='bool'),
    remote=dict(type='bool'),
    request=dict(type='bool'),
    response=dict(type='bool'),
    route_domain=dict(type='bool'),
    rtt=dict(type='bool'),
    scheme=dict(type='bool'),
    server_name=dict(type='bool'),
    ssl_cert=dict(type='bool'),
    ssl_client_hello=dict(type='bool'),
    ssl_extension=dict(type='bool'),
    ssl_server_handshake=dict(type='bool'),
    ssl_server_hello=dict(type='bool'),
    starts_with=dict(type='bool'),
    tcp=dict(type='bool'),
    text=dict(type='bool'),
    unnamed_query_parameter=dict(type='bool'),
    user_agent_token=dict(type='bool'),
    username=dict(type='bool'),
    value=dict(type='bool'),
    values=dict(type='list'),
    version=dict(type='bool'),
    vlan=dict(type='bool'),
    vlan_id=dict(type='bool')
)


class F5BigIpLtmPolicyRuleCondition(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.policy = self.mgmt_root.tm.ltm.policys.policy.load(
            **self._get_resource_id_from_path(self.params['policy']))
        self.rule = self.policy.rules_s.rules.load(name=self.params['rule'])
        self.methods = {
            'create': self.rule.conditions_s.conditions.create,
            'read': self.rule.conditions_s.conditions.load,
            'update': self.rule.conditions_s.conditions.update,
            'delete': self.rule.conditions_s.conditions.delete,
            'exists': self.rule.conditions_s.conditions.exists
        }
        del self.params['partition']
        del self.params['policy']
        del self.params['rule']


def main():
    # Translation list for conflictual params
    tr = {'tm_not': 'not'}

    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_POLICY_RULE_CONDITION_ARGS,
                                             supports_check_mode=True)

    try:
        obj = F5BigIpLtmPolicyRuleCondition(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
