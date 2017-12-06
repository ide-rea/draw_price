# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig

class SelectGoodsConfig(AppConfig):
    name = 'select_goods'
    verbose_name='搜狐邮箱-拉钩网抽奖活动'





for goods in all_goods.objects.all():
    if goods.type=='goods':
        for i in range(goods.count):
            genre=goods.type
            name=goods.name
            try:
                path=goods.path.path
            except Exception:
                path='None'
            r.lpush('all_goods_',genre+'|'+name+'|'+path)
    else:
        genre=goods.type
        name=goods.name
        ticket=goods.ticket
        code=goods.code
        try:
            path=goods.path.path
        except Exception:
            path='None'
        r.lpush('all_goods_',genre+'|'+name+'|'+ticket+'|'+code+'|'+path+'|')