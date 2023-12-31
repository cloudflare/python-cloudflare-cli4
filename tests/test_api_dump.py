""" test dump calls """

import os
import sys

sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('..'))
import CloudFlare

# test API list fetches from Cloudflare website

cf = None

OPENAPI_URL = "https://github.com/cloudflare/api-schemas/raw/main/openapi.json"

def test_cloudflare(debug=False):
    global cf
    cf = CloudFlare.CloudFlare(debug=debug)
    assert isinstance(cf, CloudFlare.CloudFlare)

def test_dump_commands():
    """dump a tree of all the known API commands"""
    w = cf.api_list()
    assert len(w) > 0

def test_dump_commands_from_web():
    """dump a tree of all the known API commands - from web"""
    w = cf.api_from_openapi(OPENAPI_URL)
    assert len(w) > 0

if __name__ == '__main__':
    test_cloudflare(debug=True)
    test_dump_commands()
    test_dump_commands_from_web()