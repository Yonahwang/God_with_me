# Hello, world!

> 嗨，大家好, 我是王凤娇. 本目录原本是存储我工作相关的代码(如dataCollection/数据采集代码/数据分析代码，以及研究成果及论文集), 现已经改成存储我离职相关工作的资料(如代码/文档等). 原数据已全部移动到oldFile目录下.

----
下面我要介绍一下我在蓝盾1年多的工作内容, 并且介绍该目录下存放的相关资料.


# 文档目录

> 下面三个目录的具体介绍, 都在相关目录的README.md中.

----
## oldFile  目录

> oldFile 目录是关于大数据基础架构的相关工作资料.

----

## sourceCode/php，sourceCode/python目录

sourceCode目录是本人工作1年数据分析以及研究相关所有的代码.

----
## vulnerability Research目录

Research目录是存储本人相关漏洞研究工作的所有有效的文档资料.

----
# 数据相关

## 数据收集与存储

> 本人工作期间，主要采集的病毒数据来自于BackBlaze（https://secure.backblaze.com/user_signin.htm //用户名:weijiang2009@gmail.com 密码：trustpath0ck!),目前数据已有600多万，并同步于集群之上。具体流程如下:
- 调用BackBlaze 官方API 将相关数据字段存储于主机172.16.7.45的mysql数据库B2 的backblaze表中
- 通过backblaze表中相关数据字段并结合官方API 将数据下载到172.16.7.45/home/zhuoxiong的目录中
- 将下载到的数据定时同步于集群（172.16.7.46 集群Master）
-  集群相关配置请细看`oldFile`详情请看里面的README.md
以上相关代码目前已更新于`sourceCode/python/dataCollect`目录,定时同步于集群的代码更新于`sourceCode/python/timedUpload`详情请看里面的README.md。（172.16.7.45的mysql数据库B2 用户名：root，密码：Love2010）

----


## 数据分析

> 
 -  文件Hash值的转换处理 （Md5->Sha256)代码已更新于`sourceCode/python/convertMD5Tosha256`目录里，详情请看里面的README.md
 -  通过Hash值获取病毒数据样本代码更新于`sourceCode/python/getHashFile`目录里,详情请看里面的README.md
 -  病毒数据样本的Virustotal report 爬取代码更新于`sourceCode/python/getVirustotalReporte`目录里,详情请看里面的README.md
 -  Virustotal report 病毒信息提取，病毒家族，病毒信息存储代码更新于`sourceCode/python/getMalwareFamily`目录里面详情请看里面的README.md

---

## 数据工具管理资源平台

> http://admin.qy.com/index.php 基于YII框架（重构的框架，详情开发文档请看该网址的文档资料以及结合YII文档）部署于主机`172.16.7.50/home/bd/www/`(用户名：root,密码：Love2010)上存储采集病毒数据样本信息以及前沿技术部门视频集合资料，集群，cve-search等
>  
-  数据工具管理资源平台（http://admin.qy.com/index.php）~~//需本地host文件添加域名(172.16.7.50 https://admin.qy.com ) ~~
-  身份验证方法 （muti，love2010）
- 网站登录密码（root，123）
- 病毒信息存储表在172.16.7.45的mysql数据库B2中malware_info（（172.16.7.45的mysql数据库B2 用户名：root，密码：Love2010）
- 该网址里的cve病毒库主要来源于cve-search，安装以及用法详情请看（https://github.com/EvilMartin/cve-search）
以上php相关代码已更新`martinCode/php`目录中，详情请看里面的README.md

## 硬盘

以上申请10个新硬盘里，用于集群第二次升级的有6个，剩余四个(已交接给江纬同学), 硬盘大小共8T.

# 致谢

感谢前沿组小伙伴一年来的合作, 与大家共处非常开心, 也非常感谢江纬同学的指导.
