# -*- coding: utf-8 -*-
"""
Detect dirty slang in russian texts and process it.

Develope for Django 1.7 but may use it without this framework partly.
"""

VERSION = (0, 1, 0,)
__version__ = '.'.join(map(str, VERSION))

from django.apps import AppConfig


default_app_config = 'djantimat.DjAntiMatConfig'

class DjAntiMatConfig(AppConfig):
    name = 'djantimat'
    verbose_name = u'Антимат'
