# -*- coding: utf-8 -*-

"""Top-level package for aioemonitor."""

__author__ = "J. Nick Koston"
__email__ = "nick@koston.org"
# Do not edit this string manually, always use bumpversion
# Details in CONTRIBUTING.md
__version__ = "1.0.5"


def get_module_version():
    return __version__


from .monitor import Emonitor  # noqa: F401
