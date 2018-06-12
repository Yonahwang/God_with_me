#!/usr/bin/python
# -*- coding: utf-8 -*-


from sklearn.datasets import load_svmlight_file
import time
import pandas as pd
import numpy as np


file = "/home/yonah/God_with_me/2018Q2/data-set/hidost2K.libsvm"
data = load_svmlight_file(file)
X, y = data[0], data[1]
X = X.todense()

df = pd.DataFrame(X,columns=None,index=None)
df.to_csv('hidost_feature.csv',index=False,sep=',')



