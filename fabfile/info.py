# vim:ts=4:sw=4:ft=python:fileencoding=utf-8
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
import os
import sys
import time

from fabric.api import cd, env, hide, hosts, prompt, run, settings, sudo, task
from fabric.contrib import files
from fabric.colors import yellow, green, red, cyan

from .settings import *


@task
def tcp_states():
    """Summarize the host(s) tcp states."""
    run("netstat -ant | sed -e '1,2d' | awk '{ print $6 }' | sort | "
        "uniq -c | sort -rn | column -t")


# Easier to just duplicate tcp_states() then use an argument
@task
def tcp_states_detail():
    """Summarize the host(s) tcp states, including destination ip."""
    run("netstat -ant | sed -e '1,2d' -e 's/:[0-9]\+//g' | "
        "awk '{ print $6,$5 }' | sort | uniq -c | sort -rn | column -t")


@task
def tcp_hosts():
    """Summarize tcp connections by remote address."""
    run("netstat -ant | sed -e '1,2d' -e 's/:[0-9]\+//g' | awk '{print $5}' "
        "| sort | uniq -c | sort -rn")
