#! /usr/bin/env python

import pyver
__version__, __version_info__ = pyver.get_version (
    pkg = __name__)
from .jsonfiledict import JsonFiledict