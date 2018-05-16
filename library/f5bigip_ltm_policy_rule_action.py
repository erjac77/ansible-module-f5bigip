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
module: f5bigip_ltm_policy_rule_action
short_description: BIG-IP ltm policy rule action module
description:
    - Configues the actions specified for the rule.
version_added: "2.4"
author:
    - "Eric Jacob (@erjac77)"
options:
    action_id:
        description:
            - Specifies that an action with a particular id should be applied.
    add:
        description:
            - Specifies that a value should be added.
    all:
        description:
            - Specifies that the action should be applied to every value selected.
    app_service:
        description:
            - Specifies the application service to which the object belongs.
    application:
        description:
            - Specifies that an application should be set.
    apply:
        description:
            - Specifies that an feature should be applied.
    asm:
        description:
            - Specifies that the Application Security Manager should be invoked.
    avr:
        description:
            - Specifies that Application Visibility Reporting should be invoked.
    cache:
        description:
            - Specifies that the cache should be modified.
    carp:
        description:
            - 
    category:
        description:
            - Specifies that a category should be set.
    classify:
        description:
            - Specifies that a value should be classified.
    clone_pool:
        description:
            - Specifies that the connection should cloned and simultaneously sent to another pool.
    code:
        description:
            - Specifies that a code should be set.
    compress:
        description:
            - Specifies that compression should be modified.
    content:
        description:
            - Specifies that content should be set.
    cookie:
        description:
            - Specifies that a cookie should be set.
    cookie_hash:
        description:
            - 
    cookie_insert:
        description:
            - 
    cookie_passive:
        description:
            - 
    cookie_rewrite:
        description:
            - 
    default:
        description:
            - Specifies that a default action should be taken.
    decompress:
        description:
            - Specifies that decompression should be modified.
    defer:
        description:
            - Specifies that a connection should be deferred.
    destination_address:
        description:
            - 
    disable:
        description:
            - Specifies that a feature should be disabled.
    domain:
        description:
            - Specifies that a domain should be set.
    enable:
        description:
            - Specifies that a feature should be enabled.
    event:
        description:
            - Specifies that an event should occur.
    expiry:
        description:
            - Specifies that an expiry should be set.
    expiry_secs:
        description:
            - 
    expression:
        description:
            - Specifies that an expression should be set.
    extension:
        description:
            - Specifies that an extension should be used.
    facility:
        description:
            - 
    forward:
        description:
            - Specifies that forwarding should be modified.
    from_profile:
        description:
            - Specifies that a from profile should be set.
    hash:
        description:
            - 
    host:
        description:
            - Specifies that a host should be set.
    http:
        description:
            - Specifies that HTTP connections should be modified.
    http_basic_auth:
        description:
            - Specifies that HTTP basic authentication should be modified.
    http_cookie:
        description:
            - Specifies that HTTP cookies should be modified.
    http_header:
        description:
            - Specifies that HTTP headers should be modified.
    http_host:
        description:
            - Specifies that HTTP hosts should be modified.
    http_referer:
        description:
            - Specifies that HTTP referers should be modified.
    http_reply:
        description:
            - Specifies that HTTP replies should be modified.
    http_set_cookie:
        description:
            - Specifies that HTTP set cookies should be modified.
    http_uri:
        description:
            - Specifies that HTTP URIs should be modified.
    ifile:
        description:
            - Specifies that an ifile should be run.
    index:
        description:
            - Specifies that an indexed value in a list should be changed.
    insert:
        description:
            - Specifies that a value should be inserted.
    internal:
        description:
            - Specifies that an internal action should be taken.
    internal_virtual:
        description:
            - Specifies that the connection should be sent through an internal virtual server.
    ip_address:
        description:
            - 
    key:
        description:
            - 
    l7dos:
        description:
            - Specifies that a Layer 7 DOS protection policy should be invoked.
    length:
        description:
            - 
    local:
        description:
            - Specifies that a local action should be taken.
    location:
        description:
            - Specifies that a location should be set.
    log:
        description:
            - Specifies that a log should be generated.
    ltm_policy:
        description:
            - 
    member:
        description:
            - Specifies that a member should be set.
    message:
        description:
            - Specifies that a message should be set.
    name:
        description:
            - Specifies unique name for the component.
        required: true
    tm_name:
        description:
            - Specifies that a name should be given.
    netmask:
        description:
            - Specifies an IPv4/IPv6 netmask.
    next:
        description:
            - Specifies that the next value should be modified.
    nexthop:
        description:
            - Specifies that a nexthop should be set.
    node:
        description:
            - Specifies that a node should be set.
    offset:
        description:
            - Specifies offset parameter.
    password:
        description:
            - Specifies that a password should be set.
    path:
        description:
            - Specifies that a path should be set.
    pem:
        description:
            - Specifies that the Policy Enforcement Manager should be applied.
    persist:
        description:
            - 
    pin:
        description:
            - Specifies that a connection should be pinned.
    policy:
        description:
            - Specifies the policy in which the rule action belongs.
        required: true
    tm_policy:
        description:
            - Specifies that a policy should be applied.
    pool:
        description:
            - Specifies that the connection should go to a specific pool.
    port:
        description:
            - Specifies that a port should be set.
    priority:
        description:
            - 
    profile:
        description:
            - Specifies that a profile should be set.
    protocol:
        description:
            - Specifies that a protocol should be set.
    query_parameter:
        description:
            - Specifies that a query parameter should be set.
    query_string:
        description:
            - Specifies that a query string should be set.
    rateclass:
        description:
            - Specifies that a rateclass should be applied.
    redirect:
        description:
            - Specifies that a connection should be redirected.
    remove:
        description:
            - Specifies that a value should be removed.
    replace:
        description:
            - Specifies that a value should be replaced.
    request:
        description:
            - Specifies that the action should be taken on a request from the Virtual Server in a connection.
    request_adapt:
        description:
            - Specifies that request adaptation should be invoked.
    reset:
        description:
            - Specifies that a connection should be reset.
    response:
        description:
            - Specifies that the action should be taken on a response from the Virtual Server in a connection.
    response_adapt:
        description:
            - Specifies that response adaptation should be invoked.
    rule:
        description:
            - Specifies the rule in which the rule condition belongs.
        required: true
    tm_rule:
        description:
            - Specifies that a rule should be applied.
    scheme:
        description:
            - Specifies that a scheme should be adopted.
    script:
        description:
            - Specifies that a script should be invoked.
    select:
        description:
            - Specifies that a value should be selected.
    server_ssl:
        description:
            - Specifies that a Server SSL profile should be invoked.
    set_variable:
        description:
            - Specifies that an variable should be set.
    snat:
        description:
            - Specifies that snatting policy should be set.
    snatpool:
        description:
            - Specifies that a snat pool should be set.
    source_address:
        description:
            - 
    ssl_client_hello:
        description:
            - 
    ssl_server_handshake:
        description:
            - 
    ssl_server_hello:
        description:
            - 
    ssl_session_id:
        description:
            - 
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    status:
        description:
            - Specifies that a status should be set.
    tcl:
        description:
            - Specifies that a TCL script should be invoked.
    tcp_nagle:
        description:
            - Specifies that TCP nagling rules should be modified.
    text:
        description:
            - Specifies that text should be set.
    timeout:
        description:
            - Specifies a timeout value in seconds.
    uie:
        description:
            - 
    universal:
        description:
            - 
    unnamed_query_parameter:
        description:
            - Specifies that an unnamed query parameter should be set.
    username:
        description:
            - Specifies that a username should be set.
    value:
        description:
            - Specifies that a value should be set.
    version:
        description:
            - Specifies that a version should be set.
    virtual:
        description:
            - Specifies that a Virtual should be set.
    vlan:
        description:
            - Specifies that a Vlan should be set.
    vlan_id:
        description:
            - Specifies that a Vlan ID should be set.
    wam:
        description:
            - Specifies that the Acceleration Module should be invoked.
    write:
        description:
            - Specifies that a value should be written.
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Create LTM Policy Rule Action
  f5bigip_ltm_policy_rule_action:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: 0
    policy: /Common/my_policy
    rule: my_rule
    forward: True
    pool: /Common/my_pool
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
            policy=dict(type='str', required=True),
            rule=dict(type='str', required=True),
            # The actions permitted for the rule
            # action_id=dict(type='str'),
            # add=dict(type='bool'),
            # all=dict(type='bool'),
            app_service=dict(type='str'),
            application=dict(type='str'),
            # apply=dict(type='bool'),
            asm=dict(type='bool'),
            avr=dict(type='bool'),
            cache=dict(type='bool'),
            carp=dict(type='bool'),
            category=dict(type='str'),
            classify=dict(type='bool'),
            clone_pool=dict(type='str'),
            code=dict(type='int'),
            compress=dict(type='bool'),
            content=dict(type='str'),
            # cookie=dict(type='bool'),
            cookie_hash=dict(type='bool'),
            cookie_insert=dict(type='bool'),
            cookie_passive=dict(type='bool'),
            cookie_rewrite=dict(type='bool'),
            # default=dict(type='bool'),
            decompress=dict(type='bool'),
            defer=dict(type='bool'),
            destination_address=dict(type='bool'),
            disable=dict(type='bool'),
            domain=dict(type='str'),
            enable=dict(type='bool'),
            expiry=dict(type='str'),
            expiry_secs=dict(type='int'),
            expression=dict(type='str'),
            extension=dict(type='str'),
            facility=dict(type='str'),
            forward=dict(type='bool'),
            from_profile=dict(type='str'),
            hash=dict(type='bool'),
            host=dict(type='str'),
            http=dict(type='bool'),
            http_basic_auth=dict(type='bool'),
            http_cookie=dict(type='bool'),
            http_header=dict(type='bool'),
            http_host=dict(type='bool'),
            http_referer=dict(type='bool'),
            http_reply=dict(type='bool'),
            http_set_cookie=dict(type='bool'),
            http_uri=dict(type='bool'),
            ifile=dict(type='str'),
            # index=dict(type='int'),
            insert=dict(type='bool'),
            # internal=dict(type='bool'),
            internal_virtual=dict(type='str'),
            ip_address=dict(type='str'),
            key=dict(type='str'),
            l7dos=dict(type='bool'),
            length=dict(type='int'),
            # local=dict(type='bool'),
            location=dict(type='str'),
            log=dict(type='bool'),
            ltm_policy=dict(type='bool'),
            member=dict(type='str'),
            message=dict(type='str'),
            tm_name=dict(type='str'),
            netmask=dict(type='str'),
            # next=dict(type='bool'),
            nexthop=dict(type='str'),
            node=dict(type='str'),
            offset=dict(type='int'),
            # password=dict(type='str'),
            path=dict(type='str'),
            pem=dict(type='bool'),
            persist=dict(type='bool'),
            pin=dict(type='bool'),
            tm_policy=dict(type='str'),
            pool=dict(type='str'),
            port=dict(type='int'),
            priority=dict(type='str'),
            profile=dict(type='str'),
            protocol=dict(type='str'),
            # query_parameter=dict(type='str'),
            query_string=dict(type='str'),
            rateclass=dict(type='str'),
            redirect=dict(type='bool'),
            remove=dict(type='bool'),
            replace=dict(type='bool'),
            request=dict(type='bool'),
            request_adapt=dict(type='bool'),
            reset=dict(type='bool'),
            response=dict(type='bool'),
            response_adapt=dict(type='bool'),
            # tm_rule=dict(type='str'),
            scheme=dict(type='str'),
            script=dict(type='str'),
            select=dict(type='bool'),
            server_ssl=dict(type='bool'),
            set_variable=dict(type='bool'),
            snat=dict(type='str'),
            snatpool=dict(type='str'),
            source_address=dict(type='bool'),
            ssl_client_hello=dict(type='bool'),
            ssl_server_handshake=dict(type='bool'),
            ssl_server_hello=dict(type='bool'),
            ssl_session_id=dict(type='bool'),
            status=dict(type='int'),
            tcl=dict(type='bool'),
            tcp_nagle=dict(type='bool'),
            text=dict(type='str'),
            timeout=dict(type='int'),
            uie=dict(type='bool'),
            universal=dict(type='bool'),
            # unnamed_query_parameter=dict(type='str'),
            # username=dict(type='str'),
            value=dict(type='str'),
            # version=dict(type='str'),
            virtual=dict(type='str'),
            vlan=dict(type='str'),
            vlan_id=dict(type='int'),
            wam=dict(type='bool'),
            write=dict(type='bool')
        )
        argument_spec.update(F5_PROVIDER_ARGS)
        argument_spec.update(F5_NAMED_OBJ_ARGS)
        del argument_spec['partition']
        return argument_spec

    @property
    def supports_check_mode(self):
        return True

    # @property
    # def tr(self):
    #     # Translation dict for conflictual params
    #     return {'tm_policy': 'policy', 'tm_rule': 'rule'}


class F5BigIpLtmPolicyRuleAction(F5BigIpNamedObject):
    def _set_crud_methods(self):
        policy = self._api.tm.ltm.policys.policy.load(
            **self._get_resource_id_from_path(self._params['policy']))
        rule = policy.rules_s.rules.load(name=self._params['rule'])
        self._methods = {
            'create': rule.actions_s.actions.create,
            'read': rule.actions_s.actions.load,
            'update': rule.actions_s.actions.update,
            'delete': rule.actions_s.actions.delete,
            'exists': rule.actions_s.actions.exists
        }
        del self._params['policy']
        del self._params['rule']


def main():
    params = ModuleParams()
    module = AnsibleModule(argument_spec=params.argument_spec, supports_check_mode=params.supports_check_mode)

    try:
        obj = F5BigIpLtmPolicyRuleAction(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
