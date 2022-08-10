#!/usr/bin/env python
"""Cloudflare API code - example"""

import os
import sys
import time

sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('..'))
import CloudFlare

def main():
    """Cloudflare API code - example"""

    # Simple timing of calls

    print('Create')
    tic = time.process_time_ns()
    cf = CloudFlare.CloudFlare()
    toc = time.process_time_ns()
    print('\t%7.3f ms' % ((toc-tic)/1000000.0))
    print('')

    print('Call')
    for ii in range(0,10):
        tic = time.process_time_ns()
        r = cf.ips()
        toc = time.process_time_ns()
        print('\t%7.3f ms' % ((toc-tic)/1000000.0))
    print('')

    print('Close')
    tic = time.process_time_ns()
    del cf
    toc = time.process_time_ns()
    print('\t%7.3f ms' % ((toc-tic)/1000000.0))
    print('')

if __name__ == '__main__':
    main()

