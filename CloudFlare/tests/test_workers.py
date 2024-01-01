""" workers tests """

import os
import sys
import time
import random

sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('..'))
import CloudFlare

# test /accounts/:id/workers/scripts

cf = None

def test_cloudflare(debug=False):
    global cf
    cf = CloudFlare.CloudFlare(debug=debug)
    assert isinstance(cf, CloudFlare.CloudFlare)

account_name = None
account_id = None

def test_find_account(find_name=None):
    global account_name, account_id
    # grab a random account identifier from the first 10 accounts
    if find_name:
        params = {'per_page':1, 'name':find_name}
    else:
        params = {'per_page':10}
    try:
        accounts = cf.accounts.get(params=params)
    except CloudFlare.exceptions.CloudFlareAPIError as e:
        print('%s: Error %d=%s' % (find_name, int(e), str(e)), file=sys.stderr)
        exit(0)
    assert len(accounts) > 0 and len(accounts) <= 10
    n = random.randrange(len(accounts))
    account_name = accounts[n]['name']
    account_id = accounts[n]['id']
    assert len(account_id) == 32
    print('account: %s %s' % (account_id, account_name), file=sys.stderr)

def test_workers():
    workers = cf.accounts.workers.scripts(account_id)
    assert len(workers) >= 0
    assert isinstance(workers, list)
    # just test one script
    n = random.randrange(len(workers))
    for w in workers[n:1]:
        assert 'id' in w
        script_name = w['id']
        script_content = cf.accounts.workers.scripts(account_id, script_name)
        assert isinstance(script_content, str)
        assert len(script_content) > 0
        # print('%s: %s' % (script_name, script_content), file=sys.stderr)

if __name__ == '__main__':
    test_cloudflare(debug=True)
    if len(sys.argv) > 1:
        test_find_account(sys.argv[1])
    else:
        test_find_account()
    test_workers()
