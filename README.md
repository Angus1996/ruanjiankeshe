# ruanjiankeshe
软件课设
服务器网络数据库程序实现及Python网页数据显示
基本要求：
（1）	申请云端数据库存储空间。申请腾讯虚拟服务器空间（学生免费或优惠），并装MySQL云端数据库，调试时可先在本机MySQL调试。
（2）	建立数据库表。调研工控领域数据库基本需求，用Visio设计关系型数据库，并导入MySQL数据库中，建立相应数据库表；
（3）	远程维护与更新数据库。编写远程终端与服务器交互程序，更新数据库数据；
（4）	关键是支持多客户端访问，服务器端程序能区分不同用户的文件描述符，多线程维护多个客户端与服务器网络套接字之间的链接，并处理相关数据；这也是网络数据库设计是否成功的关键；
（5）	用Python语言设计网页显示相关数据库信息，具备友好的人机交互界面；

ruanjiankeshe
|--ruanjiankeshe.py
|--templates
|  |__employee.html
|  |__first.html
|  |__Flasky.html
|  |__form.html
|  |__product.html
|  |__sensor.html
|--static
     |--css
     |  |__bootstap.min.css
     |  |__first.css
     |  |__loginstyle.css
     |  |__site.css
     |  |__style.css
     |  |__unite.css
     |--js
        |__bootstrp.min.js.下载
        |__jquery.min.js.下载
        |__log-out.js.下载

