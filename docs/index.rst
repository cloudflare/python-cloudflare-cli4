.. python-cloudflare documentation master file, created by
   sphinx-quickstart on Sun Mar  3 23:59:20 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

python-cloudflare - A Python-based access to Cloudflare's API's
===============================================================

Release v\ |version|.

.. image:: https://static.pepy.tech/badge/cloudflare/month
    :target: https://pepy.tech/project/cloudflare
    :alt: Requests Downloads Per Month Badge
    
.. image:: https://img.shields.io/pypi/l/cloudflare.svg
    :target: https://pypi.org/project/cloudflare/
    :alt: License Badge

.. image:: https://img.shields.io/pypi/wheel/cloudflare.svg
    :target: https://pypi.org/project/cloudflare/
    :alt: Wheel Support Badge

.. image:: https://img.shields.io/pypi/pyversions/cloudflare.svg
    :target: https://pypi.org/project/cloudflare/
    :alt: Python Version Support Badge

**python-cloudflare** is a Python library for easy access to Cloudflare's API's.

**Trivial example**::

    >>> import CloudFlare
    >>> cf = CloudFlare.cloudflare()
    >>> 
    >>> cf.ips()
    {'ipv4_cidrs': ['173.245.48.0/20', ... ], ... }
    >>>

Refer to the `examples` directory for full examples.

The User Guide
--------------

.. toctree::
   :maxdepth: 4
   :caption: Contents:

.. include:: modules.rst

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
