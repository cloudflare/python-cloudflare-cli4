""" issue-114 tests """

import os
import sys

sys.path.insert(0, os.path.abspath('..'))
import CloudFlare

# CloudFlare(email=None, key=None, token=None, certtoken=None, debug=False, raw=False, use_sessions=True, profile=None, base_url=None, global_request_timeout=5, max_request_retries=5)

class TestCloudflare:
    """ TestCloudflare """

    def test_email_key_token000(self):
        self._run(0, 0, 0)
    def test_email_key_token001(self):
        self._run(0, 0, 1)
    def test_email_key_token002(self):
        self._run(0, 0, 2)
    def test_email_key_token010(self):
        self._run(0, 1, 0)
    def test_email_key_token011(self):
        self._run(0, 1, 1)
    def test_email_key_token012(self):
        self._run(0, 1, 2)
    def test_email_key_token020(self):
        self._run(0, 2, 0)
    def test_email_key_token021(self):
        self._run(0, 2, 1)
    def test_email_key_token022(self):
        self._run(0, 2, 2)

    def test_email_key_token100(self):
        self._run(1, 1, 0)
    def test_email_key_token101(self):
        self._run(1, 1, 1)
    def test_email_key_token102(self):
        self._run(1, 1, 2)
    def test_email_key_token110(self):
        self._run(1, 1, 1)
    def test_email_key_token111(self):
        self._run(1, 1, 1)
    def test_email_key_token112(self):
        self._run(1, 1, 2)
    def test_email_key_token120(self):
        self._run(1, 2, 1)
    def test_email_key_token121(self):
        self._run(1, 2, 1)
    def test_email_key_token122(self):
        self._run(1, 2, 2)

    def test_email_key_token200(self):
        self._run(2, 0, 0)
    def test_email_key_token201(self):
        self._run(2, 0, 1)
    def test_email_key_token202(self):
        self._run(2, 0, 2)
    def test_email_key_token210(self):
        self._run(2, 1, 2)
    def test_email_key_token211(self):
        self._run(2, 1, 1)
    def test_email_key_token212(self):
        self._run(2, 1, 2)
    def test_email_key_token220(self):
        self._run(2, 2, 2)
    def test_email_key_token221(self):
        self._run(2, 2, 1)
    def test_email_key_token222(self):
        self._run(2, 2, 2)

    def _run(self, token_index, key_index, email_index):

        try:
            profile = self._profile
        except AttributeError:
            # Always clear environment
            self._setup()
            assert self._email or self._key or self._token
            # if not self._email and not self._key and not self._token:
            #     assert 'EMAIL/KEY/TOKEN all needed in order to run this test' == ''
            profile = self._profile

        # select combination
        email = [None, self._email, 'example@example.com'][email_index]
        key = [None, self._key, self._token][key_index]
        token = [None, self._token, self._key][token_index]

        print('email = ', self._obfuscate(email), 'key = ', self._obfuscate(key), 'token = ', self._obfuscate(token))

        cf = CloudFlare.CloudFlare(email=email, key=key, token=token, profile=profile)
        assert isinstance(cf, CloudFlare.CloudFlare)

        try:
            r = cf.zones(params={'per_page':1})
        except:
            r = None

        if email is None and key is None and token == self._token:
            assert isinstance(r, list)
            assert len(r) == 1
            assert isinstance(r[0], dict)
            return

        if email is None and key == self._token and token is None:
            assert isinstance(r, list)
            assert len(r) == 1
            assert isinstance(r[0], dict)
            return

        if email == self._email and key == self._key and token is None:
            assert isinstance(r, list)
            assert len(r) == 1
            assert isinstance(r[0], dict)
            return

        if email == self._email and key is None and token == self._key:
            assert isinstance(r, list)
            assert len(r) == 1
            assert isinstance(r[0], dict)
            return

        # Nothing else should work!
        assert r is None

    def _setup(self):
        """ setup """
        # Force no profile to be picked
        self._profile=''
        # read in email/key/token from config file(s)
        _config_files = [
            '.cloudflare.cfg',
            os.path.expanduser('~/.cloudflare.cfg'),
            os.path.expanduser('~/.cloudflare/cloudflare.cfg')
        ]
        email = None
        key = None
        token = None
        for filename in _config_files:
            try:
                with open(filename, 'r') as fd:
                    for l in fd:
                        if email and key and token:
                            break
                        if l[0] == '#':
                            continue
                        a = l.split()
                        if len(a) < 3:
                            continue
                        if a[1] != '=':
                            continue
                        if not email and a[0] == 'email':
                            email = a[2]
                            continue
                        if not key and a[0] == 'key':
                            key = a[2]
                            continue
                        if not token and a[0] == 'token':
                            token = a[2]
                            continue
                break
            except FileNotFoundError:
                pass
        self._email = email
        self._key = key
        self._token = token

        # now remove all env variables!
        for env in ['CLOUDFLARE_EMAIL', 'CLOUDFLARE_API_KEY', 'CLOUDFLARE_API_TOKEN']:
            try:
                del os.environ[env]
            except KeyError:
                pass
        for env in ['CF_API_EMAIL', 'CF_API_KEY', 'CF_API_TOKEN']:
            try:
                del os.environ[env]
            except KeyError:
                pass

    def _obfuscate(self, s):
        """ _obfuscate """

        if s is None:
            return ''
        return '█' * len(s)
