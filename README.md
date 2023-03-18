# Deploy-canssdran-using-docker-compose

 一.docker-compose安装并简单配置Cassandra
 
 创建docker-compose.yaml文件 参考my_code目录
 
启动compose ：docker-compose up -d 

若不是所在位置需进行指定；
docker-compose -f dir up -d


通过docker的portainer界面查看，运行状态

![图片](https://user-images.githubusercontent.com/126040842/225333857-f6da5508-18a5-4e7c-bdd0-572331f18b7c.png)


二.DataStax Python Driver

1.本次连接选择用python连接，因为python是以后最常用的代码。

2.使用openAI进行代码的辅助：

    下面是openai的代码模版，对相应的内容进行替换，后续进行补充
         该代码是连接的基础代码：没有指定预先创建的keyspace等，所以要预先创建，不适合初次使用canssdra数据库使用。
         在pythoncode的目录下，对以下代码必要的进行了补充和改进
![图片](https://user-images.githubusercontent.com/126040842/225366623-20035486-a799-4c5d-9472-eb7a7d4b840a.png)


三、cql使用
  
   主要介绍了如何用python连数据库，对数据库的连接进行了说明，同时给出了如何在python中实现数据库的相关操作：如创建keyspace、clumn等 、
   
   如何插入语句（单量和批量插入）、查询语句、查询表状态、查询结果保存为csv作为本地结果等。
   
   最后还对数据库的连接代码实行了一些优化：
     
      引入文件配置的库，解决密码隐藏的问题，防止连接时将自己的密码泄露出去造成安全风险

  代码目录：pythoncode下
      
         1.connection.py : 连接数据库代码

         2.copy_reselut_CVS.py：保存数据库到本地为csv代码

         3.create.py：创建keysapce和表代码

         4.insert_into.py：插入数据代码，包含单量插入和批量插入

         5.nect_improve.py：连接数据库的优化代码，密码隐藏

         6.select_status.py：查询数据库状态代码
  
  ![图片](https://user-images.githubusercontent.com/126040842/226094834-58b5c13b-47e3-49fc-be70-ce4eb1d1c589.png)

  
四、总结和展望
   
   本项目主要实现了docker上利用docke-compose进行编排部署，同时利用python对数据库进行管理，实现数据库的相关操作，解决目前对应客户端
   不能连接数据库的问题，比如mac上的navcate 也有可能是我没更新。利用python对数据库管理能借用python强大的库实现更高效的运维。同时对
   数据库的连接进行了隐藏密码的优化，这对于信息时代，网络安全是非常有必要的。最后，通过搭建部署数据库，对canssdra有了更加深入的了解，同时也
   观察到了，该数据与其他传统的数据库的区别，运行之后能很明显的看到，服务器的内寸被占用了一大截，正验证了，该数据库的存储机制：先提交日志后进行存储
   ，先存储到memtable（缓存），当数据持有化时放入sstable进行整合后永久存储。
   
   
   






