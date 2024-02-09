#!/usr/bin/env python
"""Cloudflare API code - example"""

import os
import sys
import json
import datetime
import requests

sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('..'))
import CloudFlare

#
# Warning: You need to enable image storage on your account for this code to work.
# You'll get 403 errors if you don't have it enabled (go pay for it)
#
# If you need to delete images after running this code you can do this:
#
# cli4 --delete /accounts/:"${ACCOUNT}"/images/v1/::${image_id}
#
# Or if you want to live dangerously - do this and delete every image you have
# You should not run this unless you really really really know what you're doing! (like rm -rf /)
#
# cli4 /accounts/:"${ACCOUNT}"/images/v1 | jq -r '.images[]|.id' | while read image_id ; do cli4 --delete /accounts/:"${ACCOUNT}"/images/v1/::$image_id ; done
#

def doit(account_name, image_filename):

    # https://developers.cloudflare.com/stream/uploading-videos/direct-creator-uploads/
    # https://developers.cloudflare.com/api/operations/cloudflare-images-create-authenticated-direct-upload-url-v-2

    with CloudFlare.CloudFlare(debug=False) as cf:
        try:
            params = {'name': account_name, 'per_page': 1}
            accounts = cf.accounts.get(params=params)
        except CloudFlare.exceptions.CloudFlareAPIError as e:
            exit('%s: %d %s - api call failed' % ('/accounts', e, e))
        try:
            account_id = accounts[0]['id']
        except IndexError:
            exit('%s: account name not found' % (account_name))

        try:
           image_fp = open(image_filename, 'rb')
        except Exception as e:
            exit('%s: %s - file read failed' % (image_filename, e))

        image_filesize = os.fstat(image_fp.fileno()).st_size
        if image_filesize > 1024*1024*1024:
                print('%s: filesize = %0.1f GBytes' % (image_filename, float(image_filesize)/1024*1024*1024))
        elif image_filesize > 1024*1024:
                print('%s: filesize = %0.1f MBytes' % (image_filename, float(image_filesize)/1024*1024))
        elif image_filesize > 1024:
                print('%s: filesize = %0.1f KBytes' % (image_filename, float(image_filesize)/1024))
        else:
                print('%s: filesize = %d Bytes' % (image_filename, image_filesize))

        # format future time in RFC3339 format (and do it UTC time)
        time_plus_one_hour_in_iso = (datetime.datetime.utcnow().replace(microsecond=0) + datetime.timedelta(hours=1)).isoformat() + 'Z'

        # direct_upload uses multipart/form-data and hence this info is passed as files (but None for filename)
        # these are the four form values
        # presently you need to upload at-least one of these until the library version is greater than 2.17.0
        # --form expiry= \
        # --form id= \
        # --form metadata= \
        # --form requireSignedURLs=

        # here's examples using metadata and expiry.
        metadata_values = {
            'source': image_filename,
            'size': image_filesize,
        }
        files = {
            ('metadata', (None, json.dumps(metadata_values))),
            ('expiry', (None, time_plus_one_hour_in_iso))
        }

        try:
            r = cf.accounts.images.v2.direct_upload.post(account_id, files=files)
        except CloudFlare.exceptions.CloudFlareAPIError as e:
            exit('%s: %d %s - api call failed' % ('/accounts/images/v2/direct_upload', e, e))
        print('v2 new image post results')
        print(json.dumps(r, indent=4))

        image_id = r['id']
        image_url = r['uploadURL']

        # https://developers.cloudflare.com/stream/uploading-videos/direct-creator-uploads/
        # curl -X POST \
        #      -F file=@/Users/mickie/Downloads/example_video.mp4 \
        #      https://upload.videodelivery.net/f65014bc6ff5419ea86e7972a047ba22

        try:
            r = requests.post(image_url, files={('file', image_fp) })
        except Exception as e:
            exit('%s: %s - api call failed' % (image_url, e))

        response_code = r.status_code
        if response_code != 200:
           exit('%s: HTTP Error %s' % (image_url, response_code))

        j = r.json()
        if j['success'] == True:
            print('Image upload results')
            print(json.dumps(j['result'], indent=4))
        else:
            exit('Error:\n    errors: %s\n    messages: %s' % (image_url, j['errors'], j['messages']))

        image_fp.close()

        # list all images
        try:
            r = cf.accounts.images.v2(account_id)
        except CloudFlare.exceptions.CloudFlareAPIError as e:
            exit('%s: %d %s - api call failed' % ('/accounts/images/v1', e, e))

        print('All account images:')
        for img in r['images']:
            print('%s   %s: %s %s %s' % ('>' if img['id'] == image_id else ' ', img['id'], img['uploaded'], img['filename'], img['variants'][0]))
            for k,v in img['meta'].items():
                print('        %s = %s' % (k, v))

        # delete the image - this was just a test (comment this out if you end up using this code for uploads)
        try:
            r = cf.accounts.images.v1.delete(account_id, image_id)
        except CloudFlare.exceptions.CloudFlareAPIError as e:
            exit('%s: %d %s - api call failed' % ('/accounts/images/v1', e, e))
        print('Image delete')
        print(json.dumps(r, indent=4))

def main():
    try:
        account_name = sys.argv[1]
    except IndexError:
        exit('usage: example_images_v2_direct_upload.py account_name image_filename')
    try:
        image_filename = sys.argv[2]
    except IndexError:
        exit('usage: example_images_v2_direct_upload.py account_name image_filename')
    doit(account_name, image_filename)
    exit(0)

if __name__ == '__main__':
    main()
