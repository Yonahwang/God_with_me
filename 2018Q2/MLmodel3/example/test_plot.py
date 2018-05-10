#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
file = pd.read_csv('/home/yonah/God_with_me/2018Q2/some_code/Robustnes.csv')


#X轴，Y轴数据
x = range(135)
y1 = file['RF']
y2 = file['SVM']
y3 = file['KNN']
y4 = file['NNET']
plt.figure(figsize=(8,4)) #创建绘图对象
plt.plot(x,y1,"b",linewidth=2)   #在当前绘图对象绘图（X轴，Y轴，蓝色虚线，线宽度）
plt.plot(x,y2,"r",linewidth=1)
plt.plot(x,y3,"y",linewidth=1)
plt.plot(x,y4,"g",linewidth=1)
plt.legend()  #label show
plt.xlabel("feature--") #X轴标签
plt.ylabel("accuracy")  #Y轴标签
#plt.title("") #图标题
plt.show()  #显示图
plt.savefig("line.jpg") #保存图