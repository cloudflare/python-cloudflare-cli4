""" get/post/delete/etc zone ruleset based tests """

import os
import sys
import uuid
import random

sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('..'))
import CloudFlare

# test GET POST PUT PATCH & DELETE - but not in that order

cf = None

def test_cloudflare(debug=False):
    """ test_cloudflare """
    global cf
    cf = CloudFlare.CloudFlare(debug=debug)
    assert isinstance(cf, CloudFlare.CloudFlare)

zone_name = None
zone_id = None

def test_find_zone(domain_name=None):
    """ test_find_zone """
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
        assert False
    assert len(zones) > 0 and len(zones) <= 10
    n = random.randrange(len(zones))
    zone_name = zones[n]['name']
    zone_id = zones[n]['id']
    assert len(zone_id) == 32
    print('zone: %s %s' % (zone_id, zone_name), file=sys.stderr)

ruleset_name = None
ruleset_ref = None
ruleset_content = None

def test_ruleset_create_values():
    """ test_ruleset_create_values """
    global ruleset_name, ruleset_ref, ruleset_content
    ruleset_name = str(uuid.uuid1())
    ruleset_ref = str(uuid.uuid1())
    ruleset_content = """
        {
          "description": "Testing 1 2 3 ...",
          "kind": "zone",
          "name": "%s",
          "phase": "http_request_firewall_custom",
          "rules": [
            {
              "action": "block",
              "description": "Block when the IP address is not 1.1.1.1",
              "enabled": false,
              "expression": "ip.src ne 1.1.1.1",
              "ref": "%s"
            }
          ]
        }
    """ % (ruleset_name, ruleset_ref)
    ruleset_content = ''.join([s.strip() for s in ruleset_content.splitlines()]).strip()

    print('ruleset: name=%s content=%s' % (ruleset_name, ruleset_content), file=sys.stderr)
    assert True

ruleset_id = None

def test_rulesets_get():
    """ test_rulesets_get """
    # GET
    ruleset_results = cf.zones.rulesets.get(zone_id)
    assert isinstance(ruleset_results, list)
    for ruleset in ruleset_results:
        assert isinstance(ruleset, dict)
        assert 'id' in ruleset
        assert 'kind' in ruleset
        assert 'phase' in ruleset
        assert 'name' in ruleset
        print('ruleset: %s: name=%s kind=%s phase=%s' % (ruleset['id'], ruleset['name'], ruleset['kind'], ruleset['phase']), file=sys.stderr)
    assert True

def test_ruleset_post():
    """ test_rulesets_post """
    global ruleset_id
    # POST
    ruleset = cf.zones.rulesets.post(zone_id, data=ruleset_content)
    assert isinstance(ruleset, dict)
    assert 'id' in ruleset
    assert 'kind' in ruleset
    assert 'phase' in ruleset
    assert 'name' in ruleset
    assert 'rules' in ruleset
    assert 'ref' in ruleset['rules'][0]
    assert ruleset['name'] == ruleset_name
    assert ruleset['rules'][0]['ref'] == ruleset_ref
    ruleset_id = ruleset['id']
    print('ruleset: %s: name=%s kind=%s phase=%s' % (ruleset['id'], ruleset['name'], ruleset['kind'], ruleset['phase']), file=sys.stderr)

def test_rulesets_get_specific():
    """ test_rulesets_get_specific """
    # GET
    ruleset = cf.zones.rulesets.get(zone_id, ruleset_id)
    assert isinstance(ruleset, dict)
    assert 'id' in ruleset
    assert 'kind' in ruleset
    assert 'phase' in ruleset
    assert 'name' in ruleset
    assert 'rules' in ruleset
    assert ruleset['id'] == ruleset_id
    print('ruleset: %s: name=%s kind=%s phase=%s' % (ruleset['id'], ruleset['name'], ruleset['kind'], ruleset['phase']), file=sys.stderr)

def test_ruleset_delete():
    """ test_rulesets_delete """
    # DELETE
    ruleset_response = cf.zones.rulesets.delete(zone_id, ruleset_id)
    # None is returned - not quite the same response as other delete's in the API
    assert ruleset_response is None

if __name__ == '__main__':
    test_cloudflare(debug=true)
    if len(sys.argv) > 1:
        test_find_zone(sys.argv[1])
    else:
        test_find_zone()
    test_ruleset_create_values()
    test_rulesets_get()
    test_ruleset_post()
    test_rulesets_get_specific()
    test_ruleset_delete()
