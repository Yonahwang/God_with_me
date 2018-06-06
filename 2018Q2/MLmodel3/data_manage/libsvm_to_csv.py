#!/usr/bin/python
# -*- coding: utf-8 -*-


import pickle
from sklearn.datasets import load_svmlight_file

import pandas






filename = "/home/yonah/God_with_me/pdf-t/test_data/hidost2K.libsvm"
data = (filename)

feature, label = data[0], data[1]


print label
print feature

