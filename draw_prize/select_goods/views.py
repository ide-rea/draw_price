# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse
from django.shortcuts import render
# Create your views here.
#确定用户是否已经参加过活动
def start_draw_prize(request):
    '''
    用redis缓存一个已参加该活动的用户的hash表
    前端发来包含有用户名的请求
    查询表如果用户已经成功参加过该活动，跳转到正常的邮箱页面
    ；否则返回库里面尚未抽取的商品.
    '''
    pass
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

