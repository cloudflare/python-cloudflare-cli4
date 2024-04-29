#!/usr/bin/env python
"""Cloudflare API code - setup.py file"""
import re
from setuptools import setup

_version_re = re.compile(r"__version__\s=\s'(.*)'")


def main():
    """Cloudflare API code - setup.py file"""

    with open('README.md', encoding="utf-8") as read_me:
        long_description = read_me.read()

    with open('CloudFlare/__init__.py', 'r') as f:
        version = _version_re.search(f.read()).group(1)

    setup(
        name='cloudflare',
        version=version,
        description='Python wrapper for the Cloudflare v4 API',
        long_description=long_description,
        long_description_content_type='text/markdown',
        author='Martin J. Levy',
        author_email='mahtin@mahtin.com',
        url='https://github.com/cloudflare/python-cloudflare',
        project_urls={
            "Documentation": "https://python-cloudflare.readthedocs.io/",
            "API Documentaton": "https://developers.cloudflare.com/api/",
            "Source Code": "https://github.com/cloudflare/python-cloudflare",
        },
        license='MIT',
        options={"bdist_wheel": {"universal": True}},
        packages=['CloudFlare', 'CloudFlare/tests', 'cli4', 'examples'],
        test_suite="CloudFlare.tests",
        include_package_data=True,
        data_files=[('share/man/man1', ['cli4/cli4.1'])],
        install_requires=['requests', 'pyyaml', 'jsonlines'],
        keywords='cloudflare',
        entry_points={
            'console_scripts': [
                'cli4=cli4.__main__:main'
            ]
        },
        python_requires='>3.6.0',
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11',
            'Programming Language :: Python :: 3 :: Only',
        ]
    )


if __name__ == '__main__':
    main()
