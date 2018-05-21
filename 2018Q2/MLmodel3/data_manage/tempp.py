#!/usr/bin/python
# -*- coding: utf-8 -*-


import pickle

with open('/home/yonah/God_with_me/pdf-t/managee/tsha1.txt','rb') as f:
    outres =pickle.load(f)

print (outres)