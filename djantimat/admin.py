# -*- coding: utf-8 -*-

from .models import Slang
from django.contrib import admin


class SlangAdmin(admin.ModelAdmin):pass
admin.site.register(Slang, SlangAdmin)
