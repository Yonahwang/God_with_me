#!/usr/bin/python
# -*- coding: utf-8 -*-

import pdfrw

import sys
import os
from pdfrw import PdfReader,PdfWriter

file1 = '/home/yonah/data/God_with_me/2018Q2/Acase1/ac4/VirusShare_00ba5c43b1cec186c634c24ac21982d3.pdf'
file2 = '/home/yonah/data/God_with_me/2018Q2/Acase1/ac4/FTtmpxDwAoE.pdf'
#inpfn, = sys.argv[1:]
#outfn = 'alter.'+ os.path.basename(inpfn)

trailer1 = PdfReader(file1)
print trailer1
trailer2 = PdfReader(file2)
print trailer2

#trailer.Info.Title = 'My New title Goes Here'
#PdfWriter(outfn,trailer = trailer).write()







