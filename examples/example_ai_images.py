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

def doit(account_name, prompt_text):

    # Or place these in your cloudflare.cfg file
    os.environ['CLOUDFLARE_API_EXTRAS'] = '/accounts/:id/ai/run/@cf/stabilityai/stable-diffusion-xl-base-1.0'

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

    image_create_data = {
        'prompt': prompt_text,
    }

    try:
        # This should be easy to call; however, the @ will not work in Python (or many languages)
        # r = cf.accounts.ai.run.@cf.stabilityai.stable-diffusion-xl-base-1.0(account_id, data=image_create_data)
        # We find the endpoint via a quick string search
        r = find_call(cf, 'accounts/ai/run/@cf/stabilityai/stable_diffusion_xl_base_1.0').post(account_id, data=image_create_data)
    except CloudFlare.exceptions.CloudFlareAPIError as e:
        exit('/ai.run %d %s - api call failed' % (e, e))

    sys.stdout.buffer.write(r)

def main():
    if sys.argv[1] == '-a':
        del sys.argv[1]
        account_name = sys.argv[1]
        del sys.argv[1]
    else:
        account_name = None
    if len(sys.argv) > 1:
        prompt_text = ' '.join(sys.argv[1:])
    else:
        prompt_text = "A happy llama running through an orange cloud"
    doit(account_name, prompt_text)

if __name__ == '__main__':
    main()
