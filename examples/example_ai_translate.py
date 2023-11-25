#!/usr/bin/env python

import os
import sys
import CloudFlare

def translate_call(cf):
    # So we walk over the @ via a getattr() call.
    # We also have to deal with a . in a verb - that does not work in Python. So sad.
    # Also, the - is actually an _ in this Python library. 
    # This is not normally needed for other calls
    m = cf.accounts.ai.run
    m = getattr(m, '@cf')
    m = getattr(m, 'meta')
    m = getattr(m, 'm2m100_1.2b')
    return m

def doit(account_name, english_text):

    # Or place these in your cloudflare.cfg file
    os.environ['CLOUDFLARE_API_EXTRAS'] = '/accounts/:id/ai/run/@cf/meta/m2m100-1.2b'

    cf = CloudFlare.CloudFlare()

    try:
        params = {'name': account_name, 'per_page': 1}
        accounts = cf.accounts.get(params=params)
    except CloudFlare.exceptions.CloudFlareAPIError as e:
        exit('/accounts %d %s - api call failed' % (e, e))

    account_id = accounts[0]['id']

    translate_data = {
        'text': english_text,
        'source_lang': 'english',
        'target_lang': 'french',
    }

    # This should be easy to call; however, the @ will not work in Python (or many languages)
    # r = cf.accounts.ai.run.@cf.meta.m2m100-1.2b(account_id, data=translate_data)

    the_call = translate_call(cf)

    try:
        r = the_call.post(account_id, data=translate_data)
    except CloudFlare.exceptions.CloudFlareAPIError as e:
        exit('/ai.run %d %s - api call failed' % (e, e))

    print(r['translated_text'])

def main():
    account_name = sys.argv[1]
    if len(sys.argv) > 2:
        english_text = ' '.join(sys.argv[2:])
    else:
        english_text = "I'll have an order of the moule frites"
    doit(account_name, english_text)

if __name__ == '__main__':
    main()
