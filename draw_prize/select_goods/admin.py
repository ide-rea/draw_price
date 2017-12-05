# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(user_msg)
admin.site.register(user_draw_prize)
admin.site.register(all_goods)
