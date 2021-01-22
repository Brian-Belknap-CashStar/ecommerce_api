#!/usr/bin/env python

import os
import sys
from pprint import pprint
import pytest


if 'DJANGO_SETTINGS_MODULE' not in os.environ:
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.test'

if "-i" in sys.argv or "--integration" in sys.argv:
    # if -i or --integration was specified then add the arg
    # to run integration tests
    try:
        sys.argv.remove("-i")
    except ValueError:
        pass

    try:
        sys.argv.remove("--integration")
    except ValueError:
        pass

    sys.argv.append("-m integration")
else:
    # otherwise explicitly do not run integration tests
    sys.argv.append("-m not integration")

if "-c" in sys.argv:
    sys.argv.remove("-c")
    sys.argv.append('--cov-config')
    sys.argv.append('.coveragerc')
    sys.argv.append('--cov-report')
    sys.argv.append('html')
    sys.argv.append('--cov-report')
    sys.argv.append('term-missing')
    sys.argv.append('--cov')
    sys.argv.append('.')

# The default traceback format is so ugly :(
sys.argv.append('--tb=native')

# sys.argv.append('-n1')

pprint("Sys.argv: ")
pprint(sys.argv)

if __name__ == '__main__':
    sys.exit(pytest.main())
