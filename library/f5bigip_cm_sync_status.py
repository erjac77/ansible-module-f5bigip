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
module: f5bigip_cm_sync_status
short_description: BIG-IP cm sync status module
description:
    - Displays the configuration synchronization status of the local device.
version_added: "2.4"
author:
    - "Eric Jacob (@erjac77)"
options:
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Gets the sync status of the device
  f5bigip_cm_sync_status:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
  delegate_to: localhost
  register: result

- name: Displays the sync status of the device
  debug:
    msg: "Sync Status: {{ result.status }}"
'''

RETURN = '''
color:
    description: The color representing the sync status of the device
    returned: success
    type: string
    sample:
        - green
        - yellow
mode:
    description: The mode in which the BIP-IP system is operating
    returned: success
    type: string
    sample:
        - high-availability
        - standalone
status:
    description: The sync status of the device
    returned: success
    type: string
    sample:
        - In Sync
        - Standalone
summary:
    description: A summary message explaining the sync status of the device
    returned: success
    type: string
    sample:
        - All devices in the device group are in sync
        - Changes Pending
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.f5_bigip import *

BIGIP_CM_SYNC_STATUS_ARGS = dict(
)


class F5BigIpCmSyncStatus(F5BigIpUnnamedObject):
    def set_crud_methods(self):
        self.methods = {
            'read': self.mgmt_root.tm.cm.sync_status
        }

    def get_sync_status(self):
        result = dict(changed=False)

        try:
            sync_status = self.methods['read']
            sync_status.refresh()
            sync_status_stats = \
                sync_status.entries['https://localhost/mgmt/tm/cm/sync-status/0']['nestedStats']['entries']
        except Exception:
            raise AnsibleF5Error("Unable to retrieve the sync status of the device.")

        result.update(
            color=sync_status_stats['color']['description'],
            mode=sync_status_stats['mode']['description'],
            status=sync_status_stats['status']['description'],
            summary=sync_status_stats['summary']['description']
        )

        return result


def main():
    module = AnsibleModuleF5BigIpUnnamedObject(argument_spec=BIGIP_CM_SYNC_STATUS_ARGS, supports_check_mode=False)

    try:
        obj = F5BigIpCmSyncStatus(check_mode=module.check_mode, **module.params)
        result = obj.get_sync_status()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
