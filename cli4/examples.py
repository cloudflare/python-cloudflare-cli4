"""Cloudflare API via command line"""

import os
import sys

if sys.version_info < (3, 9):
    # importlib.resources either doesn't exist or lacks the files()
    # function, so use the PyPI version:
    try:
        import importlib_resources
    except ModuleNotFoundError as e:
        importlib_resources = None
else:
    # importlib.resources has files(), so use that:
    import importlib.resources as importlib_resources

examples_package_name = 'examples'

def display():
    """ display() """

    if not importlib_resources:
        raise ModuleNotFoundError('Module "importlib_resources" missing - please "pip install importlib_resources" as your Python version is lower than 3.9')

    try:
        pkg = importlib_resources.files(examples_package_name)
    except ModuleNotFoundError as e:
        raise e

    for ext,name in {'c': 'C', 'h': 'C', 'cc': 'C++', 'py':'Python', 'sh':'Bash', 'awk':'AWK'}.items():
        l = sorted(pkg.glob('**/*.' + ext))
        if len(l) == 0:
            continue
        print('%s .%s files:' % (name, ext))
        for f in sorted(pkg.glob('**/*.' + ext)):
            if '__init__.py' in os.fspath(f):
                continue
            print('\t%s' % (os.fspath(f)))

