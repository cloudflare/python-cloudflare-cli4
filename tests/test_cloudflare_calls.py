""" class calling tests """

import os
import sys

sys.path.insert(0, os.path.abspath('..'))
import CloudFlare

# test Cloudflare init param (ie. debug, raw, etc)
#
# cf = CloudFlare.CloudFlare(
#          email=None, key=None, token=None, certtoken=None,
#          debug=False, raw=False, use_sessions=True,
#          profile=None,
#          base_url=None,
#          global_request_timeout=None, max_request_retries=None
#      )

cf = None

def test_cloudflare():
    global cf
    cf = CloudFlare.CloudFlare()
    assert isinstance(cf, CloudFlare.CloudFlare)

def test_ips():
    ips = cf.ips()
    assert isinstance(ips, dict)
    assert len(ips) > 0

def test_cloudflare_debug():
    global cf
    cf = CloudFlare.CloudFlare(debug=True)
    assert isinstance(cf, CloudFlare.CloudFlare)

def test_ips():
    ips = cf.ips()
    assert isinstance(ips, dict)
    assert len(ips) > 0

def test_cloudflare_raw():
    global cf
    cf = CloudFlare.CloudFlare(raw=False)
    assert isinstance(cf, CloudFlare.CloudFlare)

def test_ips():
    ips = cf.ips()
    assert isinstance(ips, dict)
    assert len(ips) > 0

def test_cloudflare_no_sessions():
    global cf
    cf = CloudFlare.CloudFlare(use_sessions=False)
    assert isinstance(cf, CloudFlare.CloudFlare)

def test_ips():
    ips = cf.ips()
    assert isinstance(ips, dict)
    assert len(ips) > 0

def test_ips():
    ips = cf.ips()
    assert isinstance(ips, dict)
    assert len(ips) > 0
