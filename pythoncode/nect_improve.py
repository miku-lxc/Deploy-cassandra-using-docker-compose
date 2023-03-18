
import csv
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider #引入认证

'''
在内部的连接方式，指定的ip其实就是回环地址
cluster = Cluster()
session = cluster.connect()
'''

'''代码优化，引入configparser'''
#下面是回顾的代码插入的
def mima():
    import configparser
    config = configparser.ConfigParser() #实例化方法
    config.read(r'key.txt')
    for section in config.sections():
       # a=section  #遍历setcion也就是ttile 有了这个再去便利里面的值
        for key in config[section]:
            b1=key
            b2=config[section][key] 
#我文件中的写法是section内的 user = passwd
    return [key,config[section][key]]
#   print(f'{config[section][key]}')
#    print(f'{section}')
###方法有点绕，这是我目前思考的解决方式，首先定义函数，对其进行遍历。得出想要的值，以列表反回然后进行读取
#print(type(mima())) #看看类型
#print(mima())
my_user=mima()[0]
my_passwd=mima()[1]
'''以上均为优化部分'''


####这里的主机端口都可以写入到配置文件，进行读取，然后进行批量操作
contact_points='your_HOST_name'
port = ''


#指定参数的说明
# 配置登陆Cassandra集群的账号和密码，记得改成自己知道的账号和密码 
auth_provider = PlainTextAuthProvider(username=my_user, password=my_passwd) #这里可以对密码进行隐藏 或者直接使用读取文件按把对应的密码读取出来
# 创建一个Cassandra的cluster y用法
cluster = Cluster(contact_points=contact_points,port=port,auth_provider=auth_provider)
# 连接并创建一个会话
session = cluster.connect()


'''
#指定ip和端口进行远程连接
# Set the contact points to your Cassandra cluster
contact_points = ['120.78.134.230']
# Set the port number for your Cassandra cluster
port = 9042
'''

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
