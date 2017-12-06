import redis
import sqlite3
from .models import *
#conn = pymysql.connect(**login)
#curr = conn.cursor()

def load_to_redis():
    r=redis.StrictRedis()
    for goods in all_goods.objects.all():
        if goods.type=='goods':
            for i in range(goods.count):
                genre=goods.type
                name=goods.name
                try:
                    path=goods.path.path
                except Exception:
                    path='None'

                r.lpush('all_goods',genre+'|'+name+'|'+path)
        else:
            genre=goods.type
            name=goods.name
            ticket=goods.ticket
            code=goods.code  if goods.code else 'None'
            try:
                path=goods.path.path
            except Exception:
                path='None'
            r.lpush('all_goods',genre+'|'+name+'|'+ticket+'|'+code+'|'+path)
    r.client_kill()
if __name__=='__main__':
    load_to_redis()



