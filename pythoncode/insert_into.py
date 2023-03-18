# -*- encoding: utf-8 -*-
# 引入Cluster模块
from cassandra.cluster import Cluster
# 引入DCAwareRoundRobinPolicy模块，可用来自定义驱动程序的行为
from cassandra.policies import DCAwareRoundRobinPolicy
from cassandra.auth import PlainTextAuthProvider #引入认证
from cassandra.query import SimpleStatement  #引入查询
import pandas as pd  ##引入数据分析模块的pandas
from cassandra import ConsistencyLevel


cluster = Cluster(contact_points=['www.mengxiu.top'], port=9042)  ###主机地址不支持字符,可以设置成列表哈 注意端口号
session =cluster.connect()  ##创建一个连接的session ，当然这是没有指定的，后续是可以进行指定的。比如下面指定数据库也就是keyspace
# Connect to the keyspace
#session = cluster.connect(keyspace)

'''
#创建新表的时候，三大步骤缺一不可：创建key 选择使用key  创建table  
# 创建KeySpace；使用第一个副本放置策略，即简单策略；选择复制因子为3个副本。 class代表的是策略 replication_factor 代表的是复制的数量
session.execute("CREATE KEYSPACE miku2 WITH replication = {'class':'SimpleStrategy', 'replication_factor' : 3};")
# 选择keyspace
session.execute('use miku2;')
#也可以使用cluster.connect(keyspace)
# 创建table
session.execute('create table miku2.user(name text primary key, age int, email varchar);')
'''

##插入数据：
session.execute('insert into miku2.user (name, age, email) values (%s, %s, %s);', ['aaa', 21, '222@21.com'])
session.execute('insert into miku2.user (name, age, email) values (%s, %s, %s);', ['bbb', 22, 'bbb@22.com'])
session.execute('insert into miku2.user (name, age, email) values (%s, %s, %s);', ['ddd', 20, 'ccc@20.com'])

# table中查询数据  记住这个迭代用的很多
rows = session.execute('select * from miku2.user;')
for row in rows:
    print(row)

'''查询可以用下面这种这是一个案列不是本次的表'''

rows = session.execute('select * from emp') #对表emp这里可以指定那个  keyspace.table  这段的意思是将查询到的作为一个列表
for row in rows:#遍历查询的结果
    print(str(row[0])+row[1]+row[2]+row[3]+str(row[4])) #如果你的row[0] 不是varchar 或者text类型，需要转一下类型，不然python会报错
for (emp_id,emp_city,emp_email,emp_name,emp_phone) in rows:#也可以用这种方式遍历查询的结果
    print(str(emp_id)+emp_city+emp_email+emp_name+str(emp_phone))

'''传参数的查询'''

'''位置传参数'''
session.execute(
"""
INSERT INTO emp (emp_id,emp_city,emp_email,emp_name,emp_phone)
VALUES (%s, %s, %s, %s, %s)
""",
(4, 'tianjin', '156.com','pon',145645)
)
session.execute("INSERT INTO emp (emp_id) VALUES (%s)", (5,)) #如果只传一个参数，用tuple的形式必须后面加“，”，或者用list的形式
session.execute("INSERT INTO emp (emp_id) VALUES (%s)", [6]) 

'''名字传参数'''
#keyspace名、表名、列名必须提前设置好。
session.execute(
"""
INSERT INTO emp (emp_id,emp_city,emp_email,emp_name,emp_phone)
VALUES (%(emp_id)s, %(emp_city)s, %(emp_email)s, %(emp_name)s, %(emp_phone)s)
""",{'emp_id': 7, 'emp_city': 'xian', 'emp_email': '777777.qq.com', 'emp_name': 'xiaoming', 'emp_phone': 55555})



'''批量插入 超级优势速度快'''
'''
import time
import numpy as np
tic = time.time()
i=0
sql = 'BEGIN BATCH\n'
with open(r'dir', 'r') as f: ##
    while True:
        line = f.readline().strip()
        if (line == '' or line == np.nan): 
            if(sql != 'BEGIN BATCH\n'):
                sql += 'APPLY BATCH;'
                session.execute(sql)
            break
        ll = line.split(',')
        sql += 'INSERT INTO lead2(name,current_title,current_company,location,id) VALUES (' + '\''+ll[0]+'\'' + ','+'\''+ll[1]+'\''+',' +'\''+ ll[2] +'\''+  ',' +'\''+ ll[3]+'\'' +',' +'\''+ ll[4] +'\''+');\n'
        i=i+1
        if (i>300):
            sql += 'APPLY BATCH;'
            session.execute(sql)
            i=0
            sql = 'BEGIN BATCH\n'
toc = time.time()
print('vectorized version:' +str((toc - tic))  +'s')  
#vectorized version:116.4514513015747s  #插入116万条数据，用时116秒
'''




# 删除table
# session.execute('drop table miku2.user;')
# 关闭连接
cluster.shutdown()
# 查看是否关闭连接
print("你已经关闭连接：{}".format(cluster.is_shutdown))

