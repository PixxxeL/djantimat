# -*- coding: utf-8 -*-
"""
Detect dirty slang in russian texts and process it.

Develope for Django 1.7 but may use it without this framework partly.
"""

VERSION = (0, 1, 3,)
__version__ = '.'.join(map(str, VERSION))

try:
    from django.apps import AppConfig
except ImportError:
    class AppConfig(object): pass


default_app_config = 'djantimat.DjAntiMatConfig'

class DjAntiMatConfig(AppConfig):
    name = 'djantimat'
    verbose_name = u'Антимат'
