#!/usr/bin/env python

#
# A Hack - not worth publishing
#

import os
import pypandoc

long_description = pypandoc.convert('README.md', 'rst')
long_description = long_description.replace("\r","")
with open('README.rst','w') as f:
    f.write(long_description)

