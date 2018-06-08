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
module: f5bigip_ltm_monitor_ftp
short_description: BIG-IP ltm ftp monitor module
description:
    - Configures a File Transfer Protocol (FTP) monitor.
version_added: "2.4"
author:
    - "Eric Jacob (@erjac77)"
options:
    adaptive:
        description:
            - Specifies whether the adaptive feature is enabled for this monitor.
        choices: ['enabled', 'disabled']
    adaptive_divergence_type:
        description:
            - Specifies whether the adaptive-divergence-value is relative or absolute.
        choices: ['relative', 'absolute']
    adaptive_divergence_value:
        description:
            - Specifies how far from mean latency each monitor probe is allowed to be.
    adaptive_limit:
        description:
            - Specifies the hard limit, in milliseconds, which the probe is not allowed to exceed, regardless of the
              divergence value.
    adaptive_sampling_timespan:
        description:
            - Specifies the size of the sliding window, in seconds, which records probe history.
    app_service:
        description:
            - Specifies the application service to which the object belongs.
    debug:
        description:
            - Specifies whether the monitor sends error messages and additional information to a log file created and
              labeled specifically for this monitor.
        default: no
        choices: ['no', 'yes']
    defaults_from:
        description:
            - Specifies the name of the monitor from which you want your custom monitor to inherit settings.
        default: ftp
    description:
        description:
            - Specifies descriptive text that identifies the component.
    destination:
        description:
            - Specifies the IP address and service port of the resource that is the destination of this monitor.
        default: '*:*'
    filename:
        description:
            - Specifies the full path and file name of the file that the system attempts to download.
    interval:
        description:
            - Specifies, in seconds, the frequency at which the system issues the monitor check when either the resource
              is down or the status of the resource is unknown.
        default: 5
    manual_resume:
        description:
            - Specifies whether the system automatically changes the status of a resource to up at the next successful
              monitor check.
        default: disabled
        choices: ['enabled', 'disabled']
    mode:
        description:
            - Specifies the data transfer process (DTP) mode.
        default: passive
        choices: ['passive', 'port']
    name:
        description:
            - Specifies a unique name for the component.
        required: true
    partition:
        description:
            - Specifies the administrative partition in which the component object resides.
        default: Common
    password:
        description:
            - Specifies the password, if the monitored target requires authentication.
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    time_until_up:
        description:
            - Specifies the amount of time, in seconds, after the first successful response before a node is marked up.
        default: 0
    timeout:
        description:
            - Specifies the number of seconds the target has in which to respond to the monitor request.
        default: 16
    up_interval:
        description:
            - Specifies, in seconds, the frequency at which the system issues the monitor check when the resource is up.
        default: 0
    username:
        description:
            - Specifies the username, if the monitored target requires authentication.
requirements:
    - BIG-IP >= 12.0
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Create LTM FTP Monitor
  f5bigip_ltm_monitor_ftp:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_ftp_monitor
    partition: Common
    state: present
  delegate_to: localhost
'''

RETURN = ''' # '''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.base import F5_ACTIVATION_CHOICES
from ansible_common_f5.base import F5_NAMED_OBJ_ARGS
from ansible_common_f5.base import F5_POLAR_CHOICES
from ansible_common_f5.base import F5_PROVIDER_ARGS
from ansible_common_f5.bigip import F5BigIpNamedObject


class ModuleParams(object):
    @property
    def argument_spec(self):
        argument_spec = dict(
            adaptive=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            adaptive_divergence_type=dict(type='str', choices=['relative', 'absolute']),
            adaptive_divergence_value=dict(type='int'),
            adaptive_limit=dict(type='int'),
            adaptive_sampling_timespan=dict(type='int'),
            app_service=dict(type='str'),
            debug=dict(type='str', choices=F5_POLAR_CHOICES),
            defaults_from=dict(type='str'),
            description=dict(type='str'),
            destination=dict(type='str'),
            filename=dict(type='str'),
            interval=dict(type='int'),
            manual_resume=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            mode=dict(type='str', choices=['passive', 'port']),
            password=dict(type='str', no_log=True),
            time_until_up=dict(type='int'),
            timeout=dict(type='int'),
            up_interval=dict(type='int'),
            username=dict(type='str')
        )
        argument_spec.update(F5_PROVIDER_ARGS)
        argument_spec.update(F5_NAMED_OBJ_ARGS)
        return argument_spec

    @property
    def supports_check_mode(self):
        return True


class F5BigIpLtmMonitorFtp(F5BigIpNamedObject):
    def _set_crud_methods(self):
        self._methods = {
            'create': self._api.tm.ltm.monitor.ftps.ftp.create,
            'read': self._api.tm.ltm.monitor.ftps.ftp.load,
            'update': self._api.tm.ltm.monitor.ftps.ftp.update,
            'delete': self._api.tm.ltm.monitor.ftps.ftp.delete,
            'exists': self._api.tm.ltm.monitor.ftps.ftp.exists
        }


def main():
    params = ModuleParams()
    module = AnsibleModule(argument_spec=params.argument_spec, supports_check_mode=params.supports_check_mode)

    try:
        obj = F5BigIpLtmMonitorFtp(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
