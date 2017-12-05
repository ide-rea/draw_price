# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse
from django.shortcuts import render
from redis import StrictRedis
from .forms import user_information
from  .models import *
import random
# Create your views here.
#确定用户是否已经参加过活动
def yes_or_not_draw_prize(request):
    '''
    用redis缓存一个已参加该活动的用户的hash表
    前端发来包含有用户名的请求
    查询表如果用户已经成功参加过该活动，跳转到正常的邮箱页面
    ；否则返回库里面尚未抽取的商品.
    '''
    #默认的连接方式
    redis_connect=StrictRedis()
    person="get from request"
    if redis_connect.hget('has_join_activity_people',person):
        flag=True
    else:
        flag=False
    redis_connect.client_kill()
    return JsonResponse({'has_draw_prize':False})

def get_draw_prize_res(request):


    '''
    这个过程，要注意锁定商品，如果没有填写成功要释放商品
    前端返回抽中的商品
    如果是数字货币，则返回邮件
    并在数据库里面记录下数字货币的减少值
    ;否则弹出一个窗口，告诉用户填写地址和联系方式
    并在数据库里面记录下商品的减少
    给用户发送邮件
    '''
    redis_connect = StrictRedis()
    count = redis_connect.hlen('has_join_activity_people')
    if count%21:
        all_real_goods=redis_connect.hkeys('real_goods')
        length=len(all_real_goods)
        goods=all_real_goods[random.randint(0,length-1)]
        redis_connect.hincrby('realgoods',goods,-1)
        redis_connect.lpush('locked_goods',{type:'real_goods'})
        return JsonResponse({'goods':goods})
    else:
        length=redis_connect.llen('virtual_goods')
        goods=redis_connect.lpop('virtual_goods')
        redis_connect.lpush('locked_goods',{'type':'virtual_goods','msg':'goods'})
        return JsonResponse({'goods':goods.split(',')[0])
    query_left_goods='from redis'

def real_or_virtual_good(request):
    '''
    检查是否是真实的商品，如果是则返回表单
    否则返回虚拟商品抽奖成功的提示信息
    '''
    if request['type']=='virtual_goods':
        form=request.

    pass
def take_virtual_good(request):
    '''
    1.锁定商品的逻辑后台负责控制
    2.30分钟释放商品的逻辑后台负责控制，端内负责30分钟的计时
    这一步需要释放商品
    并发送邮件通知商品已经发放
    并返回一个页面提示操作成功
   '''
    if request.method=='POST':
        form=user_information(request.POST)
        if form.is_valid:



    pass
def take_real_good(request):
    '''
    这一步需要验证用户填写的正确性
    如果正确，则把用户信息存储下来
    发送邮件通知商品已经发放
    并返回一个页面提示操作成功
    否则返回表单，重新填写
    '''
