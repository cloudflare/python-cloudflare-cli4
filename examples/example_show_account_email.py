#!/usr/bin/env python
"""Cloudflare API code - example"""

import os
import sys
import json
sys.path.insert(0, os.path.abspath('..'))

import CloudFlare

def main():
    """Cloudflare API code - example"""

    try:
        account_name = sys.argv[1]
    except IndexError:
        exit('usage: example_page_rules.py account')

    cf = CloudFlare.CloudFlare()

    # grab the account identifier
    try:
        params = {'name': account_name}
        accounts = cf.accounts.get(params=params)
    except CloudFlare.exceptions.CloudFlareAPIError as e:
        exit('/accounts %d %s - api call failed' % (e, e))
    except Exception as e:
        exit('/accounts.get - %s - api call failed' % (e))

    if len(accounts) == 0:
        exit('/accounts.get - %s - account not found' % (account_name))

    if len(accounts) != 1:
        exit('/accounts.get - %s - api call returned %d items' % (account_name, len(accounts)))

    account_id = accounts[0]['id']

    r = cf.accounts.email_fwdr.addresses.get(account_id)

    print(json.dumps(r, indent=4))

    exit(0)

if __name__ == '__main__':
    main()
