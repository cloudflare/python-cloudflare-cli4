""" ips tests """

import os
import sys

sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('..'))
import CloudFlare

cf = None

def test_cloudflare(debug=False):
    global cf
    cf = CloudFlare.CloudFlare(debug=debug)
    assert isinstance(cf, CloudFlare.CloudFlare)

def test_ips():
    # no auth required
    ips = cf.ips()
    assert isinstance(ips, dict)
    assert isinstance(ips['ipv4_cidrs'], list)
    assert isinstance(ips['ipv6_cidrs'], list)
    assert len(ips['ipv4_cidrs']) > 0
    assert len(ips['ipv6_cidrs']) > 0

def test_ips_plus_jdcloud():
    # no auth required
    params = {'networks':'jdcloud'}
    ips = cf.ips(params=params)
    assert isinstance(ips, dict)
    assert isinstance(ips['ipv4_cidrs'], list)
    assert isinstance(ips['ipv6_cidrs'], list)
    assert isinstance(ips['jdcloud_cidrs'], list)
    assert len(ips['ipv4_cidrs']) > 0
    assert len(ips['ipv6_cidrs']) > 0
    assert len(ips['jdcloud_cidrs']) > 0

if __name__ == '__main__':
    test_cloudflare(debug=True)
    test_ips()
    test_ips_plus_jdcloud()
