
import csv
from cassandra.cluster import Cluster

'''
在内部的连接方式，指定的ip其实就是回环地址
cluster = Cluster()
session = cluster.connect()
'''

'''
#指定参数的说明
# 配置登陆Cassandra集群的账号和密码，记得改成自己知道的账号和密码 
# auth_provider = PlainTextAuthProvider(username='XXX', password='XXX') #这里可以对密码进行隐藏 或者直接使用读取文件按把对应的密码读取出来
# 创建一个Cassandra的cluster y用法
cluster = Cluster(contact_points=contact_points,,port=port,auth_provider=auth_provider)
# 连接并创建一个会话
session = cluster.connect()
'''

#指定ip和端口进行远程连接
# Set the contact points to your Cassandra cluster
contact_points = ['120.78.134.230']
# Set the port number for your Cassandra cluster
port = 9042

#选择密钥空间 密钥空间相当于mysql的数据库
# Set the keyspace to connect to
keyspace = 'miku'

# Connect to the Cassandra cluster
cluster = Cluster(contact_points, port=port)
# Connect to the keyspace
session = cluster.connect(keyspace)
###上述代码进行连接 。指定ip地址 指定要连接的数据库
'''session.set_keyspace('otherkeyspace') #设置、修改keyspace'''

'''现在让我们来进行数据库的操作 '''

# Execute a query
rows = session.execute('SELECT * FROM miku.trip_data')

# Print the results


#查看表
for row in rows:
    print(row)
cluster.shutdown()
print(cluster.is_shutdown)
