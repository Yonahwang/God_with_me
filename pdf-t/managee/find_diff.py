#!/usr/bin/python
# -*- coding: utf-8 -*-

f1 = open('/home/yonah/Downloads/mimicus-master/data/attack.list.bak')
f2 = open('/home/yonah/God_with_me/pdf-t/test_data/mpdfs.txt')
for line1 in f1.readlines():
    for line2 in f2.readlines():
        li1 = line1.split('/')[-1].split('.p')[0]
        print li1
f1.close()