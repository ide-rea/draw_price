# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.db import models

# Create your models here.

class all_goods(models.Model):
    #商品类型
    type_choices = (('money', '礼券'),
                    ('sale', '优惠券'),
                    ('goods', '实际商品')
                    )
    type=models.CharField(choices=type_choices)
    #商品名称
    name=models.CharField(max_length=100)
    #礼券号或则优惠码
    ticket=models.CharField(null=True)
    #密码
    code=models.CharField(null=True)
    #数量
    count=models.IntegerField(null=True)
    #图片
    path=models.FileField(null=True,upload_to='uploads/')

class user_msg(models.Model):
    #寄送货物的地址
    receiver=models.CharField(max_length=100)
    #联系电话
    tell=models.CharField(max_length=50)
    #地址
    address=models.CharField(max_length=250)


class user_draw_prize(models.Model):
    #获奖用户
    user=models.CharField(max_length=100)
    #商品
    goods=models.CharField(max_length=250)
