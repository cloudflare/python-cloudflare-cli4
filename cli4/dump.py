"""Cloudflare API via command line"""

def dump_commands(cf):
    """dump a tree of all the known API commands"""
    w = cf.api_list()
    return '\n'.join(w) + '\n'

def dump_commands_from_web(cf, url=None):
    """dump a tree of all the known API commands - from web"""
    if url:
        w = cf.api_from_openapi(url)
    else:
        w = cf.api_from_web()

    a = []
    for r in w:
        if r['deprecated']:
            if r['deprecated_already']:
                a.append('%-6s %s ; deprecated %s - expired!' % (r['action'], r['cmd'], r['deprecated_date']))
            else:
                a.append('%-6s %s ; deprecated %s' % (r['action'], r['cmd'], r['deprecated_date']))
        else:
            a.append('%-6s %s' % (r['action'], r['cmd']))
    return '\n'.join(a) + '\n'


