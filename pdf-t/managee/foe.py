#!/usr/bin/python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

t_num ={'2003': 3, '2002': 1, '2008': 4, '2000': 37, '2001': 1, '2006': 6, '2007': 15, '2004': 1, '2015': 4, '2014': 28, '2017': 13, '2016': 24, '2011': 1, '2010': 11, '2013': 2, '2012': 4}

t_year = list()
num = list()
for i in t_num:
    t_year.append(i)
    num.append(t_num[i])

print t_year
print num




y= num
index= t_year
plt.bar(left=index,height=y,color='green',width=0.5)

plt.show()

