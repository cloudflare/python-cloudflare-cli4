#!/usr/bin/env python
"""Cloudflare API code - example"""

import os
import sys
import json

sys.path.insert(0, os.path.abspath('..'))
import CloudFlare

def main():
    """Cloudflare API code - example"""

    cf = CloudFlare.CloudFlare()
    try:
        found_comands= cf.api_from_web()
    except Exception as e:
        exit('api_from_web: - %s - api call connection failed' % (e))

    cmds = {}
    for r in found_comands:
        if r['deprecated'] or r['deprecated_already']:
            continue
        cmd = r['cmd']
        action = r['action']
        if cmd not in cmds:
            cmds[cmd] = {}
        cmds[cmd][action] = action

    # This produces something like this ...
    # GET    -      -      PATCH  -       /zones/:zone_identifier/settings/always_online
    # GET    -      PUT    PATCH  DELETE  /zones/:zone_identifier/waiting_rooms/:waiting_room_id

    for cmd in cmds.keys():
        p = ''
        for method in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']:
            if method in cmds[cmd]:
                p += '%-7s' % method
            else:
                p += '%-7s' % '-'
        print("%s %s" % (p, cmd))

if __name__ == '__main__':
    main()

