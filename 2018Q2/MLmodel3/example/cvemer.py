#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import pandas as pd
import glob


mal_tarin1 = pd.read_csv('/home/yonah/God_with_me/2018Q1/MLmodel2/example/merge_con.csv')
f1 = pd.read_csv('/home/yonah/Downloads/mimicus-master/mimicus/bin/normal_sogpi2K.csv') # 2K
f2 = pd.read_csv('/home/yonah/Downloads/mimicus-master/mimicus/bin/contogio_ben9K.csv',delimiter=',\t')  # 9K
# csv_list.append('/home/yonah/God_with_me/2018Q2/data-set/Virus8K.csv') #8K
# csv_list.append('/home/yonah/God_with_me/2018Q2/data-set/Virus-noParse.csv')  # 8K


def marge(fi1,fi2):
    print fi1.head(2)
    print fi1['class']
    print fi2.head(3)
    md = pd.concat([fi1,fi2])
    dfm = pd.DataFrame(md)
    #file = open("marge_ben1","w")


    return dfm



if __name__ == '__main__':
    print('start processing')
    dfm = marge(f1,f2)
    dfm.to_csv("marge_ben1.csv",index=False,sep=',')
