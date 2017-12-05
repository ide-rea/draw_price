# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.db import models

# Create your models here.
class real_goods(models.Model):
    name=models.CharField(max_length=100)
    amount=models.IntegerField()
    def __str__(self):
        return self.name
class virtual_goods_1th(models.Model):
    name=models.CharField(max_length=100)
    ticket=models.CharField(max_length=100)
    code=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class virtual_goods_2th(models.Model):
    name=models.CharField(max_length=100)
    coupon=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class user_good(models.Model):
    name=models.CharField(max_length=100)
    which_table=models.CharField(max_length)
    index=models.IntegerField()
    def __str__(self):
        return self.name
class user_information(models.Model):
    receiver=models.CharField(max_length=100)
    telephone_number=models.CharField(max_length=50)
    address=models.CharField(max_length=250)

