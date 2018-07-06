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
module: f5bigip_ltm_profile_server_ssl
short_description: BIG-IP ltm server-ssl profile module
description:
    - Configures a Server SSL profile.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    alert-timeout:
        description:
            - Specifies the maximum time period in seconds to keep the SSL session active after alert message is sent.
        default: 10
    app_service:
        description:
            - Specifies the name of the application service to which the profile belongs.
    authenticate:
        description:
            - Specifies the frequency of authentication.
    authenticate_depth:
        description:
            - Specifies the client certificate chain maximum traversal depth.
        default: 9
    authenticate_name:
        description:
            - Specifies a Common Name (CN) that is embedded in a server certificate.
    ca_file:
        description:
            - Specifies the certificate authority (CA) file name.
    cache_size:
        description:
            - Specifies the SSL session cache size.
        default: 262144
    cache_timeout:
        description:
            - Specifies the SSL session cache timeout value.
        default: 3600
        choices: range(0, 86401)
    cert:
        description:
            - Specifies the name of the certificate installed on the traffic management system for the purpose of
              terminating or initiating an SSL connection.
    chain:
        description:
            - Specifies or builds a certificate chain file that a client can use to authenticate the profile.
    ciphers:
        description:
            - Specifies a cipher name.
        default: DEFAULT
    crl_file:
        description:
            - Specifies the certificate revocation list file name.
    defaults_from:
        description:
            - Specifies the profile that you want to use as the parent profile.
        default: serverssl
    description:
        description:
            - User defined description.
    expire_cert_response_control:
        description:
            - Specifies the BIGIP action when the server certificate has expired.
        default: drop
        choices: ['drop', 'ignore']
    handshake_timeout:
        description:
            - Specifies the handshake timeout in seconds.
        default: 10
    key:
        description:
            - Specifies the key file name.
    mod_ssl_methods:
        description:
            - Enables or disables ModSSL method emulation.
        default: disabled
        choices: ['enabled', 'disabled']
    mode:
        description:
            - Enables or disables SSL processing.
        default: enabled
        choices: ['enabled', 'disabled']
    name:
        description:
            - Specifies a unique name for the component.
        required: true
    tm_options:
        description:
            - Enables options, including some industry-related workarounds.
        default: dont-insert-empty-fragments
        choices: [
            'all-bugfixes', 'cipher-server-preference', 'dont-insert-empty-fragments', 'ephemeral-rsa',
            'microsoft-big-sslv3-buffer', 'microsoft-sess-id-bug', 'msie-sslv2-rsa-padding', 'netscape-ca-dn-bug',
            'netscape-challenge-bug', 'netscape-demo-cipher-change-bug', 'netscape-reuse-cipher-change-bug',
            'no-session-resumption-on-renegotiation', 'no-ssl', 'no-sslv2', 'no-sslv3', 'no-tls', 'no-tlsv1',
            'no-tlsv1.1', 'no-tlsv1.2', 'no-dtls', 'passive-close', 'none', 'pkcs1-check-1', 'pkcs1-check-2',
            'single-dh-use', 'ssleay-080-client-dh-bug', 'sslref2-reuse-cert-type-bug', 'tls-d5-bug', 'tls-rollback-bug'
        ]
    partition:
        description:
            - Displays the administrative partition within which the component resides.
    passphrase:
        description:
            - Specifies the key passphrase, if required.
    peer_cert_mode:
        description:
            - Specifies the peer certificate mode.
        default: ignore
        choices: ['ignore', 'require']
    port:
        description:
            - Specifies a service for the data channel port used for this Server SSL profile.
    proxy_ssl:
        description:
            - Enabling this option requires a corresponding server ssl profile with proxy-ssl enabled to perform
              transparent SSL decryption.
        choices: ['enabled', 'disabled']
    proxy_ssl_passthrough:
        description:
            - This allows Proxy SSL to passthrough the traffic when ciphersuite negotiated between the client and server
              is not supported.
        default: disabled
        choices: ['enabled', 'disabled']
    renegotiate_period:
        description:
            - Specifies the number of seconds from the initial connect time after which the system renegotiates an SSL
              session.
        default: indefinite
    renegotiate_size:
        description:
            - Specifies a throughput size, in megabytes, of SSL renegotiation.
        default: Indefinite
    renegotiation:
        description:
            - Specifies whether renegotiations are enabled.
        default: enabled
        choices: ['enabled', 'disabled']
    retain_certificate:
        description:
            - APM module requires storing certificate in SSL session. When set to false, certificate will not be stored
              in SSL session.
        type: bool
    generic_alert:
        description:
            - Enables or disables generic-alert.
        default: enabled
        choices: ['enabled', 'disabled']
    secure_renegotiation:
        description:
            - Specifies the secure renegotiation mode.
        default: require-strict
        choices: ['request', 'require', 'require-strict']
    server_name:
        description:
            - Specifies the server name to be included in SNI (server name indication) extension during SSL handshake in
              ClientHello.
    session_mirroring:
        description:
            - Enables or disables the mirroring of sessions to high availability peer.
        default: disabled
        choices: ['enabled', 'disabled']
    session_ticket:
        description:
            - Enables or disables session-ticket.
        default: disabled
        choices: ['enabled', 'disabled']
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    sni_default:
        description:
            - When true, this profile is the default SSL profile when the server name in a client connection does not
              match any configured server names, or a client connection does not specify any server name at all.
        type: bool
    sni_require:
        description:
            - When this option is enabled, connections to a server that does not support SNI extension will be rejected.
        type: bool
    ssl_forward_proxy:
        description:
            - Enables or disables SSL forward proxy feature.
        default: disabled
        choices: ['enabled', 'disabled']
    ssl_forward_proxy_bypass:
        description:
            - Enables or disables SSL forward proxy bypass feature.
        default: disabled
        choices: ['enabled', 'disabled']
    ssl_sign_hash:
        description:
            - Specifies SSL sign hash algorithm which is used to sign and verify SSL Server Key Exchange and Certificate
              Verify messages for the specified SSL profiles.
        default: sha1
    strict_resume:
        description:
            - Enables or disables the resumption of SSL sessions after an unclean shutdown.
        default: disabled
        choices: ['enabled', 'disabled']
    unclean_shutdown:
        description:
            - When enabled, the SSL profile performs unclean shutdowns of all SSL connections without exchanging the
              required SSL shutdown alerts.
        choices: ['enabled', 'disabled']
    untrusted_cert_response_control:
        description:
            - Specifies the BIGIP action when the server certificate has untrusted CA.
        default: drop
        choices: ['drop', 'ignore']
requirements:
    - BIG-IP >= 12.0
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Create LTM Server SSL Profile
  f5bigip_ltm_profile_server_ssl:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_server_ssl_profile
    partition: Common
    state: present
  delegate_to: localhost
'''

RETURN = ''' # '''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.six.moves import range
from ansible_common_f5.base import F5_ACTIVATION_CHOICES
from ansible_common_f5.base import F5_NAMED_OBJ_ARGS
from ansible_common_f5.base import F5_PROVIDER_ARGS
from ansible_common_f5.bigip import F5BigIpNamedObject


class ModuleParams(object):
    @property
    def argument_spec(self):
        argument_spec = dict(
            alert_timeout=dict(type='int'),
            app_service=dict(type='str'),
            authenticate=dict(type='str'),
            authenticate_depth=dict(type='int'),
            authenticate_name=dict(type='str'),
            ca_file=dict(type='str'),
            cache_size=dict(type='int'),
            cache_timeout=dict(type='int', choices=range(0, 86401)),
            cert=dict(type='str'),
            chain=dict(type='str'),
            ciphers=dict(type='str'),
            crl_file=dict(type='str'),
            defaults_from=dict(type='str'),
            description=dict(type='str'),
            expire_cert_response_control=dict(type='str', choices=['drop', 'ignore']),
            handshake_timeout=dict(type='int'),
            key=dict(type='str'),
            mod_ssl_methods=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            mode=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            tm_options=dict(type='list'),
            passphrase=dict(type='str', no_log=True),
            peer_cert_mode=dict(type='str', choices=['ignore', 'require']),
            proxy_ssl=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            proxy_ssl_passthrough=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            renegotiate_period=dict(type='str'),
            renegotiate_size=dict(type='str'),
            renegotiation=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            retain_certificate=dict(type='bool'),
            generic_alert=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            secure_renegotiation=dict(type='str', choices=['request', 'require', 'require-strict']),
            server_name=dict(type='str'),
            session_mirroring=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            session_ticket=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            sni_default=dict(type='bool'),
            sni_require=dict(type='bool'),
            ssl_forward_proxy=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            ssl_forward_proxy_bypass=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            ssl_sign_hash=dict(type='str'),
            strict_resume=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            unclean_shutdown=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            untrusted_cert_response_control=dict(type='str', choices=['drop', 'ignore'])
        )
        argument_spec.update(F5_PROVIDER_ARGS)
        argument_spec.update(F5_NAMED_OBJ_ARGS)
        return argument_spec

    @property
    def supports_check_mode(self):
        return True


class F5BigIpLtmProfileServerSsl(F5BigIpNamedObject):
    def _set_crud_methods(self):
        self._methods = {
            'create': self._api.tm.ltm.profile.server_ssls.server_ssl.create,
            'read': self._api.tm.ltm.profile.server_ssls.server_ssl.load,
            'update': self._api.tm.ltm.profile.server_ssls.server_ssl.update,
            'delete': self._api.tm.ltm.profile.server_ssls.server_ssl.delete,
            'exists': self._api.tm.ltm.profile.server_ssls.server_ssl.exists
        }


def main():
    params = ModuleParams()
    module = AnsibleModule(argument_spec=params.argument_spec, supports_check_mode=params.supports_check_mode)

    try:
        obj = F5BigIpLtmProfileServerSsl(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
