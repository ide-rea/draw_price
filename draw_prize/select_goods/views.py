# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from .forms import user_information
from redis import StrictRedis
from  .models import *
import datetime
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
    请求格式：http://127.0.0.1:8000/draw/goods/zxy_123@sohu.com
    用redis缓存一个已参加该活动的用户的hash表
    前端发来包含有用户名的请求
    查询表如果用户已经成功参加过该活动，跳转到正常的邮箱页面
    ；否则返回库里面尚未抽取的商品.
    '''
    #默认的连接方式

    r=StrictRedis()
    no_more_goods=False
    has_join=False
    out_of_date=False
    now=datetime.datetime.now()
    if r.hget('has_join_activity_people',person):
        has_join=True
    if not r.llen('all_goods_'):
        end=True
    if now.date()==datetime.date(2017,12,22) and now.hour==24:
        out_of_date=True
    return JsonResponse({'has_join':has_join,'no_more_goods':\
                        no_more_goods,'out_of_date':out_of_date})
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
    for k,v in r.hgetall('locked').items():
        if (int(time.time())-int(k.split(b'\t')[1]))>3600:
            r.lpush('all_goods_',v)

    goods=r.lpop('all_goods_')
    r.hset('locked',person+'\t'+str(int(time.time())),goods)
    goods_=goods.decode().split('|')
    goods=goods_[1]
    #根据商品名来返回图片的连接地址
    if goods[0]=='goods':
        path='togoodspath'


    return JsonResponse({'goods':goods})
#可实现也可以不实现
#这在点击下一步的时候触发它，判断是否已经超过5分钟，
# 如果超过5分钟则告知已经过期
def take_real_or_virtual_good(request,person):
    '''
    检查是否是真实的商品，如果是则返回表单
    否则返回虚拟商品抽奖成功的提示信息
    '''
    r=StrictRedis()
    good_msg=r.hget('locked',person)
    if not good_msg:
        return JsonResponse({'time_out': True, 'release': False})
    type=goods.split(b'|')[0]
    if type.decode()=='goods':
        return take_virtual_good(request,person)
    else:
        return take_virtual_good(request,person)

#注意确定按钮的那个界面由前端人员负责生成
#到这一步我只需要返回是否已经释放商品
#触发这个函数执行的时间是用户点击了确定按钮
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
#实际商品后台不需要负责生成表单，我只需要负责处理完全正确的已经提交过来的表单
#我负责释放商品并且发送邮件
def take_real_good(request,person):
    '''
    这一步需要验证用户填写的正确性
    如果正确，则把用户信息存储下来
    发送邮件通知商品已经发放
    并返回一个页面提示操作成功
    否则返回表单，重新填写
    '''
    if request.method=='POST':
        r = StrictRedis()
        good_msg = r.hget('locked', person)
        if not good_msg:
            return JsonResponse({'time_out': True, 'release': False})
        data=request.POST
        user_msg.objects.create(receiver=data['receiver'],\
                                 tell=data['tell'],address=data['address'])
        r.hdel('locked', person)
        r.hset('has_join_activity_people', person, True)
        user_draw_prize.objects.create(user=person, goods=good_msg)
        return JsonResponse({'time_out':False,'release':True})