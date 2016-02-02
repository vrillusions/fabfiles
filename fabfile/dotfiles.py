# vim:ts=4:sw=4:ft=python:fileencoding=utf-8
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
import os
import sys

from fabric.api import cd, env, hosts, run, task, puts
from fabric.contrib import files
from fabric.colors import yellow, green, red, cyan

from .settings import *


@task
def update():
    """Update the dotfiles repo if it exists"""
    if files.exists('~/dotfiles'):
        with cd('~/dotfiles'):
            run('git pull')
    else:
        puts(yellow('~/dotfiles does not exist. Skipping'))


#@task
#def setup():
#    """setup dotfiles repo."""