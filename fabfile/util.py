# vim:ts=4:sw=4:ft=python:fileencoding=utf-8
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
import time
import sys

from fabric.api import env, run, sudo, cd, get, hide


def get_timestamp(with_time=True):
    """get a compressed timestamp suitable for filenames

    :param bool with_time: Include time as well as date. Defaults to true
    """
    datefmt = "%Y%m%d"
    if with_time:
        datefmt = "{}%H%M%S".format(datefmt)
    return time.strftime(datefmt)
