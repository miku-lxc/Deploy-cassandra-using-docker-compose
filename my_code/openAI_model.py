from cassandra.cluster import Cluster

# Set the contact points to your Cassandra cluster
contact_points = ['your_cloud_host_ip_address']

# Set the port number for your Cassandra cluster
port = 9042

# Set the keyspace to connect to
keyspace = 'your_keyspace_name'

# Connect to the Cassandra cluster
cluster = Cluster(contact_points, port=port)

# Connect to the keyspace
session = cluster.connect(keyspace)

# Execute a query
rows = session.execute('SELECT * FROM miku
                       ')

# Print the results
for row in rows:
    print(row)

    
    
    
 ##以下代码在用户终端执行非python内部：pip install cassandra-driver # 安装对应驱动


##以下代码是在cqlsh执行：
CREATE KEYSPACE miku
  WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}
  AND durable_writes = true;
  
  

  
  
  
  
  
  
  
  


