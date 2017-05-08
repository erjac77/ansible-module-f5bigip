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
module: f5bigip_ltm_profile_server_ssl
short_description: BIG-IP ltm server-ssl profile module
description:
    - Configures a Server SSL profile.
version_added: 2.3
author:
    - "Gabriel Fortin"
notes:
    - Requires BIG-IP software version >= 11.6
requirements:
    - f5-sdk
options:
    alert-timeout:
        description:
            - Specifies the maximum time period in seconds to keep the SSL session active after alert message is sent.
        required: false
        default: 10
        choices: []
        aliases: []
        version_added: 2.3
    app_service:
        description:
            - Specifies the name of the application service to which the profile belongs.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    authenticate:
        description:
            - Specifies the frequency of authentication.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    authenticate_depth:
        description:
            - Specifies the client certificate chain maximum traversal depth.
        required: false
        default: 9
        choices: []
        aliases: []
        version_added: 2.3
    authenticate_name:
        description:
            - Specifies a Common Name (CN) that is embedded in a server certificate.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    ca_file:
        description:
            - Specifies the certificate authority (CA) file name.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    cache_size:
        description:
            - Specifies the SSL session cache size.
        required: false
        default: 262144
        choices: []
        aliases: []
        version_added: 2.3
    cache_timeout:
        description:
            - Specifies the SSL session cache timeout value.
        required: false
        default: 3600
        choices: range(0,86400)
        aliases: []
        version_added: 2.3
    cert:
        description:
            - Specifies the name of the certificate installed on the traffic management system for the purpose of terminating or initiating an SSL connection.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    chain:
        description:
            - Specifies or builds a certificate chain file that a client can use to authenticate the profile.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    ciphers:
        description:
            - Specifies a cipher name.
        required: false
        default: DEFAULT
        choices: []
        aliases: []
        version_added: 2.3
    crl_file:
        description:
            - Specifies the certificate revocation list file name.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    defaults_from:
        description:
            - Specifies the profile that you want to use as the parent profile.
        required: false
        default: serverssl
        choices: []
        aliases: []
        version_added: 2.3
    description:
        description:
            - User defined description.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    expire_cert_response_control:
        description:
            - Specifies the BIGIP action when the server certificate has expired.
        required: false
        default: drop
        choices: ['drop', 'ignore']
        aliases: []
        version_added: 2.3
    handshake_timeout:
        description:
            - Specifies the handshake timeout in seconds.
        required: false
        default: 10
        choices: []
        aliases: []
        version_added: 2.3
    key:
        description:
            - Specifies the key file name.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    mod_ssl_methods:
        description:
            - Enables or disables ModSSL method emulation.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    mode:
        description:
            - Enables or disables SSL processing.
        required: false
        default: enabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    options:
        description:
            - Enables options, including some industry-related workarounds.
        required: false
        default: dont-insert-empty-fragments
        choices: ['all_bugfixes', 'cipher_server_preference', 'dont_insert_empty_fragments', 'ephemeral_rsa', 'microsoft_big_sslv3_buffer', 'microsoft_sess_id_bug', 'msie_sslv2_rsa_padding', 
                    'netscape_ca_dn_bug', 'netscape_challenge_bug', 'netscape_demo_cipher_change_bug', 'netscape_reuse_cipher_change_bug', 'no_session_resumption_on_renegotiation', 'no_ssl',
                    'no_sslv2', 'no_sslv3', 'no_tls', 'no_tlsv1', 'no_tlsv1_1', 'no_tlsv1_2', 'no_dtls', 'passive_close, none, pkcs1_check_1', 'pkcs1_check_2, single_dh_use', 'ssleay_080_client_dh_bug',
                    'sslref2_reuse_cert_type_bug', 'tls_d5_bug', 'tls_rollback_bug']
        aliases: []
        version_added: 2.3
    name:
        description:
            - Specifies a unique name for the component.
        required: true
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    partition:
        description:
            - Displays the administrative partition within which the component resides.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    passphrase:
        description:
            - Specifies the key passphrase, if required.
        required: false
        default: none
        choices: []
        aliases: []
        version_added: 2.3
    peer_cert_mode:
        description:
            - Specifies the peer certificate mode.
        required: false
        default: ignore
        choices: ['ignore', 'require']
        aliases: []
        version_added: 2.3
    port:
        description:
            - Specifies a service for the data channel port used for this Server SSL profile.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    proxy_ssl:
        description:
            - Enabling this option requires a corresponding server ssl profile with proxy-ssl enabled to perform transparent SSL decryption.
        required: false
        default: null
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    proxy_ssl_passthrough:
        description:
            - This allows Proxy SSL to passthrough the traffic when ciphersuite negotiated between the client and server is not supported.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    renegotiate_period:
        description:
            - Specifies the number of seconds from the initial connect time after which the system renegotiates an SSL session.
        required: false
        default: indefinite
        choices: []
        aliases: []
        version_added: 2.3
    renegotiate_size:
        description:
            - Specifies a throughput size, in megabytes, of SSL renegotiation.
        required: false
        default: Indefinite
        choices: []
        aliases: []
        version_added: 2.3
    renegotiation:
        description:
            - Specifies whether renegotiations are enabled.
        required: false
        default: enabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    retain_certificate:
        description:
            - APM module requires storing certificate in SSL session. When set to false, certificate will not be stored in SSL session.
        required: false
        default: True
        choices: [True, False]
        aliases: []
        version_added: 2.3
    generic_alert:
        description:
            - Enables or disables generic-alert.
        required: false
        default: enabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    secure_renegotiation:
        description:
            - Specifies the secure renegotiation mode.
        required: false
        default: require-strict
        choices: ['request', 'require', 'require-strict']
        aliases: []
        version_added: 2.3
    server_name:
        description:
            - Specifies the server name to be included in SNI (server name indication) extension during SSL handshake in ClientHello.
        required: false
        default: null
        choices: []
        aliases: []
        version_added: 2.3
    session_mirroring:
        description:
            - Enables or disables the mirroring of sessions to high availability peer.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    session_ticket:
        description:
            - Enables or disables session-ticket.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
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
    sni_default:
        description:
            - When true, this profile is the default SSL profile when the server name in a client connection does not match any configured server names, or a client connection does not specify any server name at all.
        required: false
        default: null
        choices: [true, false]
        aliases: []
        version_added: 2.3
    sni_require:
        description:
            - When this option is enabled, connections to a server that does not support SNI extension will be rejected.
        required: false
        default: null
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    ssl_forward_proxy:
        description:
            - Enables or disables SSL forward proxy feature.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    ssl_forward_proxy_bypass:
        description:
            - Enables or disables SSL forward proxy bypass feature.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    ssl_sign_hash:
        description:
            - Specifies SSL sign hash algorithm which is used to sign and verify SSL Server Key Exchange and Certificate Verify messages for the specified SSL profiles.
        required: false
        default: sha1
        choices: []
        aliases: []
        version_added: 2.3
    strict_resume:
        description:
            - Enables or disables the resumption of SSL sessions after an unclean shutdown.
        required: false
        default: disabled
        choices: ['enabled', 'disabled']
        aliases: []
        version_added: 2.3
    unclean_shutdown:
        description:
            - When enabled, the SSL profile performs unclean shutdowns of all SSL connections without exchanging the required SSL shutdown alerts.
        required: false
        default: null
        choices: ['enabled', 'disabled]
        aliases: []
        version_added: 2.3
    untrusted_cert_response_control:
        description:
            - Specifies the BIGIP action when the server certificate has untrusted CA.
        required: false
        default: drop
        choices: ['drop', 'ignore']
        aliases: []
        version_added: 2.3
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

from ansible_common_f5.f5_bigip import *

BIGIP_LTM_PROFILE_SERVER_SSL_ARGS = dict(
    alert_timeout               =   dict(type='int'),
    app_service                 =   dict(type='str'),
    authenticate                =   dict(type='str'),
    authenticate_depth          =   dict(type='int'),
    authenticate_name           =   dict(type='str'),
    ca_file                     =   dict(type='str'),
    cache_size                  =   dict(type='int'),
    cache_timeout               =   dict(type='int', choices=range(0,86400)),
    cert                        =   dict(type='str'),
    chain                       =   dict(type='str'),
    ciphers                     =   dict(type='str'),
    crl_file                    =   dict(type='str'),
    defaults_from               =   dict(type='str'),
    description                 =   dict(type='str'),
    expire_cert_response_control=   dict(type='str', choices=['drop', 'ignore']),
    handshake_timeout           =   dict(type='int'),
    key                         =   dict(type='str'),
    mod_ssl_methods             =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    mode                        =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    options                     =   dict(type='str', choices=['all_bugfixes', 'cipher_server_preference', 'dont_insert_empty_fragments', 'ephemeral_rsa', 'microsoft_big_sslv3_buffer', 'microsoft_sess_id_bug', 'msie_sslv2_rsa_padding', 
                                                                'netscape_ca_dn_bug', 'netscape_challenge_bug', 'netscape_demo_cipher_change_bug', 'netscape_reuse_cipher_change_bug', 'no_session_resumption_on_renegotiation', 'no_ssl',
                                                                'no_sslv2', 'no_sslv3', 'no_tls', 'no_tlsv1', 'no_tlsv1_1', 'no_tlsv1_2', 'no_dtls', 'passive_close, none, pkcs1_check_1', 'pkcs1_check_2, single_dh_use', 'ssleay_080_client_dh_bug',
                                                                'sslref2_reuse_cert_type_bug', 'tls_d5_bug', 'tls_rollback_bug']),
    passphrase                  =   dict(type='str'),
    peer_cert_mode              =   dict(type='str', choices=['ignore', 'require']),
    proxy_ssl                   =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    proxy_ssl_passthrough       =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    renegotiate_period          =   dict(type='str'),
    renegotiate_size            =   dict(type='str'),
    renegotiation               =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    retain_certificate          =   dict(type='bool'),
    generic_alert               =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    secure_renegotiation        =   dict(type='str', choices=['request', 'require', 'require-strict']),
    server_name                 =   dict(type='str'),
    session_mirroring           =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    session_ticket              =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    sni_default                 =   dict(type='bool'),
    sni_require                 =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    ssl_forward_proxy           =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    ssl_forward_proxy_bypass    =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    ssl_sign_hash               =   dict(type='str'),
    strict_resume               =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    unclean_shutdown            =   dict(type='str', choices=F5_ACTIVATION_CHOICES),
    untrusted_cert_response_control=dict(type='str', choices=['drop', 'ignore'])
)

class F5BigIpLtmProfileServerSsl(F5BigIpNamedObject):
    def set_crud_methods(self):
        self.methods = {
            'create':   self.mgmt_root.tm.ltm.profile.server_ssls.server_ssl.create,
            'read':     self.mgmt_root.tm.ltm.profile.server_ssls.server_ssl.load,
            'update':   self.mgmt_root.tm.ltm.profile.server_ssls.server_ssl.update,
            'delete':   self.mgmt_root.tm.ltm.profile.server_ssls.server_ssl.delete,
            'exists':   self.mgmt_root.tm.ltm.profile.server_ssls.server_ssl.exists
        }

def main():
    # Translation list for conflictual params
    tr = {}
    
    module = AnsibleModuleF5BigIpNamedObject(argument_spec=BIGIP_LTM_PROFILE_SERVER_SSL_ARGS, supports_check_mode=False)
    
    try:
        obj = F5BigIpLtmProfileServerSsl(check_mode=module.supports_check_mode, tr=tr, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()