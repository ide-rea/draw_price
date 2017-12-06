# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

# Register your models here.
from .models import *
class user_msg_admin(admin.ModelAdmin):
    search_fields = ('receiver',)

admin.site.register(user_msg,user_msg_admin)
admin.site.register(all_goods)
admin.site.register(user_draw_prize)
