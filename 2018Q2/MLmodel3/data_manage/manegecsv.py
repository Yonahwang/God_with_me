#!/usr/bin/python
# -*- coding: utf-8 -*-


import numpy as np
import pandas as pd

f = pd.read_csv('/home/yonah/data/God_with_me/2018Q2/MLmodel3/example/test_ad.csv')
print f.head(5)
'''del f['Unnamed: 138']
del f['Unnamed: 137']
del f['Unnamed: 0']
print f.head(5)

f2 = f

#f2 = pd.read_csv('/home/yonah/data/God_with_me/2018Q2/MLmodel3/data_manage/ad778.csv')
#print f2['box_nonother_types']
a = f2['box_nonother_types'] == 'FALSE'
b = f2['box_nonother_types'] == 'TRUE'
f2.loc[a, 'class'] = 0
f2.loc[b, 'class'] = 1

#file['box_nonother_types'] = file['box_nonother_types'].astype(bool)
#file['box_nonother_types'] = file['box_nonother_types'].astype(int)

a = f2['box_other_only'] == 'FALSE'
b = f2['box_other_only'] == 'TRUE'
f2.loc[a, 'box_other_only'] = 0
f2.loc[b, 'box_other_only'] = 1






#f2['box_nonother_types'] = f2['box_nonother_types'].astype(bool)
#f2['box_nonother_types'] = f2['box_nonother_types'].astype(int)
print f2['box_other_only']

#del f['Unnamed: 137']
#del f['Unnamed: 0']
#print f.head(5)

f2.to_csv('ad778.csv',index= None)'''

