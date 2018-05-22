#!/usr/bin/python
# -*- coding: utf-8 -*-


import numpy as np
import pandas as pd
import datetime


f_tarin = pd.read_csv('/home/yonah/God_with_me/2018Q2/MLmodel3/example/test4K.csv')


def get_version(file):
    ver = file['version']
    print ver

get_version(f_tarin)
