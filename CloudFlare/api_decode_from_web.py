""" API extras for Cloudflare API"""

from bs4 import BeautifulSoup, Comment

API_TYPES = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE']

def do_section(section):
    """ API extras for Cloudflare API"""

    cmds = []
    # look for deprecated first in section
    deprecated = False
    for tag2 in section.find_all('h3'):
        if 'Deprecation Warning' in str(tag2):
            deprecated = True
    # look for all API calls in section
    for tag2 in section.find_all('pre'):
        cmd = []
        for child in tag2.children:
            if isinstance(child, Comment):
                # remove <!-- react-text ... -> parts
                continue
            cmd.append(child.strip())
        if len(cmd) == 0:
            continue
        action = cmd[0]
        cmd = '/' + ''.join(cmd[1:])
        if action == '' or action not in API_TYPES:
            continue
        v = {'deprecated': deprecated, 'action': action, 'cmd': cmd}
        cmds.append(v)
    return cmds

def api_decode_from_web(content):
    """ API extras for Cloudflare API"""

    soup = BeautifulSoup(content, 'html.parser')

    all_cmds = []
    for section in soup.find_all('section'):
        all_cmds += do_section(section)

    return sorted(all_cmds, key=lambda v: v['cmd'])
