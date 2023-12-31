""" graphql tests """

import os
import sys
import time
import random
import datetime
import pytz
import json

sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('..'))
import CloudFlare

# test /graphql

cf = None

def test_cloudflare(debug=False):
    global cf
    cf = CloudFlare.CloudFlare(debug=debug)
    assert isinstance(cf, CloudFlare.CloudFlare)

zone_name = None
zone_id = None

def test_find_zone(domain_name=None):
    global zone_name, zone_id
    # grab a random zone identifier from the first 10 zones
    if domain_name:
        params = {'per_page':1, 'name':domain_name}
    else:
        params = {'per_page':10}
    try:
        zones = cf.zones.get(params=params)
    except CloudFlare.exceptions.CloudFlareAPIError as e:
        print('%s: Error %d=%s' % (domain_name, int(e), str(e)), file=sys.stderr)
        exit(0)
    assert len(zones) > 0 and len(zones) <= 10
    n = random.randrange(len(zones))
    zone_name = zones[n]['name']
    zone_id = zones[n]['id']
    assert len(zone_id) == 32
    print('zone: %s %s' % (zone_id, zone_name), file=sys.stderr)

def now_iso8601_time(h_delta):
    """need a yyyy-mm-dd string"""
    t = time.time() - (h_delta * 3600)
    # only use yyyy-mm-dd part for httpRequests1dGroups below
    r = datetime.datetime.fromtimestamp(int(t), tz=pytz.timezone("UTC")).strftime('%Y-%m-%d')
    return r

def test_graphql():
    """ /graphql test """
    date_before = now_iso8601_time(0) # now
    date_after = now_iso8601_time(3 * 24) # 3 days worth

    query = """
      query {
        viewer {
            zones(filter: {zoneTag: "%s"} ) {
            httpRequests1dGroups(limit:40, filter:{date_lt: "%s", date_gt: "%s"}) {
              sum { countryMap { bytes, requests, clientCountryName } }
              dimensions { date }
            }
          }
        }
      }
    """ % (zone_id, date_before, date_after)

    # remove whitespace from query - this isn't needed; but helps debug
    query = '\n'.join([s.strip() for s in query.splitlines()]).strip()

    # graphql query is always a post
    try:
        r = cf.graphql.post(data={'query':query})
    except CloudFlare.exceptions.CloudFlareAPIError as e:
        exit('/graphql.post %d %s - api call failed' % (e, e))

    # success - lets confirm it's graphql results as-per query above

    # basic graphql results
    assert 'data' in r
    assert 'errors' in r
    assert r['errors'] == None

    # viewer and zones from above
    assert 'viewer' in r['data']
    assert 'zones' in r['data']['viewer']

    # only one zone
    zones = r['data']['viewer']['zones']
    assert len(zones) == 1
    zone_info = zones[0]

    # the data
    assert 'httpRequests1dGroups' in zone_info
    httpRequests1dGroups = zone_info['httpRequests1dGroups']
    assert isinstance(httpRequests1dGroups, list)
    for h in httpRequests1dGroups:
        assert 'dimensions' in h
        assert 'date' in h['dimensions']
        result_date = h['dimensions']['date']
        assert 'sum' in h
        result_sum = h['sum']
        assert 'countryMap' in result_sum
        countryMap = h['sum']['countryMap']
        for element in countryMap:
            assert 'bytes' in element
            assert 'requests' in element
            assert 'clientCountryName' in element

if __name__ == '__main__':
    test_cloudflare(debug=True)
    if len(sys.argv) > 1:
        test_find_zone(sys.argv[1])
    else:
        test_find_zone()
    test_graphql()
