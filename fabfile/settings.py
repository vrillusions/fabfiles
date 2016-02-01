# vim:ts=4:sw=4:ft=python:fileencoding=utf-8
# This is intended to be imported to local namespace:
#   from .settings import *
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

from fabric.api import env

# Local options like lists of hostnames and such. Optional.
try:
    from .local import *
except ImportError:
    pass


env.use_ssh_config = True
env.colorize_errors = True
