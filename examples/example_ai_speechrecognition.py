#!/usr/bin/env python

import os
import sys
import random
import tempfile
import requests

sys.path.insert(0, os.path.abspath('.'))
import CloudFlare

def find_call(cf, verbs):
    # So we walk over the @ via a getattr() call.
    # We also have to deal with a . in a verb - that does not work in Python. So sad.
    # Also, the - is actually an _ in this Python library.
    # This is not normally needed for other calls
    m = cf
    for verb in verbs.split('/'):
        if verb == '' or verb[0] == ':':
            continue
        m = getattr(m, verb)
    return m

def user_agent():
    s = random.choice([
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
    ])
    return s

def doit(account_name, mp3_data):

    # Or place these in your cloudflare.cfg file
    os.environ['CLOUDFLARE_API_EXTRAS'] = '/accounts/:id/ai/run/@cf/openai/whisper'

    # We set the timeout because these AI calls take longer than normal API calls
    cf = CloudFlare.CloudFlare(global_request_timeout=120)

    try:
        if account_name is None or account_name == '':
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

    try:
        # This should be easy to call; however, the @ will not work in Python (or many languages)
        # r = cf.accounts.ai.run.@cf.openai/whisper(account_id, data=mp3_data)
        # We find the endpoint via a quick string search
        r = find_call(cf, '/accounts/:id/ai/run/@cf/openai/whisper').post(account_id, data=mp3_data)
    except CloudFlare.exceptions.CloudFlareAPIError as e:
        exit('/ai.run %d %s - api call failed' % (e, e))

    print('%s' % (r['text']))
    # words = [word['word'] for word in r['words']]
    # print('%s' % ('|'.join(words)))

# based on ... thank you to the author
# https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests
def download_file(url, referer, n_requested):
    headers = {}
    headers['Referer'] = referer
    headers['User-Agent'] = user_agent()

    # will be deleted once program exits
    fp = tempfile.TemporaryFile(mode='w+b')

    n_received = 0
    # NOTE the stream=True parameter below
    with requests.get(url, headers=headers, stream=True) as r:
        r.raise_for_status()
        for chunk in r.iter_content(chunk_size=16*1024):
            fp.write(chunk)
            n_received += len(chunk)
            if n_received > n_requested:
                break

    # rewind the file so it's ready to read
    fp.seek(0)
    return fp

def main():
    if len(sys.argv) > 1 and sys.argv[1] == '-a':
        del sys.argv[1]
        account_name = sys.argv[1]
        del sys.argv[1]
    else:
        account_name = None

    if len(sys.argv) > 1:
        url = sys.argv[1]
        referer = url
    else:
        url = 'https://www.americanrhetoric.com/mp3clipsXE/barackobama/barackobamapresidentialfarewellARXE.mp3'
        referer = 'https://www.americanrhetoric.com/barackobamaspeeches.htm'

    # we only grab the first 680KB of the file - that's enough to show working code
    mp3_fp = download_file(url, referer, 680 * 1024)
    mp3_data = mp3_fp.read()
    print('mp3 received: length=%d' % (len(mp3_data)))

    doit(account_name, mp3_data)

if __name__ == '__main__':
    main()
