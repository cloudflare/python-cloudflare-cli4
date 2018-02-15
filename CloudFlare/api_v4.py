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

    base = self._base
    setattr(self, "user",
            self._add_with_auth(base, "user"))
    branch = self.user
    setattr(branch, "billing",
            self._add_unused(base, "user/billing"))
    branch = self.user.billing
    setattr(branch, "history",
            self._add_with_auth(base, "user/billing/history"))
    setattr(branch, "profile",
            self._add_with_auth(base, "user/billing/profile"))
    setattr(branch, "subscriptions",
            self._add_unused(base, "user/billing/subscriptions"))
    branch = self.user.billing.subscriptions
    setattr(branch, "apps",
            self._add_with_auth(base, "user/billing/subscriptions/apps"))
    setattr(branch, "zones",
            self._add_with_auth(base, "user/billing/subscriptions/zones"))
    branch = self.user
    setattr(branch, "firewall",
            self._add_unused(base, "user/firewall"))
    branch = self.user.firewall
    setattr(branch, "access_rules",
            self._add_unused(base, "user/firewall/access_rules"))
    branch = self.user.firewall.access_rules
    setattr(branch, "rules",
            self._add_with_auth(base, "user/firewall/access_rules/rules"))
    branch = self.user
    setattr(branch, "organizations",
            self._add_with_auth(base, "user/organizations"))
    setattr(branch, "invites",
            self._add_with_auth(base, "user/invites"))
    setattr(branch, "subscriptions",
            self._add_with_auth(base, "user/subscriptions"))

def zones(self):
    """ API core commands for Cloudflare API"""

    base = self._base
    setattr(self, "zones",
            self._add_with_auth(base, "zones"))
    branch = self.zones
    setattr(branch, "activation_check",
            self._add_with_auth(base, "zones", "activation_check"))
    setattr(branch, "available_plans",
            self._add_with_auth(base, "zones", "available_plans"))
    setattr(branch, "available_rate_plans",
            self._add_with_auth(base, "zones", "available_rate_plans"))
    setattr(branch, "custom_certificates",
            self._add_with_auth(base, "zones", "custom_certificates"))
    branch = self.zones.custom_certificates
    setattr(branch, "prioritize",
            self._add_with_auth(base, "zones", "custom_certificates/prioritize"))
    branch = self.zones
    setattr(branch, "custom_pages",
            self._add_with_auth(base, "zones", "custom_pages"))
    setattr(branch, "dns_records",
            self._add_with_auth(base, "zones", "dns_records"))
    setattr(branch, "keyless_certificates",
            self._add_with_auth(base, "zones", "keyless_certificates"))
    setattr(branch, "pagerules",
            self._add_with_auth(base, "zones", "pagerules"))
    setattr(branch, "purge_cache",
            self._add_with_auth(base, "zones", "purge_cache"))
    setattr(branch, "railguns",
            self._add_with_auth(base, "zones", "railguns"))
    branch = self.zones.railguns
    setattr(branch, "diagnose",
            self._add_with_auth(base, "zones", "railguns", "diagnose"))
    branch = self.zones
    setattr(branch, "subscription",
            self._add_with_auth(base, "zones", "subscription"))
    setattr(branch, "subscriptions",
            self._add_with_auth(base, "zones", "subscriptions"))
    branch = self.zones.dns_records
    setattr(branch, "export",
            self._add_with_auth(base, "zones", "dns_records/export"))
    setattr(branch, "import",
            self._add_with_auth(base, "zones", "dns_records/import"))
    branch = self.zones
    setattr(branch, "custom_hostnames",
            self._add_with_auth(base, "zones", "custom_hostnames"))

def zones_settings(self):
    """ API core commands for Cloudflare API"""

    base = self._base
    branch = self.zones
    setattr(branch, "settings",
            self._add_with_auth(base, "zones", "settings"))
    branch = self.zones.settings
    setattr(branch, "advanced_ddos",
            self._add_with_auth(base, "zones", "settings/advanced_ddos"))
    setattr(branch, "always_online",
            self._add_with_auth(base, "zones", "settings/always_online"))
    setattr(branch, "always_use_https",
            self._add_with_auth(base, "zones", "settings/always_use_https"))
    setattr(branch, "browser_cache_ttl",
            self._add_with_auth(base, "zones", "settings/browser_cache_ttl"))
    setattr(branch, "browser_check",
            self._add_with_auth(base, "zones", "settings/browser_check"))
    setattr(branch, "cache_level",
            self._add_with_auth(base, "zones", "settings/cache_level"))
    setattr(branch, "challenge_ttl",
            self._add_with_auth(base, "zones", "settings/challenge_ttl"))
    setattr(branch, "development_mode",
            self._add_with_auth(base, "zones", "settings/development_mode"))
    setattr(branch, "email_obfuscation",
            self._add_with_auth(base, "zones", "settings/email_obfuscation"))
    setattr(branch, "hotlink_protection",
            self._add_with_auth(base, "zones", "settings/hotlink_protection"))
    setattr(branch, "ip_geolocation",
            self._add_with_auth(base, "zones", "settings/ip_geolocation"))
    setattr(branch, "ipv6",
            self._add_with_auth(base, "zones", "settings/ipv6"))
    setattr(branch, "minify",
            self._add_with_auth(base, "zones", "settings/minify"))
    setattr(branch, "mirage",
            self._add_with_auth(base, "zones", "settings/mirage"))
    setattr(branch, "mobile_redirect",
            self._add_with_auth(base, "zones", "settings/mobile_redirect"))
    setattr(branch, "origin_error_page_pass_thru",
            self._add_with_auth(base, "zones", "settings/origin_error_page_pass_thru"))
    setattr(branch, "polish",
            self._add_with_auth(base, "zones", "settings/polish"))
    setattr(branch, "prefetch_preload",
            self._add_with_auth(base, "zones", "settings/prefetch_preload"))
    setattr(branch, "response_buffering",
            self._add_with_auth(base, "zones", "settings/response_buffering"))
    setattr(branch, "rocket_loader",
            self._add_with_auth(base, "zones", "settings/rocket_loader"))
    setattr(branch, "security_header",
            self._add_with_auth(base, "zones", "settings/security_header"))
    setattr(branch, "security_level",
            self._add_with_auth(base, "zones", "settings/security_level"))
    setattr(branch, "server_side_exclude",
            self._add_with_auth(base, "zones", "settings/server_side_exclude"))
    setattr(branch, "sort_query_string_for_cache",
            self._add_with_auth(base, "zones", "settings/sort_query_string_for_cache"))
    setattr(branch, "ssl",
            self._add_with_auth(base, "zones", "settings/ssl"))
    setattr(branch, "tls_client_auth",
            self._add_with_auth(base, "zones", "settings/tls_client_auth"))
    setattr(branch, "true_client_ip_header",
            self._add_with_auth(base, "zones", "settings/true_client_ip_header"))
    setattr(branch, "tls_1_2_only",
            self._add_with_auth(base, "zones", "settings/tls_1_2_only"))
    setattr(branch, "tls_1_3",
            self._add_with_auth(base, "zones", "settings/tls_1_3"))
    # setattr(branch, "tlsadd_auth",
    #         self._add_with_auth(base, "zones", "settings/tlsadd_auth"))
    # setattr(branch, "trueadd_ip_header",
    #         self._add_with_auth(base, "zones", "settings/trueadd_ip_header"))
    setattr(branch, "websockets",
            self._add_with_auth(base, "zones", "settings/websockets"))
    setattr(branch, "waf",
            self._add_with_auth(base, "zones", "settings/waf"))
    setattr(branch, "webp",
            self._add_with_auth(base, "zones", "settings/webp"))
    setattr(branch, "http2",
            self._add_with_auth(base, "zones", "settings/http2"))
    setattr(branch, "pseudo_ipv4",
            self._add_with_auth(base, "zones", "settings/pseudo_ipv4"))
    setattr(branch, "opportunistic_encryption",
            self._add_with_auth(base, "zones", "settings/opportunistic_encryption"))
    setattr(branch, "automatic_https_rewrites",
            self._add_with_auth(base, "zones", "settings/automatic_https_rewrites"))
    setattr(branch, "brotli",
            self._add_with_auth(base, "zones", "settings/brotli"))
    setattr(branch, "privacy_pass",
            self._add_with_auth(base, "zones", "settings/privacy_pass"))

def zones_analytics(self):
    """ API core commands for Cloudflare API"""

    base = self._base
    branch = self.zones
    setattr(branch, "analytics",
            self._add_unused(base, "zones", "analytics"))
    branch = self.zones.analytics
    setattr(branch, "colos",
            self._add_with_auth(base, "zones", "analytics/colos"))
    setattr(branch, "dashboard",
            self._add_with_auth(base, "zones", "analytics/dashboard"))

def zones_firewall(self):
    """ API core commands for Cloudflare API"""

    base = self._base
    branch = self.zones
    setattr(branch, "firewall",
            self._add_unused(branch, "zones", "firewall"))
    branch = self.zones.firewall
    setattr(branch, "access_rules",
            self._add_unused(base, "zones", "firewall/access_rules"))
    setattr(branch, "waf",
            self._add_unused(base, "zones", "firewall/waf"))
    branch = self.zones.firewall.waf
    setattr(branch, "packages",
            self._add_with_auth(base, "zones", "firewall/waf/packages"))
    branch = self.zones.firewall.waf.packages
    setattr(branch, "groups",
            self._add_with_auth(base, "zones", "firewall/waf/packages", "groups"))
    setattr(branch, "rules",
            self._add_with_auth(base, "zones", "firewall/waf/packages", "rules"))
    branch = self.zones.firewall.access_rules
    setattr(branch, "rules",
            self._add_with_auth(base, "zones", "firewall/access_rules/rules"))
    branch = self.zones.firewall
    setattr(branch, "lockdowns",
            self._add_with_auth(base, "zones", "firewall/lockdowns"))
    setattr(branch, "ua_rules",
            self._add_with_auth(base, "zones", "firewall/ua_rules"))

def zones_rate_limits(self):
    """ API core commands for Cloudflare API"""

    base = self._base
    branch = self.zones
    setattr(branch, "rate_limits",
            self._add_with_auth(base, "zones", "rate_limits"))

def zones_dns_analytics(self):
    """ API core commands for Cloudflare API"""

    base = self._base
    branch = self.zones
    setattr(branch, "dns_analytics",
            self._add_unused(base, "zones", "dns_analytics"))
    branch = self.zones.dns_analytics
    setattr(branch, "report",
            self._add_with_auth(base, "zones", "dns_analytics/report"))
    branch = self.zones.dns_analytics.report
    setattr(branch, "bytime",
            self._add_with_auth(base, "zones", "dns_analytics/report/bytime"))

def zones_amp(self):
    """ API core commands for Cloudflare API"""

    base = self._base
    branch = self.zones
    setattr(branch, "amp",
            self._add_unused(base, "zones", "amp"))
    branch = self.zones.amp
    setattr(branch, "viewer",
            self._add_with_auth(base, "zones", "amp/viewer"))

def zones_logs(self):
    """ API core commands for Cloudflare API"""

    base = self._base
    branch = self.zones
    setattr(branch, "logs",
            self._add_unused(base, "zones", "logs"))
    branch = self.zones.logs
    setattr(branch, "received",
            self._add_with_auth_unwrapped(base, "zones", "logs/received"))
    branch = self.zones.logs.received
    setattr(branch, "fields",
            self._add_with_auth_unwrapped(base, "zones", "logs/received/fields"))

def railguns(self):
    """ API core commands for Cloudflare API"""

    base = self._base
    setattr(self, "railguns",
            self._add_with_auth(base, "railguns"))
    branch = self.railguns
    setattr(branch, "zones",
            self._add_with_auth(base, "railguns", "zones"))

def organizations(self):
    """ API core commands for Cloudflare API"""

    base = self._base
    setattr(self, "organizations",
            self._add_with_auth(base, "organizations"))
    branch = self.organizations
    setattr(branch, "members",
            self._add_with_auth(base, "organizations", "members"))
    setattr(branch, "invite",
            self._add_with_auth(base, "organizations", "invite"))
    setattr(branch, "invites",
            self._add_with_auth(base, "organizations", "invites"))
    setattr(branch, "railguns",
            self._add_with_auth(base, "organizations", "railguns"))
    branch = self.organizations.railguns
    setattr(branch, "zones",
            self._add_with_auth(base, "organizations", "railguns", "zones"))
    branch = self.organizations
    setattr(branch, "roles",
            self._add_with_auth(base, "organizations", "roles"))
    setattr(branch, "firewall",
            self._add_unused(base, "organizations", "firewall"))
    branch = self.organizations.firewall
    setattr(branch, "access_rules",
            self._add_unused(base, "organizations", "firewall/access_rules"))
    branch = self.organizations.firewall.access_rules
    setattr(branch, "rules",
            self._add_with_auth(base, "organizations", "firewall/access_rules/rules"))
    branch = self.organizations
    setattr(branch, "load_balancers",
            self._add_unused(base, "organizations", "load_balancers"))
    branch = self.organizations.load_balancers
    setattr(branch, "monitors",
            self._add_with_auth(base, "organizations", "load_balancers/monitors"))
    setattr(branch, "pools",
            self._add_with_auth(base, "organizations", "load_balancers/pools"))

def certificates(self):
    """ API core commands for Cloudflare API"""

    base = self._base
    setattr(self, "certificates",
            self._add_with_cert_auth(base, "certificates"))

def ips(self):
    """ API core commands for Cloudflare API"""

    base = self._base
    setattr(self, "ips",
            self._add_noauth(base, "ips"))

def zones_argo(self):
    """ API core commands for Cloudflare API"""

    base = self._base
    branch = self.zones
    setattr(branch, "argo",
            self._add_unused(base, "zones", "argo"))
    branch = self.zones.argo
    setattr(branch, "tiered_caching",
            self._add_with_auth(base, "zones", "argo/tiered_caching"))
    setattr(branch, "smart_routing",
            self._add_with_auth(base, "zones", "argo/smart_routing"))

def zones_dnssec(self):
    """ API core commands for Cloudflare API"""

    base = self._base
    branch = self.zones
    setattr(branch, "dnssec",
            self._add_with_auth(base, "zones", "dnssec"))

def zones_ssl(self):
    """ API core commands for Cloudflare API"""

    base = self._base
    branch = self.zones
    setattr(branch, "ssl",
            self._add_unused(base, "zones", "ssl"))
    branch = self.zones.ssl
    setattr(branch, "analyze",
            self._add_with_auth(base, "zones", "ssl/analyze"))
    setattr(branch, "certificate_packs",
            self._add_with_auth(base, "zones", "ssl/certificate_packs"))
    setattr(branch, "verification",
            self._add_with_auth(base, "zones", "ssl/verification"))
    setattr(branch, "universal",
            self._add_unused(base, "zones", "ssl/universal"))
    branch = self.zones.ssl.universal
    setattr(branch, "settings",
            self._add_with_auth(base, "zones", "ssl/universal/settings"))

def zones_workers(self):
    """ API core commands for Cloudflare API"""

    base = self._base
    branch = self.zones
    setattr(branch, "workers",
            self._add_unused(base, "zones", "workers"))
    branch = self.zones.workers
    setattr(branch, "filters",
            self._add_with_auth(base, "zones", "workers/filters"))
    setattr(branch, "routes",
            self._add_with_auth(base, "zones", "workers/routes"))
    setattr(branch, "script",
            self._add_with_auth(base, "zones", "workers/script"))

def zones_load_balancers(self):
    """ API core commands for Cloudflare API"""

    base = self._base
    branch = self.zones
    setattr(branch, "load_balancers",
            self._add_with_auth(base, "zones", "load_balancers"))

def user_load_balancers(self):
    """ API core commands for Cloudflare API"""

    base = self._base
    branch = self.user
    setattr(branch, "load_balancers",
            self._add_unused(base, "user/load_balancers"))
    branch = self.user.load_balancers
    setattr(branch, "monitors",
            self._add_with_auth(base, "user/load_balancers/monitors"))
    setattr(branch, "pools",
            self._add_with_auth(base, "user/load_balancers/pools"))

def user_virtual_dns(self):
    """ API core commands for Cloudflare API"""

    base = self._base
    branch = self.user
    setattr(branch, "virtual_dns",
            self._add_with_auth(base, "user/virtual_dns"))
    branch = self.user.virtual_dns
    setattr(branch, "dns_analytics",
            self._add_unused(base, "user/virtual_dns", "dns_analytics"))
    branch = self.user.virtual_dns.dns_analytics
    setattr(branch, "report",
            self._add_with_auth(base, "user/virtual_dns", "dns_analytics/report"))
    branch = self.user.virtual_dns.dns_analytics.report
    setattr(branch, "bytime",
            self._add_with_auth(base, "user/virtual_dns", "dns_analytics/report/bytime"))

def user_workers(self):
    """ API core commands for Cloudflare API"""

    base = self._base
    branch = self.user
    setattr(branch, "workers",
            self._add_unused(base, "user/workers"))
    branch = self.user.workers
    setattr(branch, "scripts",
            self._add_with_auth(base, "user/workers/scripts"))

def organizations_virtual_dns(self):
    """ API core commands for Cloudflare API"""

    base = self._base
    branch = self.organizations
    setattr(branch, "virtual_dns",
            self._add_with_auth(base, "organizations", "virtual_dns"))
    branch = self.organizations.virtual_dns
    setattr(branch, "dns_analytics",
            self._add_unused(base, "organizations", "virtual_dns", "dns_analytics"))
    branch = self.organizations.virtual_dns.dns_analytics
    setattr(branch, "report",
            self._add_with_auth(base, "organizations", "virtual_dns", "dns_analytics/report"))
    branch = self.organizations.virtual_dns.dns_analytics.report
    setattr(branch, "bytime",
            self._add_with_auth(base, "organizations", "virtual_dns", "dns_analytics/report/bytime"))

def user_audit_logs(self):
    """ API core commands for Cloudflare API"""

    base = self._base
    branch = self.user
    setattr(branch, "audit_logs",
            self._add_with_auth(base, "user/audit_logs"))

def user_load_balancing_analytics(self):
    """ API core commands for Cloudflare API"""

    base = self._base
    branch = self.user
    setattr(branch, "load_balancing_analytics",
            self._add_unused(base, "user/load_balancing_analytics"))
    branch = self.user.load_balancing_analytics
    setattr(branch, "events",
            self._add_with_auth(base, "user/load_balancing_analytics/events"))
    setattr(branch, "entities",
            self._add_with_auth(base, "user/load_balancing_analytics/entities"))

def organizations_audit_logs(self):
    """ API core commands for Cloudflare API"""

    base = self._base
    branch = self.organizations
    setattr(branch, "audit_logs",
            self._add_with_auth(base, "organizations", "audit_logs"))

def organizations_workers(self):
    """ API core commands for Cloudflare API"""

    base = self._base
    branch = self.organizations
    setattr(branch, "workers",
            self._add_unused(base, "organizations", "workers"))
    branch = self.organizations.workers
    setattr(branch, "scripts",
            self._add_with_auth(base, "organizations", "workers/scripts"))

def account(self):
    """ API core commands for Cloudflare API"""

    base = self._base
    setattr(self, "account",
            self._add_unused(base, "account"))

def account_load_balancing_analytics(self):
    """ API core commands for Cloudflare API"""

    base = self._base
    branch = self.account
    setattr(branch, "load_balancing_analytics",
            self._add_unused(base, "account", "load_balancing_analytics"))
    branch = self.account.load_balancing_analytics
    setattr(branch, "events",
            self._add_with_auth(base, "account", "load_balancing_analytics/events"))
    setattr(branch, "entities",
            self._add_with_auth(base, "account", "load_balancing_analytics/entities"))

