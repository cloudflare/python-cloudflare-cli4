""" Network for Cloudflare API"""
from __future__ import absolute_import

import requests

from .exceptions import CloudFlareAPIError

class CFnetwork():
    """ Network for Cloudflare API"""

    def __init__(self, use_sessions=True):
        """ Network for Cloudflare API"""

        self.use_sessions = use_sessions
        self.session = None

    def __call__(self, method, url, headers=None, params=None, data=None, files=None):
        """ Network for Cloudflare API"""

        if self.use_sessions:
            if self.session is None:
                self.session = requests.Session()
        else:
            self.session = requests

        method = method.upper()

        if method == 'GET':
            r = self.session.get(url, headers=headers, params=params, data=data)
        elif method == 'POST':
            if isinstance(data, str):
                r = self.session.post(url, headers=headers, params=params, data=data, files=files)
            else:
                r = self.session.post(url, headers=headers, params=params, json=data, files=files)
        elif method == 'PUT':
            if isinstance(data, str):
                r = self.session.put(url, headers=headers, params=params, data=data)
            else:
                r = self.session.put(url, headers=headers, params=params, json=data)
        elif method == 'DELETE':
            if isinstance(data, str):
                r = self.session.delete(url, headers=headers, params=params, data=data)
            else:
                r = self.session.delete(url, headers=headers, params=params, json=data)
        elif method == 'PATCH':
            if isinstance(data, str):
                r = self.session.request('PATCH', url, headers=headers, params=params, data=data)
            else:
                r = self.session.request('PATCH', url, headers=headers, params=params, json=data)
        else:
            # should never happen
            raise CloudFlareAPIError(0, 'method not supported')

        return r

    def __del__(self):
        """ Network for Cloudflare API"""

        if self.use_sessions and self.session:
            self.session.close()
            self.session = None
