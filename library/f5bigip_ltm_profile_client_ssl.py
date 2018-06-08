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
module: f5bigip_ltm_profile_client_ssl
short_description: BIG-IP ltm client-ssl profile module
description:
    - You can use the client-ssl component to create, modify, or delete a custom Client SSL profile, or display a custom
      or default Client SSL profile.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    alert-timeout:
        description:
            - Specifies the maximum time period in seconds to keep the SSL session active after alert message is sent.
        default: 10
    allow-non-ssl:
        description:
            - Enables or disables non-SSL connections.
        default: disabled
        choices: ['enabled', 'disabled']
    app-service:
        description:
            - Specifies the name of the application service to which the profile belongs.
    authenticate:
        description:
            - Specifies how often the system authenticates a user.
        default: once
    authenticate_depth:
        description:
            - Specifies the authenticate depth.
        default: 9
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
            - This option is deprecated and is maintained here for backward compatibility reasons.
            - Please check cert_key_chain option to add certificate, key, passphrase and chain to the profile.
    cert_extension_includes:
        description:
            - Specifies the extensions of the web server certificates to be included in the generated certificates using
              SSL Forward Proxy.
    cert_key_chain:
        description:
            - Adds, deletes, or replaces a set of certificate, key, passphrase, chain and OCSP Stapling Parameters
              object.
    cert_lookup_by_ipaddr_port:
        description:
            - Specifies whether to perform certificate look up by IP address and port number.
    chain:
        description:
            - This option is deprecated and is maintained here for backward compatibility reasons.
            - Please check cert_key_chain option to add certificate, key, passphrase and chain to the profile.
    ciphers:
        description:
            - Specifies a cipher name.
        default: DEFAULT
    client_cert_ca:
        description:
            - Specifies the client cert certificate authority name.
    crl_file:
        description:
            - Specifies the certificate revocation list file name.
    defaults_from:
        description:
            - This setting specifies the profile that you want to use as the parent profile.
        default: clientssl
    description:
        description:
            - User defined description.
    handshake_timeout:
        description:
            - Specifies the handshake timeout in seconds.
        default: 10
    key:
        description:
            - This option is deprecated and is maintained here for backward compatibility reasons.
            - Please check cert_key_chain option to add certificate, key, passphrase and chain to the profile.
    mod_ssl_methods:
        description:
            - Enables or disables ModSSL method emulation.
        default: disabled
        choices: ['enabled', 'disabled']
    mode:
        description:
            - Specifies the profile mode, which enables or disables SSL processing.
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
            'no-tlsv1.1', 'no-tlsv1.2', 'no-dtls', 'passive-close, none, pkcs1-check-1', 'pkcs1-check-2, single-dh-use',
            'ssleay-080-client-dh-bug', 'sslref2-reuse-cert-type-bug', 'tls-d5-bug', 'tls-rollback-bug'
        ]
    partition:
        description:
            - Displays the administrative partition within which the component resides.
    passphrase:
        description:
            - This option is deprecated and is maintained here for backward compatibility reasons.
            - Please check cert_key_chain option to add certificate, key, passphrase and chain to the profile.
    peer_cert_mode:
        description:
            - Specifies the peer certificate mode.
        default: ignore
        choices: ['ignore', 'require']
    peer_no_renegotiate_timeout:
        description:
            - Specifies the timeout in seconds when the server sends Hello Request and waits for ClientHello before it
              sends Alert with fatal alert.
        default: 10
    port:
        description:
            - Specifies a service for the data channel port used for this client-ssl profile.
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
    proxy_ca_cert:
        description:
            - Specifies the name of the certificate file that is used as the certification authority certificate when
              SSL forward proxy feature is enabled.
    proxy_ca_key:
        description:
            - Specifies the name of the key file that is used as the certification authority key when SSL forward proxy
              feature is enabled.
    proxy_ca_passphrase:
        description:
            - Specifies the passphrase of the key file that is used as the certification authority key when SSL forward
              proxy feature is enabled.
    renegotiate_max_record_delay:
        description:
            - Specifies the maximum number of SSL records that the traffic management system can receive before it
              renegotiates an SSL session.
        default: indefinite
    renegotiate_period:
        description:
            - Specifies the number of seconds required to renegotiate an SSL session.
        default: indefinite
    renegotiate_size:
        description:
            - Specifies the size of the application data, in megabytes, that is transmitted over the secure channel.
        default: Indefinite
    renegotiation:
        description:
            - Specifies whether renegotiations are enabled.
        default: enabled
        choices: ['enabled', 'disabled']
    retain_certificate:
        description:
            - APM module requires storing certificate in SSL session.
        default: true
        type: bool
    secure_renegotiation:
        description:
            - Specifies the secure renegotiation mode.
        default: require
        choices: ['request', 'require', 'require-strict']
    max_renegotiations_per_minute:
        description:
            - Specifies the maximum number of renegotiation attempts allowed in a minute.
        default: 5
    server_name:
        description:
            - Specifies the server names to be matched with SNI (server name indication) extension information in
              ClientHello from a client connection.
    session_mirroring:
        description:
            - Specifies the name of the application service to which the profile belongs.
    session_ticket:
        description:
            - Specifies the name of the application service to which the profile belongs.
    sni_default:
        description:
            - When true, this profile is the default SSL profile when the server name in a client connection does not
              match any configured server names, or a client connection does not specify any server name at all.
        type: bool
    sni_require:
        description:
            - When this option is enabled, a client connection that does not specify a known server name or does not
              support SNI extension will be rejected.
        choices: ['enabled', 'disabled']
    source_ip_blacklist:
        description:
            - Specifies the data group name of source ip blacklist when SSL forward proxy bypass feature is enabled.
    source_ip_whitelist:
        description:
            - Specifies the data group name of source ip whitelist when SSL forward proxy bypass feature is enabled.
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
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    strict_resume:
        description:
            - Specifies the name of the application service to which the profile belongs.
    unclean_shutdown:
        description:
            - When enabled, the SSL profile performs unclean shutdowns of all SSL connections without exchanging the
              required SSL shutdown alerts.
        default: enabled
        choices: ['enabled', 'disabled']
    generic_alert:
        description:
            - Enables or disables generic-alert. 
        choices: ['enabled', 'disabled']
    ssl_sign_hash:
        description:
            - Specifies SSL sign hash algorithm which is used to sign and verify SSL Server Key Exchange and Certificate
              Verify messages for the specified SSL profiles.
        default: sha1
requirements:
    - BIG-IP >= 12.0
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = ''' 
- name: Create LTM Client SSL profile
  f5bigip_ltm_profile_client_ssl:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_client_ssl_profile
    partition: Common
    key: /Common/exemple.localhost.key
    cert: /Common/exemple.localhost.crt
    ciphers: DEFAULT:!SSLv2:!SSLv3:!TLSv1
    tm_options:
      - dont-insert-empty-fragments
      - single-dh-use
      - no-sslv2
      - no-sslv3
      - no-tlsv1
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
            allow_non_ssl=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            app_service=dict(type='str'),
            authenticate=dict(type='str'),
            authenticate_depth=dict(type='int'),
            ca_file=dict(type='str'),
            cache_size=dict(type='int'),
            cache_timeout=dict(type='int', choices=range(0, 86401)),
            cert=dict(type='str'),
            # cert_extension_includes=dict(type='list'),
            # cert_key_chain=dict(type='list'),
            cert_lookup_by_ipaddr_port=dict(type='str'),
            chain=dict(type='str'),
            ciphers=dict(type='str'),
            client_cert_ca=dict(type='str'),
            crl_file=dict(type='str'),
            defaults_from=dict(type='str'),
            description=dict(type='str'),
            handshake_timeout=dict(type='int'),
            key=dict(type='str'),
            mod_ssl_methods=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            mode=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            tm_options=dict(type='list'),
            passphrase=dict(type='str', no_log=True),
            peer_cert_mode=dict(type='str', choices=['ignore', 'require']),
            peer_no_renegotiate_timeout=dict(type='int'),
            proxy_ssl=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            proxy_ssl_passthrough=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            proxy_ca_cert=dict(type='str'),
            proxy_ca_key=dict(type='str'),
            proxy_ca_passphrase=dict(type='str', no_log=True),
            renegotiate_max_record_delay=dict(type='str'),
            renegotiate_period=dict(type='str'),
            renegotiate_size=dict(type='str'),
            renegotiation=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            retain_certificate=dict(type='bool'),
            secure_renegotiation=dict(type='str'),
            max_renegotiations_per_minute=dict(type='int'),
            server_name=dict(type='str'),
            session_mirroring=dict(type='str'),
            session_ticket=dict(type='str'),
            sni_default=dict(type='bool'),
            sni_require=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            source_ip_blacklist=dict(type='str'),
            source_ip_whitelist=dict(type='str'),
            ssl_forward_proxy=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            ssl_forward_proxy_bypass=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            strict_resume=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            unclean_shutdown=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            generic_alert=dict(type='str', choices=F5_ACTIVATION_CHOICES),
            ssl_sign_hash=dict(type='str')
        )
        argument_spec.update(F5_PROVIDER_ARGS)
        argument_spec.update(F5_NAMED_OBJ_ARGS)
        return argument_spec

    @property
    def supports_check_mode(self):
        return True


class F5BigIpLtmProfileClientSsl(F5BigIpNamedObject):
    def _set_crud_methods(self):
        self._methods = {
            'create': self._api.tm.ltm.profile.client_ssls.client_ssl.create,
            'read': self._api.tm.ltm.profile.client_ssls.client_ssl.load,
            'update': self._api.tm.ltm.profile.client_ssls.client_ssl.update,
            'delete': self._api.tm.ltm.profile.client_ssls.client_ssl.delete,
            'exists': self._api.tm.ltm.profile.client_ssls.client_ssl.exists
        }


def main():
    params = ModuleParams()
    module = AnsibleModule(argument_spec=params.argument_spec, supports_check_mode=params.supports_check_mode)

    try:
        obj = F5BigIpLtmProfileClientSsl(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()
