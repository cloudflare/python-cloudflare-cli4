""" API core commands for Cloudflare API"""

def api_v4(self):
    """ API core commands for Cloudflare API"""

    # The API commands for /user/
    user(self)
    user_audit_logs(self)
    user_load_balancers(self)
    user_load_balancing_analytics(self)
    user_tokens_verify(self)

    # The API commands for /radar/
    radar(self)

    # The API commands for /zones/
    zones(self)
    zones_access(self)
    zones_amp(self)
    zones_analytics(self)
    zones_argo(self)
    zones_dns_analytics(self)
    zones_dnssec(self)
    zones_firewall(self)
    zones_load_balancers(self)
    zones_logpush(self)
    zones_logs(self)
    zones_media(self)
    zones_origin_tls_client_auth(self)
    zones_rate_limits(self)
    zones_secondary_dns(self)
    zones_settings(self)
    zones_spectrum(self)
    zones_ssl(self)
    zones_waiting_rooms(self)
    zones_workers(self)
    zones_extras(self)
    zones_web3(self)
    zones_email(self)
    zones_api_gateway(self)

    # The API commands for /railguns/
    railguns(self)

    # The API commands for /certificates/
    certificates(self)

    # The API commands for /ips/
    ips(self)

    # The API commands for /accounts/
    accounts(self)
    accounts_access(self)
    accounts_addressing(self)
    accounts_audit_logs(self)
    accounts_diagnostics(self)
    accounts_firewall(self)
    accounts_load_balancers(self)
    accounts_secondary_dns(self)
    accounts_stream(self)
    accounts_extras(self)
    accounts_email(self)
    accounts_r2(self)

    # The API commands for /memberships/
    memberships(self)

    # The API commands for /graphql
    graphql(self)

    # Issue 151
    from_developers(self)

def user(self):
    """ user """

    self.add('AUTH', 'user')
    self.add('VOID', 'user/billing')
    self.add('AUTH', 'user/billing/history')
    self.add('AUTH', 'user/billing/profile')
    self.add('VOID', 'user/billing/subscriptions')
#   self.add('AUTH', 'user/billing/subscriptions/apps')
#   self.add('AUTH', 'user/billing/subscriptions/zones')
    self.add('VOID', 'user/firewall')
    self.add('VOID', 'user/firewall/access_rules')
    self.add('AUTH', 'user/firewall/access_rules/rules')
    self.add('AUTH', 'user/invites')
    self.add('AUTH', 'user/organizations')
    self.add('AUTH', 'user/subscriptions')

def zones(self):
    """ zones """

    self.add('AUTH', 'zones')
    self.add('AUTH', 'zones', 'activation_check')
    self.add('AUTH', 'zones', 'available_plans')
    self.add('AUTH', 'zones', 'available_rate_plans')
    self.add('AUTH', 'zones', 'bot_management')
    self.add('AUTH', 'zones', 'bot_management/feedback')
    self.add('AUTH', 'zones', 'client_certificates')
    self.add('AUTH', 'zones', 'custom_certificates')
    self.add('AUTH', 'zones', 'custom_certificates/prioritize')
    self.add('AUTH', 'zones', 'custom_csrs')
    self.add('AUTH', 'zones', 'custom_hostnames')
    self.add('AUTH', 'zones', 'custom_hostnames/fallback_origin')
    self.add('AUTH', 'zones', 'custom_ns')
    self.add('AUTH', 'zones', 'custom_pages')
    self.add('AUTH', 'zones', 'dns_records')
    self.add('AUTH', 'zones', 'dns_records/export')
    self.add('AUTH', 'zones', 'dns_records/import')
    self.add('AUTH', 'zones', 'dns_records/scan')
    self.add('VOID', 'zones', 'dns_settings')
    self.add('AUTH', 'zones', 'dns_settings/use_apex_ns')
    self.add('AUTH', 'zones', 'filters')
    self.add('AUTH', 'zones', 'filters/validate-expr')
    self.add('AUTH', 'zones', 'healthchecks')
    self.add('AUTH', 'zones', 'healthchecks/preview')
    self.add('AUTH', 'zones', 'keyless_certificates')
    self.add('AUTH', 'zones', 'origin_max_http_version')
    self.add('AUTH', 'zones', 'pagerules')
    self.add('AUTH', 'zones', 'pagerules/settings')
    self.add('AUTH', 'zones', 'purge_cache')
    self.add('AUTH', 'zones', 'railguns')
    self.add('AUTH', 'zones', 'railguns', 'diagnose')
    self.add('VOID', 'zones', 'security')
    self.add('AUTH', 'zones', 'security/events')
    self.add('AUTH', 'zones', 'subscription')

def zones_settings(self):
    """ zones settings """

    self.add('AUTH', 'zones', 'settings')
    self.add('AUTH', 'zones', 'settings/0rtt')
    self.add('AUTH', 'zones', 'settings/advanced_ddos')
    self.add('AUTH', 'zones', 'settings/always_online')
    self.add('AUTH', 'zones', 'settings/always_use_https')
    self.add('AUTH', 'zones', 'settings/automatic_https_rewrites')
    self.add('AUTH', 'zones', 'settings/automatic_platform_optimization')
    self.add('AUTH', 'zones', 'settings/brotli')
    self.add('AUTH', 'zones', 'settings/browser_cache_ttl')
    self.add('AUTH', 'zones', 'settings/browser_check')
    self.add('AUTH', 'zones', 'settings/cache_level')
    self.add('AUTH', 'zones', 'settings/challenge_ttl')
    self.add('AUTH', 'zones', 'settings/ciphers')
    self.add('AUTH', 'zones', 'settings/development_mode')
    self.add('AUTH', 'zones', 'settings/early_hints')
    self.add('AUTH', 'zones', 'settings/email_obfuscation')
    self.add('AUTH', 'zones', 'settings/h2_prioritization')
    self.add('AUTH', 'zones', 'settings/hotlink_protection')
    self.add('AUTH', 'zones', 'settings/http2')
    self.add('AUTH', 'zones', 'settings/http3')
    self.add('AUTH', 'zones', 'settings/image_resizing')
    self.add('AUTH', 'zones', 'settings/ip_geolocation')
    self.add('AUTH', 'zones', 'settings/ipv6')
    self.add('AUTH', 'zones', 'settings/min_tls_version')
    self.add('AUTH', 'zones', 'settings/minify')
    self.add('AUTH', 'zones', 'settings/mirage')
    self.add('AUTH', 'zones', 'settings/mobile_redirect')
    self.add('AUTH', 'zones', 'settings/nel')
    self.add('AUTH', 'zones', 'settings/opportunistic_encryption')
    self.add('AUTH', 'zones', 'settings/opportunistic_onion')
    self.add('AUTH', 'zones', 'settings/orange_to_orange')
    self.add('AUTH', 'zones', 'settings/origin_error_page_pass_thru')
    self.add('AUTH', 'zones', 'settings/origin_max_http_version')
    self.add('AUTH', 'zones', 'settings/polish')
    self.add('AUTH', 'zones', 'settings/prefetch_preload')
    self.add('AUTH', 'zones', 'settings/privacy_pass')
    self.add('AUTH', 'zones', 'settings/proxy_read_timeout')
    self.add('AUTH', 'zones', 'settings/pseudo_ipv4')
    self.add('AUTH', 'zones', 'settings/response_buffering')
    self.add('AUTH', 'zones', 'settings/rocket_loader')
    self.add('AUTH', 'zones', 'settings/security_header')
    self.add('AUTH', 'zones', 'settings/security_level')
    self.add('AUTH', 'zones', 'settings/server_side_exclude')
    self.add('AUTH', 'zones', 'settings/sort_query_string_for_cache')
    self.add('AUTH', 'zones', 'settings/ssl')
    self.add('AUTH', 'zones', 'settings/ssl_recommender')
    self.add('AUTH', 'zones', 'settings/tls_1_3')
    self.add('AUTH', 'zones', 'settings/tls_client_auth')
    self.add('AUTH', 'zones', 'settings/true_client_ip_header')
    self.add('AUTH', 'zones', 'settings/waf')
    self.add('AUTH', 'zones', 'settings/webp')
    self.add('AUTH', 'zones', 'settings/websockets')

def zones_analytics(self):
    """ zones analytics """

    self.add('VOID', 'zones', 'analytics')
#   self.add('AUTH', 'zones', 'analytics/colos') # deprecated 2021-03-01 - expired!
#   self.add('AUTH', 'zones', 'analytics/dashboard') # deprecated 2021-03-01 - expired!
    self.add('AUTH', 'zones', 'analytics/latency')
    self.add('AUTH', 'zones', 'analytics/latency/colos')

def zones_firewall(self):
    """ zones filewall """

    self.add('VOID', 'zones', 'firewall')
    self.add('VOID', 'zones', 'firewall/access_rules')
    self.add('AUTH', 'zones', 'firewall/access_rules/rules')
    self.add('AUTH', 'zones', 'firewall/lockdowns')
    self.add('AUTH', 'zones', 'firewall/rules')
    self.add('AUTH', 'zones', 'firewall/ua_rules')
    self.add('VOID', 'zones', 'firewall/waf')
    self.add('AUTH', 'zones', 'firewall/waf/overrides')
    self.add('AUTH', 'zones', 'firewall/waf/packages')
    self.add('AUTH', 'zones', 'firewall/waf/packages', 'groups')
    self.add('AUTH', 'zones', 'firewall/waf/packages', 'rules')

def zones_rate_limits(self):
    """ zones rate_limits """

    self.add('AUTH', 'zones', 'rate_limits')

def zones_dns_analytics(self):
    """ zones dns_analytics """

    self.add('VOID', 'zones', 'dns_analytics')
    self.add('AUTH', 'zones', 'dns_analytics/report')
    self.add('AUTH', 'zones', 'dns_analytics/report/bytime')

def zones_amp(self):
    """ zones amp """

    self.add('VOID', 'zones', 'amp')
    self.add('AUTH', 'zones', 'amp/sxg')

def zones_logpush(self):
    """ zones logpush """

    self.add('VOID', 'zones', 'logpush')
    self.add('VOID', 'zones', 'logpush/datasets')
    self.add('AUTH', 'zones', 'logpush/datasets', 'fields')
    self.add('AUTH', 'zones', 'logpush/datasets', 'jobs')
    self.add('VOID', 'zones', 'logpush/edge')
    self.add('AUTH', 'zones', 'logpush/edge/jobs')
    self.add('AUTH', 'zones', 'logpush/jobs')
    self.add('AUTH', 'zones', 'logpush/ownership')
    self.add('AUTH', 'zones', 'logpush/ownership/validate')
    self.add('VOID', 'zones', 'logpush/validate')
    self.add('VOID', 'zones', 'logpush/validate/destination')
    self.add('AUTH', 'zones', 'logpush/validate/destination/exists')
    self.add('AUTH', 'zones', 'logpush/validate/origin')

def zones_logs(self):
    """ zones logs """

    self.add('VOID', 'zones', 'logs')
    self.add('VOID', 'zones', 'logs/control')
    self.add('VOID', 'zones', 'logs/control/retention')
    self.add('AUTH', 'zones', 'logs/control/retention/flag')
    self.add('AUTH_UNWRAPPED', 'zones', 'logs/received')
    self.add('AUTH_UNWRAPPED', 'zones', 'logs/received/fields')
    self.add('AUTH_UNWRAPPED', 'zones', 'logs/rayids')

def railguns(self):
    """ railguns """

    self.add('AUTH', 'railguns')
    self.add('AUTH', 'railguns', 'zones')

def certificates(self):
    """ certificates """

    self.add('CERT', 'certificates')

def ips(self):
    """ ips """

    self.add('OPEN', 'ips')

def zones_argo(self):
    """ zones argo """

    self.add('VOID', 'zones', 'argo')
    self.add('AUTH', 'zones', 'argo/tiered_caching')
    self.add('AUTH', 'zones', 'argo/smart_routing')

def zones_dnssec(self):
    """ zones dnssec """

    self.add('AUTH', 'zones', 'dnssec')

def zones_spectrum(self):
    """ zones spectrum """

    self.add('VOID', 'zones', 'spectrum')
    self.add('VOID', 'zones', 'spectrum/analytics')
    self.add('VOID', 'zones', 'spectrum/analytics/aggregate')
    self.add('AUTH', 'zones', 'spectrum/analytics/aggregate/current')
    self.add('VOID', 'zones', 'spectrum/analytics/events')
    self.add('AUTH', 'zones', 'spectrum/analytics/events/bytime')
    self.add('AUTH', 'zones', 'spectrum/analytics/events/summary')
    self.add('AUTH', 'zones', 'spectrum/apps')

def zones_ssl(self):
    """ zones ssl """

    self.add('VOID', 'zones', 'ssl')
    self.add('AUTH', 'zones', 'ssl/analyze')
    self.add('AUTH', 'zones', 'ssl/certificate_packs')
    self.add('AUTH', 'zones', 'ssl/certificate_packs/order')
    self.add('AUTH', 'zones', 'ssl/certificate_packs/quota')
    self.add('AUTH', 'zones', 'ssl/recommendation')
    self.add('AUTH', 'zones', 'ssl/verification')
    self.add('VOID', 'zones', 'ssl/universal')
    self.add('AUTH', 'zones', 'ssl/universal/settings')

def zones_origin_tls_client_auth(self):
    """ zones origin_tls_client_auth """

    self.add('AUTH', 'zones', 'origin_tls_client_auth')
    self.add('AUTH', 'zones', 'origin_tls_client_auth/hostnames')
    self.add('AUTH', 'zones', 'origin_tls_client_auth/hostnames/certificates')
    self.add('AUTH', 'zones', 'origin_tls_client_auth/settings')

def zones_workers(self):
    """ zones workers """

    self.add('VOID', 'zones', 'workers')
    self.add('AUTH', 'zones', 'workers/filters')
    self.add('AUTH', 'zones', 'workers/routes')
    self.add('AUTH', 'zones', 'workers/script')
    self.add('AUTH', 'zones', 'workers/script/bindings')

def zones_load_balancers(self):
    """ zones load_balancers """

    self.add('AUTH', 'zones', 'load_balancers')

def zones_secondary_dns(self):
    """ zones secondary_dns """

    self.add('AUTH', 'zones', 'secondary_dns')
    self.add('AUTH', 'zones', 'secondary_dns/force_axfr')
    self.add('AUTH', 'zones', 'secondary_dns/incoming')
    self.add('AUTH', 'zones', 'secondary_dns/outgoing')
    self.add('AUTH', 'zones', 'secondary_dns/outgoing/disable')
    self.add('AUTH', 'zones', 'secondary_dns/outgoing/enable')
    self.add('AUTH', 'zones', 'secondary_dns/outgoing/force_notify')
    self.add('AUTH', 'zones', 'secondary_dns/outgoing/status')

def user_load_balancers(self):
    """ API user load_balancers """

    self.add('VOID', 'user/load_balancers')
    self.add('AUTH', 'user/load_balancers/monitors')
    self.add('AUTH', 'user/load_balancers/monitors', 'preview')
    self.add('AUTH', 'user/load_balancers/monitors', 'references')
    self.add('AUTH', 'user/load_balancers/preview')
    self.add('AUTH', 'user/load_balancers/pools')
    self.add('AUTH', 'user/load_balancers/pools', 'health')
    self.add('AUTH', 'user/load_balancers/pools', 'preview')
    self.add('AUTH', 'user/load_balancers/pools', 'references')

def user_audit_logs(self):
    """ user audit_logs """

    self.add('AUTH', 'user/audit_logs')

def user_load_balancing_analytics(self):
    """ user load_balancing_analytics """

    self.add('VOID', 'user/load_balancing_analytics')
    self.add('AUTH', 'user/load_balancing_analytics/events')

def user_tokens_verify(self):
    """ user tokens """

    self.add('AUTH', 'user/tokens')
    self.add('AUTH', 'user/tokens/permission_groups')
    self.add('AUTH', 'user/tokens/verify')
    self.add('AUTH', 'user/tokens', 'value')

def accounts(self):
    """ accounts """

    self.add('AUTH', 'accounts')
    self.add('VOID', 'accounts', 'billing')
    self.add('AUTH', 'accounts', 'billing/profile')
    self.add('VOID', 'accounts', 'brand-protection')
    self.add('AUTH', 'accounts', 'brand-protection/submit')
    self.add('AUTH', 'accounts', 'brand-protection/url-info')
    self.add('AUTH', 'accounts', 'cfd_tunnel')
    self.add('AUTH', 'accounts', 'cfd_tunnel', 'configurations')
    self.add('AUTH', 'accounts', 'cfd_tunnel', 'connections')
    self.add('AUTH', 'accounts', 'cfd_tunnel', 'token')
    self.add('AUTH', 'accounts', 'custom_pages')
    self.add('VOID', 'accounts', 'dlp')
    self.add('VOID', 'accounts', 'dlp/patterns')
    self.add('AUTH', 'accounts', 'dlp/patterns/validate')
    self.add('AUTH', 'accounts', 'dlp/profiles')
    self.add('AUTH', 'accounts', 'dlp/profiles/custom')
    self.add('AUTH', 'accounts', 'dlp/profiles/predefined')
    self.add('AUTH', 'accounts', 'members')
    self.add('VOID', 'accounts', 'mnm')
    self.add('AUTH', 'accounts', 'mnm/config')
    self.add('AUTH', 'accounts', 'mnm/config/full')
    self.add('AUTH', 'accounts', 'mnm/rules')
    self.add('AUTH', 'accounts', 'mnm/rules', 'advertisement')
    self.add('AUTH', 'accounts', 'railguns')
    self.add('AUTH', 'accounts', 'railguns', 'connections')
    self.add('VOID', 'accounts', 'registrar')
    self.add('AUTH', 'accounts', 'registrar/domains')
    self.add('AUTH', 'accounts', 'registrar/contacts')
    self.add('AUTH', 'accounts', 'roles')
    self.add('VOID', 'accounts', 'rules')
    self.add('AUTH', 'accounts', 'rules/lists')
    self.add('AUTH', 'accounts', 'rules/lists', 'items')
    self.add('AUTH', 'accounts', 'rules/lists/bulk_operations')
    self.add('AUTH', 'accounts', 'rulesets')
    self.add('AUTH', 'accounts', 'rulesets', 'versions')
    self.add('AUTH', 'accounts', 'rulesets', 'versions', 'by_tag')
    self.add('AUTH', 'accounts', 'rulesets', 'versions', 'by_tag/wordpress')
    self.add('AUTH', 'accounts', 'rulesets', 'rules')
#   self.add('AUTH', 'accounts', 'rulesets/import')
    self.add('VOID', 'accounts', 'rulesets/phases')
    self.add('AUTH', 'accounts', 'rulesets/phases', 'entrypoint')
    self.add('AUTH', 'accounts', 'rulesets/phases', 'entrypoint/versions')
    self.add('AUTH', 'accounts', 'rulesets/phases', 'versions')
    self.add('VOID', 'accounts', 'storage')
    self.add('AUTH', 'accounts', 'storage/analytics')
    self.add('AUTH', 'accounts', 'storage/analytics/stored')
    self.add('VOID', 'accounts', 'storage/kv')
    self.add('AUTH', 'accounts', 'storage/kv/namespaces')
    self.add('AUTH', 'accounts', 'storage/kv/namespaces', 'bulk')
    self.add('AUTH', 'accounts', 'storage/kv/namespaces', 'keys')
    self.add('AUTH', 'accounts', 'storage/kv/namespaces', 'values')
    self.add('AUTH', 'accounts', 'storage/kv/namespaces', 'metadata')
    self.add('AUTH', 'accounts', 'subscriptions')
    self.add('AUTH', 'accounts', 'tunnels')
    self.add('AUTH', 'accounts', 'tunnels', 'connections')
    self.add('AUTH', 'accounts', 'virtual_dns')
    self.add('VOID', 'accounts', 'virtual_dns', 'dns_analytics')
    self.add('AUTH', 'accounts', 'virtual_dns', 'dns_analytics/report')
    self.add('AUTH', 'accounts', 'virtual_dns', 'dns_analytics/report/bytime')
    self.add('VOID', 'accounts', 'workers')
    self.add('AUTH', 'accounts', 'workers/account-settings')
    self.add('VOID', 'accounts', 'workers/dispatch')
    self.add('AUTH', 'accounts', 'workers/dispatch/namespaces')
    self.add('AUTH', 'accounts', 'workers/dispatch/namespaces', 'scripts')
    self.add('AUTH', 'accounts', 'workers/dispatch/namespaces', 'scripts', 'tags')
    self.add('AUTH', 'accounts', 'workers/domains')
    self.add('VOID', 'accounts', 'workers/durable_objects')
    self.add('AUTH', 'accounts', 'workers/durable_objects/namespaces')
    self.add('AUTH', 'accounts', 'workers/durable_objects/namespaces', 'objects')
    self.add('AUTH', 'accounts', 'workers/queues')
    self.add('AUTH', 'accounts', 'workers/queues', 'consumers')
    self.add('AUTH', 'accounts', 'workers/scripts')
    self.add('AUTH', 'accounts', 'workers/scripts', 'schedules')
    self.add('AUTH', 'accounts', 'workers/scripts', 'tails')
    self.add('AUTH', 'accounts', 'workers/scripts', 'usage-model')
    self.add('AUTH', 'accounts', 'workers/subdomain')

def accounts_addressing(self):
    """ accounts addressing """

    self.add('VOID', 'accounts', 'addressing')
    self.add('AUTH', 'accounts', 'addressing/address_maps')
    self.add('AUTH', 'accounts', 'addressing/address_maps', 'accounts')
    self.add('AUTH', 'accounts', 'addressing/address_maps', 'ips')
    self.add('AUTH', 'accounts', 'addressing/address_maps', 'zones')
    self.add('AUTH', 'accounts', 'addressing/loa_documents')
    self.add('AUTH', 'accounts', 'addressing/loa_documents', 'download')
    self.add('AUTH', 'accounts', 'addressing/prefixes')
    self.add('VOID', 'accounts', 'addressing/prefixes', 'bgp')
    self.add('AUTH', 'accounts', 'addressing/prefixes', 'bgp/status')
    self.add('AUTH', 'accounts', 'addressing/prefixes', 'delegations')

def accounts_audit_logs(self):
    """ accounts audit_logs """

    self.add('AUTH', 'accounts', 'audit_logs')

def accounts_load_balancers(self):
    """ accounts load_balancers """

    self.add('VOID', 'accounts', 'load_balancers')
    self.add('AUTH', 'accounts', 'load_balancers/preview')
    self.add('AUTH', 'accounts', 'load_balancers/monitors')
    self.add('AUTH', 'accounts', 'load_balancers/monitors', 'preview')
    self.add('AUTH', 'accounts', 'load_balancers/monitors', 'references')
    self.add('AUTH', 'accounts', 'load_balancers/pools')
    self.add('AUTH', 'accounts', 'load_balancers/pools', 'health')
    self.add('AUTH', 'accounts', 'load_balancers/pools', 'preview')
    self.add('AUTH', 'accounts', 'load_balancers/pools', 'references')
    self.add('AUTH', 'accounts', 'load_balancers/regions')
    self.add('AUTH', 'accounts', 'load_balancers/search')


def accounts_firewall(self):
    """ accounts firewall """

    self.add('VOID', 'accounts', 'firewall')
    self.add('VOID', 'accounts', 'firewall/access_rules')
    self.add('AUTH', 'accounts', 'firewall/access_rules/rules')

def accounts_secondary_dns(self):
    """ accounts secondary_dns """

    self.add('VOID', 'accounts', 'secondary_dns')
#   self.add('AUTH', 'accounts', 'secondary_dns/masters')
    self.add('AUTH', 'accounts', 'secondary_dns/primaries')
    self.add('AUTH', 'accounts', 'secondary_dns/tsigs')
    self.add('AUTH', 'accounts', 'secondary_dns/acls')
    self.add('AUTH', 'accounts', 'secondary_dns/peers')

def accounts_stream(self):
    """ accounts stream """

    self.add('AUTH', 'accounts', 'stream')
    self.add('AUTH', 'accounts', 'stream', 'captions')
    self.add('AUTH', 'accounts', 'stream', 'embed')
    self.add('AUTH', 'accounts', 'stream', 'downloads')
    self.add('AUTH', 'accounts', 'stream', 'token')
    self.add('AUTH', 'accounts', 'stream/clip')
    self.add('AUTH', 'accounts', 'stream/copy')
    self.add('AUTH', 'accounts', 'stream/direct_upload')
    self.add('AUTH', 'accounts', 'stream/keys')
#   self.add('AUTH', 'accounts', 'stream/preview')
    self.add('AUTH', 'accounts', 'stream/watermarks')
    self.add('AUTH', 'accounts', 'stream/webhook')
    self.add('AUTH', 'accounts', 'stream/live_inputs')
    self.add('AUTH', 'accounts', 'stream/live_inputs', 'outputs')
    self.add('AUTH', 'accounts', 'stream/live_inputs', 'outputs', 'enabled')

def zones_media(self):
    """ zones media """

    self.add('AUTH', 'zones', 'media')
    self.add('AUTH', 'zones', 'media', 'embed')
    self.add('AUTH', 'zones', 'media', 'preview')

def memberships(self):
    """ memberships """

    self.add('AUTH', 'memberships')

def graphql(self):
    """ graphql """

    self.add('AUTH', 'graphql')

def zones_access(self):
    """ zones access """

    self.add('VOID', 'zones', 'access')
    self.add('AUTH', 'zones', 'access/apps')
    self.add('AUTH', 'zones', 'access/apps', 'policies')
    self.add('AUTH', 'zones', 'access/apps', 'revoke_tokens')
    self.add('AUTH', 'zones', 'access/bookmarks')
    self.add('AUTH', 'zones', 'access/certificates')
#   self.add('AUTH', 'zones', 'access/apps/ca')
    self.add('AUTH', 'zones', 'access/apps', 'ca')
    self.add('AUTH', 'zones', 'access/apps', 'user_policy_checks')
    self.add('AUTH', 'zones', 'access/groups')
    self.add('AUTH', 'zones', 'access/identity_providers')
    self.add('AUTH', 'zones', 'access/organizations')
    self.add('AUTH', 'zones', 'access/organizations/revoke_user')
    self.add('AUTH', 'zones', 'access/service_tokens')

def accounts_access(self):
    """ accounts access """

    self.add('VOID', 'accounts', 'access')
#   self.add('AUTH', 'accounts', 'access/bookmarks') # deprecated 2023-03-19
    self.add('AUTH', 'accounts', 'access/gateway_ca')
    self.add('AUTH', 'accounts', 'access/groups')
    self.add('AUTH', 'accounts', 'access/identity_providers')
    self.add('AUTH', 'accounts', 'access/organizations')
#   self.add('AUTH', 'accounts', 'access/organizations/doh') # deprecated 2020-02-04 - expired!
    self.add('AUTH', 'accounts', 'access/organizations/revoke_user')
    self.add('AUTH', 'accounts', 'access/service_tokens')
    self.add('AUTH', 'accounts', 'access/service_tokens', 'refresh')
    self.add('AUTH', 'accounts', 'access/service_tokens', 'rotate')
    self.add('AUTH', 'accounts', 'access/apps')
#   self.add('AUTH', 'accounts', 'access/apps/ca')
    self.add('AUTH', 'accounts', 'access/apps', 'ca')
    self.add('AUTH', 'accounts', 'access/apps', 'policies')
    self.add('AUTH', 'accounts', 'access/apps', 'revoke_tokens')
    self.add('AUTH', 'accounts', 'access/apps', 'user_policy_checks')
    self.add('AUTH', 'accounts', 'access/certificates')
    self.add('AUTH', 'accounts', 'access/keys')
    self.add('AUTH', 'accounts', 'access/keys/rotate')
    self.add('VOID', 'accounts', 'access/logs')
    self.add('AUTH', 'accounts', 'access/logs/access_requests')
    self.add('AUTH', 'accounts', 'access/seats')
    self.add('AUTH', 'accounts', 'access/users')
    self.add('AUTH', 'accounts', 'access/users', 'failed_logins')

def accounts_diagnostics(self):
    """ accounts diagnostics """

    self.add('VOID', 'accounts', 'diagnostics')
    self.add('AUTH', 'accounts', 'diagnostics/traceroute')

def zones_waiting_rooms(self):
    """ zones waiting_rooms """

    self.add('AUTH', 'zones', 'waiting_rooms')
    self.add('AUTH', 'zones', 'waiting_rooms', 'events')
    self.add('AUTH', 'zones', 'waiting_rooms', 'events', 'details')
    self.add('AUTH', 'zones', 'waiting_rooms', 'rules')
    self.add('AUTH', 'zones', 'waiting_rooms', 'status')
    self.add('AUTH', 'zones', 'waiting_rooms/preview')

def accounts_extras(self):
    """ extras """

    self.add('VOID', 'accounts', 'alerting')
    self.add('VOID', 'accounts', 'alerting/v3')
    self.add('AUTH', 'accounts', 'alerting/v3/available_alerts')
    self.add('VOID', 'accounts', 'alerting/v3/destinations')
    self.add('AUTH', 'accounts', 'alerting/v3/destinations/eligible')
    self.add('AUTH', 'accounts', 'alerting/v3/destinations/pagerduty')
    self.add('AUTH', 'accounts', 'alerting/v3/destinations/webhooks')
    self.add('AUTH', 'accounts', 'alerting/v3/history')
    self.add('AUTH', 'accounts', 'alerting/v3/policies')

    self.add('AUTH', 'accounts', 'custom_ns')
    self.add('AUTH', 'accounts', 'custom_ns/availability')
    self.add('AUTH', 'accounts', 'custom_ns/verify')

    self.add('AUTH', 'accounts', 'devices')
    self.add('AUTH', 'accounts', 'devices', 'override_codes')
    self.add('AUTH', 'accounts', 'devices/policies')
    self.add('AUTH', 'accounts', 'devices/policy')
    self.add('AUTH', 'accounts', 'devices/policy', 'exclude')
#   self.add('AUTH', 'accounts', 'devices/policy/exclude')
    self.add('AUTH', 'accounts', 'devices/policy', 'fallback_domains')
#   self.add('AUTH', 'accounts', 'devices/policy/fallback_domains')
    self.add('AUTH', 'accounts', 'devices/policy', 'include')
#   self.add('AUTH', 'accounts', 'devices/policy/include')
    self.add('AUTH', 'accounts', 'devices/posture')
    self.add('AUTH', 'accounts', 'devices/posture/integration')
    self.add('AUTH', 'accounts', 'devices/revoke')
    self.add('AUTH', 'accounts', 'devices/settings')
    self.add('AUTH', 'accounts', 'devices/unrevoke')

    self.add('AUTH', 'accounts', 'dns_firewall')
    self.add('VOID', 'accounts', 'dns_firewall', 'dns_analytics')
    self.add('AUTH', 'accounts', 'dns_firewall', 'dns_analytics/report')
    self.add('AUTH', 'accounts', 'dns_firewall', 'dns_analytics/report/bytime')

    self.add('AUTH', 'accounts', 'gateway')
    self.add('AUTH', 'accounts', 'gateway/app_types')
    self.add('AUTH', 'accounts', 'gateway/categories')
    self.add('AUTH', 'accounts', 'gateway/configuration')
    self.add('AUTH', 'accounts', 'gateway/lists')
    self.add('AUTH', 'accounts', 'gateway/lists', 'items')
    self.add('AUTH', 'accounts', 'gateway/locations')
    self.add('AUTH', 'accounts', 'gateway/logging')
    self.add('AUTH', 'accounts', 'gateway/proxy_endpoints')
    self.add('AUTH', 'accounts', 'gateway/rules')

    self.add('VOID', 'accounts', 'images')
    self.add('AUTH', 'accounts', 'images/v1')
    self.add('AUTH', 'accounts', 'images/v1', 'blob')
    self.add('AUTH', 'accounts', 'images/v1/keys')
    self.add('AUTH', 'accounts', 'images/v1/stats')
    self.add('AUTH', 'accounts', 'images/v1/variants')
    self.add('VOID', 'accounts', 'images/v2')
    self.add('AUTH', 'accounts', 'images/v2/direct_upload')

    self.add('VOID', 'accounts', 'intel')
    self.add('VOID', 'accounts', 'intel-phishing')
    self.add('AUTH', 'accounts', 'intel-phishing/predict')
    self.add('AUTH', 'accounts', 'intel/asn')
    self.add('AUTH', 'accounts', 'intel/asn', 'subnets')
    self.add('AUTH', 'accounts', 'intel/dns')
    self.add('AUTH', 'accounts', 'intel/domain')
    self.add('AUTH', 'accounts', 'intel/domain-history')
    self.add('AUTH', 'accounts', 'intel/domain/bulk')
    self.add('AUTH', 'accounts', 'intel/ip')
    self.add('AUTH', 'accounts', 'intel/ip-list')
    self.add('AUTH', 'accounts', 'intel/miscategorization')
    self.add('AUTH', 'accounts', 'intel/whois')

    self.add('VOID', 'accounts', 'magic')
    self.add('AUTH', 'accounts', 'magic/cf_interconnects')
    self.add('AUTH', 'accounts', 'magic/gre_tunnels')
    self.add('AUTH', 'accounts', 'magic/ipsec_tunnels')
    self.add('AUTH', 'accounts', 'magic/ipsec_tunnels', 'psk_generate')
    self.add('AUTH', 'accounts', 'magic/routes')

    self.add('VOID', 'accounts', 'pages')
    self.add('AUTH', 'accounts', 'pages/projects')
    self.add('AUTH', 'accounts', 'pages/projects', 'deployments')
    self.add('VOID', 'accounts', 'pages/projects', 'deployments', 'history')
    self.add('AUTH', 'accounts', 'pages/projects', 'deployments', 'history/logs')
    self.add('AUTH', 'accounts', 'pages/projects', 'deployments', 'retry')
    self.add('AUTH', 'accounts', 'pages/projects', 'deployments', 'rollback')
    self.add('AUTH', 'accounts', 'pages/projects', 'domains')

    self.add('AUTH', 'accounts', 'pcaps')
    self.add('AUTH', 'accounts', 'pcaps', 'download')
    self.add('AUTH', 'accounts', 'pcaps/ownership')
    self.add('AUTH', 'accounts', 'pcaps/ownership/validate')

    self.add('VOID', 'accounts', 'teamnet')
    self.add('AUTH', 'accounts', 'teamnet/routes')
    self.add('AUTH', 'accounts', 'teamnet/routes/ip')
    self.add('AUTH', 'accounts', 'teamnet/routes/network')
    self.add('AUTH', 'accounts', 'teamnet/virtual_networks')

def zones_extras(self):
    """ zones extras """

    self.add('VOID', 'zones', 'acm')
    self.add('AUTH', 'zones', 'acm/total_tls')
    self.add('VOID', 'zones', 'cache')
    self.add('AUTH', 'zones', 'cache/variants')
    self.add('AUTH', 'zones', 'cache/cache_reserve')
    self.add('AUTH', 'zones', 'managed_headers')
    self.add('AUTH', 'zones', 'page_shield')
    self.add('AUTH', 'zones', 'page_shield/scripts')
    self.add('AUTH', 'zones', 'page_shield/connections')
    self.add('AUTH', 'zones', 'rulesets')
    self.add('AUTH', 'zones', 'rulesets', 'rules')
    self.add('AUTH', 'zones', 'rulesets', 'versions')
    self.add('VOID', 'zones', 'rulesets/phases')
    self.add('AUTH', 'zones', 'rulesets/phases', 'entrypoint')
    self.add('AUTH', 'zones', 'rulesets/phases', 'entrypoint/versions')
    self.add('VOID', 'zones', 'rulesets/phases/http_custom_errors')
    self.add('AUTH', 'zones', 'rulesets/phases/http_custom_errors/entrypoint')
    self.add('AUTH', 'zones', 'rulesets/phases', 'versions')
    self.add('AUTH', 'zones', 'url_normalization')

def zones_web3(self):
    """ zones web3 """

    self.add('VOID', 'zones', 'web3')
    self.add('AUTH', 'zones', 'web3/hostnames')
    self.add('VOID', 'zones', 'web3/hostnames', 'ipfs_universal_path')
    self.add('AUTH', 'zones', 'web3/hostnames', 'ipfs_universal_path/content_list')
    self.add('AUTH', 'zones', 'web3/hostnames', 'ipfs_universal_path/content_list/entries')

def accounts_email(self):
    """ accounts email """

    self.add('VOID', 'accounts', 'email')
    self.add('VOID', 'accounts', 'email/routing')
    self.add('AUTH', 'accounts', 'email/routing/addresses')

def accounts_r2(self):
    """ accounts r2 """

    self.add('VOID', 'accounts', 'r2')
    self.add('AUTH', 'accounts', 'r2/buckets')
    self.add('AUTH', 'accounts', 'r2/buckets', 'usage')
    self.add('AUTH', 'accounts', 'r2/buckets', 'objects')

def zones_email(self):
    """ zones email """

    self.add('VOID', 'zones', 'email')
    self.add('AUTH', 'zones', 'email/routing')
    self.add('AUTH', 'zones', 'email/routing/disable')
    self.add('AUTH', 'zones', 'email/routing/dns')
    self.add('AUTH', 'zones', 'email/routing/enable')
    self.add('AUTH', 'zones', 'email/routing/rules')
    self.add('AUTH', 'zones', 'email/routing/rules/catch_all')

def zones_api_gateway(self):
    """ zones api_gateway """

    self.add('VOID', 'zones', 'api_gateway')
    self.add('AUTH', 'zones', 'api_gateway/configuration')
    self.add('AUTH', 'zones', 'api_gateway/discovery')
    self.add('AUTH', 'zones', 'api_gateway/operations')
    self.add('AUTH', 'zones', 'api_gateway/schemas')

def radar(self):
    """ radar """
    self.add('VOID', 'radar')
    self.add('VOID', 'radar/annotations')
    self.add('AUTH', 'radar/annotations/outages')
    self.add('AUTH', 'radar/annotations/outages/locations')
    self.add('VOID', 'radar/attacks')
    self.add('VOID', 'radar/attacks/layer3')
    self.add('AUTH', 'radar/attacks/layer3/summary')
    self.add('AUTH', 'radar/attacks/layer3/timeseries')
    self.add('AUTH', 'radar/attacks/layer3/timeseries_groups')
    self.add('VOID', 'radar/attacks/layer7')
    self.add('AUTH', 'radar/attacks/layer7/summary')
    self.add('AUTH', 'radar/attacks/layer7/timeseries')
    self.add('AUTH', 'radar/attacks/layer7/timeseries_groups')
    self.add('VOID', 'radar/attacks/layer7/top')
    self.add('VOID', 'radar/attacks/layer7/top/ases')
    self.add('AUTH', 'radar/attacks/layer7/top/ases/origin')
    self.add('AUTH', 'radar/attacks/layer7/top/attacks')
    self.add('VOID', 'radar/attacks/layer7/top/locations')
    self.add('AUTH', 'radar/attacks/layer7/top/locations/origin')
    self.add('AUTH', 'radar/attacks/layer7/top/locations/target')
    self.add('VOID', 'radar/bgp')
    self.add('VOID', 'radar/bgp/leaks')
    self.add('AUTH', 'radar/bgp/leaks/events')
    self.add('AUTH', 'radar/bgp/timeseries')
    self.add('VOID', 'radar/bgp/top')
    self.add('AUTH', 'radar/bgp/top/ases')
    self.add('AUTH', 'radar/bgp/top/prefixes')
    self.add('AUTH', 'radar/datasets')
    self.add('AUTH', 'radar/datasets/download')
    self.add('VOID', 'radar/dns')
    self.add('VOID', 'radar/dns/top')
    self.add('AUTH', 'radar/dns/top/ases')
    self.add('AUTH', 'radar/dns/top/locations')
    self.add('VOID', 'radar/entities')
    self.add('AUTH', 'radar/entities/asns')
    self.add('AUTH', 'radar/entities/asns/ip')
    self.add('AUTH', 'radar/entities/locations')
    self.add('VOID', 'radar/http')
    self.add('VOID', 'radar/http/summary')
    self.add('AUTH', 'radar/http/summary/bot_class')
    self.add('AUTH', 'radar/http/summary/device_type')
    self.add('AUTH', 'radar/http/summary/http_protocol')
    self.add('AUTH', 'radar/http/summary/http_version')
    self.add('AUTH', 'radar/http/summary/ip_version')
    self.add('AUTH', 'radar/http/summary/tls_version')
    self.add('VOID', 'radar/http/timeseries')
    self.add('AUTH', 'radar/http/timeseries/bot_class')
    self.add('AUTH', 'radar/http/timeseries/browser')
    self.add('AUTH', 'radar/http/timeseries/browser_family')
    self.add('AUTH', 'radar/http/timeseries/device_type')
    self.add('AUTH', 'radar/http/timeseries/http_protocol')
    self.add('AUTH', 'radar/http/timeseries/http_version')
    self.add('AUTH', 'radar/http/timeseries/ip_version')
    self.add('AUTH', 'radar/http/timeseries/tls_version')
    self.add('VOID', 'radar/http/top')
    self.add('AUTH', 'radar/http/top/ases')
    self.add('AUTH', 'radar/http/top/ases/bot_class')
    self.add('AUTH', 'radar/http/top/ases/device_type')
    self.add('AUTH', 'radar/http/top/ases/http_protocol')
    self.add('AUTH', 'radar/http/top/ases/http_version')
    self.add('AUTH', 'radar/http/top/ases/ip_version')
    self.add('AUTH', 'radar/http/top/ases/tls_version')
    self.add('AUTH', 'radar/http/top/browsers')
    self.add('AUTH', 'radar/http/top/browser_families')
    self.add('AUTH', 'radar/http/top/locations')
    self.add('AUTH', 'radar/http/top/locations/bot_class')
    self.add('AUTH', 'radar/http/top/locations/device_type')
    self.add('AUTH', 'radar/http/top/locations/http_protocol')
    self.add('AUTH', 'radar/http/top/locations/http_version')
    self.add('AUTH', 'radar/http/top/locations/ip_version')
    self.add('AUTH', 'radar/http/top/locations/tls_version')
    self.add('VOID', 'radar/netflows')
    self.add('AUTH', 'radar/netflows/timeseries')
    self.add('VOID', 'radar/netflows/top')
    self.add('AUTH', 'radar/netflows/top/ases')
    self.add('AUTH', 'radar/netflows/top/locations')
    self.add('VOID', 'radar/ranking')
    self.add('AUTH', 'radar/ranking/timeseries')
    self.add('AUTH', 'radar/ranking/top')
    self.add('VOID', 'radar/search')
    self.add('AUTH', 'radar/search/global')
    self.add('AUTH', 'radar/specialevents')
    self.add('VOID', 'radar/verified_bots')
    self.add('VOID', 'radar/verified_bots/top')
    self.add('AUTH', 'radar/verified_bots/top/bots')
    self.add('AUTH', 'radar/verified_bots/top/categories')

def from_developers(self):
    """ from_developers """
    self.add('VOID', 'accounts', 'analytics_engine')
    self.add('AUTH', 'accounts', 'analytics_engine/sql')

    self.add('AUTH', 'accounts', 'images/v1/config')
#   self.add('AUTH', 'accounts', 'images/v1/direct_upload') # deprecated 2022-07-01 - expired!

    self.add('VOID', 'accounts', 'logpush')
    self.add('AUTH', 'accounts', 'logpush/jobs')

    self.add('VOID', 'accounts', 'logs')
    self.add('AUTH', 'accounts', 'logs/retrieve')

    self.add('VOID', 'accounts', 'magic/advanced_tcp_protection')
    self.add('VOID', 'accounts', 'magic/advanced_tcp_protection/configs')
    self.add('AUTH', 'accounts', 'magic/advanced_tcp_protection/configs/allowlist')
    self.add('AUTH', 'accounts', 'magic/advanced_tcp_protection/configs/prefixes')
    self.add('AUTH', 'accounts', 'magic/advanced_tcp_protection/configs/prefixes/bulk')
    self.add('VOID', 'accounts', 'magic/advanced_tcp_protection/configs/syn_protection')
    self.add('AUTH', 'accounts', 'magic/advanced_tcp_protection/configs/syn_protection/rules')
    self.add('VOID', 'accounts', 'magic/advanced_tcp_protection/configs/tcp_flow_protection')
    self.add('AUTH', 'accounts', 'magic/advanced_tcp_protection/configs/tcp_flow_protection/rules')
    self.add('AUTH', 'accounts', 'magic/advanced_tcp_protection/configs/tcp_protection_status')

    self.add('VOID', 'accounts', 'pubsub')
    self.add('AUTH', 'accounts', 'pubsub/namespaces')
    self.add('AUTH', 'accounts', 'pubsub/namespaces', 'brokers')
    self.add('AUTH', 'accounts', 'pubsub/namespaces', 'brokers', 'credentials')

    self.add('VOID', 'accounts', 'rulesets/phases/ddos_l4')
    self.add('AUTH', 'accounts', 'rulesets/phases/ddos_l4/entrypoint')
    self.add('VOID', 'accounts', 'rulesets/phases/ddos_l7')
    self.add('AUTH', 'accounts', 'rulesets/phases/ddos_l7/entrypoint')
    self.add('VOID', 'accounts', 'rulesets/phases/http_request_firewall_custom')
    self.add('AUTH', 'accounts', 'rulesets/phases/http_request_firewall_custom/entrypoint')
    self.add('VOID', 'accounts', 'rulesets/phases/http_request_firewall_managed')
    self.add('AUTH', 'accounts', 'rulesets/phases/http_request_firewall_managed/entrypoint')

    self.add('VOID', 'accounts', 'stream/analytics')
    self.add('AUTH', 'accounts', 'stream/analytics/views')
    self.add('AUTH', 'accounts', 'stream/live_inputs', 'videos')

#   self.add('AUTH', 'organizations', 'load_balancers/monitors')

    self.add('AUTH', 'users')

    self.add('VOID', 'zones', 'content-upload-scan')
    self.add('AUTH', 'zones', 'content-upload-scan/disable')
    self.add('AUTH', 'zones', 'content-upload-scan/enable')
    self.add('AUTH', 'zones', 'content-upload-scan/payloads')
    self.add('AUTH', 'zones', 'content-upload-scan/settings')

    self.add('VOID', 'zones', 'phases')
    self.add('VOID', 'zones', 'phases/http_request_firewall_managed')
    self.add('AUTH', 'zones', 'phases/http_request_firewall_managed/entrypoint')

    self.add('VOID', 'zones', 'rulesets/phases/ddos_l7')
    self.add('AUTH', 'zones', 'rulesets/phases/ddos_l7/entrypoint')
    self.add('VOID', 'zones', 'rulesets/phases/http_ratelimit')
    self.add('AUTH', 'zones', 'rulesets/phases/http_ratelimit/entrypoint')
    self.add('VOID', 'zones', 'rulesets/phases/http_request_cache_settings')
    self.add('AUTH', 'zones', 'rulesets/phases/http_request_cache_settings/entrypoint')
    self.add('VOID', 'zones', 'rulesets/phases/http_request_firewall_custom')
    self.add('AUTH', 'zones', 'rulesets/phases/http_request_firewall_custom/entrypoint')
    self.add('VOID', 'zones', 'rulesets/phases/http_request_firewall_managed')
    self.add('AUTH', 'zones', 'rulesets/phases/http_request_firewall_managed/entrypoint')
    self.add('AUTH', 'zones', 'rulesets/phases/http_request_firewall_managed/entrypoint/versions')
