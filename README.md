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

![图片](https://user-images.githubusercontent.com/126040842/225366623-20035486-a799-4c5d-9472-eb7a7d4b840a.png)


三、cql使用





