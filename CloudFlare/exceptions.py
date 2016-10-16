""" errors for Cloudflare API"""

class CloudFlareError(Exception):
    """ errors for Cloudflare API"""

    def __init__(self, code, message):
        """ errors for Cloudflare API"""

        self.code = code
        self.message = message

    def __int__(self):
        """ errors for Cloudflare API"""

        return self.code

    def __str__(self):
        """ errors for Cloudflare API"""

        return self.message

class CloudFlareAPIError(CloudFlareError):
    """ errors for Cloudflare API"""

    pass

class CloudFlareInternalError(CloudFlareError):
    """ errors for Cloudflare API"""

    pass

