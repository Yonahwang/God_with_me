# -*- coding: utf-8 -*-
# !/usr/bin/python

import numpy
import pandas as pand


name = [0, 3, 4, 6, 7, 8, 11, 17, 18, 19, 22, 23, 24, 26, 31, 33, 34, 35, 38, 39]
test_y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
predint = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0]

table = {'name':name,'test':test_y,'predint':predint}

frame = pand.DataFrame(table)


print frame



