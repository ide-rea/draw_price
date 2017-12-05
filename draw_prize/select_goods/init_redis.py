import redis
import pymysql
login={'host':'',
       'port':'',
       'database':'',
       'user':'',
       'passwd':''

}
def load_to_redis()
    r=redis.StrictRedis(host='',port='')
    conn=pymysql.connect(**login)
    curr=conn.cursor()
    curr.execute('select * from  all_goods')
    data=curr.fetchall()
    for row in data:
        if row[1]=='goods':
            for i in range(numbers):
                r.lpush('all_goods',row[1])
        else:
            goods_msg='|'.join([ele for ele in row  if ele])
            r.lpush('all_goods',goods_msg)
    r.client_kill()




