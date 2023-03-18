
# -*- encoding: utf-8 -*-
# 引入Cluster模块
from cassandra.cluster import Cluster
# 引入DCAwareRoundRobinPolicy模块，可用来自定义驱动程序的行为
from cassandra.policies import DCAwareRoundRobinPolicy
from cassandra.auth import PlainTextAuthProvider #引入认证
from cassandra.query import SimpleStatement  #引入查询
import pandas as pd  ##引入数据分析模块的pandas
from cassandra import ConsistencyLevel

'''
# 默认本机数据库集群(IP127.0.0.1).这是基于本地的
cluster = Cluster()
# 连接并创建一个会话
session = cluster.connect()
'''

'''使用远程进行连接'''
# Connect to the Cassandra cluster

'''
# 配置登陆Cassandra集群的账号和密码，记得改成自己知道的账号和密码
# auth_provider = PlainTextAuthProvider(username='XXX', password='XXX') #这里可以对密码进行隐藏 或者直接使用读取文件按把对应的密码读取出来
# 创建一个Cassandra的cluster y用法
cluster = Cluster(contact_points=contact_points,,port=port,auth_provider=auth_provider)
# 连接并创建一个会话
session = cluster.connect()
'''

cluster = Cluster(contact_points=['www.mengxiu.top'], port=9042)  ###主机地址不支持字符,可以设置成列表哈 注意端口号
session =cluster.connect()  ##创建一个连接的session ，当然这是没有指定的，后续是可以进行指定的。比如下面指定数据库也就是keyspace
# Connect to the keyspace
#session = cluster.connect(keyspace)


# 创建KeySpace；使用第一个副本放置策略，即简单策略；选择复制因子为3个副本。 class代表的是策略 replication_factor 代表的是复制的数量
session.execute("CREATE KEYSPACE miku2 WITH replication = {'class':'SimpleStrategy', 'replication_factor' : 3};")

# 选择keyspace
session.execute('use miku2;')
#也可以使用cluster.connect(keyspace)

# 创建table
session.execute('create table miku2.user(name text primary key, age int, email varchar);')
# 删除table
# session.execute('drop table test.user;')
# 关闭连接
#cluster.shutdown()
# 查看是否关闭连接
#print(cluster.is_shutdown)

'''根据上述的情况对表进行查询其状态,查询keyspaces/tables/columns状态'''

print(cluster.metadata.keyspaces)
print('----------')
print(cluster.metadata.keyspaces['miku2'].tables)
print('----------')
print(cluster.metadata.keyspaces['miku2'].tables['user'])
print('----------')
print(cluster.metadata.keyspaces['miku2'].tables['user'].columns)
print('----------')
print(cluster.metadata.keyspaces['miku2'].tables['user'].columns['age'])
print('----------')


# 关闭连接
cluster.shutdown()
# 查看是否关闭连接
print(cluster.is_shutdown)
