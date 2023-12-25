""" dns import/export test """

import os
import sys
import uuid

sys.path.insert(0, os.path.abspath('..'))
import CloudFlare

# test IMPORT EXPORT

cf = None
zone_name = None
zone_id = None

def test_cloudflare():
    global cf
    cf = CloudFlare.CloudFlare()
    assert isinstance(cf, CloudFlare.CloudFlare)

dns_name = None
dns_id = None

def test_find_zone():
    global zone_name, zone_id
    # grab the first zone identifier
    params = {'per_page':1}
    zones = cf.zones.get(params=params)
    assert  len(zones) == 1
    zone_name = zones[0]['name']
    zone_id = zones[0]['id']
    assert len(zone_id) == 32
    print('zone: %s %s' % (zone_id, zone_name))

def test_dns_import():
    # IMPORT
    fd = open('/dev/null', 'rb')
    results = cf.zones.dns_records.import_.post(zone_id, files={'file':fd})
    # {"recs_added": 0, "recs_added_by_type": {}, "total_records_parsed": 0}
    assert len(results) > 0
    assert results['recs_added'] == 0
    assert len(results['recs_added_by_type']) == 0
    assert results['total_records_parsed'] == 0

def test_dns_export():
    # EXPORT
    dns_records = cf.zones.dns_records.export.get(zone_id)
    assert len(dns_records) > 0
    assert isinstance(dns_records, str)
    assert 'SOA' in dns_records
    assert 'NS' in dns_records
