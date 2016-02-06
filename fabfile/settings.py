# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from fabric.api import env

# Local options like lists of hostnames and such. Optional.
try:
    from .local import *
except ImportError:
    pass


env.use_ssh_config = True
env.colorize_errors = True
env.skip_bad_hosts = True
