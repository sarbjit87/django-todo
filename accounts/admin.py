# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import AppUser

class AppUserAdmin(admin.ModelAdmin):
    pass

admin.site.register(AppUser, AppUserAdmin)
