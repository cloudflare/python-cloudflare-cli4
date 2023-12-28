""" get/post/delete/etc dns based tests """

import os
import sys
import uuid
import random

sys.path.insert(0, os.path.abspath('..'))
import CloudFlare

# test GET POST PUT PATCH & DELETE - but not in that order

cf = None

def test_cloudflare():
    global cf
    cf = CloudFlare.CloudFlare()
    assert isinstance(cf, CloudFlare.CloudFlare)

zone_name = None
zone_id = None

def test_find_zone():
    global zone_name, zone_id
    # grab a random zone identifier from the first 10 zones
    params = {'per_page':10}
    zones = cf.zones.get(params=params)
    assert len(zones) > 0 and len(zones) <= 10
    n = random.randrange(len(zones))
    zone_name = zones[n]['name']
    zone_id = zones[n]['id']
    assert len(zone_id) == 32
    print('zone: %s %s' % (zone_id, zone_name), file=sys.stderr)

dns_name = None
dns_type = None
dns_content1 = None
dns_content2 = None
dns_content3 = None

def test_dns_records():
    global dns_name, dns_type, dns_content1, dns_content2, dns_content3
    dns_name = str(uuid.uuid1())
    dns_type = 'TXT'
    dns_content1 = 'temp pytest element 1'
    dns_content2 = 'temp pytest element 2'
    dns_content3 = 'temp pytest element 3'
    print('dns_record: %s' % (dns_name), file=sys.stderr)

def test_dns_records_get1():
    # GET
    params = {'name':dns_name + '.' + zone_name, 'match':'all', 'type':dns_type}
    dns_results = cf.zones.dns_records.get(zone_id, params=params)
    assert len(dns_results) == 0

dns_id = None

def test_dns_records_post():
    global dns_id
    # POST
    dns_record = {'name':dns_name, 'type':dns_type, 'content':dns_content1}
    dns_result = cf.zones.dns_records.post(zone_id, data=dns_record)
    assert dns_result['name'] == dns_name + '.' + zone_name
    assert dns_result['type'] == dns_type
    assert dns_result['content'] == dns_content1

    dns_id = dns_result['id']
    assert len(dns_id) == 32
    print('dns_record: %s %s' % (dns_name, dns_id), file=sys.stderr)

def test_dns_records_get2():
    # GET
    params = {'name':dns_name + '.' + zone_name, 'match':'all', 'type':dns_type}
    dns_results = cf.zones.dns_records.get(zone_id, params=params)
    assert len(dns_results) == 1
    assert dns_results[0]['name'] == dns_name + '.' + zone_name
    assert dns_results[0]['type'] == dns_type
    assert dns_results[0]['content'] == dns_content1

def test_dns_records_get3():
    # GET
    dns_result = cf.zones.dns_records.get(zone_id, dns_id)
    assert dns_result['name'] == dns_name + '.' + zone_name
    assert dns_result['type'] == dns_type
    assert dns_result['content'] == dns_content1

def test_dns_records_patch():
    # PATCH
    dns_record = {'content':dns_content2}
    dns_result = cf.zones.dns_records.patch(zone_id, dns_id, data=dns_record)
    assert dns_result['name'] == dns_name + '.' + zone_name
    assert dns_result['type'] == dns_type
    assert dns_result['content'] == dns_content2

def test_dns_records_put():
    # PUT
    dns_record = {'name':dns_name, 'type':dns_type, 'content':dns_content3}
    dns_result = cf.zones.dns_records.put(zone_id, dns_id, data=dns_record)
    assert dns_result['name'] == dns_name + '.' + zone_name
    assert dns_result['type'] == dns_type
    assert dns_result['content'] == dns_content3

def test_dns_records_get4():
    # GET
    dns_result = cf.zones.dns_records.get(zone_id, dns_id)
    assert dns_result['name'] == dns_name + '.' + zone_name
    assert dns_result['type'] == dns_type
    assert dns_result['content'] == dns_content3

def test_dns_records_delete():
    # DELETE
    dns_result = cf.zones.dns_records.delete(zone_id, dns_id)
    assert dns_result['id'] == dns_id

def test_dns_records_get5():
    # GET
    params = {'name':dns_name + '.' + zone_name, 'match':'all', 'type':dns_type}
    dns_results = cf.zones.dns_records.get(zone_id, params=params)
    assert len(dns_results) == 0
