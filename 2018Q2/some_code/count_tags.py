#!/usr/bin/python
# -*- coding: utf-8 -*-



import numpy as np
import pandas as pd
from collections import Counter
import re
from pandas import DataFrame


files = pd.read_csv('/home/yonah/data/God_with_me/2018Q2/some_code/tags_ratio.csv')

#print Counter(l)
tag_list = files['tags']
tags = []
for l in tag_list:
    if l != '0':
        lc = l[1:-1]
        tag = lc.split(',')
        #tag = re.findall('(.+?)',l)
        for t in tag:
            tags.append(t)

df = DataFrame(columns=['tag''number'])
df['file_name'] = Counter(tags)
df.to_csv('tags_plot.csv',index=False,sep=',')
print Counter(tags)

