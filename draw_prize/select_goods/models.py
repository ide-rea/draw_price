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
    type=models.CharField(choices=type_choices,verbose_name='商品类型',max_length=100)
    #商品名称
    name=models.CharField(max_length=100,verbose_name='商品名称')
    #礼券号或则优惠码
    ticket=models.CharField(null=True,blank=True,verbose_name='券号或优惠码',max_length=100)
    #密码
    code=models.CharField(null=True,blank=True,verbose_name='卡密',max_length=100)
    #数量
    count=models.IntegerField(null=True,blank=True,verbose_name='数量',default=1)
    #图片
    path=models.FileField(null=True,blank=True,upload_to='uploads/',verbose_name='商品图片')
    def __str__(self):
        return "%s-%s-%s"%(self.type,self.name,self.ticket)
    class Meta:
        verbose_name_plural='商品信息'

class user_msg(models.Model):
    #寄送货物的地址
    receiver=models.CharField(max_length=100,verbose_name='联系人')
    #联系电话
    tell=models.CharField(max_length=50,verbose_name='联系电话')
    #地址
    address=models.CharField(max_length=250,verbose_name='地址')
    def __str__(self):
        return  self.receiver
    class Meta:
        verbose_name_plural='获奖人信息'

class user_draw_prize(models.Model):
    #获奖用户
    user=models.CharField(max_length=100,verbose_name='用户')
    #商品
    goods=models.CharField(max_length=250,verbose_name='获奖记录')
    def __str__(self):
        return "%s:%s"%(self.user,self.goods)
    class Meta:
        verbose_name_plural='获奖记录'
