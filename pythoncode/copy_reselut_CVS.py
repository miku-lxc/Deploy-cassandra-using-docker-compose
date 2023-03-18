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

'''定义一条cql的查询语句'''
cql_str = 'select * from miku2.user limit 5;'
simple_statement = SimpleStatement(cql_str,consistency_level=ConsistencyLevel.ONE)
# 对语句的执行设置超时时间为None
execute_result = session.execute(simple_statement, timeout=None)
# 获取执行结果中的原始数据
result = execute_result._current_rows
# 把结果转成DataFrame格式
result = pd.DataFrame(result)
print(result)
# 把查询结果写入csv
result.to_csv('连接远程数据库.csv', mode='w+', header=True)

# 关闭连接
cluster.shutdown()
# 查看是否关闭连接
print(cluster.is_shutdown)
