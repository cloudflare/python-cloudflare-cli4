""" radar returning CSV test """

import os
import sys
import uuid

sys.path.insert(0, os.path.abspath('..'))
import CloudFlare

# test radar - this tests CSV responses

cf = None

def test_cloudflare():
    global cf
    cf = CloudFlare.CloudFlare()
    assert isinstance(cf, CloudFlare.CloudFlare)

def test_radar_datasets_ranking_top_200():
    results = cf.radar.datasets('ranking_top_200')
    assert len(results) > 0
    lines = results.splitlines()
    assert lines[0] == 'domain'
    assert len(lines) >= 200+1

def test_radar_datasets_ranking_top_1000():
    results = cf.radar.datasets('ranking_top_1000')
    assert len(results) > 0
    lines = results.splitlines()
    assert lines[0] == 'domain'
    assert len(lines) >= 1000+1

