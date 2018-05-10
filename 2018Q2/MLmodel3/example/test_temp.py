#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd

name_list = ['author_dot', 'author_lc', 'author_len', 'author_mismatch', 'author_num']
num_list = [5.39079101e-04,1.15897698e-04,4.84011775e-05,3.51138912e-04,3.85006090e-04]


def fact(n):
    if n==0:
        return 1
    print name_list[:n]
    print n
    return n * fact(n - 1)

n = len(name_list)
fact(n)

