""" Network for Cloudflare API"""
from __future__ import absolute_import

from urllib.parse import urlparse

import requests
from requests.adapters import HTTPAdapter

from .exceptions import CloudFlareAPIError


class CFnetwork:
    """Network for Cloudflare API"""

    def __init__(
        self, max_request_retries, use_sessions=True, global_request_timeout=5,
    ):
        """Network for Cloudflare API"""

        self.use_sessions = use_sessions
        self.global_request_timeout = global_request_timeout
        self.max_request_retries = max_request_retries
        self.session = None

    def __call__(self, method, url, headers=None, params=None, data=None, files=None):
        """Network for Cloudflare API"""

        if self.use_sessions:
            if self.session is None:
                s = requests.Session()
                if self.max_request_retries is not None:
                    hostname = urlparse(url).netloc
                    s.mount(
                        f"https://{hostname}",
                        HTTPAdapter(max_retries=self.max_request_retries),
                    )
                self.session = s
        else:
            self.session = requests

        method = method.upper()

        if method == 'GET':
            r = self.session.get(
                url,
                headers=headers,
                params=params,
                data=data,
                timeout=self.global_request_timeout,
            )
        elif method == 'POST':
            if isinstance(data, str):
                r = self.session.post(
                    url,
                    headers=headers,
                    params=params,
                    data=data,
                    files=files,
                    timeout=self.global_request_timeout,
                )
            else:
                r = self.session.post(
                    url,
                    headers=headers,
                    params=params,
                    json=data,
                    files=files,
                    timeout=self.global_request_timeout,
                )
        elif method == 'PUT':
            if isinstance(data, str):
                r = self.session.put(
                    url,
                    headers=headers,
                    params=params,
                    data=data,
                    timeout=self.global_request_timeout,
                )
            else:
                r = self.session.put(
                    url,
                    headers=headers,
                    params=params,
                    json=data,
                    timeout=self.global_request_timeout,
                )
        elif method == 'DELETE':
            if isinstance(data, str):
                r = self.session.delete(
                    url,
                    headers=headers,
                    params=params,
                    data=data,
                    timeout=self.global_request_timeout,
                )
            else:
                r = self.session.delete(
                    url,
                    headers=headers,
                    params=params,
                    json=data,
                    timeout=self.global_request_timeout,
                )
        elif method == 'PATCH':
            if isinstance(data, str):
                r = self.session.request(
                    'PATCH',
                    url,
                    headers=headers,
                    params=params,
                    data=data,
                    timeout=self.global_request_timeout,
                )
            else:
                r = self.session.request(
                    'PATCH',
                    url,
                    headers=headers,
                    params=params,
                    json=data,
                    timeout=self.global_request_timeout,
                )
        else:
            # should never happen
            raise CloudFlareAPIError(0, 'method not supported')

        return r

    def __del__(self):
        """Network for Cloudflare API"""

        if self.use_sessions and self.session:
            self.session.close()
            self.session = None
