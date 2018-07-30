#!/usr/bin/python
# -*- coding: utf-8 -*-


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

f_tarin = pd.read_csv('/home/yonah/data/God_with_me/2018Q2/MLmodel3/data_manage/test4K.csv')


def get_version(file):
    ver = file['version']
    return ver.tolist()
ver = get_version(f_tarin)
#ver = [4, 3, 5, 4, 3, 4, 3, 4, 3, 2, 5, 5, 4, 6, 5, 5, 5, 4, 6, 6, 4, 5, 4, 7, 4, 6, 5, 5, 5, 5, 7, 5, 4, 6, 4, 7, 4, 4, 4, 4, 4, 5, 5, 3, 5, 5, 6, 5, 4, 5, 4, 6, 7, 2, 6, 3, 5, 6, 5, 2, 4, 5, 7, 5]
Se_ver = pd.value_counts(ver)
print Se_ver
labels =  Se_ver.index._data

label = []
for la in labels:
    label.append(la/10.0 +1)

name_list = ['1.0','1.1','1.2','1.3','1.4','1.5','1.6','1.7']
vaR = [85,7,80,467,815,874,1674,174]

values =  Se_ver.values
va = values.tolist()
valu = []
for v in vaR :
    val = float(v)/sum(vaR)
    valu.append(int(val*100))

print valu

fig = plt.figure()
plt.bar(range(len(valu)),valu,color = "green",tick_label = name_list)
#index = [0,1,2,3,4,5,6,7]
#index = [1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7]
#plt.xticks(index,name_list)
plt.xlabel("Version")
plt.ylabel("presentage")
plt.title("Version distribution")
plt.show()





'''
# 设置x，y轴刻度一致，这样饼图才能是圆的
plt.axes(aspect=1)  # set this , Figure is round, otherwise it is an ellipse
# autopct ，show percet
plt.pie(x=values, labels=labels, autopct='%3.1f %%',
        labeldistance=1.1, startangle=90)
plt.show()'''

'''
fig = plt.figure(1)
plt.pie(values, labels=labels, autopct='%1.2f%%')  # 画饼图（数据，数据对应的标签，百分数保留两位小数点）
plt.title("Version distribution")

plt.show()'''


