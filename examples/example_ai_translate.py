#!/usr/bin/env python

import os
import sys
import CloudFlare

def find_call(cf, verbs):
    # So we walk over the @ via a getattr() call.
    # We also have to deal with a . in a verb - that does not work in Python. So sad.
    # Also, the - is actually an _ in this Python library. 
    # This is not normally needed for other calls
    m = cf
    for verb in verbs.split('/'):
        m = getattr(m, verb)
    return m

def doit(account_name, english_text):

    # Or place these in your cloudflare.cfg file
    os.environ['CLOUDFLARE_API_EXTRAS'] = '/accounts/:id/ai/run/@cf/meta/m2m100-1.2b'

    # We set the timeout because these AI calls take longer than normal API calls
    cf = CloudFlare.CloudFlare(global_request_timeout=120)

    try:
        if account_name == None or account_name == '':
            params = {'per_page': 1}
        else:
            params = {'name': account_name, 'per_page': 1}
        accounts = cf.accounts.get(params=params)
    except CloudFlare.exceptions.CloudFlareAPIError as e:
        exit('/accounts %d %s - api call failed' % (e, e))

    try:
        account_id = accounts[0]['id']
    except IndexError:
        exit('%s: account name not found' % (account_name))

    translate_data = {
        'text': english_text,
        'source_lang': 'english',
        'target_lang': 'french',
    }

    try:
        # This should be easy to call; however, the @ will not work in Python (or many languages)
        # r = cf.accounts.ai.run.@cf.meta.m2m100-1.2b(account_id, data=translate_data)
        # We find the endpoint via a quick string search
        r = find_call(cf, 'accounts/ai/run/@cf/meta/m2m100_1.2b').post(account_id, data=translate_data)
    except CloudFlare.exceptions.CloudFlareAPIError as e:
        exit('/ai.run %d %s - api call failed' % (e, e))

    print(r['translated_text'])

def main():
    if sys.argv[1] == '-a':
        del sys.argv[1]
        account_name = sys.argv[1]
        del sys.argv[1]
    else:
        account_name = None
    if len(sys.argv) > 1:
        english_text = ' '.join(sys.argv[1:])
    else:
        english_text = "I'll have an order of the moule frites"
    doit(account_name, english_text)

if __name__ == '__main__':
    main()
