#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from pandas import *
import csv


data = pd.read_csv('/home/yonah/God_with_me/2018Q2/MLmodel3/example/merge_real.csv')


#file = csv.reader(open('/home/yonah/God_with_me/2018Q2/MLmodel3/example/merge_real.csv',"r")) # 10K samples, balanced dataset


#print f_tarin[0]
#print file.head(10)

ac = [0.99,0.97,0.998]
ai = []
for i in ac:
    i = int(i)
    ai.append(i)

print ai


c = data.loc[0:1]
print c
#print file["0"]

