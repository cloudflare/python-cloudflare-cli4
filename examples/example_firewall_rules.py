#!/usr/bin/env python
"""Cloudflare API code - example"""

import os
import sys
import re
import json

sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('..'))
import CloudFlare

def main():
    """Cloudflare API code - example"""

    cf = CloudFlare.CloudFlare()

    try:
        zone_name = sys.argv[1]
    except IndexError:
        exit('usage: example_bot_management.py zone_name True/False')

    # grab the zone identifier
    try:
        params = {'name': zone_name}
        zones = cf.zones.get(params=params)
    except CloudFlare.exceptions.CloudFlareAPIError as e:
        exit('/zone %d %s - api call failed' % (e, e))
    except Exception as e:
        exit('/zone.get - %s - api call failed' % (e))

    if len(zones) == 0:
        exit('/zones.get - %s - zones not found' % (zone_name))

    if len(zones) != 1:
        exit('/zones.get - %s - api call returned %d items' % (zone_name, len(zones)))

    zone_id = zones[0]['id']

    # SHOW EXISTSING FIREWALL RULES
    r = cf.zones.firewall.rules.get(zone_id)
    print('filewall rules =\n' + json.dumps(r, indent=4, sort_keys=False) + '\n')

    # CREATE A FILTER & FIREWALL RULES

    my_filter = {
        # 'id': '00000000000000000000000000000000',
        'expression': 'http.request.uri.path == "/private.html$"',
        'paused': True,
        'description': 'stop access to /foo.html',
        'ref': 'FILTER-1',
    }

    my_data = [
        {
            'action': 'block',
            'filter': my_filter,
            # 'id': '00000000000000000000000000000000',
            # 'products': ['waf'],
            # 'priority': 1,
            # 'paused': True,
            # 'description': 'stop access to /foo.html',
            # 'ref': 'FILTER-1',
        }
    ]

    try:
        r = cf.zones.firewall.rules.post(zone_id, data=my_data)
    except Exception as e:
        print(e)
        exit(1)

    print('firewall rule created =\n' + json.dumps(r, indent=4, sort_keys=False) + '\n')

    # SHOW EXISTSING FILTERS
    r = cf.zones.filters.get(zone_id)
    print('filters =\n' + json.dumps(r, indent=4, sort_keys=False) + '\n')

    # DELETE EXISTSING FILTERS
    for f in r:
        print('id = ' + f['id'])
        r2 = cf.zones.filters.delete(zone_id, f['id'])
        print('deleted id = ' + r2['id'])

    # SHOW EXISTSING FIREWALL RULES
    r = cf.zones.firewall.rules.get(zone_id)
    print('filewall rules =\n' + json.dumps(r, indent=4, sort_keys=False) + '\n')

    # DELETE EXISTSING FIREWALL RULES
    for f in r:
        print('id = ' + f['id'])
        r2 = cf.zones.firewall.rules.delete(zone_id, f['id'])
        print('deleted id = ' + r2['id'])

if __name__ == '__main__':
    main()

