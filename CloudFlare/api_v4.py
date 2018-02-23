""" API core commands for Cloudflare API"""

def api_v4(self):
    """ API core commands for Cloudflare API"""

    # The API commands for /user/
    user(self)
    user_audit_logs(self)
    user_load_balancers(self)
    user_load_balancing_analytics(self)
    user_virtual_dns(self)
    user_workers(self)

    # The API commands for /zones/
    zones(self)
    zones_amp(self)
    zones_analytics(self)
    zones_argo(self)
    zones_dns_analytics(self)
    zones_dnssec(self)
    zones_firewall(self)
    zones_load_balancers(self)
    zones_logs(self)
    zones_media(self)
    zones_rate_limits(self)
    zones_settings(self)
    zones_ssl(self)
    zones_workers(self)

    # The API commands for /railguns/
    railguns(self)

    # The API commands for /organizations/
    organizations(self)
    organizations_audit_logs(self)
    organizations_virtual_dns(self)
    organizations_workers(self)

    # The API commands for /certificates/
    certificates(self)

    # The API commands for /ips/
    ips(self)

    # The API commands for /account/
    account(self)
    account_load_balancing_analytics(self)

def user(self):
    """ API core commands for Cloudflare API"""

    self.add('AUTH', self, "user")
    self.add('VOID', self.user, "user/billing")
    self.add('AUTH', self.user.billing, "user/billing/history")
    self.add('AUTH', self.user.billing, "user/billing/profile")
    self.add('VOID', self.user.billing, "user/billing/subscriptions")
    self.add('AUTH', self.user.billing.subscriptions, "user/billing/subscriptions/apps")
    self.add('AUTH', self.user.billing.subscriptions, "user/billing/subscriptions/zones")
    self.add('VOID', self.user, "user/firewall")
    self.add('VOID', self.user.firewall, "user/firewall/access_rules")
    self.add('AUTH', self.user.firewall.access_rules, "user/firewall/access_rules/rules")
    self.add('AUTH', self.user, "user/invites")
    self.add('AUTH', self.user, "user/organizations")
    self.add('AUTH', self.user, "user/subscriptions")

def zones(self):
    """ API core commands for Cloudflare API"""

    self.add('AUTH', self, "zones")
    self.add('AUTH', self.zones, "zones", "activation_check")
    self.add('AUTH', self.zones, "zones", "available_plans")
    self.add('AUTH', self.zones, "zones", "available_rate_plans")
    self.add('AUTH', self.zones, "zones", "custom_certificates")
    self.add('AUTH', self.zones.custom_certificates, "zones", "custom_certificates/prioritize")
    self.add('AUTH', self.zones, "zones", "custom_hostnames")
    self.add('AUTH', self.zones, "zones", "custom_pages")
    self.add('AUTH', self.zones, "zones", "dns_records")
    self.add('AUTH', self.zones.dns_records, "zones", "dns_records/export")
    self.add('AUTH', self.zones.dns_records, "zones", "dns_records/import")
    self.add('AUTH', self.zones, "zones", "keyless_certificates")
    self.add('AUTH', self.zones, "zones", "pagerules")
    self.add('AUTH', self.zones, "zones", "purge_cache")
    self.add('AUTH', self.zones, "zones", "railguns")
    self.add('AUTH', self.zones.railguns, "zones", "railguns", "diagnose")
    self.add('AUTH', self.zones, "zones", "subscription")
    self.add('AUTH', self.zones, "zones", "subscriptions")

def zones_settings(self):
    """ API core commands for Cloudflare API"""

    self.add('AUTH', self.zones, "zones", "settings")
    self.add('AUTH', self.zones.settings, "zones", "settings/advanced_ddos")
    self.add('AUTH', self.zones.settings, "zones", "settings/always_online")
    self.add('AUTH', self.zones.settings, "zones", "settings/always_use_https")
    self.add('AUTH', self.zones.settings, "zones", "settings/browser_cache_ttl")
    self.add('AUTH', self.zones.settings, "zones", "settings/browser_check")
    self.add('AUTH', self.zones.settings, "zones", "settings/cache_level")
    self.add('AUTH', self.zones.settings, "zones", "settings/challenge_ttl")
    self.add('AUTH', self.zones.settings, "zones", "settings/development_mode")
    self.add('AUTH', self.zones.settings, "zones", "settings/email_obfuscation")
    self.add('AUTH', self.zones.settings, "zones", "settings/hotlink_protection")
    self.add('AUTH', self.zones.settings, "zones", "settings/ip_geolocation")
    self.add('AUTH', self.zones.settings, "zones", "settings/ipv6")
    self.add('AUTH', self.zones.settings, "zones", "settings/minify")
    self.add('AUTH', self.zones.settings, "zones", "settings/mirage")
    self.add('AUTH', self.zones.settings, "zones", "settings/mobile_redirect")
    self.add('AUTH', self.zones.settings, "zones", "settings/origin_error_page_pass_thru")
    self.add('AUTH', self.zones.settings, "zones", "settings/polish")
    self.add('AUTH', self.zones.settings, "zones", "settings/prefetch_preload")
    self.add('AUTH', self.zones.settings, "zones", "settings/response_buffering")
    self.add('AUTH', self.zones.settings, "zones", "settings/rocket_loader")
    self.add('AUTH', self.zones.settings, "zones", "settings/security_header")
    self.add('AUTH', self.zones.settings, "zones", "settings/security_level")
    self.add('AUTH', self.zones.settings, "zones", "settings/server_side_exclude")
    self.add('AUTH', self.zones.settings, "zones", "settings/sort_query_string_for_cache")
    self.add('AUTH', self.zones.settings, "zones", "settings/ssl")
    self.add('AUTH', self.zones.settings, "zones", "settings/tls_client_auth")
    self.add('AUTH', self.zones.settings, "zones", "settings/true_client_ip_header")
    self.add('AUTH', self.zones.settings, "zones", "settings/tls_1_2_only")
    self.add('AUTH', self.zones.settings, "zones", "settings/tls_1_3")
    self.add('AUTH', self.zones.settings, "zones", "settings/websockets")
    self.add('AUTH', self.zones.settings, "zones", "settings/waf")
    self.add('AUTH', self.zones.settings, "zones", "settings/webp")
    self.add('AUTH', self.zones.settings, "zones", "settings/http2")
    self.add('AUTH', self.zones.settings, "zones", "settings/pseudo_ipv4")
    self.add('AUTH', self.zones.settings, "zones", "settings/opportunistic_encryption")
    self.add('AUTH', self.zones.settings, "zones", "settings/automatic_https_rewrites")
    self.add('AUTH', self.zones.settings, "zones", "settings/brotli")
    self.add('AUTH', self.zones.settings, "zones", "settings/privacy_pass")

def zones_analytics(self):
    """ API core commands for Cloudflare API"""

    self.add('VOID', self.zones, "zones", "analytics")
    self.add('AUTH', self.zones.analytics, "zones", "analytics/colos")
    self.add('AUTH', self.zones.analytics, "zones", "analytics/dashboard")

def zones_firewall(self):
    """ API core commands for Cloudflare API"""

    self.add('VOID', self.zones, "zones", "firewall")
    self.add('VOID', self.zones.firewall, "zones", "firewall/access_rules")
    self.add('AUTH', self.zones.firewall.access_rules, "zones", "firewall/access_rules/rules")
    self.add('AUTH', self.zones.firewall, "zones", "firewall/lockdowns")
    self.add('AUTH', self.zones.firewall, "zones", "firewall/ua_rules")
    self.add('VOID', self.zones.firewall, "zones", "firewall/waf")
    self.add('AUTH', self.zones.firewall.waf, "zones", "firewall/waf/packages")
    self.add('AUTH', self.zones.firewall.waf.packages, "zones", "firewall/waf/packages", "groups")
    self.add('AUTH', self.zones.firewall.waf.packages, "zones", "firewall/waf/packages", "rules")

def zones_rate_limits(self):
    """ API core commands for Cloudflare API"""

    self.add('AUTH', self.zones, "zones", "rate_limits")

def zones_dns_analytics(self):
    """ API core commands for Cloudflare API"""

    self.add('VOID', self.zones, "zones", "dns_analytics")
    self.add('AUTH', self.zones.dns_analytics, "zones", "dns_analytics/report")
    self.add('AUTH', self.zones.dns_analytics.report, "zones", "dns_analytics/report/bytime")

def zones_amp(self):
    """ API core commands for Cloudflare API"""

    self.add('VOID', self.zones, "zones", "amp")
    self.add('AUTH', self.zones.amp, "zones", "amp/viewer")

def zones_logs(self):
    """ API core commands for Cloudflare API"""

    self.add('VOID', self.zones, "zones", "logs")
    self.add('AUTH_UNWRAPPED', self.zones.logs, "zones", "logs/received")
    self.add('AUTH_UNWRAPPED', self.zones.logs.received, "zones", "logs/received/fields")

def railguns(self):
    """ API core commands for Cloudflare API"""

    self.add('AUTH', self, "railguns")
    self.add('AUTH', self.railguns, "railguns", "zones")

def organizations(self):
    """ API core commands for Cloudflare API"""

    self.add('AUTH', self, "organizations")
    self.add('AUTH', self.organizations, "organizations", "members")
    self.add('AUTH', self.organizations, "organizations", "invite")
    self.add('AUTH', self.organizations, "organizations", "invites")
    self.add('AUTH', self.organizations, "organizations", "railguns")
    self.add('AUTH', self.organizations.railguns, "organizations", "railguns", "zones")
    self.add('AUTH', self.organizations, "organizations", "roles")
    self.add('VOID', self.organizations, "organizations", "firewall")
    self.add('VOID', self.organizations.firewall, "organizations", "firewall/access_rules")
    self.add('AUTH', self.organizations.firewall.access_rules, "organizations", "firewall/access_rules/rules")
    self.add('VOID', self.organizations, "organizations", "load_balancers")
    self.add('AUTH', self.organizations.load_balancers, "organizations", "load_balancers/monitors")
    self.add('AUTH', self.organizations.load_balancers, "organizations", "load_balancers/pools")

def certificates(self):
    """ API core commands for Cloudflare API"""

    self.add('CERT', self, "certificates")

def ips(self):
    """ API core commands for Cloudflare API"""

    self.add('OPEN', self, "ips")

def zones_argo(self):
    """ API core commands for Cloudflare API"""

    self.add('VOID', self.zones, "zones", "argo")
    self.add('AUTH', self.zones.argo, "zones", "argo/tiered_caching")
    self.add('AUTH', self.zones.argo, "zones", "argo/smart_routing")

def zones_dnssec(self):
    """ API core commands for Cloudflare API"""

    self.add('AUTH', self.zones, "zones", "dnssec")

def zones_ssl(self):
    """ API core commands for Cloudflare API"""

    self.add('VOID', self.zones, "zones", "ssl")
    self.add('AUTH', self.zones.ssl, "zones", "ssl/analyze")
    self.add('AUTH', self.zones.ssl, "zones", "ssl/certificate_packs")
    self.add('AUTH', self.zones.ssl, "zones", "ssl/verification")
    self.add('VOID', self.zones.ssl, "zones", "ssl/universal")
    self.add('AUTH', self.zones.ssl.universal, "zones", "ssl/universal/settings")

def zones_workers(self):
    """ API core commands for Cloudflare API"""

    self.add('VOID', self.zones, "zones", "workers")
    self.add('AUTH', self.zones.workers, "zones", "workers/filters")
    self.add('AUTH', self.zones.workers, "zones", "workers/routes")
    self.add('AUTH', self.zones.workers, "zones", "workers/script")

def zones_load_balancers(self):
    """ API core commands for Cloudflare API"""

    self.add('AUTH', self.zones, "zones", "load_balancers")

def user_load_balancers(self):
    """ API core commands for Cloudflare API"""

    self.add('VOID', self.user, "user/load_balancers")
    self.add('AUTH', self.user.load_balancers, "user/load_balancers/monitors")
    self.add('AUTH', self.user.load_balancers, "user/load_balancers/pools")

def user_virtual_dns(self):
    """ API core commands for Cloudflare API"""

    self.add('AUTH', self.user, "user/virtual_dns")
    self.add('VOID', self.user.virtual_dns, "user/virtual_dns", "dns_analytics")
    self.add('AUTH', self.user.virtual_dns.dns_analytics, "user/virtual_dns", "dns_analytics/report")
    self.add('AUTH', self.user.virtual_dns.dns_analytics.report, "user/virtual_dns", "dns_analytics/report/bytime")
    return

def user_workers(self):
    """ API core commands for Cloudflare API"""

    self.add('VOID', self.user, "user/workers")
    self.add('AUTH', self.user.workers, "user/workers/scripts")

def organizations_virtual_dns(self):
    """ API core commands for Cloudflare API"""

    self.add('AUTH', self.organizations, "organizations", "virtual_dns")
    self.add('VOID', self.organizations.virtual_dns, "organizations", "virtual_dns", "dns_analytics")
    self.add('AUTH', self.organizations.virtual_dns.dns_analytics, "organizations", "virtual_dns", "dns_analytics/report")
    self.add('AUTH', self.organizations.virtual_dns.dns_analytics.report, "organizations", "virtual_dns", "dns_analytics/report/bytime")
    return

def user_audit_logs(self):
    """ API core commands for Cloudflare API"""

    self.add('AUTH', self.user, "user/audit_logs")

def user_load_balancing_analytics(self):
    """ API core commands for Cloudflare API"""

    self.add('VOID', self.user, "user", "load_balancing_analytics")
    self.add('AUTH', self.user.load_balancing_analytics, "user", "load_balancing_analytics/events")
    self.add('AUTH', self.user.load_balancing_analytics, "user", "load_balancing_analytics/entities")

def organizations_audit_logs(self):
    """ API core commands for Cloudflare API"""

    self.add('AUTH', self.organizations, "organizations", "audit_logs")

def organizations_workers(self):
    """ API core commands for Cloudflare API"""

    self.add('VOID', self.organizations, "organizations", "workers")
    self.add('AUTH', self.organizations.workers, "organizations", "workers/scripts")

def account(self):
    """ API core commands for Cloudflare API"""

    self.add('VOID', self, "account")

def account_load_balancing_analytics(self):
    """ API core commands for Cloudflare API"""

    self.add('VOID', self.account, "account", "load_balancing_analytics")
    self.add('AUTH', self.account.load_balancing_analytics, "account", "load_balancing_analytics/events")
    self.add('AUTH', self.account.load_balancing_analytics, "account", "load_balancing_analytics/entities")

def zones_media(self):
    """ API core commands for Cloudflare API"""

    self.add('AUTH', self.zones, "zones", "media")
    self.add('AUTH', self.zones.media, "zones", "media", "embed")
    self.add('AUTH', self.zones.media, "zones", "media", "preview")

