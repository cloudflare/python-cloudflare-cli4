""" reading the config file for Cloudflare API"""

import os
import re
try:
    import ConfigParser  # py2
except ImportError:
    import configparser as ConfigParser  # py3

def read_configs(profile=None):
    """ reading the config file for Cloudflare API"""

    # envioronment variables override config files
    email = os.getenv('CF_API_EMAIL')
    token = os.getenv('CF_API_KEY')
    certtoken = os.getenv('CF_API_CERTKEY')
    extras = os.getenv('CF_API_EXTRAS')

    # grab values from config files
    config = ConfigParser.RawConfigParser()
    config.read([
        '.cloudflare.cfg',
        os.path.expanduser('~/.cloudflare.cfg'),
        os.path.expanduser('~/.cloudflare/cloudflare.cfg')
    ])

    if profile is None:
        profile = 'CloudFlare'

    if len(config.sections()) == 0:
        ## no config file found - so env values (even if empty) should be returned
        ## this isn't an error
        return [email, token, certtoken, extras, profile]

    if profile not in config.sections():
        ## section is missing - this is an error
        raise

    if email is None:
        try:
            email = re.sub(r"\s+", '', config.get(profile, 'email'))
        except (ConfigParser.NoOptionError, ConfigParser.NoSectionError):
            email = None

    if token is None:
        try:
            token = re.sub(r"\s+", '', config.get(profile, 'token'))
        except (ConfigParser.NoOptionError, ConfigParser.NoSectionError):
            token = None

    if certtoken is None:
        try:
            certtoken = re.sub(r"\s+", '', config.get(profile, 'certtoken'))
        except (ConfigParser.NoOptionError, ConfigParser.NoSectionError):
            certtoken = None

    if extras is None:
        try:
            extras = re.sub(r"\s+", ' ', config.get(profile, 'extras'))
        except (ConfigParser.NoOptionError, ConfigParser.NoSectionError):
            extras = None

        if extras:
            extras = extras.split(' ')

    return [email, token, certtoken, extras, profile]
