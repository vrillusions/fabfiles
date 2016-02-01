# vim:ts=4:sw=4:ft=python:fileencoding=utf-8
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
import os
import sys

from fabric.api import cd, env, hide, hosts, prompt, run, settings, sudo, task
from fabric.contrib import files
from fabric.colors import yellow, green, red, cyan

from .settings import *


@task
def version(gitdir=None):
    """Get the current revision of given path."""
    if not gitdir:
        gitdir = prompt('Enter the full path to remote git project: ')
    git_describe_opts = '--always --long'
    with hide('commands'), cd(gitdir):
        _version = sudo('git describe {}'.format(git_describe_opts))
    print(green('{} - {} - {}'.format(env.host, gitdir, _version)))


@task
def status(gitdir=None):
    """Get the current revision and changes of given path."""
    if not gitdir:
        gitdir = prompt('Enter the full path to remote git project: ')
    git_describe_opts = '--always --long'
    git_status_opts = '--porcelain'
    with hide('commands'), cd(gitdir):
        _version = sudo('git describe {}'.format(git_describe_opts))
        _status = sudo('git status {}'.format(git_status_opts))
    if not _status:
        _status = green('clean')
    print()
    print(cyan('Current version:'), _version)
    print(cyan('State of working directory'))
    print(_status)
