""" Network for Cloudflare API"""

from urllib.parse import urlparse

import requests
from requests.adapters import HTTPAdapter

from .exceptions import CloudFlareAPIError

class CFnetwork():
    """Network for Cloudflare API"""

    def __init__(
        self, use_sessions=True, global_request_timeout=5, max_request_retries=5
    ):
        """Network for Cloudflare API"""

        self.use_sessions = use_sessions
        self.global_request_timeout = global_request_timeout
        self.max_request_retries = max_request_retries
        self.session = None

    def __call__(self, method, url, headers=None, params=None, data_str=None, data_json=None, files=None):
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

        # https://docs.python-requests.org/en/latest/user/quickstart/#post-a-multipart-encoded-file
        # Note, the json parameter is ignored if either data or files is passed.
        # This should have been handled well before here (it is!)

        if method == 'GET':
            # no data or files
            r = self.session.get(
                url,
                headers=headers,
                params=params,
                timeout=self.global_request_timeout,
            )
        elif method == 'POST':
            r = self.session.post(
                url,
                headers=headers,
                params=params,
                data=data_str,
                json=data_json,
                files=files,
                timeout=self.global_request_timeout,
            )
        elif method == 'PUT':
            r = self.session.put(
                url,
                headers=headers,
                params=params,
                data=data_str,
                json=data_json,
                files=files,
                timeout=self.global_request_timeout,
            )
        elif method == 'DELETE':
            r = self.session.delete(
                url,
                headers=headers,
                params=params,
                data=data_str,
                json=data_json,
                timeout=self.global_request_timeout,
            )
        elif method == 'PATCH':
            r = self.session.request(
                'PATCH',
                url,
                headers=headers,
                params=params,
                data=data_str,
                json=data_json,
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
