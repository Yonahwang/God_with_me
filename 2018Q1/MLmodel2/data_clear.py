#!/usr/bin/python
# -*- coding: utf-8 -*-


from sklearn.datasets import load_svmlight_file


filename = "/home/yonah/God_with_me/pdf-t/test_data/hidost2K.libsvm"
data = load_svmlight_file(filename)
labels, datas = data[0], data[1]
print labels
print "*****************************************************************************"
print datas




import pandas as pd
import numpy as np

df = pd.read_csv("transfered.csv")

y_data = np.array(df['is_malware'])
del df['is_malware']

X_data = np.array(df)



