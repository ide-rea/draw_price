# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from .forms import user_information
from redis import StrictRedis
from  .models import *
import smtplib
import time
import random
# Create your views here.
#确定用户是否已经参加过活动
def send_mail(to_addr='1946628674@qq.com',content='hello'):
    from_addr='xiaoyuzhang004339@sohu-inc.com'
    smtp=smtplib.SMTP(host='mail.sohu.com',port=25)
    smtp.login(from_addr,'Wyqmg1104')
    smtp.sendmail(from_addr,to_addr,content)
def yes_or_not_draw_prize(request,person):
    '''
    用redis缓存一个已参加该活动的用户的hash表
    前端发来包含有用户名的请求
    查询表如果用户已经成功参加过该活动，跳转到正常的邮箱页面
    ；否则返回库里面尚未抽取的商品.
    '''
    #默认的连接方式
    r=StrictRedis()
    end=False
    if r.hget('has_join_activity_people',person):
        flag=True
    else:
        flag=False
    if r.hlen('all_goods') == 0:
        end=True
    r.client_kill()
    return JsonResponse({'has_draw_prize':flag,'end':end})
def get_draw_prize_res(request,person):


    '''
    这个过程，要注意锁定商品，如果没有填写成功要释放商品
    前端返回抽中的商品
    如果是数字货币，则返回邮件
    并在数据库里面记录下数字货币的减少值
    ;否则弹出一个窗口，告诉用户填写地址和联系方式
    并在数据库里面记录下商品的减少
    给用户发送邮件
    '''
    r=StrictRedis()
    for k,v in r.hgetall().items():
        if (time.time()-int(k.split('\t')[1]))>3600:
            r.lpush('all_goods_',v)
    goods=r.lpop('all_goods')
    r.hset('locked',person+'\t'+str(int(time.time())),goods)
    goods=goods.split(b'|')[1].decode()
    return JsonResponse({'goods':goods})
#可实现也可以不实现
def real_or_virtual_good(request,name):
    '''
    检查是否是真实的商品，如果是则返回表单
    否则返回虚拟商品抽奖成功的提示信息
    '''
    return JsonResponse({'goods':goods,'path':r.hget})


def take_virtual_good(request,person):
    '''
    1.锁定商品的逻辑后台负责控制
    2.30分钟释放商品的逻辑后台负责控制，端内负责30分钟的计时
    这一步需要释放商品
    并发送邮件通知商品已经发放
    并返回一个页面提示操作成功
   '''
    r=StrictRedis()
    good_msg=r.hget('locked',person)
    if not good_msg:
        return JsonResponse({'time_out':True,'release':False})
    send_mail(person,good_msg)
    r.hdel('locked',person)
    r.hset('has_join_activity_people', person,True)
    user_draw_prize.objects.create(user=person,goods=good_msg)
    return JsonResponse({'release':True,'time_out':False})
def take_real_good(request,person):
    '''
    这一步需要验证用户填写的正确性
    如果正确，则把用户信息存储下来
    发送邮件通知商品已经发放
    并返回一个页面提示操作成功
    否则返回表单，重新填写
    '''
    r=StrictRedis()
    if request.method=='POST':
        form=user_information(request.POST)
        if form.is_valid():
            good_msg = r.hget('locked', person)
            data=form.cleaned_data
            user_msg.objects.create(receiver=data['receiver'],\
                                    tell=data['tell'],address=data['address'])
            r.hdel('locked', person)
            r.hset('has_join_activity_people', person, True)
            user_draw_prize.objects.create(user=person, goods=good_msg)
            return JsonResponse({'pass':True})
        else:
            return JsonResponse({['receiver','tell','adress','repeat']})
    else:
        return JsonResponse({['receiver','tell','adress']})

