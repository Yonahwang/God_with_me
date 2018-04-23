#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from pandas import *
import csv


fx = pd.read_excel('/home/yonah/God_with_me/2018Q2/data-set/congagio9K.xlsx')
print fx.pop(5)
#fx.to_csv('c9k.csv', encoding='utf-8')
f1 = pd.read_csv('/home/yonah/God_with_me/2018Q2/data-set/normal_sogpi2K.csv')
print f1.head(1)

f2 = pd.read_csv('/home/yonah/God_with_me/2018Q2/some_code/c9k.csv') # 2K

print f2.head(2)
