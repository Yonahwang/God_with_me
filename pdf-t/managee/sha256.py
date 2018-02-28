#!/usr/bin/python
# -*- coding: utf-8 -*-

import hashlib
import os

files =r"/home/yonah/PDFdata/pdfnormal"
pathDir =  os.listdir(files)

downf = open("sha2.txt",'wb')

for file in pathDir:
    f = files + "/" + file
    fr = open(f, 'rb')
    sh = hashlib.sha256()
    sh.update(fr.read())
    print sh.hexdigest()
    downf.write(sh.hexdigest())

downf.close()
