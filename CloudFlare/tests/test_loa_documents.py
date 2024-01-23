""" loa_documents tests """

import os
import sys
import time
import random

sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('..'))
import CloudFlare

# test /accounts/:id/addressing/prefixes
# test /accounts/:id/addressing/loa_documents
# test /accounts/:id/addressing/loa_documents/:id/download

cf = None

def test_cloudflare(debug=False):
    """ test_cloudflare """
    global cf
    cf = CloudFlare.CloudFlare(debug=debug)
    assert isinstance(cf, CloudFlare.CloudFlare)

account_name = None
account_id = None

def test_find_account(find_name=None):
    """ test_find_account """
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
        assert False
    assert len(accounts) > 0 and len(accounts) <= 10
    # n = random.randrange(len(accounts))
    # stop using a random account - use the primary account (i.e. the zero'th one)
    n = 0
    account_name = accounts[n]['name']
    account_id = accounts[n]['id']
    assert len(account_id) == 32
    print('account: %s %s' % (account_id, account_name), file=sys.stderr)

def test_addressing_prefixs():
    """ test_addressing_prefixs """
    prefixes = cf.accounts.addressing.prefixes(account_id)
    assert isinstance(prefixes, list)
    for p in prefixes:
        assert 'id' in p
        assert 'cidr' in p
        assert 'asn' in p
        assert 'advertised' in p
        assert 'approved' in p
        print('%s: cidr=%s asn=%s advertised=%s approved=%s' % (
            p['id'],
            p['cidr'],
            p['asn'],
            p['advertised'],
            p['approved']
        ), file=sys.stderr)

def test_addressing_loa_documents():
    """ test_addressing_loa_documents """
    loa_documents = cf.accounts.addressing.loa_documents(account_id)
    assert isinstance(loa_documents, list)
    for loa_document in loa_documents:
        assert isinstance(loa_document, dict)
        assert 'id' in loa_document
        assert 'filename' in loa_document
        assert 'verified' in loa_document
        assert 'size_bytes' in loa_document
        print('%s: filename=%s size_bytes=%d verified=%s' % (
           loa_document['id'],
           loa_document['filename'],
           loa_document['size_bytes'],
           loa_document['verified']
        ), file=sys.stderr)

def test_addressing_loa_documents_upload(filename=None):
    """ test_addressing_loa_documents_upload """
    if not filename:
        filename = 'CloudFlare/tests/dummy_loa_document.pdf'
    try:
        pdf_file = open(filename, 'rb')
    except (FileNotFoundError, IsADirectoryError, PermissionError) as e:
        print('%s: %s' % (filename, e), file=sys.stderr)
        assert False

    size_bytes = os.fstat(pdf_file.fileno()).st_size
    print('filename=%s size_bytes=%d' % (filename, size_bytes), file=sys.stderr)

    files = {'loa_document': pdf_file}
    try:
        loa_document = cf.accounts.addressing.loa_documents.post(account_id, files=files)
    except CloudFlare.exceptions.CloudFlareAPIError as e:
        print('%s: Error %d=%s' % (filename, int(e), str(e)), file=sys.stderr)
        assert False
    assert isinstance(loa_document, dict)
    assert 'id' in loa_document
    assert 'filename' in loa_document
    assert 'verified' in loa_document
    assert 'size_bytes' in loa_document
    print('%s: filename=%s size_bytes=%d verified=%s' % (
        loa_document['id'],
        loa_document['filename'],
        loa_document['size_bytes'],
        loa_document['verified']
    ), file=sys.stderr)
    assert size_bytes == loa_document['size_bytes']

def ispdf(s):
    """ ispdf """
    idx = 0
    while s[idx] in [b'\r', b'\n']:
        idx += 1
    # maybe ... \xef\xbb\xbf%PDF- ... which is  U+FEFF - the byte order mark, or BOM
    if s[idx:idx+3] == b'\xef\xbb\xbf':
        idx += 3
    # Simple %PDF- starter
    if s[idx:idx+5] == b'%PDF-':
        return True
    # check further down the file - which seems messy and in-fact is!
    # https://stackoverflow.com/questions/77753113/pdf-not-at-start-of-file-but-why
    if b'%PDF-' in s[0:1024]:
        return True
    # give up!
    return False

def test_addressing_loa_documents_download():
    """ test_addressing_loa_documents_download """
    loa_documents = cf.accounts.addressing.loa_documents(account_id)
    assert isinstance(loa_documents, list)
    for loa_document in loa_documents:
        assert isinstance(loa_document, dict)
        assert 'id' in loa_document
        assert 'filename' in loa_document
        assert 'verified' in loa_document
        assert 'size_bytes' in loa_document
        assert isinstance(loa_document['size_bytes'], int)
        print('%s: filename=%s size_bytes=%d verified=%s' % (
            loa_document['id'],
            loa_document['filename'],
            loa_document['size_bytes'],
            loa_document['verified']
        ), file=sys.stderr)
        loa_document_identifier = loa_document['id']
        size_bytes = loa_document['size_bytes']
        pdf_content = cf.accounts.addressing.loa_documents.download(account_id, loa_document_identifier)
        assert size_bytes == len(pdf_content)
        print('%s: %s' % (loa_document_identifier, pdf_content[0:10]))
        assert ispdf(pdf_content)

if __name__ == '__main__':
    test_cloudflare(debug=True)
    if len(sys.argv) > 1:
        test_find_account(sys.argv[1])
    else:
        test_find_account()
    test_addressing_prefixs()
    test_addressing_loa_documents()
    if len(sys.argv) > 2:
        test_addressing_loa_documents_upload(sys.argv[2])
    else:
        test_addressing_loa_documents_upload()
    test_addressing_loa_documents_download()
