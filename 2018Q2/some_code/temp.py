#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('/home/yonah/God_with_me/2018Q2/MLmodel3/file_test_predict.csv')
l = data['predint']
p = data['test']
data['diff'] = data['predint']- data['test']
print data.head(10)
#print data[data['diff'] != 0]



#print l.tolist()

