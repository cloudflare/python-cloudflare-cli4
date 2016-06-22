""" reading the config file for CloudFlare API"""

import os
import re
import ConfigParser

def read_configs():
    """ reading the config file for CloudFlare API"""

    # envioronment variables override config files
    email = os.getenv('CF_API_EMAIL')
    token = os.getenv('CF_API_KEY')
    certtoken = os.getenv('CF_API_CERTKEY')

    # grab values from config files
    config = ConfigParser.RawConfigParser()
    config.read([
        '.cloudflare.cfg',
        os.path.expanduser('~/.cloudflare.cfg'),
        os.path.expanduser('~/.cloudflare/cloudflare.cfg')
    ])

    if email is None:
        email = config.get('CloudFlare', 'email')
        try:
            email = re.sub(r"\s+", '', config.get('CloudFlare', 'email'))
        except ConfigParser.NoOptionError:
            email = None

    if token is None:
        try:
            token = re.sub(r"\s+", '', config.get('CloudFlare', 'token'))
        except ConfigParser.NoOptionError:
            token = None

    if certtoken is None:
        try:
            certtoken = re.sub(r"\s+", '', config.get('CloudFlare', 'certtoken'))
        except ConfigParser.NoOptionError:
            certtoken = None

    try:
        extras = re.sub(r"\s+", ' ', config.get('CloudFlare', 'extras'))
    except ConfigParser.NoOptionError:
        extras = None

    if extras:
        extras = extras.split(' ')

    return [email, token, certtoken, extras]

