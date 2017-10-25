# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import SearchUsers
# Register your models here.

class SearchUsersAdmin(admin.ModelAdmin):
    list_display = ('login', 'url',)
    list_filter = ('login',)


admin.site.register(SearchUsers,SearchUsersAdmin)