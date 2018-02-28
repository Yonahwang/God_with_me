#!/usr/bin/python
# -*- coding: utf-8 -*-

import hashlib
import os

#file = open('F:\PDFdata\data2000\VirusS\VirusShare_0a4ad7052d9e9206303f6791d691f16d', 'rb')
files =r"F:\PDFdata\data2000\VirusS"

#sh = hashlib.sha256()
#sh.update(f.read())
#print sh.hexdigest()

pathDir =  os.listdir(files)

for file in pathDir:
    f = files + file
    fr = open(f , 'rb')
    sh = hashlib.sha256()
    sh.update(f.read())
    print sh.hexdigest()

