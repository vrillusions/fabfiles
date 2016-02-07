# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
import os
import sys

from fabric.api import cd, env, hide, hosts, prompt, run, settings, sudo, task
from fabric.contrib import files
from fabric.colors import yellow, green, red, cyan

from .settings import *
# all the modules that have fab tasks in them
from . import apt, dotfiles, git, info, puppet


@task(alias='usk')
def update_ssh_key():
    """ensures local user's ssh key is on remote server"""
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
