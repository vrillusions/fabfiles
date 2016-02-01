# vim:ts=4:sw=4:ft=python:fileencoding=utf-8
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

from fabric.api import env, task, sudo, with_settings


@task
def update():
    """updates package lists"""
    sudo('apt-get -q update')

# This can sometimes fail if there are dependency loops and want other hosts to
# still update
@task
@with_settings(warn_only=True)
def dist_upgrade(warn_only=True):
    """runs a dist-upgrade"""
    sudo('apt-get -q -y dist-upgrade')
