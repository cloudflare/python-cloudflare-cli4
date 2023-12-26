""" radar returning CSV test """

import os
import sys
import uuid

sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('..'))
import CloudFlare

# test radar - this tests CSV responses

cf = None

def test_cloudflare():
    global cf
    cf = CloudFlare.CloudFlare()
    assert isinstance(cf, CloudFlare.CloudFlare)

aliases = None

def test_radar_datasets_ranking():
    # get the list of aliases - we only need to grab 12 values
    global aliases
    params = {'limit':12}
    results = cf.radar.datasets(params=params)
    assert len(results) > 0
    assert 'datasets' in results
    aliases = []
    for v in results['datasets']:
        aliases.append(
            (v['id'], v['alias'], v['meta']['top'])
        )
    aliases = sorted(aliases, key=lambda v: v[2], reverse=False)

def test_radar_datasets_ranking_three_aliases():
    for v in aliases[0:3]:
        alias = v[1]
        n_lines = v[2]
        results = cf.radar.datasets(alias)
        # produces CSV results
        assert len(results) > 0
        lines = results.splitlines()
        assert lines[0] == 'domain'
        assert len(lines) >= n_lines + 1

