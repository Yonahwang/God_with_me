# -*- coding: utf-8 -*-
# !/usr/bin/python


import os
newfile = os.getcwd() + '/filevirus/'    #获取当前路径
count = 0
for root,dirs,files in os.walk(newfile):    #遍历统计
      for each in files:
             count += 1   #统计文件夹下文件个数
print count               #输出结果