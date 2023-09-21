""" ips tests """

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import CloudFlare

class TestCloudflare:
    def test_ips(self):
        # no auth required
        cf = CloudFlare.CloudFlare()
        assert isinstance(cf, CloudFlare.CloudFlare)
        ips = cf.ips()
        assert isinstance(ips, dict)
        assert isinstance(ips['ipv4_cidrs'], list)
        assert isinstance(ips['ipv6_cidrs'], list)
        assert len(ips['ipv4_cidrs']) > 0
        assert len(ips['ipv6_cidrs']) > 0

