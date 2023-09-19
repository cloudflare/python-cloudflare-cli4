import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import CloudFlare

class TestCloudflare:
    def test_creating_default_client(self):
        cf = CloudFlare.CloudFlare()
        assert isinstance(cf, CloudFlare.CloudFlare)


    def test_with_global_request_timeout(self):
        cf = CloudFlare.CloudFlare({'global_request_timeout': 10})
        assert isinstance(cf, CloudFlare.CloudFlare)

    def test_with_max_request_retries(self):
        cf = CloudFlare.CloudFlare({'max_request_retries': 2})
        assert isinstance(cf, CloudFlare.CloudFlare)
