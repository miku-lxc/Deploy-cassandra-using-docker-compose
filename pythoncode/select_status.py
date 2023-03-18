# -*- encoding: utf-8 -*-
# 引入Cluster模块
from cassandra.cluster import Cluster
# 引入DCAwareRoundRobinPolicy模块，可用来自定义驱动程序的行为
from cassandra.policies import DCAwareRoundRobinPolicy
from cassandra.auth import PlainTextAuthProvider #引入认证
from cassandra.query import SimpleStatement  #引入查询
import pandas as pd  ##引入数据分析模块的pandas
from cassandra import ConsistencyLevel
##y由于时间仓促，就不去删除必要的导入语句了，这些都是其他包共有的


cluster = Cluster(contact_points=['www.mengxiu.top'], port=9042)  ###主机地址不支持字符,可以设置成列表哈 注意端口号
session =cluster.connect()  ##创建一个连接的session ，当然这是没有指定的，后续是可以进行指定的。比如下面指定数据库也就是keyspace
# Connect to the keyspace
#session = cluster.connect(keyspace)



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
