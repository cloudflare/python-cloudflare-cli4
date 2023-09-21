""" issue-114 tests """

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import CloudFlare

# CloudFlare(email=None, key=None, token=None, certtoken=None, debug=False, raw=False, use_sessions=True, profile=None, base_url=None, global_request_timeout=5, max_request_retries=5)

class TestCloudflare:
    """ TestCloudflare """
    def test_email_key_token(self):
        """ test_email_key_token """
        # Always clear environment
        self._setup()

        profile = self._profile

        assert self._email or self._key or self._token

        # if not self._email and not self._key and not self._token:
        #     assert 'EMAIL/KEY/TOKEN all needed in order to run this test' == ''

        cf = None
        # loop over each combination
        for email in [None, self._email, 'example@example.com']:
            for key in [None, self._key, self._token]:
                for token in [None, self._token, self._key]:
                    print('email = ', self._obfuscate(email), 'key = ', self._obfuscate(key), 'token = ', self._obfuscate(token))
                    if cf:
                        del cf
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
                        continue

                    if email is None and key == self._token and token is None:
                        assert isinstance(r, list)
                        assert len(r) == 1
                        assert isinstance(r[0], dict)
                        continue

                    if email == self._email and key == self._key and token is None:
                        assert isinstance(r, list)
                        assert len(r) == 1
                        assert isinstance(r[0], dict)
                        continue

                    if email == self._email and key is None and token == self._key:
                        assert isinstance(r, list)
                        assert len(r) == 1
                        assert isinstance(r[0], dict)
                        continue

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
