#!/usr/bin/python
# -*- coding: utf-8 -*-



import  numpy as np
import  matplotlib.mlab as mlab
import  matplotlib.pyplot as plt


X = [1,2,3,4,5,6,7]
Y = [234,345,546,765,75,2134,75]
fig = plt.figure()
plt.bar(X,Y,0.4,color = "green")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("yonah-plt")

plt.show()
