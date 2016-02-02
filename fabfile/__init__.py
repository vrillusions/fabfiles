# vim:ts=4:sw=4:ft=python:fileencoding=utf-8
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
import os
import sys

from fabric.api import cd, env, hide, hosts, prompt, run, settings, sudo, task
from fabric.contrib import files
from fabric.colors import yellow, green, red, cyan

from .settings import *
from . import apt, dotfiles, git, info, puppet, util


@task(alias='usk')
def update_ssh_key():
    """Ensures local user's ssh key is on remote server."""
    home = os.path.expanduser('~')
    with file('{0}/.ssh/id_rsa.pub'.format(home)) as f:
        pubkey = f.read().rstrip()
    if not files.exists('$HOME/.ssh'):
        run('mkdir -m 0700 $HOME/.ssh')
    files.append(text=pubkey, filename='$HOME/.ssh/authorized_keys')
    run('chmod 0600 $HOME/.ssh/authorized_keys')

@task()
def reboot():
    """reboot host"""
    sudo('shutdown -r now')
