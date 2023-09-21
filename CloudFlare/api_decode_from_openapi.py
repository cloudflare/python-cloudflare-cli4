""" API from OpenAPI for Cloudflare API"""

import sys
import re
import datetime
import json

API_TYPES = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE']

match_identifier = re.compile(r'\{[A-Za-z0-9_]*\}')

def do_path(cmd, values):
    """ do_path() """

    cmds = []

    if cmd[0] != '/':
        cmd = '/' + cmd  # make sure there's a leading /

    cmd = match_identifier.sub(':id', cmd) 
    if cmd[-4:] == '/:id':
        cmd = cmd[:-4]
    if cmd[-4:] == '/:id':
        cmd = cmd[:-4]

    for action in values:
        if action == '' or action.upper() not in API_TYPES:
            continue
        if 'deprecated' in values[action] and values[action]['deprecated']:
            deprecated = True
            deprecated_date = datetime.datetime.now().strftime('%Y-%m-%d')
            deprecated_already = True
        else:
            deprecated = False
            deprecated_date = ''
            deprecated_already = False
        v = {'action': action.upper(), 'cmd': cmd, 'deprecated': deprecated, 'deprecated_date': deprecated_date, 'deprecated_already': deprecated_already}
        cmds.append(v)
    return cmds

def api_decode_from_openapi(content):
    """ API decode from OpenAPI for Cloudflare API"""

    try:
        j = json.loads(content)
    except Exception as e:
        sys.stderr.write("OpenAPI json format issue: %s\n" % (e))
        return None

    try:
        components = j['components']
        info = j['info']
        openapi = j['openapi']
        paths = j['paths']
        servers = ['servers']
    except Exception as e:
        sys.stderr.write("OpenAPI json format structure: %s\n" % (e))
        return None

    sys.stderr.write("OpenAPI %s json file - version: %s\n" % (openapi, info['version']))

    all_cmds = []
    for path in paths:
        if path[0] != '/':
            sys.stderr.write("OpenAPI invalid path: %s\n" % (path))
            continue
        all_cmds += do_path(path, paths[path])

    return sorted(all_cmds, key=lambda v: v['cmd'])
