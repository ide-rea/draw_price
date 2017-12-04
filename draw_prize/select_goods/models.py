# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.db import models

# Create your models here.
class real_goods(models.Model):
    name=models.CharField(max_length=100)
    amount=models.IntegerField()
class virtual_goods_1(models.Model):
    name=models.CharField(max_length=100)
    ticket=models.CharField(max_length=100)
    code=models.CharField(max_length=100)
class virtual_goods_2(models.Model):
    name=models.CharField(max_length=100)
    coupon=models.CharField(max_length=100)
class user


